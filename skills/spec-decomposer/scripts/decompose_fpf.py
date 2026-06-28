from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _common import (
    PATTERN_ID_RE,
    DecomposeReport,
    ExtractedUnit,
    format_reference,
    generate_index,
    idempotent_write,
    remove_trivial,
    slugify,
)


END_RE = re.compile(r"^(#{1,6})\s+(.+):End\s*$", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
TOC_ROW_RE = re.compile(r"^\|\s*\**([A-Z](?:\.[A-Z0-9]+)+|\*\*\*Cluster[^*]+\*\*\*)\s*\|")
TOC_CLUSTER_RE = re.compile(r"^\|\s*\*\*Cluster\b")


def parse_fpf_spec(spec_path: Path) -> DecomposeReport:
    text = spec_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)
    spec_filename = spec_path.name

    report = DecomposeReport(
        spec_path=str(spec_path),
        spec_type="FPF",
        total_patterns=0,
        patterns_extracted=0,
        toc_parsed=False,
        toc_entries=0,
    )

    end_markers = _collect_end_markers(lines)
    end_marker_ids = {pid for pid, _ in end_markers}
    report.total_patterns = len(end_markers)

    all_headings = _build_heading_list(lines)

    # Remove sub-headings that are children of a pattern that has :End (internal sub-sections)
    heading_pids = {
        pid
        for pid in {h[0] for h in all_headings}
        if pid not in end_marker_ids
        and not any(pid.startswith(p + ".") for p in end_marker_ids)
    } | end_marker_ids

    toc_data = _parse_toc(text, report)

    units: list[ExtractedUnit] = []
    for pid, end_line in end_markers:
        # Find the best opening heading: prefer exact PID match as first word,
        # then higher heading level (fewer #), then closest to :End.
        candidates = [(ln, ht) for hpid, ln, ht in all_headings if hpid == pid and ln < end_line]
        if not candidates:
            report.warnings.append(f"PID {pid}: :End marker found at L{end_line} but no opening heading found")
            continue

        # Prefer exact first-word match (real pattern opening, not sub-section)
        exact = [(ln, ht) for ln, ht in candidates
                 if ht.split()[0].rstrip("`") == pid]
        if exact:
            # Among exact matches, prefer closest to :End
            start_line, heading_text = max(exact, key=lambda x: x[0])
        else:
            # Fallback: closest candidate
            start_line, heading_text = max(candidates, key=lambda x: x[0])
        title = heading_text
        if pid in toc_data:
            t = toc_data[pid]
            title = t.get("title", title)

        raw_lines = lines[start_line - 1 : end_line]
        body = "".join(raw_lines)

        meta: dict = {"id": pid, "title": title}
        if pid in toc_data:
            t = toc_data[pid]
            if "status" in t:
                meta["status"] = t["status"]
            if "keywords" in t:
                meta["keywords"] = t["keywords"]
            if "dependencies" in t and t["dependencies"]:
                meta["dependencies"] = t["dependencies"]

        units.append(ExtractedUnit(
            pid=pid,
            title=title,
            body=body,
            start_line=start_line,
            end_line=end_line,
            metadata=meta,
        ))

    # Filter warnings: only warn for Stable patterns (status is known from ToC)
    def _is_stable(pid: str) -> bool:
        if pid not in toc_data:
            return True  # warn if we can't determine status
        status = toc_data[pid].get("status", "")
        return status == "Stable"

    # Check headings without :End
    heading_pids_no_end = heading_pids - end_marker_ids
    for pid in heading_pids_no_end:
        if _is_stable(pid):
            candidates = [(ln, ht) for hpid, ln, ht in all_headings if hpid == pid]
            if candidates:
                report.warnings.append(f"PID {pid}: opening heading at L{candidates[0][0]} has no :End marker")

    for pid in toc_data:
        if pid not in end_marker_ids and pid not in heading_pids_no_end:
            if _is_stable(pid):
                report.warnings.append(f"PID {pid}: listed in ToC but no :End marker found")

    report.patterns_extracted = len(units)

    # Extract non-pattern ## and # sections (structural context)
    pattern_open_lines = {ln for _, ln, _ in all_headings}
    context_units = _extract_non_pattern_sections(lines, all_headings, end_marker_ids, pattern_open_lines, toc_data, spec_filename)

    return report, units, context_units, spec_filename


def _extract_non_pattern_sections(
    lines: list[str],
    all_headings: list[tuple[str, int, str]],
    end_marker_ids: set[str],
    pattern_open_lines: set[int],
    toc_data: dict[str, dict],
    spec_filename: str,
) -> list[ExtractedUnit]:
    """Extract ## and # sections that are not pattern bodies — only intro text before first pattern."""
    # Collect all #/## headings that are NOT pattern openings
    top_headings: list[tuple[int, int, str]] = []  # (level, line_no, heading_text)
    TOP_RE = re.compile(r"^(#{1,2})\s+(.+)$")
    for line_no, line in enumerate(lines, start=1):
        raw = line.rstrip("\n\r")
        m = TOP_RE.match(raw)
        if not m:
            continue
        level = len(m.group(1))
        heading_text = m.group(2).strip()
        if heading_text.endswith(":End"):
            continue
        if line_no in pattern_open_lines:
            continue
        if heading_text in ("Table of Content",):
            continue
        top_headings.append((level, line_no, heading_text))

    # Build sorted list of all "stopping" lines: pattern openings + next #/## headings
    all_stops = sorted(set(pattern_open_lines) | {ln for _, ln, _ in top_headings})

    context_units: list[ExtractedUnit] = []
    for level, start_line, heading_text in top_headings:
        # End at first stop after this heading
        end_line = len(lines)
        for stop in all_stops:
            if stop > start_line:
                end_line = stop - 1
                break

        raw_lines = lines[start_line - 1 : end_line]
        body = "".join(raw_lines).rstrip()
        if not body.strip():
            continue

        slug = heading_text.strip("#* ").split(" - ")[0].split(" — ")[0].strip()
        slug = re.sub(r"[^A-Za-z0-9]+", "-", slug).strip("-")
        if not slug:
            slug = f"section-{start_line}"
        pid = f"_ctx.{slug}"

        context_units.append(ExtractedUnit(
            pid=pid,
            title=heading_text,
            body=body,
            start_line=start_line,
            end_line=end_line,
            metadata={"id": pid, "title": heading_text},
        ))

    return context_units


def _collect_end_markers(lines: list[str]) -> list[tuple[str, int]]:
    result: list[tuple[str, int]] = []
    for line_no, line in enumerate(lines, start=1):
        m = END_RE.match(line.rstrip("\n\r"))
        if m:
            pid = m.group(2).strip()
            result.append((pid, line_no))
    return result


def _build_heading_list(lines: list[str]) -> list[tuple[str, int, str]]:
    """Return all headings with their PID, line number, and text: [(pid, line_no, heading_text), ...]"""
    result: list[tuple[str, int, str]] = []
    for line_no, line in enumerate(lines, start=1):
        raw = line.rstrip("\n\r")
        m = HEADING_RE.match(raw)
        if not m:
            continue
        heading_text = m.group(2).strip()
        if heading_text.endswith(":End"):
            continue

        pid = _extract_id(heading_text)
        if pid is None:
            continue

        result.append((pid, line_no, heading_text))
    return result


def _extract_id(heading: str) -> str | None:
    candidates = PATTERN_ID_RE.findall(heading)
    if not candidates:
        return None

    stripped = heading.lstrip("#*` ").strip()
    first_word = stripped.split()[0] if stripped.split() else ""

    for c in candidates:
        if first_word.startswith(c):
            return c
        if stripped.startswith(c):
            return c

    return None


def _parse_toc(text: str, report: DecomposeReport) -> dict[str, dict]:
    """
    Parse the FPF-Spec Table of Contents.
    Returns {pid: {title, status, keywords, dependencies}}.
    """
    result: dict[str, dict] = {}

    # Find the ToC section: between "# Table of Content" and the first pattern opening
    toc_start = text.find("# Table of Content")
    if toc_start < 0:
        report.warnings.append("ToC not found: '# Table of Content' heading missing")
        return result

    # Find the first :End marker as the approximate end of ToC
    first_end = END_RE.search(text)
    if not first_end:
        report.warnings.append("ToC parsing failed: no :End markers in spec")
        return result

    toc_section = text[toc_start:first_end.start()]

    entry_count = 0
    for line in toc_section.splitlines():
        line_stripped = line.strip()
        if not line_stripped.startswith("| "):
            continue
        if not TOC_ROW_RE.match(line_stripped):
            # Might be a cluster header row
            if TOC_CLUSTER_RE.match(line_stripped):
                continue
            # Skip non-pattern rows (header, separator, empty)
            continue

        cells = _split_toc_row(line_stripped)
        if len(cells) < 3:
            continue

        pid_raw = cells[0].strip().strip("*").strip()
        if not pid_raw or TOC_CLUSTER_RE.match(pid_raw):
            continue

        pid = _extract_id(pid_raw) or pid_raw

        title = cells[1].strip().strip("*").strip()
        title = re.sub(r"\*\*(.+?)\*\*", r"\1", title)

        status = cells[2].strip() if len(cells) > 2 else ""

        keywords: list[str] = []
        dependencies: dict[str, list[str]] = {}

        if len(cells) > 3:
            keywords = _parse_keywords(cells[3])

        if len(cells) > 4:
            dependencies = _parse_dependencies(cells[4])

        result[pid] = {
            "title": title,
            "status": status,
            "keywords": keywords,
            "dependencies": dependencies,
        }
        entry_count += 1

    report.toc_parsed = True
    report.toc_entries = entry_count
    return result


def _split_toc_row(line: str) -> list[str]:
    """Split a markdown table row by |, handling inline formatting."""
    if line.startswith("| "):
        line = line[2:]
    if line.endswith(" |"):
        line = line[:-2]
    # Simple split by | — ToC has no pipes inside cells in FPF-Spec
    return [c.strip() for c in line.split("|")]


def _parse_keywords(cell: str) -> list[str]:
    """Extract keywords from the Keywords & Queries column."""
    keywords: list[str] = []
    for part in cell.split("*Keywords:"):
        if part is cell.split("*Keywords:")[0]:
            continue
        kw_text = part
        if "*Queries:" in kw_text:
            kw_text = kw_text.split("*Queries:")[0]
        kw_text = kw_text.replace("**", "").replace("*", "")
        for word in re.split(r"[;,]", kw_text):
            word = word.strip().strip('"').strip("'")
            if word and len(word) > 1:
                keywords.append(word)
    return keywords


def _parse_dependencies(cell: str) -> dict[str, list[str]]:
    """Parse dependency relations from the Dependencies column."""
    result: dict[str, list[str]] = {}

    dep_patterns = [
        (r"\*\*Builds on:\*\*\s*(.+?)(?=\*\*|$)", "builds_on"),
        (r"\*\*Coordinates with:\*\*\s*(.+?)(?=\*\*|$)", "coordinates_with"),
        (r"\*\*Constrains:\*\*\s*(.+?)(?=\*\*|$)", "constrains"),
        (r"\*\*Prerequisite for:\*\*\s*(.+?)(?=\*\*|$)", "prerequisite_for"),
        (r"\*\*Refines:\*\*\s*(.+?)(?=\*\*|$)", "refines"),
        (r"\*\*Informs:\*\*\s*(.+?)(?=\*\*|$)", "informs"),
        (r"\*\*Used by:\*\*\s*(.+?)(?=\*\*|$)", "used_by"),
    ]

    for pattern, key in dep_patterns:
        m = re.search(pattern, cell)
        if m:
            raw = m.group(1).strip()
            ids = _extract_dep_ids(raw)
            if ids:
                result[key] = ids

    return result


def _extract_dep_ids(text: str) -> list[str]:
    """Extract pattern IDs from dependency text like 'E.2, A.5, C.17-C.19'."""
    ids: list[str] = []
    # Match pattern IDs (A.1, B.5.3, E.4.DPF, etc.) and ranges (C.17-C.19)
    for match in re.finditer(r"[A-Z]\.[0-9A-Z]+(?:\.[0-9A-Z]+)*", text):
        ids.append(match.group())
    return ids


def main():
    parser = argparse.ArgumentParser(description="Decompose FPF monolith spec into skill references")
    parser.add_argument("spec_path", type=Path, help="Path to FPF monolith .md file")
    parser.add_argument("--skills-dir", type=Path, required=True, help="Path to skill root directory (references/ will be created inside)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    spec_path = args.spec_path.expanduser().resolve()
    if not spec_path.is_file():
        print(f"Error: spec file not found: {spec_path}", file=sys.stderr)
        sys.exit(1)

    skills_dir = args.skills_dir.expanduser().resolve()
    refs_dir = skills_dir / "references"

    print(f"Decomposing FPF spec: {spec_path}", file=sys.stderr)
    print(f"Output directory: {refs_dir}", file=sys.stderr)

    report, units, context_units, spec_filename = parse_fpf_spec(spec_path)

    # Write context sections (non-pattern ##/# headings)
    ctx_written = 0
    ctx_skipped = 0
    ctx_trivial = 0
    for ct_unit in context_units:
        # Skip sections whose body (after heading) is trivially empty
        body_lines = [ln for ln in ct_unit.body.splitlines() if ln.strip()]
        if len(body_lines) <= 1:  # just the heading itself
            ctx_trivial += 1
            continue
        ctx_content, raw_len, opt_len = format_reference(ct_unit, spec_filename)
        report.size_stats.raw_bytes += raw_len
        report.size_stats.optimized_bytes += opt_len
        filepath = refs_dir / slugify(ct_unit.pid)
        if idempotent_write(filepath, ctx_content, dry_run=args.dry_run):
            ctx_written += 1
        else:
            ctx_skipped += 1
    if context_units:
        status = f"{ctx_written} written, {ctx_skipped} skipped (unchanged)"
        if ctx_trivial:
            status += f", {ctx_trivial} trivial skipped"
        print(f"Context sections: {status}", file=sys.stderr)

    if units:
        written = 0
        skipped = 0
        for unit in units:
            content, raw_len, opt_len = format_reference(unit, spec_filename)
            report.size_stats.raw_bytes += raw_len
            report.size_stats.optimized_bytes += opt_len
            filename = slugify(unit.pid)
            filepath = refs_dir / filename
            if idempotent_write(filepath, content, dry_run=args.dry_run):
                written += 1
            else:
                skipped += 1

        index_content = generate_index(units, spec_path.stem, spec_filename, has_relations=False)
        index_path = refs_dir / "INDEX.md"
        if idempotent_write(index_path, index_content, dry_run=args.dry_run):
            print(f"INDEX.md written ({len(units)} entries)", file=sys.stderr)
        else:
            print(f"INDEX.md unchanged ({len(units)} entries)", file=sys.stderr)

        print(f"References: {written} written, {skipped} skipped (unchanged)", file=sys.stderr)
    else:
        print("No patterns extracted!", file=sys.stderr)

    if report.warnings:
        print(f"\nWarnings ({len(report.warnings)}):", file=sys.stderr)
        for w in report.warnings:
            print(f"  - {w}", file=sys.stderr)

    if report.errors:
        print(f"\nErrors ({len(report.errors)}):", file=sys.stderr)
        for e in report.errors:
            print(f"  - {e}", file=sys.stderr)

    report.print()


if __name__ == "__main__":
    main()

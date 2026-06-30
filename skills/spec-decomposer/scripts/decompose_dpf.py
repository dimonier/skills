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
    slugify,
)


SECTION_RE = re.compile(r"^##\s+(\d+)\.\s+")
PROBLEM_CARD_RE = re.compile(r"^###\s+6\.(\d+)\s+")
PID_RE = re.compile(r"`([^`]+)`")


def parse_dpf_spec(spec_path: Path) -> DecomposeReport:
    text = spec_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)
    spec_filename = spec_path.name

    report = DecomposeReport(
        spec_path=str(spec_path),
        spec_type="DPF",
        total_patterns=0,
        patterns_extracted=0,
        toc_parsed=False,
        toc_entries=0,
    )

    # Step 1: Find section boundaries
    sections = _find_sections(lines)

    # Step 2: Identify section 6 (Problem Cards) and section 7 (Relations)
    sec6_start = None
    sec6_end = None
    sec7_start = None
    sec7_end = None

    for num, start_line, _heading in sections:
        if num == 6:
            sec6_start = start_line
        elif num == 7:
            sec6_end = start_line
            sec7_start = start_line
        elif num == 8 and sec7_start is not None and sec7_end is None:
            sec7_end = start_line

    if sec6_start is None:
        report.errors.append("Section 6 (Problem Cards) not found")
        return report, [], spec_filename

    if sec6_end is None:
        sec6_end = len(lines) + 1

    if sec7_start is None:
        report.warnings.append("Section 7 (Relations) not found")
    elif sec7_end is None:
        sec7_end = len(lines) + 1

    # Step 3: Extract problem cards from section 6
    units = _extract_problem_cards(lines, sec6_start, sec6_end, report)

    # Step 4: Extract relations
    relations_text = None
    if sec7_start is not None:
        relations_text = _extract_relations(lines, sec7_start, sec7_end, report)

    report.total_patterns = len(units)
    report.patterns_extracted = len(units)

    non_extractable = []
    for num, start_line, heading in sections:
        if num not in (6, 7):
            non_extractable.append(f"Section {num}: {heading} (L{start_line})")
    report.non_extractable = non_extractable

    return report, units, spec_filename, relations_text, sec7_start, sec7_end


def _find_sections(lines: list[str]) -> list[tuple[int, int, str]]:
    """Find all ## N. sections, returning (section_number, start_line, heading_text)."""
    sections: list[tuple[int, int, str]] = []
    for line_no, line in enumerate(lines, start=1):
        raw = line.rstrip("\n\r")
        m = SECTION_RE.match(raw)
        if m:
            num = int(m.group(1))
            heading = raw.strip()
            sections.append((num, line_no, heading))
    return sections


def _extract_problem_cards(
    lines: list[str],
    sec6_start: int,
    sec6_end: int,
    report: DecomposeReport,
) -> list[ExtractedUnit]:
    """Extract problem cards from section 6."""
    # Find all problem card headings within section 6
    card_starts: list[tuple[int, str, str]] = []  # (line_no, pid, heading_text)
    for line_no in range(sec6_start, sec6_end):
        raw = lines[line_no - 1].rstrip("\n\r")
        m = PROBLEM_CARD_RE.match(raw)
        if not m:
            continue

        pid = _extract_dpf_pid(raw)
        if pid is None:
            report.warnings.append(f"L{line_no}: Problem card heading with no recognizable PID: {raw[:80]}")
            continue

        # Extract title: everything after the PID in the heading
        heading_stripped = raw.lstrip("#").strip()
        title = _extract_dpf_title(heading_stripped, pid)
        card_starts.append((line_no, pid, title))

    if not card_starts:
        report.errors.append("No problem cards found in section 6")
        return []

    # Determine boundaries
    units: list[ExtractedUnit] = []
    for i, (start_line, pid, title) in enumerate(card_starts):
        if i + 1 < len(card_starts):
            end_line = card_starts[i + 1][0] - 1
        else:
            end_line = sec6_end - 1

        raw_lines = lines[start_line - 1 : end_line]
        body = "".join(raw_lines)

        units.append(ExtractedUnit(
            pid=pid,
            title=title,
            body=body,
            start_line=start_line,
            end_line=end_line,
            metadata={"id": pid, "title": title},
        ))

    return units


def _extract_dpf_pid(heading: str) -> str | None:
    """Extract pattern ID from a DPF problem card heading like '### 6.1 `MPAG.TranscriptToProtocol` — Name'."""
    # Try backtick-delimited PID first
    m = PID_RE.search(heading)
    if m:
        pid = m.group(1)
        if PATTERN_ID_RE.match(pid):
            return pid

    # Try PATTERN_ID_RE directly
    candidates = PATTERN_ID_RE.findall(heading)
    if candidates:
        # Filter out the section number (6.1, etc.) which wouldn't match PATTERN_ID_RE
        # Pick the longest match that looks like a real PID
        for c in candidates:
            if "." in c and c[0].isalpha():
                return c
        return candidates[0]

    return None


def _extract_dpf_title(heading: str, pid: str) -> str:
    """Extract title from a DPF heading like '6.1 `MPAG.TranscriptToProtocol` — Название'."""
    heading = heading.strip()

    # Remove section number prefix and the PID (with or without backticks)
    for prefix_pattern in [
        rf"6\.\d+\s+`{re.escape(pid)}`\s*[—–\-]\s*",
        rf"6\.\d+\s+{re.escape(pid)}\s*[—–\-]\s*",
    ]:
        m = re.search(prefix_pattern, heading)
        if m:
            rest = heading[m.end():].strip()
            rest = re.sub(r"\*\*(.+?)\*\*", r"\1", rest)
            if rest:
                return rest

    # Fallback: take everything after the PID
    pid_positions = [m.end() for m in re.finditer(re.escape(pid), heading)]
    for pos in pid_positions:
        rest = heading[pos:].strip().lstrip("`").strip()
        if rest.startswith("—") or rest.startswith("–") or rest.startswith("-"):
            rest = rest[1:].strip()
        rest = re.sub(r"\*\*(.+?)\*\*", r"\1", rest)
        if rest:
            return rest

    return pid


def _extract_relations(
    lines: list[str],
    sec7_start: int,
    sec7_end: int,
    report: DecomposeReport,
) -> str | None:
    """Extract relations from section 7."""
    raw_lines = lines[sec7_start - 1 : sec7_end - 1]
    text = "".join(raw_lines).strip()
    if not text:
        report.warnings.append("Section 7 is empty")
        return None
    return text


def format_relations(relations_text: str) -> str:
    body = relations_text.rstrip()
    if body.endswith("---"):
        body = body[:-3].rstrip()
    header = f"# Relation Records (E.4.PFR)\n\n"
    return header + body


def main():
    parser = argparse.ArgumentParser(description="Decompose DPF/LPF monolith spec into skill references")
    parser.add_argument("spec_path", type=Path, help="Path to DPF monolith .md file")
    parser.add_argument("--skills-dir", type=Path, required=True, help="Path to skill root directory (references/ will be created inside)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    spec_path = args.spec_path.expanduser().resolve()
    if not spec_path.is_file():
        print(f"Error: spec file not found: {spec_path}", file=sys.stderr)
        sys.exit(1)

    skills_dir = args.skills_dir.expanduser().resolve()
    refs_dir = skills_dir / "references"

    print(f"Decomposing DPF spec: {spec_path}", file=sys.stderr)
    print(f"Output directory: {refs_dir}", file=sys.stderr)

    report, units, spec_filename, relations_text, sec7_start, sec7_end = parse_dpf_spec(spec_path)

    if units:
        written = 0
        skipped = 0
        for unit in units:
            content, raw_len, opt_len = format_reference(unit)
            report.size_stats.raw_bytes += raw_len
            report.size_stats.optimized_bytes += opt_len
            filename = slugify(unit.pid)
            filepath = refs_dir / filename
            if idempotent_write(filepath, content, dry_run=args.dry_run):
                written += 1
            else:
                skipped += 1

        index_content = generate_index(units, spec_path.stem, spec_filename, has_relations=True)
        index_path = refs_dir / "INDEX.md"
        if idempotent_write(index_path, index_content, dry_run=args.dry_run):
            print(f"INDEX.md written ({len(units)} entries)", file=sys.stderr)
        else:
            print(f"INDEX.md unchanged ({len(units)} entries)", file=sys.stderr)

        print(f"References: {written} written, {skipped} skipped (unchanged)", file=sys.stderr)
    else:
        print("No patterns extracted!", file=sys.stderr)

    if relations_text:
        relations_content = format_relations(
            relations_text,
        )
        relations_path = refs_dir / "relations.md"
        if idempotent_write(relations_path, relations_content, dry_run=args.dry_run):
            print("relations.md written", file=sys.stderr)
        else:
            print("relations.md unchanged", file=sys.stderr)

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

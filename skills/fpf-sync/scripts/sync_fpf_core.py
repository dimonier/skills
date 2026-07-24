"""
Sync fpf-core skill from the canonical FPF-Spec.md monolith.

Self-contained — bundles decompose_fpf.py + _common.py directly.
No external dependencies beyond Python stdlib + git.
All paths are derived from this script's location — portable across machines.

Workflow:
  1. git pull in FPF repo root
  2. Compare FPF-Spec.md with skills/fpf-core/assets/FPF-Spec.md
  3. If changed: copy monolith -> decompose -> update SKILL.md

Usage:
  python sync_fpf_core.py              # full sync
  python sync_fpf_core.py --check      # only check, exit 0=up-to-date, 1=needs update
  python sync_fpf_core.py --dry-run    # preview without writing
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import decompose_fpf
from _common import format_reference, generate_index, idempotent_write, slugify

SCRIPT_DIR = Path(__file__).resolve().parent
FPF_REPO = SCRIPT_DIR.parent.parent.parent
SPEC_NAME = "FPF-Spec.md"
SPEC_SOURCE = FPF_REPO / SPEC_NAME
SKILL_DIR = FPF_REPO / "skills" / "fpf-core"
SPEC_ASSET = SKILL_DIR / "assets" / SPEC_NAME
SKILL_MD = SKILL_DIR / "SKILL.md"
REFERENCES_DIR = SKILL_DIR / "references"

LINES_RE = re.compile(r"(canonical specification \()(\d+K\+)( lines\))")
REFS_RE = re.compile(r"(\*\*Ready\*\* — )(\d+)( pattern reference files \+ INDEX \+ )(\d+)( context sections\.)")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_lines(path: Path) -> int:
    raw = path.read_text(encoding="utf-8", errors="replace")
    return len(raw.splitlines())


def count_references(refs_dir: Path) -> tuple[int, int]:
    """Return (pattern_ref_count, context_section_count)."""
    if not refs_dir.is_dir():
        return 0, 0
    pattern_count = 0
    ctx_count = 0
    for f in refs_dir.iterdir():
        if not f.is_file() or f.suffix != ".md":
            continue
        name = f.name
        if name in ("INDEX.md", "relations.md"):
            continue
        if name.startswith("_ctx."):
            ctx_count += 1
        else:
            pattern_count += 1
    return pattern_count, ctx_count


def git_pull(repo: Path) -> tuple[bool, str]:
    """Run git pull. Returns (ok, output_text)."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "pull"],
            capture_output=True, text=True, timeout=60,
        )
        output = (result.stdout + result.stderr).strip()
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def run_decompose(spec_path: Path, skills_dir: Path, *, dry_run: bool = False) -> tuple[str, dict | None]:
    """Decompose monolith into references/. Returns (status_text, report_dict)."""
    refs_dir = skills_dir / "references"
    refs_dir.mkdir(parents=True, exist_ok=True)

    report, units, context_units, spec_filename = decompose_fpf.parse_fpf_spec(spec_path)

    output_lines: list[str] = []
    output_lines.append(f"Decomposing FPF spec: {spec_path}")
    output_lines.append(f"Output directory: {refs_dir}")
    output_lines.append(f"Total patterns (with :End markers): {report.total_patterns}")
    output_lines.append(f"Patterns extracted: {len(units)}")
    output_lines.append(f"ToC entries: {report.toc_entries}")

    if report.warnings:
        output_lines.append(f"\nWarnings ({len(report.warnings)}):")
        for w in report.warnings:
            output_lines.append(f"  - {w}")

    # Write context sections
    ctx_written = 0
    ctx_skipped = 0
    ctx_trivial = 0
    for ct_unit in context_units:
        body_lines = [ln for ln in ct_unit.body.splitlines() if ln.strip()]
        if len(body_lines) <= 1:
            ctx_trivial += 1
            continue
        ctx_content, raw_len, opt_len = format_reference(ct_unit)
        report.size_stats.raw_bytes += raw_len
        report.size_stats.optimized_bytes += opt_len
        filepath = refs_dir / slugify(ct_unit.pid)
        if idempotent_write(filepath, ctx_content, dry_run=dry_run):
            ctx_written += 1
        else:
            ctx_skipped += 1

    ctx_status = f"{ctx_written} written, {ctx_skipped} skipped (unchanged)"
    if ctx_trivial:
        ctx_status += f", {ctx_trivial} trivial skipped"
    output_lines.append(f"Context sections: {ctx_status}")

    # Write pattern references
    if units:
        written = 0
        skipped = 0
        for unit in units:
            content, raw_len, opt_len = format_reference(unit)
            report.size_stats.raw_bytes += raw_len
            report.size_stats.optimized_bytes += opt_len
            filepath = refs_dir / slugify(unit.pid)
            if idempotent_write(filepath, content, dry_run=dry_run):
                written += 1
            else:
                skipped += 1

        index_content = generate_index(units, spec_path.stem, spec_filename, has_relations=False)
        index_path = refs_dir / "INDEX.md"
        if idempotent_write(index_path, index_content, dry_run=dry_run):
            output_lines.append(f"INDEX.md written ({len(units)} entries)")
        else:
            output_lines.append(f"INDEX.md unchanged ({len(units)} entries)")

        output_lines.append(f"References: {written} written, {skipped} skipped (unchanged)")
    else:
        output_lines.append("No patterns extracted!")

    report_dict = report.to_dict()
    output_lines.append("")
    output_lines.append(json.dumps(report_dict, indent=2, ensure_ascii=False))

    return "\n".join(output_lines), report_dict


def update_skill_md(skill_md: Path, line_count: int, pattern_count: int, ctx_count: int) -> bool:
    """Update line count and reference counts in SKILL.md. Returns True if changed."""
    text = skill_md.read_text(encoding="utf-8")

    thousands = max(1, (line_count + 500) // 1000)
    text, n1 = LINES_RE.subn(rf"\g<1>{thousands}K+\g<3>", text)

    text, n2 = REFS_RE.subn(rf"\g<1>{pattern_count}\g<3>{ctx_count}\g<5>", text)

    if n1 == 0 and n2 == 0:
        return False

    skill_md.write_text(text, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(description="Sync fpf-core skill from FPF monolith")
    parser.add_argument("--check", action="store_true", help="Exit 0=up-to-date, 1=update needed")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--no-git", action="store_true", help="Skip git pull")
    args = parser.parse_args()

    errors: list[str] = []

    # 1. git pull
    if not args.no_git:
        print("=== Step 1: git pull ===")
        ok, output = git_pull(FPF_REPO)
        print(output)
        if not ok and "fatal" not in output and "error" not in output.lower():
            pass
        elif not ok:
            print("WARNING: git pull had issues — continuing with local state")

    # 2. Check if update needed
    print("\n=== Step 2: Checking for changes ===")
    if not SPEC_SOURCE.is_file():
        print(f"ERROR: Source spec not found: {SPEC_SOURCE}")
        sys.exit(2)

    source_hash = sha256_file(SPEC_SOURCE)
    source_lines = count_lines(SPEC_SOURCE)

    asset_exists = SPEC_ASSET.is_file()
    asset_hash = sha256_file(SPEC_ASSET) if asset_exists else ""
    asset_lines = count_lines(SPEC_ASSET) if asset_exists else 0

    print(f"Source: {source_lines} lines, sha256={source_hash[:16]}...")
    print(f"Asset:  {asset_lines} lines, sha256={asset_hash[:16]}..." if asset_exists else "Asset:  MISSING")

    if asset_exists and source_hash == asset_hash:
        print("\nFPF-Spec.md is up-to-date. Nothing to do.")
        sys.exit(0 if args.check else 0)

    if args.check:
        print("\nUpdate needed — source has changed.")
        sys.exit(1)

    if args.dry_run:
        print("\n[DRY-RUN] Would update the skill. Stopping.")
        sys.exit(0)

    # 3. Copy monolith to assets
    print("\n=== Step 3: Copying monolith to assets ===")
    SPEC_ASSET.parent.mkdir(parents=True, exist_ok=True)
    SPEC_ASSET.write_bytes(SPEC_SOURCE.read_bytes())
    print(f"Copied: {SPEC_SOURCE} -> {SPEC_ASSET}")

    # 4. Run decomposition
    print("\n=== Step 4: Running decomposition ===")
    output, report = run_decompose(SPEC_ASSET, SKILL_DIR, dry_run=args.dry_run)
    print(output)
    if report:
        if report.get("errors"):
            errors.extend(report["errors"])
        if report.get("warnings"):
            for w in report["warnings"]:
                print(f"WARNING: {w}")

    # 5. Count and update SKILL.md
    print("\n=== Step 5: Updating SKILL.md ===")
    pattern_count, ctx_count = count_references(REFERENCES_DIR)
    line_count = count_lines(SPEC_SOURCE)
    thousands = max(1, (line_count + 500) // 1000)

    print(f"Pattern references: {pattern_count}")
    print(f"Context sections:  {ctx_count}")
    print(f"Monolith lines:    {line_count} (~{thousands}K)")

    updated = update_skill_md(SKILL_MD, line_count, pattern_count, ctx_count)
    if updated:
        print("SKILL.md updated.")
    else:
        print("SKILL.md already up-to-date.")

    # 6. Report
    print("\n=== Sync complete ===")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("SUCCESS — fpf-core skill is in sync with canonical FPF-Spec.md")


if __name__ == "__main__":
    main()

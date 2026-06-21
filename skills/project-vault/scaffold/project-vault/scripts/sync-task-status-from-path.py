#!/usr/bin/env python3
"""
Sync `status` in task frontmatter from folder name under project-vault/work/tasks/.

Convention:
  - work/tasks/*.md              -> status: open
  - work/tasks/done/*.md         -> status: done
  - work/tasks/cancelled/*.md    -> status: cancelled

Run from repository root:
  python3 project-vault/scripts/sync-task-status-from-path.py

Optional:
  --dry-run   print changes only
  --fix-root  also set status: open for any *.md directly under tasks/ (use if you rely on folder as truth)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _set_status_in_frontmatter(fm: str, status: str) -> tuple[str, bool]:
    """Return (new_fm, changed)."""
    if re.search(r"(?m)^status:\s*", fm):
        new_fm = re.sub(r"(?m)^status:\s*.*$", f"status: {status}", fm, count=1)
        return new_fm, new_fm != fm
    stripped = fm.rstrip("\n")
    addition = f"\nstatus: {status}\n"
    return stripped + addition, True


def sync_file(path: Path, status: str, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    _, fm, body = parts
    new_fm, changed = _set_status_in_frontmatter(fm, status)
    if not changed:
        return False
    new_text = f"---{new_fm}---{body}"
    if dry_run:
        print(f"would update: {path} -> status: {status}")
    else:
        path.write_text(new_text, encoding="utf-8")
        print(f"updated: {path} -> status: {status}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root (default: parent of project-vault/)",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--fix-root",
        action="store_true",
        help="Sync status: open for TASK files in work/tasks/ (not in subfolders)",
    )
    args = parser.parse_args()

    here = Path(__file__).resolve()
    script_dir = here.parent
    if args.root:
        repo_root = args.root.resolve()
    else:
        repo_root = script_dir.parent.parent

    tasks = repo_root / "project-vault" / "work" / "tasks"
    if not tasks.is_dir():
        print(f"error: tasks directory not found: {tasks}", file=sys.stderr)
        return 1

    mapping = [
        (tasks / "done", "done"),
        (tasks / "cancelled", "cancelled"),
    ]

    count = 0
    for folder, status in mapping:
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("TASK-*.md")):
            if sync_file(path, status, args.dry_run):
                count += 1

    if args.fix_root:
        for path in sorted(tasks.glob("TASK-*.md")):
            if sync_file(path, "open", args.dry_run):
                count += 1

    if count == 0 and not args.dry_run:
        print("no frontmatter status changes needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

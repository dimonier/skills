#!/usr/bin/env python3
"""Build/validate the project-vault intra-LPF relation map from card frontmatter.

The dependency graph has a single authored home: each card's frontmatter
`dependencies` (see `PLAS.GoverningCues`). This script is the named consumer:
it derives the readable `references/relations.md` projection (`E.4.PFR:3.2`) and,
with `--check`, fails if the generated block drifts from the authored graph.

Usage (from the skill root or anywhere):
    python scripts/build_relations.py            # regenerate relations.md
    python scripts/build_relations.py --check    # exit 1 if out of date
    python scripts/build_relations.py --root <skill-root>

Relation functions come from FPF `E.4.PFR:3.3` only: `builds_on`,
`coordinates_with`, `specializes`. Specialization is authored on the CHILD side
(`specializes`); its inverse `specialized_by` is derived here and never authored.
No `governs`/`applies-to`. As in PLAS, this file's graph block is the intra-LPF
graph only; the FPF content edges live in each card's frontmatter, not here.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

BEGIN = "<!-- BEGIN GENERATED GRAPH -->"
END = "<!-- END GENERATED GRAPH -->"

FPF_EDGES = ("builds_on", "coordinates_with")


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        import yaml  # type: ignore

        return yaml.safe_load(parts[1]) or {}
    except ImportError:
        # Minimal fallback: no PyYAML -> cannot validate reliably.
        raise SystemExit("PyYAML is required: pip install pyyaml")
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f"YAML parse error in {path}: {exc}")


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def collect(references: Path):
    cards = {}
    for path in sorted(references.glob("*.md")):
        if path.name in ("relations.md", "INDEX.md"):
            continue
        fm = parse_frontmatter(path)
        if fm is None:
            continue
        deps = fm.get("dependencies") or {}
        cid = fm.get("id")
        if not cid:
            raise SystemExit(f"{path.name}: missing 'id' in frontmatter")
        cards[cid] = {
            "builds_on": as_list(deps.get("builds_on")),
            "coordinates_with": as_list(deps.get("coordinates_with")),
            "specialized_by": as_list(deps.get("specialized_by")),
            "specializes": as_list(deps.get("specializes")),
        }
    return cards


def build_edges(cards):
    fpf = []           # (from, relation, to)
    spec = set()       # authored: (child, "specializes", parent)
    derived = set()    # generated inverse: (parent, "specialized_by", child)
    problems = []

    for cid, d in cards.items():
        for rel in FPF_EDGES:
            for target in d[rel]:
                fpf.append((cid, rel, target))
        if d["specialized_by"]:
            problems.append(
                f"{cid}: `specialized_by` is not authored (variant C) — declare the "
                f"edge child-side via `specializes`; the inverse is generated"
            )
        for parent in d["specializes"]:
            spec.add((cid, "specializes", parent))
            derived.add((parent, "specialized_by", cid))
    return fpf, spec, derived, problems


def render(cards):
    _, spec, derived, _ = build_edges(cards)
    lines = []
    lines.append("### Specialization — authored (`specializes`, child → parent)")
    lines.append("")
    lines.append("| From (child) | Relation | To (parent) |")
    lines.append("|---|---|---|")
    for frm, rel, to in sorted(spec):
        lines.append(f"| `{frm}` | `{rel}` | `{to}` |")
    lines.append("")
    lines.append("### Specialization — derived inverse (`specialized_by`, parent → child)")
    lines.append("")
    lines.append("| From (parent) | Relation | To (child) |")
    lines.append("|---|---|---|")
    for frm, rel, to in sorted(derived):
        lines.append(f"| `{frm}` | `{rel}` | `{to}` |")
    lines.append("")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None, help="skill root (dir containing references/)")
    ap.add_argument("--check", action="store_true", help="fail if relations.md is stale")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    references = root / "references"
    relations = references / "relations.md"
    if not relations.exists():
        raise SystemExit(f"not found: {relations}")

    cards = collect(references)
    _, _, _, problems = build_edges(cards)
    generated = render(cards)

    text = relations.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        raise SystemExit(f"{relations} must contain {BEGIN} / {END} markers")
    head, rest = text.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    new_text = f"{head}{BEGIN}\n{generated}{END}{tail}"

    if problems:
        for p in problems:
            print(f"WARN: {p}", file=sys.stderr)

    if args.check:
        if text != new_text:
            print("STALE: relations.md differs from generated graph", file=sys.stderr)
            return 1
        print("OK: relations.md matches the authored frontmatter graph")
        return 0

    relations.write_text(new_text, encoding="utf-8")
    print(f"Generated: {relations} ({len(cards)} cards)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

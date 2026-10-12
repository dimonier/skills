#!/usr/bin/env python3
"""build_relations.py — regenerate / validate references/relations.md for
dpf-business-analysis (full carrier).

Canonical contract (PLAS.SkillLayout:4 item 10; CC-SL.13 / CC-QR.7):
  * regenerate  :  python build_relations.py            -> rewrites the generated block
  * check       :  python build_relations.py --check    -> exits non-zero on drift
  * never edits card bodies
  * generated block is delimited by BEGIN / END markers
  * empty intra-LPF Specialization graph -> explicit stub line (FPF-edges-present form)

Frontmatter (single authored home of the dependency graph):
    ---
    id: BAR.X
    ...
    dependencies:
      builds_on: [C.22.2, C.11]
      coordinates_with: [A.2, C.16]
      specializes: []            # optional; intra-LPF parent cards, child side only
    ---
"""

import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REFERENCES = HERE.parent / "references"
RELATIONS = REFERENCES / "relations.md"

BEGIN = "<!-- BEGIN GENERATED GRAPH -->"
END = "<!-- END GENERATED GRAPH -->"

_CUE_BLOCK_RE = re.compile(r"Governing(?:\u2010|\u2011|-|\s)[Pp]attern")
_FPF_PATH_RE = re.compile(r"^\s*→\s*(?:\.\./)?fpf-core", re.M)


def _field(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else None


def _list(fm, key):
    m = re.search(rf"^\s*{key}:\s*\[(.*)\]", fm, re.M)
    if not m:
        return []
    inner = m.group(1).strip()
    if not inner:
        return []
    return [x.strip() for x in inner.split(",") if x.strip()]


def parse_card(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    fm = m.group(1)
    cid = _field(fm, "id")
    if cid is None:
        return None
    return {
        "file": path.name,
        "id": cid,
        "builds_on": _list(fm, "builds_on"),
        "coordinates_with": _list(fm, "coordinates_with"),
        "specializes": _list(fm, "specializes"),
    }


def load_cards():
    cards = []
    for p in sorted(REFERENCES.glob("*.md")):
        if p.name in ("INDEX.md", "relations.md"):
            continue
        c = parse_card(p)
        if c:
            cards.append(c)
    return cards


def build_graph_block(cards):
    specializes = [(c["id"], c["specializes"]) for c in cards if c["specializes"]]
    has_fpf_edges = any(c["builds_on"] or c["coordinates_with"] for c in cards)
    lines = []
    if not specializes:
        if has_fpf_edges:
            lines.append(
                "Intra-LPF Specialization graph: empty — none of the "
                f"{len(cards)} sibling cards `specializes` another."
            )
            lines.append("FPF content edges live only in card frontmatter.")
        else:
            lines.append("Intra-LPF Specialization graph: empty — no `specializes` edges,")
            lines.append("and no FPF content edges (self-sufficient carrier).")
    else:
        lines.append("| Child | Parent (`specializes`) |")
        lines.append("|---|---|")
        by_parent = {}
        for cid, parents in specializes:
            for parent in parents:
                lines.append(f"| `{cid}` | `{parent}` |")
                by_parent.setdefault(parent, []).append(cid)
        lines.append("")
        lines.append("`specialized_by` (derived, never authored):")
        for parent in sorted(by_parent):
            children = ", ".join(f"`{c}`" for c in by_parent[parent])
            lines.append(f"- `{parent}` ← {children}")
    return "\n".join(lines)


def replace_block(text, block):
    m = re.search(re.escape(BEGIN) + r".*?" + re.escape(END), text, re.DOTALL)
    if m:
        return text[: m.start()] + block + text[m.end():]
    return text.rstrip() + "\n\n" + block + "\n"


def regenerate(cards):
    block = f"{BEGIN}\n{build_graph_block(cards)}\n{END}"
    RELATIONS.write_text(
        replace_block(RELATIONS.read_text(encoding="utf-8"), block), encoding="utf-8"
    )
    return block


def check(cards):
    ok = True
    current = RELATIONS.read_text(encoding="utf-8")
    if current.count(BEGIN) != 1 or current.count(END) != 1:
        print("ERROR: relations.md must contain exactly one BEGIN and one END marker.")
        ok = False
    want = build_graph_block(cards)
    m = re.search(re.escape(BEGIN) + r"(.*?)" + re.escape(END), current, re.DOTALL)
    if m:
        if m.group(1).strip("\n") != want:
            print("ERROR: generated graph block drifts from card frontmatter.")
            ok = False
    else:
        print("ERROR: no generated graph block in relations.md.")
        ok = False
    for c in cards:
        body = (REFERENCES / c["file"]).read_text(encoding="utf-8")
        if _CUE_BLOCK_RE.search(body) or _FPF_PATH_RE.search(body):
            print(f"ERROR: {c['file']} repeats a governing-cue block in its body.")
            ok = False
    return ok


def main():
    cards = load_cards()
    if not cards:
        print("ERROR: no card frontmatter found in references/.")
        return 1
    if "--check" in sys.argv:
        ok = check(cards)
        print("relations.md OK" if ok else "relations.md FAILED")
        return 0 if ok else 1
    regenerate(cards)
    print(f"regenerated relations.md ({len(cards)} cards parsed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
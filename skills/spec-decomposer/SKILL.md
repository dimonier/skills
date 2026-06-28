---
name: spec-decomposer
description: |
  Spec-Decomposer: splits monolithic framework specifications (FPF/DPF/LPF) into
  atomic skill reference files. Use when: decomposing a framework monolith into
  skill references, updating references/ after monolith changes, or setting up a new
  DPF/LPF skill from a monolith. Depends on fpf-core, dpf-fpf-literacy, dpf-lfw-architecture.
---

# DPF: Spec-Decomposer

**Depends on:** `fpf-core`, `dpf-fpf-literacy`, `dpf-lfw-architecture`
**Bounded context:** Decomposing monolithic framework specs into LFW skills
**Source of truth:** `assets/SpecDecomposer-dpf.md`

## Quick Start: Decompose a Monolith

```bash
# For DPF/LPF monoliths (sections 1-10 structure):
python scripts/decompose_dpf.py <monolith.md> --skills-dir <output-skill-dir>

# For FPF monoliths (:End-delimited patterns):
python scripts/decompose_fpf.py <monolith.md> --skills-dir <output-skill-dir>

# Preview without writing:
python scripts/decompose_fpf.py <monolith.md> --skills-dir <output-skill-dir> --dry-run
```

The agent reads the monolith header, determines the type (FPF vs DPF), and invokes the correct script.
Output is a complete skill: `references/*.md` + `INDEX.md` + (for DPF) `relations.md`.

## When to load which pattern

| Situation | Load | Governing cues |
|---|---|---|
| Unclear what to extract from monolith | `references/unit-recognition.md` | C.22.2, E.8, E.4.DPF |
| Need to determine problem card boundaries | `references/boundary-detection.md` | C.22.2, E.8 |
| Need reference file format | `references/reference-file-format.md` | C.33, E.17.EFP, E.4.PFAD |
| Need to convert governing-pattern links | `references/governing-cue-conversion.md` | E.5.3, E.4.PFR |
| Need to generate INDEX.md | `references/index-generation.md` | C.33 |
| Need to extract relation records | `references/relations-extraction.md` | E.4.PFR |
| Need to update SKILL.md after decomposition | `references/dispatcher-update.md` | EWA.SkillDispatcher |
| Agent tries to read monolith instead of references | `references/carrier-split.md` | EWA.MonolithInSkill |
| References out of sync with monolith | `references/sync-discipline.md` | EWA.MonolithInSkill, G.11 |
| Need to decide what to automate | `references/automation-boundary.md` | E.16, G.2 |

## Source for Agent vs Human

- **Agent**: always use `references/`. Do NOT read `assets/SpecDecomposer-dpf.md`.
- **Human**: read and edit the canonical monolith `assets/SpecDecomposer-dpf.md`. After edits, run `scripts/decompose_dpf.py` to rebuild `references/`.

## References Status

**Ready** — 10 problem cards + INDEX + relations + scripts.

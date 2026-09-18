# Pattern Language as Agent Skill — Relation Records

> **Generated projection — do not hand-edit the graph block.** The graph has a single
> authored home: each card's frontmatter `dependencies` — FPF content edges
> (`builds_on`/`coordinates_with`) and local Specialization (`specializes`, authored on
> the **child** side; the inverse `specialized_by` is derived here and is never
> authored). This file is the derived, readable map of the **intra-LPF Specialization
> graph only**; FPF content edges are **not** repeated here — they live only in the
> frontmatter. Rebuilt by `scripts/build_relations.py` (`E.4.PFR:3.2`: derived views
> cite one assertion and are never maintained independently). Run
> `python scripts/build_relations.py` after changing frontmatter; `--check` fails on
> drift. Cards' `:12 Relations` carry only a pointer to the frontmatter.
>
> **Relation functions (canon).** Edges use only `E.4.PFR:3.3` functions:
> `builds_on`, `coordinates_with`, `specializes`/`specialized_by`. `governs` /
> `applies-to` / `→ *all cards*` is **not** an edge — it is a content fact written as
> prose, not a graph row.
>
> **Direction.** `specializes` = child (narrower) → parent.

## Source / edition citation

- Governing method: FPF `E.4.DPF` (+ `E.4.PFAD`, `E.4.PFR`, `E.8`, `E.4.DPF.DA`),
  available as the `fpf-core` skill.
- Carrier mechanics: `create-agent-skill` (a skill dependency, not an FPF pattern).
- A self-sufficient DPF (`PLAS.SelfSufficient`) carries no FPF edges by design.

## Dependency graph

<!-- BEGIN GENERATED GRAPH -->
### Specialization — authored (`specializes`, child → parent)

| From (child) | Relation | To (parent) |
|---|---|---|
| `PLAS.CompactedProjection` | `specializes` | `PLAS.PatternBody` |
| `PLAS.CompactedProjection` | `specializes` | `PLAS.SkillLayout` |
| `PLAS.Dispatcher` | `specializes` | `PLAS.SkillLayout` |
| `PLAS.GoverningCues` | `specializes` | `PLAS.PatternBody` |
| `PLAS.PatternBody` | `specializes` | `PLAS.SkillLayout` |
| `PLAS.SelfSufficient` | `specializes` | `PLAS.EntryRoute` |
| `PLAS.SelfSufficient` | `specializes` | `PLAS.SkillLayout` |
| `PLAS.SkillLayout` | `specializes` | `PLAS.EntryRoute` |

### Specialization — derived inverse (`specialized_by`, parent → child)

| From (parent) | Relation | To (child) |
|---|---|---|
| `PLAS.EntryRoute` | `specialized_by` | `PLAS.SelfSufficient` |
| `PLAS.EntryRoute` | `specialized_by` | `PLAS.SkillLayout` |
| `PLAS.PatternBody` | `specialized_by` | `PLAS.CompactedProjection` |
| `PLAS.PatternBody` | `specialized_by` | `PLAS.GoverningCues` |
| `PLAS.SkillLayout` | `specialized_by` | `PLAS.CompactedProjection` |
| `PLAS.SkillLayout` | `specialized_by` | `PLAS.Dispatcher` |
| `PLAS.SkillLayout` | `specialized_by` | `PLAS.PatternBody` |
| `PLAS.SkillLayout` | `specialized_by` | `PLAS.SelfSufficient` |
<!-- END GENERATED GRAPH -->

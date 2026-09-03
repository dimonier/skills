# Pattern Language as Agent Skill — Relation Records

> **Canonical home.** This file is the canonical home for the source/edition/
> dependency citation and the dependency graph. The same graph appears in three
> views — each card's frontmatter `dependencies` (machine-readable), each card's
> `:12 Relations` (human-readable), and this file (the global map). All three must
> agree in membership and edge direction; change one → change all three.
>
> **Edge direction.** A row reads `From → To` = "From depends on / is placed by /
> applies to To". A `builds_on` edge is written as "dependent pattern → what it
> builds on". SKILL.md carries only a one-line pointer here.

| From (→) | To | Relation function |
|---|---|---|
| `PLAS.EntryRoute` | `PLAS.SkillLayout` | A "new/revised framework" outcome selects the single-surface skill layout (access-facing carrier bearing the edition) |
| `PLAS.EntryRoute` | `PLAS.SelfSufficient` | A `self-sufficient` scope routes authoring to the self-sufficient variant |
| `PLAS.SkillLayout` | `PLAS.Dispatcher` | Layout places the dispatcher at `SKILL.md` |
| `PLAS.SkillLayout` | `PLAS.PatternBody` | Layout places pattern bodies in `references/` |
| `PLAS.PatternBody` | `PLAS.GoverningCues` | Each body carries governing-pattern cues to FPF |
| `PLAS.Naming` | → *all pattern cards* | Naming applies to the skill name and every PatternID |
| `PLAS.QualityAndRefresh` | → *all pattern cards* | Quality/refresh applies to every card |

The dependency chain is unidirectional (`E.5.3`): `pattern-language-as-agent-skill` → `FPF` →
(nothing). `create-agent-skill` is a skill dependency for carrier mechanics, not
an FPF pattern. A self-sufficient DPF (`PLAS.SelfSufficient`) carries no FPF edges
by design; its single source of truth and dependencies are pinned here instead.

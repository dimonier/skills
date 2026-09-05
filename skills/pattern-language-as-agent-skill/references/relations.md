# Pattern Language as Agent Skill — Relation Records

> **Canonical home — the intra-LPF graph.** This file is the canonical home for the
> source/edition/dependency citation and for the *intra-LPF* dependency graph (edges
> between local `PLAS.*` patterns). **FPF-dependency edges are NOT here** — they live
> in each card's frontmatter `dependencies` (`builds_on`, `coordinates_with`) and in
> the card's "Governing FPF patterns" block. LPF-specialization (`specialized_by`) is
> recorded in frontmatter/`:12` and mirrored here. Change one view → change all.
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
| `PLAS.SkillLayout` | `PLAS.SelfSufficient` | The self-sufficient variant reuses the layout with the FPF-governing layer dropped |
| `PLAS.PatternBody` | `PLAS.GoverningCues` | Each body carries governing-pattern cues to FPF |
| `PLAS.Naming` | → *all pattern cards* | Naming applies to the skill name and every PatternID |
| `PLAS.QualityAndRefresh` | → *all pattern cards* | Quality/refresh applies to every card |

The dependency chain is unidirectional (`E.5.3`): `pattern-language-as-agent-skill` → `FPF` →
(nothing). `create-agent-skill` is a skill dependency for carrier mechanics, not
an FPF pattern. A self-sufficient DPF (`PLAS.SelfSufficient`) carries no FPF edges
by design; its single source of truth and dependencies are pinned here instead.

---
name: pattern-language-as-agent-skill
description: |
  Author and improve a Domain Principle Framework (DPF) or Local Practices
  Framework (LPF) directly in Agent-skill form (SKILL.md + references/). Use when
  creating, revising, or maintaining a DPF/LPF as a skill, or when the user mentions
  "pattern language as agent skill".
---

# Pattern Language as Agent Skill (PLAS)

**Depends on:** FPF (governing method `E.4.DPF` + its coordinates; available as the `fpf-core` skill), `create-agent-skill` (skill carrier mechanics)
**Bounded context:** authoring, using, and evolving a DPF or LPF whose sole carrier is an Agent skill
**Edition carrier = skill:** `references/*.md` are the canonical pattern bodies — an access-facing carrier bearing the edition; there is no monolith and no reader-facing publication form (see `references/PLAS.SkillLayout.md`).

## When to load which pattern

| Situation | Load |
|---|---|
| Deciding whether and what to author as a DPF-skill (cold start) | `references/PLAS.EntryRoute.md` |
| Authoring a DPF-skill with no FPF dependency (self-sufficient variant) | `references/PLAS.SelfSufficient.md` |
| Authoring/evaluating a compacted (minified) runtime projection with episteme-block bodies | `references/PLAS.CompactedProjection.md` |
| Setting up the skill directory layout and the single-surface decision | `references/PLAS.SkillLayout.md` |
| Writing SKILL.md as a routing-only dispatcher | `references/PLAS.Dispatcher.md` |
| Writing one pattern body in references/ | `references/PLAS.PatternBody.md` |
| Recording a card's FPF dependencies (frontmatter) | `references/PLAS.GoverningCues.md` |
| Naming the skill and PatternIDs | `references/PLAS.Naming.md` |
| Evaluating, improving, refreshing a DPF-skill | `references/PLAS.QualityAndRefresh.md` |

## Navigation rule

First load `references/PLAS.EntryRoute.md` — it decides whether a DPF-skill is
the right outcome at all and fixes the authoring scenario (FPF-grounded vs
self-sufficient; from-scratch vs external-standard). The self-sufficient variant
routes to `references/PLAS.SelfSufficient.md`; a deliberately minified carrier routes
to `references/PLAS.CompactedProjection.md` (episteme-block bodies, allow-list/
delete-list, compacted readiness profile). Then `references/PLAS.SkillLayout.md`
for the single-surface decision and directory layout. Only then the mechanics cards
(Dispatcher → PatternBody → GoverningCues → Naming), with QualityAndRefresh
closing the loop.

## Lookup rules

- **Index first, then "no".** Before looking for a pattern, check
  `references/INDEX.md`. If the id is not listed there, the pattern does not
  exist — answer "no"; do not open files searching for it.
- **Read once.** Once a file has been read, do not open it again; refer to what
  was already read.

## Source (single surface)

`references/` IS the canonical source. Both the agent and the human author read
and edit `references/*.md` directly. There is no `assets/` monolith and no
reader-facing publication form to rebuild. A **compacted runtime projection**
(`references/PLAS.CompactedProjection.md`) is a legitimate second body form — cards
render as `episteme` blocks instead of `E.8` bodies — but it remains a projection
that names its canonical source; it never becomes the source of truth. The dependency
graph has one authored home
— each card's frontmatter `dependencies`; `references/relations.md` is a generated
projection of the **intra-LPF Specialization** graph (`scripts/build_relations.py`),
never hand-edited. FPF content edges and governing cues live **only** in the
frontmatter — not repeated in card bodies or in `relations.md`. Carrier mechanics
follow `create-agent-skill`.

## references/ status

**Status levels** — 9 pattern cards + INDEX + relations. Bodies are `E.8` bodies; a card's
frontmatter `status` carries the **level** (`seed`/`stable`), **not** the readiness mode.
Five bodies carry `stable` (`PLAS.Dispatcher`, `PLAS.PatternBody`, `PLAS.QualityAndRefresh`,
`PLAS.SelfSufficient`, `PLAS.SkillLayout`): each has a per-coordinate `E.21` result and at
least two feedback-driven repairs in the trailing month — the card was repaired because a
real skill applied it. Four stay `seed` with the reason named: `PLAS.EntryRoute`,
`PLAS.GoverningCues`, `PLAS.Naming` (no repair in that window, not an unevaluated card) and
`PLAS.CompactedProjection` (authored after the `E.21` per-coordinate pass, so it has no
`E.21` result yet — repairs alone do not promote it).

**Readiness mode (declared collectively, per package):** `source-faithful` —
faithful to FPF (`E.4.DPF`, `E.8`, `E.4.PFR`) + `create-agent-skill`; **not**
`case-validated`. The package passed the per-coordinate `E.21` evaluation and four
heterogeneous applications; `case-validated` is withheld because the bodies still lack a
filled worked case, a counter-case and transfer coverage, one completed `E.8:11`
comparison, and the FPF edition is not yet pinned. This follows FPF: a card's `status`
is the pattern status (`Stable`/`Draft`), while package adequacy is a separate
aggregate result (`E.4.DPF.DA:4.5` `DPFPackageAdequacyStatus`); no per-card
`readiness:` key is used (`PLAS.PatternBody:4` item 6, CC-PB.5).

**Exception — self-sufficient cards.** A self-sufficient DPF
(`references/PLAS.SelfSufficient.md`) has no FPF-governed pattern-status level, so its
card carries the explicit readiness mode in `status` (`status: source-faithful` /
`status: case-validated`) instead — the documented exception to `CC-PB.5`.

**Carrier profile — compacted projection.** A compacted runtime projection
(`references/PLAS.CompactedProjection.md`) is a second legitimate carrier form: its
bodies are `episteme` blocks, not `E.8` bodies. It declares the mode **only
collectively** (the package is integral, so cards cannot diverge), but reads the
`source-faithful` threshold against the **compacted** profile (runtime allow-list
present + LEAK/DROP-free split + complete routing + source/edition citation, plus the
`Grounding (FPF)` slot for a non-self-sufficient carrier) instead of the
full-structure threshold. The `E.8`-section CCs are marked N/A for this carrier; a
compacted card carries **no frontmatter** — identity is the filename stem + body H1,
local links are `Continues`/`Reopen`, and the FPF link is a single in-block
`Grounding (FPF)` slot. The dependency graph and provenance live in the canonical
source, not in the projection.

**Provenance of the last pass.** A wording-pass (`PLAS.QualityAndRefresh:4` item 3,
`CC-QR.8`) over every hand-authored body and this file ran on 2026-10-13; it produced the
craft-rule citation rule, the source-naming rule, and the `:5` marker and status
actualizations. Before/after evidence for disputed passages stays in the project vault.

**Self-assessment (reflexive):** this framework runs its own loop. Passed: `E.4.PFAD`
outcome + `E.9` DRR (process state held outside the skill), coverage map and representative
application, four heterogeneous applications, and a per-coordinate `E.21` pass. Not passed,
disclosed: `CC-ER.1` — the cold-reader route was run as later probes, not before the first
bodies were drafted; `CC-QR.2` for `PLAS.CompactedProjection` — authored after the `E.21`
pass, so it has no per-coordinate result yet; the FPF edition is not pinned, so
currentness rests on the resolver line rather than a version; and the bodies still lack a
filled worked case with counter-case and transfer coverage.

## Guardrails

When a judgment is ambiguous — dropping or widening source content, placing an
attachment, renaming a marker beyond the language rule of `PLAS.PatternBody:4` item 3
(`CC-PB.9`), or any choice that could diverge from the owner's
intent — **ask the owner before acting**; do not resolve it silently. This applies
both when authoring a new DPF-skill and when revising an existing one.

- **Deployment is owner-owned.** The authoring agent edits only the repo carrier;
  the installed copy in the user-level skills directory is read-only and is synced
  exclusively by the owner (`PLAS.SkillLayout:4` item 12).

## Evolution

If the user is dissatisfied with the result or clarifies the process, offer to
update this skill — its `description`, routing table, or a `references/` body.
Evolving the DPF content itself follows `references/PLAS.QualityAndRefresh.md`.

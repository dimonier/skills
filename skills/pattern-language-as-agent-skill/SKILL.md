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

**First seed** — 9 pattern cards + INDEX + relations. Pattern bodies are draft
`E.8` bodies marked `seed` (level only); a card's frontmatter `status` carries the
level (`seed`/`stable`), **not** the readiness mode. They stay `seed` until they
pass `E.21` / `E.4.DPF.DA` (see `references/PLAS.QualityAndRefresh.md`).

**Readiness mode (declared collectively, per package):** `source-faithful` —
faithful to FPF (`E.4.DPF`, `E.8`, `E.4.PFR`) + `create-agent-skill`; **not**
`case-validated` (no heterogeneous cases yet). This follows FPF: a card's `status`
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

**Self-assessment (reflexive):** this framework has not yet passed its own
`PLAS.EntryRoute` CC-ER.1–6 — no `E.4.PFAD` answer, no `E.9` DRR, no coverage map,
no representative application, and the authoring-scenario axes are declared but not
yet evaluated. Disclosed as an honest first-seed gap, not silently omitted.

## Guardrails

When a judgment is ambiguous — dropping source content, placing an attachment,
translating or renaming markers, or any choice that could diverge from the owner's
intent — **ask the owner before acting**; do not resolve it silently. This applies
both when authoring a new DPF-skill and when revising an existing one.

- **Deployment is owner-owned.** The authoring agent edits only the repo carrier;
  the installed copy in the user-level skills directory is read-only and is synced
  exclusively by the owner (`PLAS.SkillLayout:4` item 12).

## Evolution

If the user is dissatisfied with the result or clarifies the process, offer to
update this skill — its `description`, routing table, or a `references/` body.
Evolving the DPF content itself follows `references/PLAS.QualityAndRefresh.md`.

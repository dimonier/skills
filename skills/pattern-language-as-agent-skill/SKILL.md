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

| Situation | Load | Governing cues (FPF) |
|---|---|---|
| Deciding whether and what to author as a DPF-skill (cold start) | `references/PLAS.EntryRoute.md` | E.4.DPF, E.4.PFAD, E.9, E.4.DPF.DA |
| Authoring a DPF-skill with no FPF dependency (self-sufficient variant) | `references/PLAS.SelfSufficient.md` | none — create-agent-skill (skill dependency) |
| Setting up the skill directory layout and the single-surface decision | `references/PLAS.SkillLayout.md` | E.4.DPF, C.33, C.2.1, E.24.PUB |
| Writing SKILL.md as a routing-only dispatcher | `references/PLAS.Dispatcher.md` | E.4.DPF, E.11 |
| Writing one pattern body in references/ | `references/PLAS.PatternBody.md` | E.8, E.4.DPF, E.21 |
| Naming governing-pattern cues to FPF patterns | `references/PLAS.GoverningCues.md` | E.5.3, E.4.PFR, E.4.DPF |
| Naming the skill and PatternIDs | `references/PLAS.Naming.md` | F.18, F.14, E.4.DPF |
| Evaluating, improving, refreshing a DPF-skill | `references/PLAS.QualityAndRefresh.md` | E.4.DPF.DA, E.21, E.23, G.11, E.22 |

## Navigation rule

First load `references/PLAS.EntryRoute.md` — it decides whether a DPF-skill is
the right outcome at all and fixes the authoring scenario (FPF-grounded vs
self-sufficient; from-scratch vs external-standard). The self-sufficient variant
routes to `references/PLAS.SelfSufficient.md`. Then `references/PLAS.SkillLayout.md`
for the single-surface decision and directory layout. Only then the mechanics cards
(Dispatcher → PatternBody → GoverningCues → Naming), with QualityAndRefresh
closing the loop.

## Source (single surface)

`references/` IS the canonical source. Both the agent and the human author read
and edit `references/*.md` directly. There is no `assets/` monolith and no derived
projection to rebuild or sync. Governing-pattern cues name the governing FPF
patterns; carrier mechanics follow `create-agent-skill`.

## references/ status

**First seed** — 8 pattern cards + INDEX + relations. Pattern bodies are draft
`E.8` bodies, marked `seed` (with an explicit readiness mode) until they pass
`E.21` / `E.4.DPF.DA` (see `references/PLAS.QualityAndRefresh.md`).

**Self-assessment (reflexive):** this framework has not yet passed its own
`PLAS.EntryRoute` CC-ER.1–6 — no `E.4.PFAD` answer, no `E.9` DRR, no coverage map,
no representative application, and the authoring-scenario axes are declared but not
yet evaluated. Readiness mode for every card is `source-faithful` (faithful to FPF +
`create-agent-skill`), not `case-validated`. Disclosed as an honest first-seed gap,
not silently omitted.

## Guardrails

When a judgment is ambiguous — dropping source content, placing an attachment,
translating or renaming markers, or any choice that could diverge from the owner's
intent — **ask the owner before acting**; do not resolve it silently. This applies
both when authoring a new DPF-skill and when revising an existing one.

## Evolution

If the user is dissatisfied with the result or clarifies the process, offer to
update this skill — its `description`, routing table, or a `references/` body.
Evolving the DPF content itself follows `references/PLAS.QualityAndRefresh.md`.

---
name: project-vault
description: >-
  Maintains project state in a markdown vault: a single decision card carrying
  decisions, questions, risks, contradictions as status-based positions
  (open/proposed/accepted). Governs working tracks as the mandatory container for
  work. Use after meetings, decisions; inbox/outbox; vault init, migration.
---

# Project Vault — Compacted Runtime Projection (LPF)

Compacted runtime projection of the canonical `project-vault` skill.
Bodies are `episteme` blocks (F3 hybrid) with no per-card frontmatter; each card's FPF link is an
in-block `Grounding (FPF)` slot. Depends on `fpf-core`. Readiness (collective): `source-faithful`.

## When to load which pattern

| Situation | Load |
|---|---|
| Understand the vault schema: entities, directories, ID allocation, discovery | `references/PV.VaultSchema.md` |
| Process the inbox (transcripts, PDFs, articles, research) | `references/PV.Inbox.md` |
| Update state from a meeting transcript / dialog news (DEC card, open/proposed/accepted) | `references/PV.StateUpdate.md` |
| Bind an external study/article/report two-way | `references/PV.ExternalResearch.md` |
| Manage tracks / continue work in a track | `references/PV.Track.md` |
| Create a track-bound artifact | `references/PV.Artifact.md` |
| Record a substantive step (WRK) | `references/PV.WorkRecord.md` |
| Initialize a new vault (scaffold copy, inbox/outbox creation) | `references/PV.Init.md` |
| Migrate an old vault (retire legacy kinds / directories into DEC card + artifacts) | `references/PV.Migration.md` |
| Send outgoing feedback / a proposal to another system or skill | `references/PV.Outbox.md` |

## Navigation rule

Several usage scenarios — enter per use-case (there is no single linear chain):

- **Update the vault after a meeting/briefing** → `PV.StateUpdate` (as needed
  `PV.VaultSchema` for the schema, `PV.Track` for new signals).
- **Intake** → `PV.Inbox`; route onward to `PV.StateUpdate` / `PV.ExternalResearch`
  / `PV.Track`.
- **Productive work in a track** → `PV.Track`; record steps via `PV.WorkRecord`,
  artifacts via `PV.Artifact`.
- **Initialize a vault** → `PV.Init`.
- **Migrate an old vault** → `PV.Migration`.
- **Send feedback to another system/skill** → `PV.Outbox`; the recipient processes
  it as a normal `PV.Inbox` arrival.

## Guardrails

When a judgment is ambiguous (a decision's status, material binding, a
risk/contradiction wording, any action that may diverge from the owner's intent) —
**ask the owner, do not decide silently**. The remaining constraints are in the
`Checks` slot of each `references/PV.*.md`.

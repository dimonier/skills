---
name: project-vault
description: >-
  Maintains project state in a markdown vault (decisions, open questions, risks,
  contradictions, dependencies) from transcripts, notes, PDFs, or owner chat.
  Governs working tracks as the mandatory container for productive work. Use
  after meetings, briefings, decisions; inbox/outbox; vault init.
---

# Project Vault — Local Practices Framework (LPF)

LPF for the practice "managing project state in a markdown-vault". Users:
the owner (name — in the repo root `AGENTS.md`) + an AI assistant.

## When to load which pattern

| Situation | Load | Governing FPF cues |
|---|---|---|
| Understand the vault schema: entities, directories, ID allocation, discovery | `references/PV.VaultSchema.md` | C.33, C.2.1, E.4.DPF |
| Process the inbox (transcripts, PDFs, articles, research) | `references/PV.Inbox.md` | E.11, C.11 |
| Update state from a meeting transcript / dialog news (DEC/Q/RISK/CON) | `references/PV.StateUpdate.md` | C.32.ADR, E.9, C.11 |
| Bind an external study/article/report two-way | `references/PV.ExternalResearch.md` | E.4.PFR, C.11, G.11 |
| Manage tracks / continue work in a track | `references/PV.Track.md` | C.22.2, G.5, A.15.1, A.15.2, E.23 |
| Create a track-bound artifact | `references/PV.Artifact.md` | A.15.1, A.15.2, E.24.PUB |
| Record a substantive step (WRK) | `references/PV.WorkRecord.md` | A.15.1, E.10 |
| Create a report / assemble the meeting agenda | `references/PV.Report.md` | E.17, E.23, E.9 |
| Initialize a new vault (scaffold copy, inbox/outbox creation) | `references/PV.Init.md` | C.33, E.4.DPF |
| Send outgoing feedback/a proposal to another system or skill | `references/PV.Outbox.md` | C.33, E.11, C.11 |

## Navigation rule

Several usage scenarios — enter per use-case (there is no single linear chain):

- **Update the vault after a meeting/briefing** → start with `PV.StateUpdate` (as
  needed `PV.VaultSchema` for the schema, `PV.Track` for new signals).
- **Intake** → start with `PV.Inbox`; route onward to
  `PV.StateUpdate` / `PV.ExternalResearch` / `PV.Track`.
- **Productive work in a track** → start with `PV.Track`; record steps via
  `PV.WorkRecord`, artifacts via `PV.Artifact`.
- **Initialize a vault** → `PV.Init`.
- **Send feedback to another system/skill** → `PV.Outbox`; the recipient processes
  it as a normal `PV.Inbox` arrival.

## Source (single surface)

`references/` — the canonical source: 10 E.8 pattern bodies + `INDEX.md` +
`relations.md`. There is no monolith; `SKILL.md` is routing only. Edit
`references/*.md` directly. The vault schema changes → edit `PV.VaultSchema`. The
dependency map and source/edition citation — in `references/relations.md`.

## Guardrails

When a judgment is ambiguous (a decision's status, material binding, a risk/
contradiction wording, any action that may diverge from the owner's intent) —
**ask the owner, do not decide silently**. The remaining constraints are in the
pattern bodies (the Conformance Checklist of each `references/PV.*.md`).

## Evolution

If the owner is unhappy with a result or refines the process — propose updating this
skill: its `description`, the routing table, or the body of a `references/*.md`.
The evolution of the LPF content itself follows `references/PLAS.QualityAndRefresh.md`
from the `pattern-language-as-agent-skill` skill. Refresh triggers (when to revisit
this skill — G.11) — in `references/relations.md`; machine frontmatter check before
trusting the skill — `scripts/check_frontmatter.py`.

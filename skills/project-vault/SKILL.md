---
name: project-vault
description: >-
  Maintains project state in a markdown vault (decisions, open questions, risks,
  contradictions) from transcripts, notes, PDFs, or owner chat.
  Governs working tracks as the mandatory container for productive work. Use
  after meetings, briefings, decisions; inbox/outbox; vault init.
---

# Project Vault — Local Practices Framework (LPF)

LPF for the practice "managing project state in a markdown-vault". Users:
the owner (name — in the repo root `AGENTS.md`) + an AI assistant.

## When to load which pattern

| Situation | Load |
|---|---|
| Understand the vault schema: entities, directories, ID allocation, discovery | `references/PV.VaultSchema.md` |
| Process the inbox (transcripts, PDFs, articles, research) | `references/PV.Inbox.md` |
| Update state from a meeting transcript / dialog news (DEC/Q/RISK/CON) | `references/PV.StateUpdate.md` |
| Bind an external study/article/report two-way | `references/PV.ExternalResearch.md` |
| Manage tracks / continue work in a track | `references/PV.Track.md` |
| Create a track-bound artifact | `references/PV.Artifact.md` |
| Record a substantive step (WRK) | `references/PV.WorkRecord.md` |
| Create a report / assemble the meeting agenda | `references/PV.Report.md` |
| Initialize a new vault (scaffold copy, inbox/outbox creation) | `references/PV.Init.md` |
| Send outgoing feedback/a proposal to another system or skill | `references/PV.Outbox.md` |

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
`references/*.md` directly. The vault schema changes → edit `PV.VaultSchema`.

The dependency graph has its single authored home in each card's frontmatter
`dependencies` (FPF content edges + intra-LPF Specialization). `references/relations.md`
is the generated readable projection of the intra-LPF Specialization graph only (FPF
content edges are not repeated there); it is rebuilt by `scripts/build_relations.py`
(`--check` validates) and never hand-edited. The source/edition citation and refresh
triggers live in `references/relations.md`.

## Status

All 10 pattern bodies are `status: seed` (first seed; not yet `E.21`-evaluated).
Readiness mode, declared **collectively** for the package: **`source-faithful`**
(faithful to FPF + the owner's procedural practice), **not** `case-validated` (no
heterogeneous cases yet). Publication-form checks (`E.11.PFP` `PFM1`–`PFM12`) are N/A —
there is no reader-facing publication form for this skill carrier.

## Deployment boundary

The repo's `skill/project-vault/` is the single *editable* carrier; the copy installed
in the user-level skills directory is a *read-only* deployment, synced only by the
owner — never by the authoring agent.

## Guardrails

When a judgment is ambiguous (a decision's status, material binding, a risk/
contradiction wording, any action that may diverge from the owner's intent) —
**ask the owner, do not decide silently**. The remaining constraints are in the
pattern bodies (the Conformance Checklist of each `references/PV.*.md`).

## Evolution

If the owner is unhappy with a result or refines the process — propose updating this
skill: its `description`, the routing table, or the body of a `references/*.md`.
The evolution of the LPF content itself follows `PLAS.QualityAndRefresh` (the
`pattern-language-as-agent-skill` skill dependency), applied directly to the skill
form. A substantive method-feedback signal captured at WRK closure (`PV.WorkRecord`
W.4) is emitted as an outbox proposal (`PV.Outbox`) instead of being lost in the chat.
Refresh triggers (when to revisit this skill — `G.11`) — in `references/relations.md`;
before trusting the skill, run the machine frontmatter check
`scripts/check_frontmatter.py` and the graph check
`python scripts/build_relations.py --check`.

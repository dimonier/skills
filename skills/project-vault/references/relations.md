# Project Vault — Relation Records

> **Canonical home.** This file is the canonical home for the source/edition/
> dependency citation and the dependency graph. The same graph appears in three
> views — each card's frontmatter `dependencies` (machine-readable), each card's
> `:12 Relations` (human-readable), and this file (the global map). All three must
> agree in membership and edge direction; change one → change all three.
>
> **Edge direction.** A row reads `From → To` = "From depends on / is placed by /
> applies to To". A `builds_on` edge is written as "dependent pattern → what it
> builds on". SKILL.md carries only a one-line pointer here.

## Source / edition citation

- **Skill:** `project-vault` (LPF — Local Practices Framework).
- **Authoring scenario (EntryRoute):** outcome (a) "revise framework";
  axes — `FPF-grounded` (relies on FPF Core) and `language-from-scratch`
  (the canonical carrier is this skill's own `references/*.md`; no externally
  published projection document exists).
- **Field / field boundary:** the practice "managing project state in a
  markdown-vault": capturing state from sources (transcripts/dialogues), binding
  external research, track lifecycle, work records, artifact creation, report
  creation, schema and ID integrity.
- **Dependency chain (unidirectional, `E.5.3`):** `project-vault` → `FPF` → (nothing).
  `create-agent-skill` — a skill dependency on carrier mechanics, not an FPF pattern.
  `pdf2md` — a skill dependency of `PV.Inbox` (PDF conversion).
- **Readiness:** all 10 patterns are `status: seed`, readiness mode `source-faithful`
  (faithful to the approved source — FPF + the owner's procedural practice);
  not `case-validated`.

## Refresh triggers (G.11)

Revisit this skill (reopen → refresh per `G.11`) on any of the following:

1. **Source change** (`E.4.PFR`, G.11 `EditionPinChange`): a revision of the FPF Core
   patterns that the governing-cues build on (`E.8`, `E.9`, `C.32.ADR`,
   `C.33`, `C.2.1`, `A.15.1`, `A.15.2`, `G.11`, `F.14`, `F.18`).
2. **Vault schema change** (the field boundary of the practice): a new entity kind,
   a new directory, a new carrier or search tool → edit `PV.VaultSchema` and the
   affected neighbouring bodies.
3. **PLAS change** (`E.4.PFAD` revision): the `pattern-language-as-agent-skill` skill
   changes conformance requirements (E.8 sections, EntryRoute, carrier mechanics).
4. **Local-use telemetry** (G.11 `TelemetryDelta`): the owner reports that the skill
   misfired, is ambiguous, or a weak model (`create-agent-skill` weak-model gate)
   does not follow the steps without invention.
5. **Carrier-mechanics change** (`create-agent-skill`): atomicity, layout, or
   single-surface agreements change.

Minimal revisit route: `E.4.DPF.DA` D1–D12 + `E.21` for the affected bodies
+ a run of `scripts/check_frontmatter.py` — without a full "tsar-track" rebuild.

## Dependency graph

| From (→) | To | Relation function |
|---|---|---|
| `PV.Inbox` | `PV.StateUpdate` | Inbox routes transcripts/meeting protocols to state update |
| `PV.Inbox` | `PV.ExternalResearch` | Inbox routes external research to two-way binding |
| `PV.Inbox` | `PV.Track` | Inbox files valuable artifacts into tracks |
| `PV.StateUpdate` | `PV.VaultSchema` | Entity creation and ID allocation follow the schema |
| `PV.StateUpdate` | `PV.Track` | Operational signals from a source open/change tracks |
| `PV.ExternalResearch` | `PV.StateUpdate` | An external signal may require a new decision/risk |
| `PV.ExternalResearch` | `PV.VaultSchema` | Signals are written into vault entities |
| `PV.Track` | `PV.VaultSchema` | Tracks are vault entities with an auto-index |
| `PV.Artifact` | `PV.Track` | An artifact is created bound to a track |
| `PV.WorkRecord` | `PV.Track` | A WRK captures a step within a track |
| `PV.WorkRecord` | `PV.VaultSchema` | WRKs are `work/` entities with an auto-index |
| `PV.Report` | `PV.StateUpdate` | The agenda takes `proposed`/`deferred` decision slots |
| `PV.Report` | `PV.VaultSchema` | A report is a derived summary in `reports/` |
| `PV.Outbox` | `PV.Inbox` | Outbox messages transfer into the recipient's inbox |
| `PV.Outbox` | `PV.VaultSchema` | `outbox/` is a channel directory with a transient message kind |
| `PV.Init` | `PV.VaultSchema` | Init reproduces the schema from the scaffold |
| `PV.Init` | `PV.Inbox` | Init creates `inbox/` at the repository root |
| `PV.Init` | `PV.Outbox` | Init creates `outbox/` at the repository root |

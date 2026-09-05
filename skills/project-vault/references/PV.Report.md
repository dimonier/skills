---
id: PV.Report
title: "Report creation: derived summaries on request, incl. the meeting agenda"
status: seed
readiness: source-faithful
keywords: [report, derived-summary, agenda, meeting, off-limits, request, projection]
dependencies:
  builds_on:
    - E.17
    - E.23
    - E.9
  coordinates_with:
    - A.15.2
---

## PV.Report - Report creation: derived summaries on request, incl. the meeting agenda

> **Trigger:** When the owner asks for a derived summary of the vault — a report (`project-vault/reports/YYYY-MM-DD-slug.md`), or the next-meeting agenda in particular.
> **Governing FPF patterns:**
>   → E.17 (a report is a description/view of entities, not a new entity kind)
>   → E.23 (improvement cycle — returning to open items)
>   → E.9 (DRR — returning `proposed`/`deferred` to a decision, for the agenda's slots)
> **Skill dependencies:**
>   → none

---

### PV.Report:1 - Problem frame

Use this pattern to create a report — a derived summary of the vault, produced only
on request — in general, and to assemble the next-meeting agenda as its canonical
special case.

### PV.Report:2 - Problem

A report assembled "from the head" (or composed in advance) skips the vault's
state: it either duplicates entities that are already atomic, or invents items not
present in the vault. Reports must be derived from the vault, not composed — and
they must not multiply into new entity kinds (they are descriptions, not
decisions/risks/questions/contradictions).

### PV.Report:3 - Forces

| Force | Settlement |
|---|---|
| Derivable vs composed | A report is assembled from the vault's entities; it never introduces new entity kinds. |
| One report kind vs many | Reports vary (agenda, status, executive summary, ...) → no fixed template; one dated file per report. |
| Off-limits vs request | Reports — only on the owner's explicit request. |
| Derived vs atomic | A report is a projection; the underlying entities stay atomic and unchanged. |

### PV.Report:4 - Solution

**R.1 — general report creation.**

1. Only on the owner's explicit request.
2. Derive the content from the vault: open entities (`grep`/`SocratiCode`), tracks,
   decisions, dependencies — the report is a projection of the current state.
3. Write `project-vault/reports/YYYY-MM-DD-slug.md` — one dated, self-contained
   file; no fixed template (report kinds vary).
4. A report does not create/close entities. If the material introduces a new
   decision/risk/question/contradiction — route it to `PV.StateUpdate`/`PV.Track`
   instead of a report.

**R.2 — the meeting agenda (the canonical report kind).**

Assemble from the vault's open items — top questions, blockers, contradictions,
risks; slots from `project-vault/decisions/` (close `proposed`, return `deferred`
with an approaching `revisit_by`) — and write it as
`project-vault/reports/YYYY-MM-DD-agenda.md`.

**When blocked:**
- No open questions/risks/contradictions → mark "agenda empty — no open items".

### PV.Report:5 - Archetypal Grounding

**Show.** In this project the next-meeting agenda is assembled on request from the
open Q/RISK/CON and the `proposed`/`deferred` decision slots — a projection, not a
composed document.

### PV.Report:6 - Bias-Annotation

The temptation is to prepare a report in advance "just in case", even without a
request, or to write it detached from the vault's state. The symmetric temptation
is to let a report create new entities on the side. Counterweights: off-limits
without a request, derivation from the vault, and no new entity kinds.

### PV.Report:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-RP.1 | A report is created/updated only on an explicit request. |
| CC-RP.2 | The report is derived from the vault's entities; it introduces no new entity kind. |
| CC-RP.3 | A report is one dated file `reports/YYYY-MM-DD-slug.md`; no fixed template. |
| CC-RP.4 | The agenda is assembled from the open Q/RISK/CON + `proposed`/`deferred` decision slots. |
| CC-RP.5 | An empty agenda — "agenda empty — no open items". |

### PV.Report:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| A report without a request | Do not create/update. |
| A report that duplicates/creates entities | Derive; route new signals to `PV.StateUpdate`/`PV.Track`. |
| An agenda not from the vault | Derive from the open entities. |
| A fixed report template | No template; reports vary. |

### PV.Report:9 - Consequences

The report always matches the current vault state and stays off-limits without a
request. The agenda remains the canonical report kind; other reports are ad hoc.
Returning `deferred`/`proposed` decisions — the `E.9` mechanism (revisit).

### PV.Report:10 - Rationale

`E.17` — a report is a description/view of entities, not a new entity kind; `E.23` —
the cycle of returning to open items (the report surfaces them); `E.9` — decisions
with `revisit_by` return to the agenda for confirmation/cancellation. Hence — the
report as a projection of the vault's state, not a separately composed document.

### PV.Report:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.17` (description/view on a record) | Adopt | A report as a derived view, no new entities | Reopen on `E.17` revision |
| FPF `E.23` (return cycle) | Adopt | Reports surface open items | Reopen on `E.23` revision |
| FPF `E.9` (DRR revisit) | Adopt | `proposed`/`deferred` slots with `revisit_by` in the agenda | Reopen on `E.9` revision |

Best-known line: the report as a projection of the open state. Rejected rival: "a
report composed in advance / detached from the vault" — rejected.

### PV.Report:12 - Relations

- **Builds on:** `E.17` (derived view), `E.23` (return to open items), `E.9` (decision revisit).
- **Coordinates with:** `A.15.2` (planning).
- **Applies to:** `PV.StateUpdate` (the agenda takes `proposed`/`deferred` slots), `PV.VaultSchema` (the `reports/` directory).

### PV.Report:End

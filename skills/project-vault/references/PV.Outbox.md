---
id: PV.Outbox
title: "Outgoing feedback: outbox procedure for sending notes to other systems/skills"
status: seed
readiness: source-faithful
keywords: [outbox, feedback, outgoing, send, transfer, message, addressee]
dependencies:
  builds_on:
    - E.11
    - C.33
    - C.11
  coordinates_with:
    - A.15.1
---

## PV.Outbox - Outgoing feedback: outbox procedure for sending notes to other systems/skills

> **Trigger:** When feedback, a proposal, or a note arises that is addressed to another system or skill, and it must be captured and delivered instead of evaporating after the dialog.
> **Governing FPF patterns:**
>   → E.11 (practical entry: a named send-feedback entry-path)
>   → C.33 (kind discipline: `outbox/` and the message as a distinct kind)
>   → C.11 (capture fidelity: write the feedback faithfully before transfer)
> **Skill dependencies:**
>   → none

---

### PV.Outbox:1 - Problem frame

Use this pattern to record outgoing feedback or proposals to other systems/skills
as one message file in `outbox/`, transfer the message to the recipient's `inbox/`,
and mark it `sent` — so the recipient processes it as an ordinary inbox arrival.

### PV.Outbox:2 - Problem

Outgoing feedback to other systems or skills has no carrier: there is `inbox/` for
incoming material but nothing for outgoing. Feedback that arises in a dialog
(e.g. a proposal addressed to another project's skill) is lost after the dialog —
the recipient never learns what was proposed, and the sender has no record.

### PV.Outbox:3 - Forces

| Force | Settlement |
|---|---|
| Incoming vs outgoing | `inbox/` receives, `outbox/` sends; both are one message per file. |
| Transient vs durable | A message is a transient file with `status: pending → sent`; no monotonic ID. |
| Capture vs transfer | The sender captures into its own `outbox/`, then transfers to the recipient's `inbox/`. |

### PV.Outbox:4 - Solution

1. **Capture.** When feedback/a proposal addressed to another system or skill
   arises, write one `.md` file in `outbox/` (one file = one message) with frontmatter
   `created`, `addressee`, `source_project`, `source_context`, and `status: pending`.
   Note the send in a WRK (the current track).
2. **Transfer.** The author manually moves the message into the recipient's `inbox/`
   (or the recipient fetches it), clearing their own `outbox/`. On transfer, set
   `status: sent` if a record is kept, or remove the file.
3. **Reception.** For the recipient this is an ordinary new arrival in `inbox/` —
   process it by the standard `PV.Inbox` procedure.
4. **Discovery.** `outbox/` has no `_index.md` and its messages have no monotonic ID;
   find them via `ls` or `grep` (e.g. `grep -l "^status: pending" outbox/`).

### PV.Outbox:5 - Archetypal Grounding

**Show.** The motivating case: the knowy project (dialog 2026-09-05) put a proposal
addressed to the `project-vault` skill into its own `outbox/`; the proposal arrived
in this project's `inbox/` and was routed to a track by `PV.Inbox`.

### PV.Outbox:6 - Bias-Annotation

The temptation is to give a message a monotonic ID like DEC/TRK, over-engineering a
transient object; the symmetric temptation is to leave feedback in the chat and
forget to clear `outbox/` after transfer. Counterweights: no ID, a transient
`pending → sent` status, and clearing `outbox/` on transfer.

### PV.Outbox:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-OB.1 | One message = one file in `outbox/` with `created`/`addressee`/`source_project`/`source_context`/`status`. |
| CC-OB.2 | No monotonic ID and no `_index.md` in `outbox/`; discovery via `ls`/`grep`. |
| CC-OB.3 | `status` flips `pending → sent` on transfer; `outbox/` is cleared after transfer. |
| CC-OB.4 | The recipient processes the transferred message as an ordinary `PV.Inbox` arrival. |

### PV.Outbox:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Outgoing feedback left in the chat (no file) | Write one message file in `outbox/`. |
| A monotonic ID or `_index.md` for `outbox/` | No ID, no index; a transient file. |
| `outbox/` not cleared after transfer | Clear it on transfer. |
| The recipient treats it as special | It is an ordinary inbox arrival. |

### PV.Outbox:9 - Consequences

Outgoing feedback becomes traceable and two-way, but requires the
write-then-transfer-then-clear discipline. The message is a transient object, not a
durable vault entity (unlike DEC/Q/RISK/CON/TRK).

### PV.Outbox:10 - Rationale

`C.33` kind discipline: `outbox/` is a separate kind directory and the message is a
transient kind, distinct from the monotonic-ID entities. `E.11` practical entry: a
named send-feedback path instead of ad-hoc chat. `C.11` capture fidelity: the
feedback is written faithfully before it is transferred.

### PV.Outbox:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `C.33` (kind discipline) | Adopt | `outbox/` + the message as a transient kind | Reopen on `C.33` revision |
| FPF `E.11` (practical entry) | Adopt | The send-feedback entry path | Reopen on `E.11` revision |
| FPF `C.11` (capture fidelity) | Adopt | Faithful capture before transfer | Reopen on `C.11` revision |

Best-known line: a symmetric outgoing channel to `inbox/`. Rejected rival:
"feedback in the chat only" — rejected as untraceable.

### PV.Outbox:12 - Relations

- **Builds on:** `C.33` (kind discipline), `E.11` (practical entry), `C.11` (capture fidelity).
- **Coordinates with:** `A.15.1` (execution).
- **Applies to:** `PV.Inbox` (transfers into the recipient's `inbox/`), `PV.VaultSchema` (`outbox/` as a directory).
- **Applied by:** `PV.Init` (creates `outbox/`).

### PV.Outbox:End

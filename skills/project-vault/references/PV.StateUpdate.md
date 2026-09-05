---
id: PV.StateUpdate
title: "State update from a source: DEC/Q/RISK/CON from a transcript or dialogue"
status: seed
readiness: source-faithful
keywords: [state-update, transcript, dialogue, decision, DEC, ADR, question, risk, contradiction]
dependencies:
  builds_on:
    - C.32.ADR
    - E.9
    - C.11
  coordinates_with:
    - C.18
    - C.19
    - A.3.2
---

## PV.StateUpdate - State update from a source: DEC/Q/RISK/CON from a transcript or dialogue

> **Trigger:** When a new state source appears — a meeting transcript (Input 1) or dialog news without a transcript (Input 2) — and the vault must be brought in line.
> **Governing FPF patterns:**
>   → C.32.ADR (decision-record discipline: problem frame → outcome → consequences → confirmation/supersession)
>   → E.9 (DRR: one bounded decision, input filter)
>   → C.11 (any new claim — with a reference to the source)
> **Skill dependencies:**
>   → none

---

### PV.StateUpdate:1 - Problem frame

Use this pattern to turn a meeting transcript or a dialogue briefing into a
verifiable vault update: capture the source, create/close atomic entities
(DEC/Q/RISK/CON), and reconcile against the active open-question registry without
inventing facts absent from the source.

### PV.StateUpdate:2 - Problem

A source can be thin or contradictory: decision formulations are vague, a decision
is mentioned but not approved, a contradiction is suspected but not asserted. If
entities are filled in "by the spirit of it", the vault fills up with unconfirmed
decisions and unchecked facts. If "choice" is not distinguished from "paraphrase",
the decision canon clogs with junk entries.

### PV.StateUpdate:3 - Forces

| Force | Settlement |
|---|---|
| Completeness vs verifiability | Record only what is verifiable from the source; decision/question/risk formulations — only in atomic files. |
| Accepted vs proposed | `accepted` — only on explicit approval in the source; otherwise `proposed` + "pending owner confirmation". |
| Choice vs paraphrase | DEC — only for a bounded architectural choice with consequences; editorial/summary — as context in the capture header, no DEC. |
| One vs several | One decision = one DEC; independent topics are not merged. |

### PV.StateUpdate:4 - Solution

**Input 1 — meeting transcript.**

1. Save the source into `project-vault/sources/captures/`.
2. Write 2–3 lines of summary "what the source is about" (context) into the capture header.
3. **Open-question registry in context:** find the active open questions via
   `grep -l "^status: open" project-vault/open-questions/*.md`, read the relevant
   ones. If the source gives a signal on an active Q (closes / partially answers /
   contradicts) — write it into the Q file (`status`/note + `sources` pointing to
   the capture). A negative outcome ("no signals") is not recorded.
4. For **key** decisions — create/update `project-vault/decisions/DEC-NNNN.md`
   from the template `project-vault/decisions/_template.md`; the DEC's
   `sources` — to the capture. Rules:
   - **Input filter (before creating a DEC):** a DEC only if the statement has
     (a) a bounded *architectural* question, (b) a positively chosen answer that
     changes the target system/design with a long-lived consequence, (c) which a
     future architect can rely on. If the formulation is about the content of a
     working document, an editorial choice, a repetition of an already recorded
     position, or a summary without a choice → record as context in the capture
     header, do not create a DEC.
   - **Fill all sections** of the template; do not invent what is absent — write
     "not discussed" / "unknown" / "not applicable".
   - `decision_type` — one of `adr | org | strategy | scope | process | procurement | product`;
     `characteristic` — only for `decision_type: adr`.
   - "Considered options" ≥ 2 → fill "Option comparison"; one option → "single option".
   - Always fill "Revisit conditions"; `revisit_by` or an open-ended note.
5. Run the common steps (below).

**Input 2 — dialog news (no transcript).**

1. The source is fixed in the entity: a signal/problem/directive → a track (or an
   atomic entity) with a "Signal" section (the direct quote + date + provenance).
2. For key decisions — create/update a DEC with `sources` to the dialog (provenance
   in the frontmatter: `source_kind: user_dialogue`, `evidence_captured_at`).
3. If there are signals to active Qs — write them into the Q files (do not create a
   separate reconciliation record).
4. Run the common steps (below).

**Insufficient input.**
- The transcript is not enough for a meaningful update → a minimal capture header and stop.
- A decision is mentioned but not explicitly approved → `status: proposed` + "pending owner confirmation".
- A contradiction is suspected but not asserted → CON with `status: proposed` + "requires clarification".
- An opinion/preference, not a decision → no DEC; if needed — as context in the capture header.
- The dialog contradicts an existing `accepted` → CON + a `revisit_by` flag on the decision.

**Common steps (after Input 1 or 2).**

1. Creation/closure of atomic entities (DEC, Q, RISK, CON) — the file is created;
   closed ones stay in place with a `status` (no `archive/`).
2. New external blockers → update `project-vault/dependencies.md`.
3. New regulatory/architectural constraints → update `project-vault/state/constraints.md`.
4. **Track maintenance:** the source introduces an operational signal, changes a
   track's status, or closes it:
   - **New signal** → `project-vault/tracks/TRK-NNNN.md` with `status: cue` (template
     `tracks/_template.md`); then `python scripts/vault.py tracks`.
   - **Status change** → update the `status` field in the frontmatter and in the
     track's inline fields. Lifecycle: `cue → problem-framed → method-selected →
     work-planned → in-progress → performed → evaluated`; side transitions:
     `blocked`, `deferred`, `retired` (terminal). Then — `vault.py tracks`.
   - **Track closed/retired** → `status: retired` (stays in `tracks/`); then `vault.py tracks`.
   - **Track unblocked** → return the previous active status; then `vault.py tracks`.
   - Do not create a track for every DEC/RISK/Q — only for operational lines with
     blockers, spanning several related entities.
5. **Assignments to the repo owner:** if the source has an explicit assignment to
   the owner (by name) — only one directly expressed, without invention:
   - Read `project-vault/tracks/_index.md` and pick the most fitting track by topic.
   - Write the assignment as a new item of the numbered list in the track's "Next
     moves" field. With a deadline — `(deadline YYYY-MM-DD)`; if overdue —
     `(deadline YYYY-MM-DD, overdue)`.
   - If the field is called "Next step" (singular) and is already taken — turn it
     into "Next moves" (plural: first item — the previous step, second — the new assignment).
   - Do not create a new track for a personal assignment — always into an existing one.
   - No fitting track → write into the capture header and flag to the owner for resolution.

### PV.StateUpdate:5 - Archetypal Grounding

**Show.** A post-meeting update in this project: the source in `captures/`, a key
architectural decision as an atomic DEC with the input filter, reconciliation with
the open-question registry, an operational signal as a track.

### PV.StateUpdate:6 - Bias-Annotation

The temptation is to raise a decision's status to `accepted` "in the spirit of" the
meeting without explicit approval, and to open a DEC for every statement for the
sake of canon completeness. The DEC input filter (E.9 "cheap stop") and the rule
"accepted only explicitly" are the two counterweights.

### PV.StateUpdate:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-SU.1 | Every new claim — with a reference to the source (capture/dialog). |
| CC-SU.2 | `accepted` — only on explicit approval in the source. |
| CC-SU.3 | Two incompatible formulations — an atomic CON. |
| CC-SU.4 | A DEC is created only after the input filter (bounded architectural choice). |
| CC-SU.5 | The DEC body carries only the DEC-ID and a web-URL; other references — in the frontmatter. |
| CC-SU.6 | A decision change = edit the card + "Revision history", not a duplicate. |

### PV.StateUpdate:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| `accepted` without explicit approval | `proposed` + "pending owner confirmation". |
| DEC for editorial/summary content | Context in the capture header; no DEC. |
| Duplicate DEC on a decision change | Edit the same card + "Revision history". |
| A capture/artifact reference in the DEC body | Only DEC-ID and URL; the rest in the frontmatter. |

### PV.StateUpdate:9 - Consequences

Strict record discipline makes the decision canon a support for a future architect,
but slows down recording and requires an explicit "choice / paraphrase" distinction.
A decision change means an edit with a revision history, not a new file.

### PV.StateUpdate:10 - Rationale

`C.32.ADR` requires problem frame → outcome → consequences → confirmation/supersession;
`E.9` holds a DRR as one bounded decision with an input filter ("cheap stop" for
editorial edits). `C.11` — any claim with a reference. Hence — accepted/proposed,
the DEC input filter, and "do not invent".

### PV.StateUpdate:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `C.32.ADR` (ADR record) | Adopt | DEC template sections, `accepted` only explicitly | Reopen on `C.32.ADR` revision |
| FPF `E.9` (DRR, one bounded decision) | Adopt | DEC input filter, "one topic — one card" | Reopen on `E.9` revision |
| FPF `C.11` (source reference) | Adopt | Guardrail "any claim — with a reference" | Reopen on `C.11` revision |

Best-known line: ADR discipline with an input filter. Rejected rival: "recording
every statement as a decision" — rejected as canon clutter.

### PV.StateUpdate:12 - Relations

- **Builds on:** `C.32.ADR` (decision records), `E.9` (DRR), `C.11` (source).
- **Coordinates with:** `C.18`/`C.19` (probes/comparison), `A.3.2` (method description).
- **Applies to:** `PV.VaultSchema` (entity creation/ID allocation), `PV.Track` (operational signals open/change tracks).
- **Applied by:** `PV.Inbox` (routes transcripts), `PV.ExternalResearch` (external signals requiring new entities), `PV.Report` (closing `proposed`/`deferred` slots).

### PV.StateUpdate:End

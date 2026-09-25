---
id: PV.StateUpdate
title: "State update from a source: DEC card (open/proposed/accepted) from a transcript or dialogue"
status: seed
keywords: [state-update, transcript, dialogue, decision, DEC, ADR, status, open, proposed, accepted, question, risk, contradiction]
dependencies:
  builds_on:
    - A.7
    - A.10
    - C.32.ADR
    - E.9
---

## PV.StateUpdate - State update from a source: DEC card from a transcript or dialogue

> **Trigger:** When a new state source appears — a meeting transcript (Input 1) or dialog news without a transcript (Input 2) — and the vault must be brought in line.
> **Skill dependencies:**
>   → none

---

### PV.StateUpdate:1 - Problem frame

Use this pattern to turn a meeting transcript or a dialogue briefing into a
verifiable vault update: capture the source, create/close decision cards (the single
state entity), and reconcile against the registry of open cards without inventing
facts absent from the source.

### PV.StateUpdate:2 - Problem

A source can be thin or contradictory: decision formulations are vague, a decision
is mentioned but not approved, a contradiction is suspected but not asserted. If
cards are filled in "by the spirit of it", the vault fills up with unconfirmed
decisions and unchecked facts. If "choice" is not distinguished from "paraphrase",
the decision canon clogs with junk entries. And because every state position (a
decision-to-be, a question, a risk, a contradiction) is now one card kind, the
complementary risk is over-creating cards for transient observations.

### PV.StateUpdate:3 - Forces

| Force | Settlement |
|---|---|
| Completeness vs verifiability | Record only what is verifiable from the source; formulations — only in atomic cards. |
| Accepted vs open/proposed | `accepted` — only on explicit approval in the source; a formed but unapproved position — `proposed` + "pending owner confirmation"; an unformed open position — `open`. |
| State position vs paraphrase | A card only for a bounded state position with a long-lived consequence; editorial/summary — as context in the capture header, no card. |
| Strategic vs transient | A card only for a position a future architect can rely on in a month/quarter; a weekly/one-off, event-bound one — as context in the capture header or a signal in a long-term card's "Related entities"/"External signals", no standalone card. |
| One vs several | One position = one card; independent topics are not merged. |
| Named vs role attribution | The card body stays impersonal: no personal names and no "owner"-style attribution; attribute by role or situation. A specific person — only in the frontmatter `decision_owner`. |
| Single entity vs kinds | One card kind holds every state position (decision, question, risk, contradiction); the difference is a status/position, not an entity kind. |

### PV.StateUpdate:4 - Solution

**Input 1 — meeting transcript.**

1. Save the source into `project-vault/sources/`.
2. Write 2–3 lines of summary "what the source is about" (context) into the capture header.
3. **Open-card registry in context:** find the open cards via
   `grep -l "^status: open" project-vault/decisions/*.md` (and `^status: proposed`),
   read the relevant ones. If the source gives a signal on an open card (closes /
   partially answers / contradicts) — write it into the card (`status`/note + `sources`
   pointing to the capture). A negative outcome ("no signals") is not recorded.
4. For **key positions** (a decision-to-be, a question, a risk, a contradiction) —
   create/update `project-vault/decisions/DEC-NNNN.md` from the template
   `project-vault/decisions/_template.md`; the card's `sources` — to the capture.
   Rules:
   - **No architectural-only gate.** A card is created for any bounded state position
     with a long-lived consequence, whether it is already a decision or still an open
     position (question/risk/contradiction); the difference is the card's `status`.
   - **Transient positions (horizon filter):** a position tied to a one-off/weekly
     event (e.g. a one-time demo, a one-time deadline) that goes stale within ~a week →
     **not** a standalone card; file it as context in the capture header or as a signal
     in the "Related entities"/"External signals" of the long-term card it concerns.
     Check before creating: "will this still be relevant in a month/quarter?"
   - **Fill all sections** of the template; do not invent what is absent — write
     "not discussed" / "unknown" / "not applicable".
   - **Status and field timing:**
     - `status` — `open` (default; no candidate yet) | `proposed` (candidate formulated,
       not approved) | `accepted` (explicitly approved) | `superseded` | `retired`.
     - `decision_type` (one of `adr | org | strategy | scope | process | procurement | product`)
       and `characteristic` (only for `decision_type: adr`) — filled at creation, even
       for an `open` card.
     - `decision_owner` — appears at the `proposed` stage (a specific person is involved).
     - `decision_date` — only at `accepted`.
   - "Considered options" ≥ 2 → fill "Option comparison"; one option → "single option".
     A contradiction is laid out here: two incompatible positions, one card.
   - Always fill "Revisit conditions"; `revisit_by` or an open-ended note.
   - **Body attribution (no names, no "owner"):** the card body never contains personal
     names/surnames and never attributes by "the owner" (ambiguous — owner of what?).
     Attribute by role or situation (e.g. "architect", "decided at the review"). If a
     specific person made the decision, record that person only in the frontmatter
     field `decision_owner` — never in the body.
5. Run the common steps (below).

**Input 2 — dialog news (no transcript).**

1. The source is fixed in the entity: a signal/problem/directive → a track (or a
   card) with a "Signal" section (the direct quote + date + provenance).
2. For key positions — create/update a card with `sources` to the dialog (provenance
   in the frontmatter: `source_kind: user_dialogue`, `evidence_captured_at`).
3. If there are signals to open cards — write them into the cards (do not create a
   separate reconciliation record).
4. Run the common steps (below).

**Insufficient input.**

- The transcript is not enough for a meaningful update → a minimal capture header and stop.
- A decision is mentioned but not explicitly approved → `status: proposed` + "pending owner confirmation".
- A position is suspected but not asserted → `status: open` + "requires clarification".
- An opinion/preference, not a position → no card; if needed — as context in the capture header.
- The dialog contradicts an existing `accepted` → a note on the card + a `revisit_by` flag.

**Common steps (after Input 1 or 2).**

1. Creation/closure of cards — the file is created; closed ones (`superseded`,
   `retired`) stay in place with a `status` (no `archive/`).
2. New external blockers → a card with `status: open` (a risk position) — only for a
   **strategic/long-lived** one (still relevant in a month/quarter). A transient one
   → context in the capture header or a signal in a long-term card, no standalone
   card. If the blocker spans several entities — also a track with `status: blocked`.
3. New regulatory/architectural constraints → a DEC card (a constraint position;
   `status: open`/`proposed`, `decision_type` per its nature). There is no separate
   `constraints` file.
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
   - Do not create a track for every card — only for operational lines with
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

**Show.** A post-meeting update in this project: the source in `sources/`, key
positions as atomic cards with the correct `status`, reconciliation with the open
registry, an operational signal as a track.

### PV.StateUpdate:6 - Bias-Annotation

The temptation is to raise a card's status to `accepted` "in the spirit of" the
meeting without explicit approval, and to open a card for every statement for the
sake of canon completeness. The rule "accepted only explicitly" and the horizon
filter ("strategic vs transient") are the two counterweights.

### PV.StateUpdate:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-SU.1 | Every new claim — with a reference to the source (capture/dialog). |
| CC-SU.2 | `accepted` — only on explicit approval in the source; a formed but unapproved position — `proposed`; an unformed open position — `open`. |
| CC-SU.3 | Two incompatible formulations — one card with `status: open`/`proposed` (the two positions under "Considered options"), not a separate kind. |
| CC-SU.4 | A card is created for any bounded state position (decision/question/risk/contradiction); there is no "architectural choice only" gate. |
| CC-SU.5 | The card body carries only the card-ID and a web-URL; other references (source paths, entity IDs) — in the frontmatter. This applies to every body section, including "External signals" and "Revision history": in a signal's text only a verbal source name is allowed (e.g. "owner review 2026-09-08"); a path/ID goes to the frontmatter (`sources` for a path, `references` / `related_decisions` for entity IDs). |
| CC-SU.6 | A decision change = edit the card + "Revision history", not a duplicate. |
| CC-SU.7 | A card is created only for a strategic/long-lived position; a weekly/one-off one is filed as capture context or a signal in a long-term card, not as a standalone card. |
| CC-SU.8 | The card body contains no personal names/surnames and no "owner"-style attribution; attribution is by role/situation, and a specific person is recorded only in the frontmatter field `decision_owner`. |

### PV.StateUpdate:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| `accepted` without explicit approval | `proposed` + "pending owner confirmation". |
| A card for editorial/summary content | Context in the capture header; no card. |
| Duplicate card on a decision change | Edit the same card + "Revision history". |
| A capture/artifact reference in the card body | Only card-ID and URL; the rest in the frontmatter. |
| An inline source path or entity ID in the card body (incl. "External signals"/"Revision history") | Verbal source name in the text; path/ID to the frontmatter (`sources`/`references`). |
| A standalone card for a one-off/weekly event | Context in the capture header or a signal in a long-term card; no standalone card. |
| A personal name or an "owner"-style attribution in the card body | Attribute by role/situation; the person goes to the frontmatter `decision_owner`. |

### PV.StateUpdate:9 - Consequences

Strict record discipline makes the decision canon a support for a future architect,
but slows down recording and requires an explicit "choice / paraphrase" distinction.
A decision change means an edit with a revision history, not a new file. One card
kind for every position removes premature classification, but transfers the burden
to the `status` field and the horizon filter, which keep the open registry meaningful.

### PV.StateUpdate:10 - Rationale

`C.32.ADR` requires problem frame → outcome → consequences → confirmation/supersession;
`E.9` holds a DRR as one bounded decision with an input filter ("cheap stop" for
editorial edits) — the same filter yields the strategic-vs-transient horizon. `A.10` —
any claim with a reference to its source. Hence — accepted/proposed/open, the horizon
filter, and "do not invent". One card kind per state position implements `A.7`
(status vs kind): question/risk/contradiction are positions on the same card's
lifecycle, not parallel kinds.

### PV.StateUpdate:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `C.32.ADR` (ADR record) | Adopt | Card template sections, `accepted` only explicitly | Reopen on `C.32.ADR` revision |
| FPF `E.9` (DRR, one bounded decision) | Adopt | Card horizon filter, "one topic — one card" | Reopen on `E.9` revision |
| FPF `A.10` (source reference) | Adopt | Guardrail "any claim — with a reference" | Reopen on `A.10` revision |

Best-known line: ADR discipline with a status lifecycle and one card kind. Rejected
rival: "recording every statement as a decision" — rejected as canon clutter.

### PV.StateUpdate:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PV.StateUpdate:End
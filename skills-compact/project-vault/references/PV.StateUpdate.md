# PV.StateUpdate - State update from a source: DEC card (open/proposed/accepted) from a transcript or dialogue

> **Trigger:** When a new state source appears — a meeting transcript (Input 1) or dialog news without a transcript (Input 2) — and the vault must be brought in line.

```episteme id="PV.StateUpdate" context="ProjectVault"
Grounding (FPF):
  builds_on: A.7, A.10, C.32.ADR, E.9

UseThisWhen:
  turning a meeting transcript or a dialogue briefing into a verifiable vault update: capture the source, create/close decision cards (the single state entity), reconcile against the open registry
  never by inventing facts absent from the source

Result:
  the vault in line with the source: sources/ capture, DEC cards created/closed with correct status, open registry reconciled, operational signals as tracks

Solution:
  Input1.MeetingTranscript:
    save the source into project-vault/sources/
    write 2–3 lines of summary ("what the source is about") into the capture header
    open-card registry: find open cards via grep -l "^status: open" project-vault/decisions/*.md (and ^status: proposed), read the relevant ones; a signal on an open card (closes/partially answers/contradicts) → write it into the card (status/note + sources → capture); a negative outcome ("no signals") is not recorded
    key positions → create/update project-vault/decisions/DEC-NNNN.md from project-vault/decisions/_template.md; card sources → the capture, under the card rules (below)
  Input2.DialogNews(noTranscript):
    the source is fixed in the entity: a signal/problem/directive → a track (or a card) with a "Signal" section (direct quote + date + provenance)
    key positions → create/update a card with sources → the dialog (frontmatter: source_kind: user_dialogue, evidence_captured_at)
    signals to open cards → write them into the cards (no separate reconciliation record)
  CardRules:
    no architectural-only gate: a card for any bounded state position with a long-lived consequence (decision or open position — question/risk/contradiction), the difference is status
    horizon filter (transient positions): a one-off/weekly event-bound position that goes stale within ~a week → not a standalone card; file as capture-header context or a signal in the long-term card ("Related entities"/"External signals"); check "will this still be relevant in a month/quarter?"
    fill all template sections; do not invent what is absent — write "not discussed"/"unknown"/"not applicable"
    status: open (default, no candidate) | proposed (candidate, not approved) | accepted (explicitly approved) | superseded | retired
    decision_type (adr | org | strategy | scope | process | procurement | product) and characteristic (only decision_type: adr) — filled at creation, even for an open card
    decision_owner — appears at proposed (a specific person); decision_date — only at accepted
    "Considered options" ≥ 2 → fill "Option comparison"; one option → "single option"; a contradiction is laid out here (two incompatible positions, one card)
    always fill "Revisit conditions" (revisit_by or an open-ended note)
    body attribution: never personal names/surnames, never "the owner" (ambiguous) — attribute by role or situation (e.g. "architect", "decided at the review"); a specific person only in frontmatter decision_owner, never the body
  InsufficientInput:
    transcript not enough for a meaningful update → a minimal capture header and stop
    decision mentioned but not explicitly approved → status: proposed + "pending owner confirmation"
    position suspected but not asserted → status: open + "requires clarification"
    opinion/preference, not a position → no card; if needed, capture-header context
    dialog contradicts an existing accepted → a note on the card + a revisit_by flag
  CommonSteps (after Input 1 or 2):
    card creation/closure — file created; closed ones (superseded/retired) stay in place with status (no archive/)
    new external blockers → a card status: open (risk position), only for a strategic/long-lived one; transient → context or a signal; if it spans several entities → also a track status: blocked
    new regulatory/architectural constraints → a DEC card (constraint position; status open/proposed, decision_type per nature); no separate constraints file
    track maintenance — a new operational signal → project-vault/tracks/TRK-NNNN.md with status: cue (template tracks/_template.md), then python scripts/vault.py tracks; a status change → update frontmatter + inline fields, then vault.py tracks; closed → status: retired (stays in tracks/), then vault.py tracks; unblocked → previous active status, then vault.py tracks
    lifecycle: cue → problem-framed → method-selected → work-planned → in-progress → performed → evaluated; side: blocked, deferred, retired (terminal); do not create a track for every card — only for operational lines with blockers spanning several entities
    assignments to the repo owner (only one directly expressed, by name, without invention): read project-vault/tracks/_index.md, pick the fitting track by topic, write the assignment as a new numbered item in "Next moves"; with a deadline → (deadline YYYY-MM-DD), overdue → (deadline YYYY-MM-DD, overdue); "Next step" (singular) already taken → turn into "Next moves" (plural); never a new track for a personal assignment; no fitting track → capture header + flag the owner

Stop:
  every source-derived position is a card with correct status (accepted only on explicit approval); the open registry is reconciled; no invented fact

Checks:
  every new claim references its source (capture/dialog)
  accepted only on explicit approval; formed-but-unapproved → proposed; unformed open → open
  two incompatible formulations → one card (the two positions under "Considered options"), not a separate kind
  a card for any bounded state position (decision/question/risk/contradiction); no "architectural choice only" gate
  card body carries only the card-ID and a web-URL; other references (source paths, entity IDs) → frontmatter (sources for a path; references / related_decisions for IDs) — applies to "External signals" and "Revision history" too; a signal's text holds only a verbal source name
  a decision change = edit the card + "Revision history", not a duplicate
  a card only for a strategic/long-lived position; a weekly/one-off one → capture context or a signal, not a standalone card
  card body contains no personal names/surnames and no "owner"-style attribution; a specific person only in frontmatter decision_owner

Antipatterns:
  accepted without explicit approval → proposed + "pending owner confirmation"
  a card for editorial/summary content → capture-header context; no card
  duplicate card on a decision change → edit the same card + "Revision history"
  a capture/artifact path or entity ID in the card body → verbal source name in text; path/ID to frontmatter
  a standalone card for a one-off/weekly event → capture context or a signal in a long-term card
  a personal name or "owner" attribution in the body → attribute by role/situation; person to frontmatter decision_owner

Continues:
  PV.VaultSchema (schema/fields), PV.Track (operational signals), PV.WorkRecord (record the update)

Reopen:
  C.32.ADR / E.9 / A.10 revision
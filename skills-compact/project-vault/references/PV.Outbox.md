# PV.Outbox - Outgoing feedback: outbox procedure for sending notes to other systems/skills

> **Trigger:** When feedback, a proposal, or a note arises that is addressed to another system or skill — including a substantive method-feedback signal captured at a WRK closure (`PV.WorkRecord` W.4) — and it must be captured and delivered instead of evaporating after the dialog.

```episteme id="PV.Outbox" context="ProjectVault"
Grounding (FPF):
  builds_on: A.7, C.2.1, C.33, E.11
  coordinates_with: A.15.1

UseThisWhen:
  recording outgoing feedback or proposals to other systems/skills as one message file in outbox/, transferring it to the recipient's inbox/, and marking it sent — so the recipient processes it as an ordinary inbox arrival

Result:
  traceable, two-way outgoing feedback: one outbox/ message per note, transferred and marked sent, received as an ordinary inbox arrival

Solution:
  capture:
    one .md file in outbox/ (one file = one message) with frontmatter created, addressee, source_project, source_context, status: pending
    note the send in a WRK (the current track)
    a substantive method-feedback signal from a WRK closure (PV.WorkRecord W.4) is emitted the same way — one message addressed to the owning skill/author, referencing the WRK id, the rule locus (PatternID/section), and a concrete proposed fix
  transfer:
    the author moves the message into the recipient's inbox/ (or the recipient fetches it), clearing their own outbox/; on transfer set status: sent if a record is kept, or remove the file
  reception:
    for the recipient this is an ordinary new arrival in inbox/ — process by the standard PV.Inbox procedure
  discovery:
    outbox/ has no _index.md and its messages have no monotonic ID — find via ls or grep (e.g. grep -l "^status: pending" outbox/)

Stop:
  the message is written, transferred to the recipient's inbox/, and outbox/ is cleared (status flipped pending → sent)

Checks:
  one message = one file in outbox/ with created/addressee/source_project/source_context/status
  no monotonic ID and no _index.md in outbox/; discovery via ls/grep
  status flips pending → sent on transfer; outbox/ cleared after transfer
  the recipient processes the transferred message as an ordinary PV.Inbox arrival

Antipatterns:
  outgoing feedback left in the chat (no file) → write one message file in outbox/
  a monotonic ID or _index.md for outbox/ → no ID, no index; a transient file
  outbox/ not cleared after transfer → clear it on transfer
  the recipient treats it as special → it is an ordinary inbox arrival

Continues:
  PV.Inbox (the recipient's reception), PV.WorkRecord (the emitting closure)

Reopen:
  A.7 / C.33 / E.11 / C.2.1 revision
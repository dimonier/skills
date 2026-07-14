---
name: project-vault
description: >-
  Maintains project state in a markdown vault (key decisions, open questions,
  risks, contradictions, dependencies) from meeting transcripts, structured notes,
  or owner chat updates. Use for updating project-vault after meetings, dialog
  briefings, decision records, and next-meeting agendas. Triggers: project state,
  transcripts, meeting notes, chat updates, risks, dependencies, contradictions,
  ADR-style decisions.
---

# Project Vault — Personal Project Storage

Owner: Dmitry Ulanov. Users: Dmitry Ulanov + AI assistant.

## Vault Core

Key artifacts, maintained up-to-date:
- `project-vault/decisions/` — atomic decision cards (DEC-NNNN-slug.md) + summary `_index.md`
- `project-vault/open-questions/` — atomic open question cards (Q-NNNN.md) + summary `_index.md`
- `project-vault/risks/` — atomic risk cards (RISK-NNNN.md) + summary `_index.md`
- `project-vault/contradictions/` — atomic contradiction cards (CON-NNNN.md) + summary `_index.md`
- `project-vault/archive/` — mirror structure for closed entities (risks, questions, contradictions, events)
- `project-vault/dependencies.md` — external blockers
- `project-vault/state/overview.md` — concise current state
- `project-vault/state/constraints.md` — regulatory and architectural constraints

Auxiliary:
- `project-vault/events/` — event chronicle (YYYY-MM-DD-NN.md) + summary `_index.md`
- `project-vault/sources/` — captured originals (`captures/`) and analysis digests (`digests/`) + summary `_index.md`
- `project-vault/agenda-next.md` — next meeting agenda (on demand)

## Inbox Procedure

**Inbox:** on request "process inbox" (and similar), process files from `inbox/` using `project-vault` skill procedures. After full processing — clear `inbox/`.

## Procedure A — State Update from Source

### Input 1 — Meeting Transcript

1. Save the captured source to `project-vault/sources/captures/`.
2. Create `project-vault/sources/digests/YYYY-MM-DD_slug.md` using template `templates/digest-meeting.md`.
3. **Q Registry in Context:** before filling, read active rows in `project-vault/open-questions/_index.md` (`status: open`).
4. Fill digest only with what is verifiable from the source: context, links to created atomic files (DEC, Q, RISK, CON), reconciliation against Q registry. Decision/question/risk wording — only in atomic files, never copied into digest.
5. For **key** decisions: create/update `project-vault/decisions/DEC-NNNN-slug.md` using template `templates/decision.md`; `accepted` only upon explicit approval in the source.
6. Execute common steps below.

**When input is insufficient:**
- If transcript lacks enough information to fill a digest meaningfully → create a minimal digest noting "insufficient data" and stop.
- If a decision is mentioned but not explicitly approved → set `status: proposed`, note in digest "not yet accepted — pending owner confirmation".
- If a contradiction is suspected but not clearly stated → create CON entry with `status: proposed` and note "requires clarification".

### Input 2 — Dialogue News (no new transcript)

1. Create `project-vault/sources/digests/YYYY-MM-DD_slug.md` using template `templates/digest-dialogue.md`.
2. For key decisions — create/update DEC-* with `sources` pointing to digest.
3. If signals to active Q-* exist — record reconciliation.
4. Execute common steps below.

**When input is insufficient:**
- If the user statement is opinion/preference rather than a verifiable decision → create a digest noting "opinion expressed, not a decision" and skip DEC creation.
- If the dialogue contradicts an existing `accepted` decision → create CON entry and flag the decision with `revisit_by` or note in `_index.md`.

### Common Steps After Input 1 or 2

1. Update `project-vault/state/overview.md` when substantial new facts appear or when `accepted` decisions are made.
2. When creating/closing atomic entities — create/move the corresponding file (DEC, Q, RISK, CON) and update the summary `_index.md` in the respective directory. Closed entities — into `project-vault/archive/` (mirror structure).
3. Update `project-vault/dependencies.md` when new external blockers appear.
4. Update `project-vault/events/` — new file `YYYY-MM-DD-NN.md` and `_index.md` upon significant changes.

## Procedure E — Next Meeting Agenda

Update `project-vault/agenda-next.md` using template `templates/agenda.md`: top questions, blockers, contradictions, risks; slots from `project-vault/decisions/` (close `proposed`, return `deferred` with approaching `revisit_by`).

**When blocked:**
- If `agenda-next.md` does not exist yet → create from template.
- If there are no open questions/risks/contradictions → fill only the "0–5 Goal" slot and note "agenda empty — no open items."

## Guardrails

1. Any new claim — link to source (digest, capture).
2. No basis in source — do not mark as resolved.
3. Two incompatible formulations — atomic file in `contradictions/` + row in `_index.md`.
4. Do not set decision status to `accepted` without explicit wording in `sources`.
5. **Reports are off-limits without request:** do not create or update `project-vault/reports/*` without explicit request.

## After Changes

Briefly list modified and created files.

## Evolution

If the user is dissatisfied with a result or clarifies the process, offer to update this skill. When updating:
- If the trigger is wrong → fix the `description` in frontmatter.
- If a procedure is incomplete → add steps or failure paths in the relevant Procedure section.
- If a template is missing fields → update the template file in `templates/`.
- If the vault schema changed → update `references/architecture.md`.

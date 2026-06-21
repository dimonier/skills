# project-vault

A file-based project state vault: canon in `state/`, meeting analyses in `meetings/`, raw text in `transcripts/raw/`, dialogue news capture in `inputs/briefings/`, key decision log in `decisions/`.

## Artifact roles

| Path | Role |
|------|------|
| `transcripts/raw/` | Raw transcript: append-only; do not edit as "after-the-fact truth". |
| `meetings/.../processed.md` | Structured meeting analysis; basis for `sources` in canon. |
| `inputs/briefings/*.md` | What the owner explicitly said in chat (or another agreed-upon entry); body contains only what was conveyed, without conjecture. |
| `state/` | Concise current understanding of the project. |
| `work/tasks/` | Tasks with dependencies and traceability (see "Tasks" section below). |
| `decisions/` | Key decision cards: options, comparison, status, relationships; do not replace `processed`, but reference it in `sources`. |

Valid entry types are listed here and in the agent skill; new types — only after explicit agreement in the README.

## Tasks (`work/tasks/`)

**Where each status lives:** open — `work/tasks/TASK-*.md`; completed — `work/tasks/done/`; cancelled — `work/tasks/cancelled/`. Details and synchronization of the `status` field with the folder — see the actual vault `README.md` after copying from scaffold (or refer to the `project-vault` skill → tasks section). Script: `project-vault/scripts/sync-task-status-from-path.py`.

**Task mentions:** in canon, use only the explicit `TASK-YYYY-NNNN` (plain text); do not use file paths to task files in text — see the vault `README.md` after deployment.

## Key decisions (process, brief)

1. **Identification** — during `processed` analysis or briefing: explicit choices, commitments, priorities, boundaries → candidate for `decisions/` (status no higher than source: without explicit "we accept" in the text — not `accepted`).
2. **Recording** — file `decisions/DEC-NNNN-slug.md` per `_template.md`, `sources` only to an already-created `processed` or briefing; row in `decisions/_index.md`.
3. **Canon** (`state/`, tasks, dependencies) — update from a decision only when **`accepted`**. For `proposed`, only tasks like "prepare material for decision" are allowed, if stated in the source.
4. **`proposed`** — keep on the agenda until `accepted` / `rejected` / deliberate `deferred`; for `deferred`, `revisit_by` or an explicit condition in the card body is mandatory.
5. **`rejected`** — do not raise again without a **new** `sources` (new meeting, new briefing, new data).
6. **`superseded`** — new card with `supersedes: [DEC-…]`; do not rewrite the old one retroactively.
7. **Owner** — in `decision_owner`; if not named in the source — the card stays `proposed`, item in `open-questions.md`: who approves.

## Frontmatter: common fields

Field names in English; body text language — per team agreement.

- `id`, `updated`, `sources` (list of paths), `source_kind`: `meeting_transcript` | `meeting_processed` | `user_dialogue` | `other`
- `evidence_captured_at` — ISO 8601 date (YYYY-MM-DD or full datetime) when the source linkage was recorded or when the **substantive** assertion was last changed for the same semantic position. Minor spelling fixes do not shift the date.
- `source_event_date` — optional, date of the meeting or briefing day; if the date is unambiguous from the path `meetings/YYYY-MM-DD_...`, the field may be omitted.
- `review_by` or `valid_until` — for `claim_type: hypothesis`, time-bound estimates, and explicitly time-limited assertions — **mandatory** (see below). For stable `fact` from a protocol — leave empty until a new source or contradiction appears.
- `owner`, `status`, `claim_type` where applicable: `fact` | `obligation` | `hypothesis`

## Evidence date policy

1. Any new canonical assertion backed by a source gets the current `evidence_captured_at`.
2. `review_by` / `valid_until`: the list of record types for which the field is mandatory is extended by the team as needed; by default it is mandatory for `hypothesis` and any phrasing like "we expect", "presumably", "by the end of the week without a firm commitment from the source".

## Naming raw transcripts

Recommendation: `YYYY-MM-DD_short-topic.txt` or `.md` in `transcripts/raw/`.

## Source references in markdown body

Use relative paths from the file containing the reference (e.g. `../../transcripts/raw/2026-04-14_standup.txt`).

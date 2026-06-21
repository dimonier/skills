---
name: project-vault
description: >-
  Maintains project state in a markdown vault (tasks, dependencies, risks,
  key decisions, open questions, agendas, reports) from meeting transcripts,
  structured notes, or owner chat updates. Use when the user needs to:
  (1) initialize a project-vault in a new repository, (2) update project state
  from meeting transcripts, (3) record user dialogue briefings, (4) manage
  stakeholders and responsibilities, (5) generate status reports, (6) list
  open questions, (7) surface contradictions and risks, (8) prepare next-meeting
  agendas. Triggers: project state, transcripts, meeting notes, chat updates,
  risks, agenda, dependencies, contradictions, ADR-style decisions.
---

# Project vault — automated project maintenance

## Reading paths

- **Skill root** — the directory containing this `SKILL.md`. All paths like `assets/...`, `scaffold/...` are relative to the skill root (not the repository).
- **Repository root** — the root of the project this skill is applied to. All paths like `project-vault/...` are relative to the repository root.

For a visual overview of the vault structure, see `references/architecture.md`.

Reply to the user in English.

## Tasks: location by status (`project-vault/work/tasks/`)

- **Open** tasks — `TASK-*.md` files directly in `project-vault/work/tasks/` (the root of the `tasks/` directory).
- **Closed** statuses — in **subdirectories** by meaning, e.g.:
  - `project-vault/work/tasks/done/` — completed;
  - `project-vault/work/tasks/cancelled/` — cancelled.
- Subdirectory names are defined in the repository's `project-vault/README.md`; the agent creates tasks **only in the root** of `tasks/` for active work.
- **Deduplication** of a task by `id` or title: search the entire tree, e.g. `project-vault/work/tasks/**/TASK-*.md` (including `done/` and `cancelled/`), to avoid creating a second file with the same `id`.
- **Task mentions** in canon (`state/`, `dependencies.md`, `risks.md`, `meetings/.../processed.md`, etc.): use only the explicit `id` — `TASK-YYYY-NNNN` (plain text). People read the vault as text; click-based navigation is not expected. The agent finds the task file by searching `work/tasks/**/TASK-*.md`. Do **not** insert markdown links to the task file path in these documents — they are fragile when moved to `done/` and unnecessary for the agent.
- The **`status` field in a task's frontmatter** must match its folder; synchronization can be automated via `project-vault/scripts/sync-task-status-from-path.py` (see `project-vault/README.md`).

## Questions (`project-vault/open-questions.md`, `project-vault/work/questions/`)

- **Identifier** — `Q-YYYY-NNNN` (plain text in canon), not `OQ-…`. Active table — `project-vault/open-questions.md`; closed — `project-vault/work/questions/closed/Q-YYYY-NNNN.md`. Deduplication by `id`: search the entire tree `work/questions/**/Q-*.md` and rows in `open-questions.md`.

## Initializing a vault in a new project

If the repository does not yet have a `project-vault/` directory, create it by copying the tree from the skill.

From the **repository root** run (substitute the path to the **skill root** — the directory containing this `SKILL.md`):

```bash
cp -a <skill-root>/scaffold/project-vault ./project-vault
```

Details and warnings if `project-vault/` already exists: `references/scaffold.md` (in skill root).

Then adjust dates and placeholders in `project-vault/index.md` as needed. Continue working by procedures A–E.

## Before any edits

1. Read `project-vault/index.md`, relevant files in `project-vault/state/`, `project-vault/meetings/_index.md`, `project-vault/decisions/_index.md`.
2. When updating from chat, review the latest files in `project-vault/inputs/briefings/`.

## Procedure A — updating state from a source

### Entry 1 — meeting transcript

1. Save the raw text to `project-vault/transcripts/raw/` (naming per the policy in `project-vault/README.md`).
2. Create `project-vault/meetings/YYYY-MM-DD_slug/processed.md`, copying the structure from `project-vault/meetings/_template.md` or from `assets/meeting-processed.md` (skill root); include a link to the file in `transcripts/raw/` in the frontmatter or header.
3. **Q registry in context:** before filling in content sections, read the active rows (`status: open`) in `project-vault/open-questions.md` and keep them in mind while parsing the transcript ("source leads" logic, not iterating through questions one by one in a separate pass).
4. Fill in `processed.md` only with what is verifiable from the source: participants, topic, agreements, decisions, actions (who/what/deadline — only if explicit in the text), blockers, risks, new open questions from this meeting, contradictions with canon; **mandatory** sections: **"Q Registry Cross-Reference"** per `meetings/_template.md` and **one row** in `project-vault/work/questions/review-coverage.md`.
5. For **key** decisions (see `project-vault/README.md` → "Key Decisions"): create or update `project-vault/decisions/DEC-NNNN-slug.md` using the template `assets/decision.md`; set `status` no higher than the explicitness level in the source (`accepted` only with explicit agreement/approval in the text); update `project-vault/decisions/_index.md`; add a link to the card in `processed.md`.
6. Update `project-vault/meetings/_index.md`.
7. Perform the common steps below.

### Entry 2 — dialogue news (no new transcript)

1. Create `project-vault/inputs/briefings/YYYY-MM-DD_slug.md` using the template `assets/briefing.md`: only what the user explicitly said (bullets or short quotes). Do not add facts on behalf of the user.
2. In frontmatter: `source_kind: user_dialogue`, fill `evidence_captured_at` (today, per the date recorded in the vault).
3. For **key** decisions in the user's statements — create or update `project-vault/decisions/DEC-NNNN-slug.md` with `sources` pointing to this briefing; update `project-vault/decisions/_index.md` (same status rules as Entry 1).
4. If the briefing yields verifiable signals for active `Q-YYYY-…` in `open-questions.md` — record the cross-reference (briefly in the briefing body and/or a row in `project-vault/work/questions/review-coverage.md` with the path to this briefing).
5. Perform the common steps below.

### Common steps after Entry 1 or 2

1. Update `project-vault/state/*` when new verifiable facts appear **or** when a decision status is `accepted` in `project-vault/decisions/*.md` (do not carry decision consequences into canon at `proposed`/`deferred`, except for explicitly stated preparation tasks per README); for files with frontmatter, specify `sources` pointing to `processed.md`, `inputs/briefings/*.md` and/or `decisions/DEC-*.md`, `evidence_captured_at`; when applicable `source_event_date`, `claim_type`, `review_by` / `valid_until` per README.
2. Create or update task files in `project-vault/work/tasks/` (new **open** tasks — in the **root** of `tasks/`) without duplicates: before creating, search for an existing `id` via `project-vault/work/tasks/**/TASK-*.md`; each task with `sources` and dates per vault policy.
3. **Mandatory status reassessment:** after each new `processed.md` or briefing, **independently** re-evaluate related **active** `TASK-*` and `Q-*` based on all already-processed sources in the vault plus the current entry. Do not stop at noting "signal present": make an explicit decision `done / closed / partial / still open` and immediately reflect it in tasks, `open-questions.md`, `work/questions/closed/` cards, `dependencies.md`, and `state/*`, if there are sufficient grounds. For user messages, first capture them in `inputs/briefings/*.md`, then use that briefing as the basis. If ambiguity truly cannot be resolved from sources, **only then** ask the user for clarification.
4. Update `project-vault/dependencies.md`, `project-vault/risks.md`, `project-vault/contradictions.md`, `project-vault/open-questions.md` (only **active** `open` rows) and when closing a question — the card in `project-vault/work/questions/closed/Q-YYYY-NNNN.md` using `assets/open-question-resolved.md`; see `project-vault/work/questions/README.md`.
5. Update `project-vault/index.md`: last updated date and "what changed" block (3–7 items).

### Procedure A1 — mandatory `state/stakeholders.md` maintenance

The file `project-vault/state/stakeholders.md` is the canonical registry of responsibility and escalation paths.  
Its maintenance is **mandatory** when roles, owners, or decision zones change.

**Who performs:**

- `record_owner` — makes changes to cards, source references, changelog.
- `review_owner` — verifies role consistency, owner coverage, absence of duplicates.
- `approval_role` — confirms major changes to responsibility composition and escalations.

**When to update (triggers and SLA):**

- onboarding of a new role or participant — same business day;
- role/responsibility change — within 24 hours;
- new decision/risk/contradiction affecting responsibility — within 48 hours;
- publication of a new `meetings/.../processed.md` with role/escalation agreements — within 24 hours;
- scheduled: weekly light-check, monthly full review, quarterly redesign review.

**How to perform the update:**

1. In the registry, update or create a stakeholder entry: `context_id`, `role`, `decision_scope`, `responsibilities`, `escalation_path`.
2. Check linkage with **active** tasks (files in the **root** of `project-vault/work/tasks/`, not in `done/`/`cancelled/`) and/or `reports/*open-tasks-by-owner*`: critical tasks must have a clear ownership contour.
3. Update `sources`, `updated`, `evidence_captured_at` and add a row to `Change log` with reason and references.
4. If owner wording conflicts between `stakeholders.md` and tasks/reports — record in `project-vault/contradictions.md` and initiate escalation via `escalation_path`.

**Minimum quality gates before completion:**

- each active card has exactly one `context_id` and one escalation path;
- do not mix entities "person/role/team" in a single field;
- every significant change has a source reference;
- SLA overdue items are marked stale and raised at the next weekly light-check.

**Contradictions:** do not overwrite old canon without a record in `project-vault/contradictions.md`; if sources conflict — add a new row there.

## Procedure B — brief status report

Sources: `project-vault/state/`, **active** tasks (`project-vault/work/tasks/TASK-*.md` in the root of `tasks/`), `project-vault/state/milestones.md`, `project-vault/dependencies.md`, `project-vault/risks.md`, `project-vault/decisions/`, the last 1–2 `project-vault/meetings/.../processed.md`, and, if available, the latest `project-vault/inputs/briefings/*.md`.

Output: a file in `project-vault/reports/` with the **date at the start of the filename** followed by a meaningful slug, e.g. `project-vault/reports/2026-04-15-status.md`, using the template `assets/status-report.md`, or a chat reply with the same sections. Include a subsection for overdue and soon-expiring `review_by` / `valid_until` (scan tasks/risks/questions with frontmatter). Separately and briefly: new and changed decisions in `project-vault/decisions/` (by status: `accepted`, pending `proposed`, `deferred` with `revisit_by` in range).

## Procedure C — list of open questions

Source: the active table in `project-vault/open-questions.md` (`open` rows). If history of closed ones is needed — `project-vault/work/questions/closed/Q-*.md`. Filter `open`, sort by `blocked_work` and `decision_needed_by`, remove duplicates, indicate the consequences of not closing each.

## Procedure D — contradictions and risks

- Unclosed rows in `project-vault/contradictions.md`, candidates from the latest analysis and briefing, cross-check with `project-vault/state/`.
- Risks: a slice of `project-vault/risks.md` with priority and measures.

Output: a file in `project-vault/reports/` with the **date at the start of the filename** followed by a meaningful slug, e.g. `project-vault/reports/2026-04-15-risks.md`, or a structured chat reply. Separately: overdue / near `review_by`.

### Report naming rule in `reports/`

- For any report file created/updated in `project-vault/reports/`, the date is **mandatory in the filename**.
- Date format: `YYYY-MM-DD`.
- Date goes **at the start of the filename** (prefix), then a short slug, e.g.:
  - `2026-04-15-status.md`
  - `2026-04-15-risks.md`
  - `2026-04-15-executive-summary.md`

## Procedure E — next meeting agenda

Update `project-vault/agenda-next.md` using the template `assets/agenda.md`: top questions, `blocked` blockers, milestones within 2 weeks, contradictions, risks; timeslots with minutes. Add a slot for **`project-vault/decisions/`** where needed: close `proposed`, return `deferred` with an approaching `revisit_by`, do not raise `rejected` without a new source.

After A, do **not** update files in `project-vault/reports/` by default.
Only create/update reports (`reports/*`, procedures B and D) **upon explicit user request**.
`project-vault/agenda-next.md` may be updated via procedure E if the task explicitly warrants it.

## Guardrails

1. Any new assertion in `project-vault/state/` and any task status change — provide a source reference: `project-vault/meetings/.../processed.md`, a fragment from `project-vault/transcripts/raw/`, and/or `project-vault/inputs/briefings/*.md` quoting the user's message (per README).
2. No source basis — do not mark as resolved; leave in the active `open-questions.md` table or annotate as "not confirmed by source". Close with a move to `work/questions/closed/` only with a filled `resolved_by`.
3. Two incompatible statements — record in `project-vault/contradictions.md` with both references and an owner/deadline for resolution.
4. Do not close task A while task B is open, if the dependency is explicitly recorded, unless a new source removes the dependency.
5. Reprocessing the same entry does not duplicate canon; edit existing sections (or append to the briefing per README policy).
6. The canon for planning is: `processed.md`, captured `inputs/briefings/*.md`, `state/`, the glossary **inside `project-vault/`** — not "raw chat" and not `transcripts/raw/` alone without analysis.
7. Do not push onto the user the routine decision of "already closed or not yet" if it can be determined from already-processed transcripts, briefings, and vault canon. The user is needed only to resolve genuine ambiguity, not as a substitute for the agent's status reassessment.
8. Where `claim_type` is present, do not mix facts, obligations, and hypotheses in a single report row without markup.
9. When adding or substantially changing a canonical assertion, fill `evidence_captured_at`; for temporary claims and hypotheses — `review_by` or `valid_until` per README; do not silently extend expirations without a new source.
10. Do not assign `accepted` status to a decision and do not carry its consequences into `project-vault/state/` without an explicit formulation in `sources`; if the decision owner is absent — record in `project-vault/open-questions.md`, not a fabricated `decision_owner`.
11. **Do not touch reports without a request:** do not create or update `project-vault/reports/*` unless the user explicitly asked to compile/update a specific report.
12. Do not silently close or change questions, tasks, or decisions based on stale signals. A source older than the last status change on the item is not automatically authoritative.

## After changes

Briefly list the changed and newly created files to the user.

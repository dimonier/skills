---
name: project-vault
description: >-
  Maintains project state in a markdown vault (key decisions, open questions,
  risks, contradictions, dependencies) from meeting transcripts, structured notes,
  PDF documents, or owner chat updates. Governs working tracks as the mandatory
  container for all productive activity (research, analysis, synthesis). Use for
  updating project-vault after meetings, dialog briefings, decision records, and
  next-meeting agendas. Triggers: project state, transcripts, meeting notes,
  PDF documents, chat updates, risks, dependencies, contradictions, ADR-style
  decisions, track creation and lifecycle, inbox processing.
---

# Project Vault — Personal Project Storage

Check owner's name in AGENTS.md in repo's root.
Users: owner + AI assistant.

## Vault Core

Key artifacts, maintained up-to-date:
- `project-vault/decisions/` — atomic decision cards (DEC-NNNN-slug.md) + summary `_index.md`
- `project-vault/open-questions/` — atomic open question cards (Q-NNNN.md) + summary `_index.md`
- `project-vault/risks/` — atomic risk cards (RISK-NNNN.md) + summary `_index.md`
- `project-vault/contradictions/` — atomic contradiction cards (CON-NNNN.md) + summary `_index.md`
- `project-vault/archive/` — mirror structure for closed entities (risks, questions, contradictions, events, tracks)
- `project-vault/dependencies.md` — external blockers
- `project-vault/state/overview.md` — concise current state
- `project-vault/state/constraints.md` — regulatory and architectural constraints
- `project-vault/tracks/` — operational tracks (`TRK-NNNN.md` + summary `_index.md`); tracks archive: `archive/tracks/`
- `project-vault/work/` — dated work records (WRK-YYYY-MM-DD-hhmmss.md + summary `_index.md`), template: `work/_template.md`
- `project-vault/methods/` — reusable method descriptions (`U.MethodDescription`, A.3.2) + summary `_index.md`

Auxiliary:
- `project-vault/events/` — event chronicle (YYYY-MM-DD-NN.md) + summary `_index.md`
- `project-vault/sources/` — captured originals (`captures/`) and analysis digests (`digests/`) + summary `_index.md`
- `project-vault/agenda-next.md` — next meeting agenda (on demand)

## Inbox Procedure

**Inbox:** on request "process inbox" (and similar), process files from `inbox/` using `project-vault` skill procedures. After full processing — clear `inbox/`.

**External research** (independent Knowy research, narrativizations, articles, conference talks, tutorials) process via **Procedure R** — with two-way binding to any project entities that accept references (Q, RISK, CON, DEC, TRK).

**PDF pre-processing:** if `.pdf` files are found in the inbox — before substantive processing, convert each PDF to Markdown using the `pdf2md` skill (script `scripts/extract_pdfs.py` with parameters `--source <inbox_dir> --first N`). Use the resulting `.md` file (in `inbox/_markdown/`) as source material for further processing per the standard procedures (Procedure A, T.4). Do not analyze the original PDF directly — only via the converted Markdown. If the `pdf2md` skill is unavailable or the conversion fails — record this in the inbox processing result and notify the user.

## Procedure A — State Update from Source

### Input 1 — Meeting Transcript

1. Save the captured source to `project-vault/sources/captures/`.
2. Create `project-vault/sources/digests/YYYY-MM-DD_slug.md` using customized `project-vault/sources/_digest-template.md` or otherwise default template `templates/digest-meeting.md`.
3. **Q Registry in Context:** before filling, read active rows in `project-vault/open-questions/_index.md` (`status: open`).
4. Fill digest only with what is verifiable from the source: context, links to created atomic files (DEC, Q, RISK, CON), reconciliation against Q registry. Decision/question/risk wording — only in atomic files, never copied into digest.
5. For **key** decisions: create/update `project-vault/decisions/DEC-NNNN-slug.md` using customized `project-vault/decisions/_decision_template.md` or otherwise default template `templates/decision.md`; `accepted` only upon explicit approval in the source.
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
5. **Track maintenance:** when a source (meeting, briefing, directive) introduces a new operational signal, changes the status of an existing track, or closes one:
   - **New signal** → create `project-vault/tracks/TRK-NNNN.md` with status `cue` (using `tracks/_template.md`); add row to `project-vault/tracks/_index.md`.
   - **Status change** → update the track file (`status` field in frontmatter and inline status fields) and the corresponding row in `tracks/_index.md`. Status transitions follow the elaboration lifecycle: `cue` → `problem-framed` → `method-selected` → `work-planned` → `in-progress` → `performed` → `evaluated`. Side transitions: `blocked` (from any active status), `deferred` (from any active status), `retired` (terminal).
   - **Track closed/retired** → move track file to `project-vault/archive/tracks/`; remove row from `tracks/_index.md`.
   - **Track unblocked** → restore previous active status and update `tracks/_index.md`.
   - Do NOT create a track for every DEC/RISK/Q — only for operational lines that represent distinct work streams with blockers. A track typically spans multiple related DEC/RISK/Q/CON entities.
6. **Assignments to repo owner:** if a source (transcript, meeting protocol) contains an explicit assignment to the owner of this repo (referred by name) — only one directly expressed, without guessing or reading in:
   - Read `project-vault/tracks/_index.md` and select the most suitable existing track by topical similarity.
   - Record the assignment as a new numbered-list item in the track's "Next moves" field. If the source specifies a deadline — add `(deadline YYYY-MM-DD)`; if the deadline has already passed relative to today — `(deadline YYYY-MM-DD, overdue)`.
   - If the track field is named "Next step" (singular) and it is already occupied — convert it to "Next moves" (plural, numbered list: first item — the previous step, second — the new assignment).
   - Do **not** create a new track for a personal assignment — always assign it to an existing one.
   - If no existing track fits the topic — record it in the digest and flag it for the owner to resolve.

## Procedure R — External Research (reference material)

**Scope:** material that is neither a meeting transcript nor dialogue news: independent research (Knowy), narrativization, article, conference talk, tutorial. The purpose of processing is for the material to be taken into account in decision-making, not left as an "orphan".

1. Save the capture to `project-vault/sources/captures/`.
2. Create a digest `project-vault/sources/digests/YYYY-MM-DD_slug.md` (source_kind: `independent_research` / `web_article` / `conference` / `research_article`).
3. Read the entity registries (`project-vault/open-questions/_index.md`, `risks/_index.md`, `contradictions/_index.md`, `decisions/_index.md`, `tracks/_index.md`) — determine which entities accept references and are relevant to the material's topic.
4. Fill the "Reconciliation" section in the digest with a signal strength for each affected entity (`strong` / `partial` / `weak` / `supporting` / `no_signal`).
5. **Propagate signals into the entity files themselves (mandatory, two-way link):** for each affected entity (Q, RISK, CON, DEC — any that has a `sources`/`source` field or a "Related entities" section), append the signal to its file — as a frontmatter field `signal_YYYY-MM-DD` or as a body note "Signal YYYY-MM-DD" with a link to the digest. Listing IDs only in the digest's "Reconciliation" (one-way link) is **not sufficient**.
6. **Bind the digest to at least one reference-bearing entity:** add the digest to a track's "Related entities" → "Sources"/"Artifacts", or to the `sources`/`source`/"Related entities" of a suitable Q/RISK/CON/DEC (by topical similarity).
7. Create atomic entities (DEC/Q/RISK/CON) only if the material introduces a **new** decision/risk/question/contradiction. Purely reference material does not require them.
8. If the material is truly outside the scope of all entities — explicitly write "not bound — outside the project scope" in the digest (a deliberate decision, not an omission).
9. Update `project-vault/sources/_index.md` (capture↔digest pair); on substantial contribution — `overview.md` and `events/`.

## Procedure T — Track-Bound Productive Work

**Scope:** any productive activity (research, analysis, synthesis, architecture elaboration, artifact writing) is performed only within a track. Small one-step requests ("find a file", "explain a concept", "fix a typo") do not require a track.

### T.1 — User Request Arrives

1. Determine whether the request is productive activity (research, analysis, synthesis, multi-step work) or a small one-step task.
2. If it is a small task — perform it without a track, report the result.
3. **If the request does not point to a specific track** (e.g., "let's continue", "let's keep going"):
   a. Get the top-5 tracks by last-modified time: `Get-ChildItem project-vault\tracks\TRK-*.md | Sort-Object LastWriteTime -Descending | Select-Object -First 5`.
   b. Additionally review **all active** tracks (not `performed`, not `evaluated`, not `retired`) for deadlines in "Next moves": single out those with a `(deadline YYYY-MM-DD)` date within 3 calendar days of today (including overdue ones — marked "overdue").
   c. Show the combined list: top-3 by freshness + tracks with an approaching deadline (marked "approaching deadline YYYY-MM-DD" or "overdue deadline YYYY-MM-DD"). Sort: first overdue, then nearest deadline, then fresh. Propose the most urgent. Wait for confirmation.
4. If it is productive activity with an explicit topic — check `project-vault/tracks/_index.md` for a suitable track:
   - **Exactly one suitable** → report in chat: "Continuing track TRK-NNNN (title), current status — X. Transitioning to Y." Wait for confirmation.
   - **Several similar** → show all candidates with their statuses, propose the most suitable. Wait for confirmation.
   - **None suitable** → report: "Creating a new track for [request essence]." Wait for confirmation.
5. After confirmation — act on the track.

### T.2 — New Track Creation

1. A new track **always** starts with status `cue`.
2. Further advancement — strictly per FPF-core: `cue` → problem card formulation (C.22.2 ProblemCard@Context) → `problem-framed` → method selection (G.5/A.15) → `method-selected` → work plan (A.15.2) → `work-planned` → execution (A.15.1) → `performed` → result evaluation → `evaluated`.
3. At each transition: announce in chat the intent to move the track to the next status with a brief rationale (what exactly changed), wait for confirmation, then update the track and `_index.md`.
4. Track creation: file `TRK-NNNN.md` per template `tracks/_template.md` + a row in `tracks/_index.md`.

### T.3 — Track Continuation

1. When continuing an existing track: report in chat the current status, the next status, and a brief rationale for the transition. Wait for confirmation.
2. After confirmation: update `status` in frontmatter and in the track's status fields, update the row in `_index.md`.
3. If work within the track creates new artifacts (`artifacts/`) — list them in the track's "Related entities" section.
4. If a substantive step that produced a result was performed — create a WRK file per Procedure W.2 and add a line to the track's "Completed moves".
5. If a blocker is discovered during work — move the track to `blocked`, record the blocker in the track's status fields. On unblocking — restore the previous active status.

### T.4 — Inbox Processing and Tracks

When processing the inbox:
- If the material contains research or valuable artifacts → file it into the relevant existing track or create a new one (per T.1–T.2).
- If the material contains a transcript/meeting protocol → process it per the existing Procedure A, update related entities (DEC, Q, RISK, CON). If the meeting affects an existing track — update its status/blockers/next moves.

## Procedure AR — Artifact Creation

**Scope:** any artifact (`artifacts/YYYY-MM-DD-slug.md`) is created bound to a track and recorded as a WRK.

### AR.1 — Track binding and plan check

1. Determine which track the artifact being created belongs to. Check against `project-vault/tracks/_index.md`: the artifact's topic must match the track's essence.
2. Check whether the work of creating the artifact is in this track's "Next moves":
   - **There is an explicit item** → use it as `plan_item_ref` in the future WRK.
   - **No explicit item, but the topic matches** → before creating the artifact, add an item to the track's "Next moves", announce in chat.
   - **No track fits** → create a new track (Procedure T.2) with status `cue`, then add an item to "Next moves".
3. Report in chat: "Artifact [essence] belongs to track TRK-NNNN, plan item — [N or 'new item added']. Proceeding." Wait for confirmation.

### AR.2 — Collecting relevant materials

1. Read the track's ProblemCard@Context — the core of the problem.
2. Collect all relevant materials from the track: links to DEC, Q, RISK, CON, artifacts, WRK, digests — everything related to the topic of the artifact being created.
3. If necessary — read the atomic files of related entities (DEC, CON, Q, RISK) for full context.
4. If the artifact relies on FPF patterns — load the corresponding references from fpf-core.

### AR.3 — Preparing and writing the artifact

1. Create the file `artifacts/YYYY-MM-DD-slug.md`.
2. Follow guardrail 6: the artifact must be self-contained and alienable — readable without consulting other project entities. References to DEC-NNNN, Q-NNNN, etc. are prohibited; instead of an entity code, give a brief substantive description.
3. Follow the language rule: narration in Russian, English inclusions — only proper names, technology names, and terms without a stable Russian equivalent.

### AR.4 — Recording completed work (WRK)

1. After writing the artifact — immediately create a WRK file per Procedure W.2.
2. In `plan_item_ref`, specify the item from the track's "Next moves" identified at step AR.1.
3. In `output_refs`, specify the created artifact.
4. Update the track's "Completed moves" and `work/_index.md`.
5. If the artifact closes a PlanItem — **delete** the item from the track's "Next moves" (the completed item is already recorded by the WRK in "Completed moves"). Do not strike through `~~...~~` and do not mark `[x]`. If partial — leave it with a clarification.

## Procedure W — Work Record

**Scope:** every completed substantive step within a track is recorded as an atomic file `project-vault/work/WRK-YYYY-MM-DD-hhmmss.md`. A work record is `U.Work` (A.15.1): a dated occurrence of work. The record is a separate episteme denoting the occurrence.

### W.1 — When to create a WRK

Create a WRK file when:
- A substantive step was performed within a track that produced a new result (artifact, decision, analysis, structural change to project-vault).
- The result of the step must be traceable in the running log `work/_index.md`.

**Do not create** a WRK for:
- Item 0 in "Next moves" (reconnaissance, freshness check).
- Small administrative actions (updating `_index.md` without substantive work).
- Fixing obvious errors (typos, formatting).

### W.2 — Creating a WRK

1. Determine `hhmmss` — the current time (the moment the step is completed).
2. Create the file `project-vault/work/WRK-YYYY-MM-DD-hhmmss.md` per template `work/_template.md`.
3. Fill in the frontmatter:
   - `id`, `completed` (completion moment, `YYYY-MM-DD hh:mm:ss`), `performer`, `performed_under` (track).
   - `plan_item_ref` — the number of the item from the track's "Next moves" that was performed (optional for the thin form).
   - `enacted_method` — the FPF pattern applied (one or more, comma-separated).
   - `input_refs` — incoming entities: preceding WRKs, DEC, artifacts, source tracks (optional for the thin form).
   - `output_refs` — created/changed entities: artifacts, decisions, tracks, risks, questions, contradictions.
   - `status`: `performed` (completed), `partial` (partial), `probe` (reconnaissance), `rework-needed`.
4. Write the body: 1–3 paragraphs describing the completed work. Do not duplicate the content of the output artifact.
5. Add a line to the track's "Completed moves": `[[WRK-YYYY-MM-DD-hhmmss]] — FPF-pattern: brief essence`.
6. Add a line to `project-vault/work/_index.md` (table: ID, Track, FPF-pattern, Essence).
7. If the step closes a PlanItem — **delete** the item from the track's "Next moves" (the completed item is recorded by the WRK in "Completed moves"), renumber the remaining items if necessary. Do not strike through `~~...~~` and do not mark `[x]`. If partial — leave it with a clarification.
8. If the step created new entities (DEC, RISK, Q, CON, TRK) — update the corresponding `_index.md`.

### W.3 — Resuming a track

When returning to a track, the reading order is:
1. ProblemCard@Context in the track body — problem side, context, scope cut.
2. "Next moves" — the remaining PlanItems.
3. "Completed moves" — the list of WRKs. If necessary — open the atomic file for details.
4. Item 0 in "Next moves" (if present) — resumption actions.

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
5a. **Agenda is off-limits without request:** do not create or update `project-vault/agenda-next.md` without explicit request. When requested, fill using Procedure E.
6. **Artifacts must be self-contained and alienable** (`artifacts/`): every artifact must be readable and understandable without consulting any other project entity. References to internal project entities (DEC-NNNN, Q-NNNN, RISK-NNNN, CON-NNNN, INV-NN, FR-XXX-NN, etc.) are **prohibited**. Instead of an entity code, always provide a brief substantive description inline.
7. **Track discipline:** a track (`tracks/TRK-NNNN.md`) must have exactly one current status. Status is stored in both frontmatter (`status:`) and the inline table. When updating a track, update both. Do not delete tracks — retired tracks go to `archive/tracks/`. A track must have at least one blocker.
8. **Track-bound work:** any productive activity (research, analysis, synthesis) must be performed within a track (Procedure T). Before acting, announce intent in chat, get user confirmation, then proceed. Do not skip statuses — always start at `cue` and advance step by step.
9. **Work records mandatory:** every completed productive step within a track that produces a new result must be recorded as a WRK file (`project-vault/work/WRK-YYYY-MM-DD-hhmmss.md`) per Procedure W. The track's "Completed moves" list and `work/_index.md` must be updated accordingly.
10. **One track — one ProblemCard@Context:** ProblemCard lives in the track body. If work discovers a new independent problem signal (different EntityOfConcern, different scope cut) — create a child track with its own ProblemCard, not a second ProblemCard in the same track.
11. **File name uniqueness:** file names (except `_index.md`) must not repeat across different project-vault directories. For example, if `artifacts/YYYY-MM-DD_slug.md` is created, then a `sources/digests/YYYY-MM-DD_slug.md` with the same name must not be created — the digest or artifact gets a distinguishing name (via a different slug). The rule eliminates collisions in references (Obsidian, grep) and eases navigation.
12. **No orphan research materials (two-way binding of external research):** every external research digest must be bound two-way — its signals recorded in the files of the corresponding entities (Q, RISK, CON, DEC — any that accept `sources`/`source` or "Related entities"), and the digest added to "Related entities"/`sources` of at least one entity. If the material is outside the scope of all entities — explicitly mark "not bound — outside the project scope" in the digest. A one-way "Reconciliation" only in the digest counts as an incomplete processing.

## After Changes

Briefly list modified and created files.

## Evolution

If the user is dissatisfied with a result or clarifies the process, offer to update this skill. When updating:
- If the trigger is wrong → fix the `description` in frontmatter.
- If a procedure is incomplete → add steps or failure paths in the relevant Procedure section.
- If a template is missing fields → update the template file in `templates/`.
- If the vault schema changed → update `references/architecture.md`.

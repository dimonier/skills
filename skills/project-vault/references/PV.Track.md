---
id: PV.Track
title: "Track as the mandatory container for productive work: lifecycle, statuses, continuation"
status: seed
keywords: [track, lifecycle, status, problem-card, track-bound, work-plan]
dependencies:
  builds_on:
    - C.22.2
    - G.5
    - A.15.1
    - A.15.2
    - E.23
---

## PV.Track - Track as the mandatory container for productive work: lifecycle, statuses, continuation

> **Trigger:** When a request for productive activity arrives (research, analysis, synthesis, architecture work, writing an artifact), or when a track must be continued/created/closed.
> **Skill dependencies:**
>   → none

---

### PV.Track:1 - Problem frame

Use this pattern to decide whether a request is productive work and to govern it
inside a track: create tracks at `cue`, advance them step-by-step through the
elaboration lifecycle, and continue/retire them without skipping statuses.

### PV.Track:2 - Problem

Productive activity without a container sprawls: work is done outside a track,
statuses are skipped, signals are not recorded, "let's continue" has nothing to
lean on. A track must be the mandatory container, but must not proliferate for
every trifle (not for every DEC/RISK/Q).

### PV.Track:3 - Forces

| Force | Settlement |
|---|---|
| Mandatory vs lightweight | Productive work — only in a track; small one-step requests — without a track. |
| One status vs several | A track has exactly one current status (frontmatter + inline). |
| Gradual vs skip | Always start from `cue`, step by step; statuses are not skipped. |
| Container vs proliferation | A track — for an operational line with blockers, spanning several entities. |
| Product vs service track | A product track carries a ProblemCard and the full lifecycle from `cue`; a service track is a standing line for a repeating maintenance procedure, started directly in `in-progress`. |

### PV.Track:4 - Solution

**T.1 — request arrival.**

1. Determine: productive activity (research, analysis, synthesis, multi-step work)
   or a small one-step request.
2. A small task — do it without a track, report.
3. **The request does not point to a track** (e.g. "let's continue", "let's go on"):
   a. Take the top-5 tracks by modification time: `Get-ChildItem
   project-vault\tracks\TRK-*.md | Sort-Object LastWriteTime -Descending |
   Select-Object -First 5`.
   b. Additionally review **all active** tracks (not `performed`/
   `evaluated`/`retired`) for deadlines in "Next moves": highlight
   `(deadline YYYY-MM-DD)` within 3 days of today (including overdue ones).
   c. Show a summary list (top-3 by freshness + tracks with an approaching
   deadline). Sorting: overdue first, then nearest deadline, then fresh. Propose the
   most urgent. Await confirmation.
4. Productive activity with an explicit topic — find a fitting track
   (`SocratiCode codebase_search` or `grep -l "<keyword>" project-vault/tracks/TRK-*.md`):
   - **Exactly one fitting** → "Continuing track TRK-NNNN (name), status — X. Moving to Y". Await confirmation.
   - **Several similar** → show all candidates with statuses, propose the fitting one.
   - **None fitting** → "Creating a new track for [the gist of the request]". Await confirmation.
5. After confirmation — act on the track.

**T.2 — track creation.**

1. A new track always starts with `status: cue`.
2. Advancement — strictly per FPF-core: `cue` → problem-card formulation
   (C.22.2 ProblemCard@Context) → `problem-framed` → method choice (G.5/A.15) →
   `method-selected` → work plan (A.15.2) → `work-planned` → execution (A.15.1)
   → `performed` → result evaluation → `evaluated`.
3. On each transition: announce in chat the intent to move the track to the next
   status with a brief justification (what exactly changed), await confirmation,
   then update the track. After a status change — `vault.py tracks`.
4. Creation: the file `TRK-NNNN.md` from the template `tracks/_template.md`; then `vault.py tracks`.

**T.3 — track continuation.**

1. On continuation: report the current status, the next status, and a brief
   justification for the transition. Await confirmation.
2. After confirmation: update `status` in the frontmatter and in the track's status
   fields. Then — `vault.py tracks`.
3. New artifacts (`artifacts/`) — list them in the track's "Related entities".
4. A substantive step with a result — create a WRK (the WorkRecord procedure) and a
   line in "Completed moves".
5. A blocker found → `blocked`, the blocker into the status fields. On unblocking —
   return the previous active status.

**T.4 — inbox processing and tracks.**
- A material with research/valuable artifacts → into an existing track or create a
  new one (T.1–T.2).
- A transcript/protocol → per StateUpdate, update the related entities (DEC, Q,
  RISK, CON). If the meeting affects an existing track — update the
  status/blockers/next moves.

**T.5 — service track (fallback maintenance container).** A run of a repeating
maintenance procedure (ingestion `PV.Inbox`, vault maintenance) is recorded as a WRK:
- **into a fitting product track**, when the run's material/result belongs to one (the
  routed material landed in or created a track);
- **under the permanent service track**, only when no fitting product track exists
  (e.g. the ingestion produced only atomic entities — DEC/Q/RISK/CON — with no
  operational line).

The service track itself:

- Created once; marked `kind: service` in the frontmatter; permanent while the
  procedure exists.
- Starts directly with `status: in-progress` (a sanctioned exception to "always from
  `cue`", CC-TR.3): it carries no ProblemCard@Context — it is a standing procedure,
  not a problem being solved.
- Exempt from the "at least one blocker" rule (CC-TR.4): a service line has no own
  blocker; its posture is standing, and its "Next moves" hold the recurring
  procedure steps.

**Status lifecycle.** `cue` → `problem-framed` → `method-selected` →
`work-planned` → `in-progress` → `performed` → `evaluated`. Side transitions:
`blocked` (from any active), `deferred` (from any active), `retired` (terminal). A
track has exactly one current status — in the frontmatter and in the inline table.
A service track (T.5) is created directly in `in-progress` and stays there.

### PV.Track:5 - Archetypal Grounding

**Show.** This project's tracks: TRK-2026-0036 went through `cue → problem-framed →
method-selected → work-planned` and is being executed; every transition was
announced in chat and recorded by a WRK.

### PV.Track:6 - Bias-Annotation

The temptation is to create a track for every decision/risk, turning tracks into a
duplicate of the entity registry. The symmetric temptation is to skip statuses
("straight into in-progress"), losing the ProblemCard@Context. Counterweights: a
track — only for an operational line with blockers, and strict step-by-step
advancement.

### PV.Track:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-TR.1 | Productive work is done only in a track; small requests — without a track. |
| CC-TR.2 | A track has exactly one current status (frontmatter + inline). |
| CC-TR.3 | Always starts from `cue`; statuses are not skipped (exception: a service track starts directly in `in-progress` — T.5). |
| CC-TR.4 | A track has at least one blocker (exception: a service track — T.5). |
| CC-TR.5 | Tracks are not deleted; retired ones stay in `tracks/` with `status: retired`. |
| CC-TR.6 | Every status transition is announced and confirmed; then — `vault.py tracks`. |

### PV.Track:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Work outside a track | Create/bind a track before starting the work. |
| Skipping statuses | Always from `cue`, step by step. |
| A track for every entity | Only for an operational line with blockers. |
| Deleting a retired track | Leave it with `status: retired`. |
| Several ProblemCards in one track | A new independent signal → a child track with its own ProblemCard. |
| A track opened for each inbox pass / one-step maintenance act | Record the run as a WRK under the service track (T.5). |
| A service track forced through `cue` or given a fake blocker | A service track starts in `in-progress` with no own blocker (T.5). |

### PV.Track:9 - Consequences

The track as a mandatory container makes work resumable and auditable, but requires
announcing every transition and status discipline. Opening a new independent
problem (another EntityOfConcern / scope cut) — a child track, not a second
ProblemCard in the same track.

### PV.Track:10 - Rationale

`C.22.2` fixes ProblemCard@Context as the core of a track's problem; `G.5`/`A.15` —
method choice and execution; `A.15.2` — the work plan; `E.23` — result evaluation
(the fulfilment assertion). Hence — the lifecycle and the container's mandatory
nature.

### PV.Track:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `C.22.2` (ProblemCard@Context) | Adopt | Problem/context/scope cut in the track body | Reopen on `C.22.2` revision |
| FPF `A.15.2` (work plan) | Adopt | "Next moves" as PlanItems | Reopen on `A.15.2` revision |
| FPF `E.23` (improvement cycle) | Adopt | `performed → evaluated` by the P2W criterion | Reopen on `E.23` revision |

Best-known line: the track as the mandatory container for productive work. Rejected
rival: "work without a track / a track for every entity" — rejected.

### PV.Track:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PV.Track:End

# PV.Track - Track as the mandatory container for productive work: lifecycle, statuses, continuation

> **Trigger:** When a request for productive activity arrives (research, analysis, synthesis, architecture work, writing an artifact), or when a track must be continued, created, or closed.

```episteme id="PV.Track" context="ProjectVault"
Grounding (FPF):
  builds_on: C.22.2, G.5, A.15.1, A.15.2, E.23

UseThisWhen:
  deciding whether a request is productive work and governing it inside a track: create tracks at cue, advance step-by-step through the lifecycle, continue/retire without skipping statuses
  not for a small one-step request (do it without a track); not for every card position

Result:
  productive work resumable and auditable inside a track with exactly one current status, advanced only on owner confirmation

Solution:
  T1.RequestArrival:
    determine productive activity (research/analysis/synthesis/multi-step) vs a small one-step request; a small task → do it without a track, report
    request not pointing to a track ("let's continue"): take top-5 tracks by modification time — Get-ChildItem project-vault\tracks\TRK-*.md | Sort-Object LastWriteTime -Descending | Select-Object -First 5; additionally review all active tracks (not performed/evaluated/retired) for deadlines in "Next moves" (highlight (deadline YYYY-MM-DD) within 3 days, incl. overdue); show top-3 by freshness + tracks with approaching deadline (sort overdue first, then nearest deadline, then fresh); propose the most urgent; await confirmation
    productive with an explicit topic → find a fitting track (SocratiCode codebase_search or grep -l "<keyword>" project-vault/tracks/TRK-*.md): exactly one → "Continuing track TRK-NNNN (name), status — X. Moving to Y", await confirmation; several → show candidates with statuses, propose the fitting one; none → "Creating a new track for [gist]", await confirmation
  T2.TrackCreation:
    always start status: cue
    a draft plan in "Next moves" may be held while cue, marked "draft" (intended, not committed — U.WorkPlan intended-work, asserts no Work, neither advances nor skips the ladder); status advances only on owner confirmation
    advancement strictly per fpf-core: cue → problem-card formulation (C.22.2 ProblemCard@Context) → problem-framed → method choice (G.5/A.15) → method-selected → work plan (A.15.2) → work-planned → execution (A.15.1) → performed → evaluation → evaluated
    each transition: announce intent in chat with a brief justification, await confirmation, then update; after a status change → vault.py tracks
    create TRK-NNNN.md from tracks/_template.md; then vault.py tracks
  T3.TrackContinuation:
    on continuation: report current status, next status, brief justification; await confirmation
    after confirmation: update status in frontmatter + inline fields; then vault.py tracks
    new artifacts → list them in the track's "Related entities"
    a substantive step with a result → a WRK (PV.WorkRecord) + a line in "Completed moves"
    a step closing a PlanItem → remove the item from "Next moves" (never strike through, never [x]); its trace is the WRK line in "Completed moves" (PV.WorkRecord W.2 step 8); "Next moves" holds only remaining PlanItems
    a blocker found → blocked, blocker into the status fields; on unblocking → previous active status
  T4.InboxProcessing:
    material with research/valuable artifacts → into an existing track or create one (T.1–T.2)
    transcript/protocol → per StateUpdate, update the related DEC; if the meeting affects a track → update status/blockers/next moves
  T5.ServiceTrack:
    record a repeating maintenance run (PV.Inbox ingestion, vault maintenance) as a WRK — into a fitting product track when the run belongs to one, under the permanent service track only when no product track fits
    created once; frontmatter kind: service; permanent while the procedure exists
    starts directly status: in-progress (sanctioned exception to "always from cue"); carries no ProblemCard@Context (a standing procedure, not a problem)
    exempt from the "at least one blocker" rule; "Next moves" hold the recurring procedure steps
  Lifecycle:
    cue → problem-framed → method-selected → work-planned → in-progress → performed → evaluated; side: blocked (from any active), deferred (from any active), retired (terminal)

Stop:
  the track's status is current (one status, frontmatter + inline), every transition owner-confirmed and recorded

Checks:
  productive work only in a track; small requests without a track
  exactly one current status (frontmatter + inline)
  always from cue; statuses not skipped (exception: service track starts in-progress — T.5)
  at least one blocker (exception: service track — T.5)
  tracks not deleted; retired ones stay in tracks/ with status: retired
  every transition announced and confirmed; then vault.py tracks
  "Next moves" holds only uncompleted PlanItems; a completed one is removed (trace is the WRK in "Completed moves"), never struck through

Antipatterns:
  work outside a track → create/bind a track before starting
  skipping statuses → always from cue, step by step
  a track for every entity → only for an operational line with blockers
  deleting a retired track → leave with status: retired
  several ProblemCards in one track → a new independent signal → a child track with its own ProblemCard
  a track opened for each inbox pass / one-step maintenance act → WRK under the service track (T.5)
  a service track forced through cue or given a fake blocker → service track starts in-progress, no own blocker (T.5)

Continues:
  PV.WorkRecord (record steps), PV.Artifact (artifacts), PV.StateUpdate (signals/status from sources)

Reopen:
  C.22.2 / A.15.2 / E.23 revision
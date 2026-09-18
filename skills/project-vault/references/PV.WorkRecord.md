---
id: PV.WorkRecord
title: "Work record (WRK): atomic capture of each substantive step in a track"
status: seed
keywords: [work-record, WRK, U.Work, traceability, completed-moves]
dependencies:
  builds_on:
    - A.7
    - A.15.1
    - A.15.2
    - E.23
    - G.11
---

## PV.WorkRecord - Work record (WRK): atomic capture of each substantive step in a track

> **Trigger:** When a substantive step with a new result (an artifact, a decision, an analysis, a structural vault change) has been completed inside a track, and it must be recorded.
> **Skill dependencies:**
>   → none

---

### PV.WorkRecord:1 - Problem frame

Use this pattern to record each completed substantive step in a track as an atomic
WRK file (`U.Work`, A.15.1), so the step is traceable via discovery tools and the
track's "Completed moves" stays current.

### PV.WorkRecord:2 - Problem

Steps not recorded atomically are lost: one cannot trace what exactly was done and
by which method. On the other hand, recording every trifle bloats the journal. A
substantiveness threshold is needed.

### PV.WorkRecord:3 - Forces

| Force | Settlement |
|---|---|
| Traceability vs bloating | A WRK — for a substantive step with a result; not for reconnaissance/trifles/typos. |
| Atomicity vs monolith | One WRK = one dated step, a separate file. |
| Duplication vs brevity | The WRK body — 1–3 paragraphs about the work done, not repeating the output artifact. |
| Improvement vs ritual | Method feedback is an optional pass at WRK closure, emitted only when the substantiveness threshold fires — not a ritual recording of every word. |

### PV.WorkRecord:4 - Solution

**W.1 — when to create a WRK.** Create when:
- A substantive step with a new result (an artifact created via `PV.Artifact`, a
  decision, an analysis, a structural vault change) has been completed inside a track.
- The result must be traceable via discovery tools (`grep`, `SocratiCode`, the
  generated `work/_index.md`).

`performed_under` names the container: the fitting **product track** when the work
belongs to one, or the **service track** for a maintenance run that fits no product
track (inbox intake with no fitting track, vault maintenance — `PV.Track` T.5). Either
way the run is "inside a track".

**Do not create** for: item 0 in "Next moves" (reconnaissance, freshness check);
small administrative actions; fixing obvious errors (typos, formatting).

**W.2 — creating a WRK.**

1. Determine `hhmmss` — the current time (the step's completion moment).
2. Create `project-vault/work/WRK-YYYY-MM-DD-hhmmss.md` from `work/_template.md`.
3. Fill the frontmatter:
   - `id`, `completed` (the completion moment, `YYYY-MM-DD hh:mm:ss`), `performer`, `performed_under` (the container track — the fitting product track, or the service track when none fits).
   - `plan_item_ref` — the number of the item from the track's "Next moves" that was completed (optional for the thin form).
   - `enacted_method` — the applied FPF pattern(s), comma-separated.
   - `input_refs` — the incoming entities (optional for the thin form).
   - `output_refs` — the created/changed entities.
   - `status`: `performed` (done), `partial` (partial), `probe` (reconnaissance), `rework-needed`.
4. Write the body: 1–3 paragraphs about the work done. Do not duplicate the output artifact.
5. Run the method-feedback pass at closure (W.4) before finalizing; on a substantive
   signal — emit it to `outbox/`, otherwise leave the block empty.
6. Add a line to the track's "Completed moves": `[[WRK-YYYY-MM-DD-hhmmss]] — FPF-pattern: the gist`.
7. **Regenerate the indexes** after the WRK: `python scripts/vault.py all` (updates
   `work/_index.md` and `tracks/_index.md`). Do not edit these files by hand.
8. If the step closes a PlanItem — **remove** the item from "Next moves" (the WRK is
   recorded in "Completed moves"), renumbering if needed. Do not strike through and
   do not `[x]`. Partial — leave with a clarification.
9. New entities (DEC/RISK/Q/CON/TRK) — no separate index needed (`grep`/`SocratiCode`
   will find them). A new track — `vault.py tracks`.

**W.3 — track resumption.** Reading order on return:
1. The ProblemCard@Context in the track body — the problem side, context, scope cut.
2. "Next moves" — the remaining PlanItems.
3. "Completed moves" — the list of WRKs; open the atomic file if needed.
4. Item 0 in "Next moves" (if present) — the resumption actions.

**W.4 — method feedback at closure (optional pass).** Before finalizing a WRK, run a
short method-feedback pass over the work just done — it is the private projection of
the improvement loop (`E.23`) and refresh telemetry (`G.11`) onto the WRK closure, so
the most valuable signal about gaps in the skill is not lost in the chat:

1. **Recall the "rethink events":** a decision revisited ≥2 times; a skill rule that
   proved ambiguous; a first version corrected after checking the source
   (`fpf-core`/DPF); an owner clarification that removed an ambiguity.
2. **Classify — emit only if at least one threshold holds** (keep it light, no token
   counters):
   - the signal closes a **gap in the skill** (a missing rule) or **corrects a wrong
     rule** — not a one-off fact of the case;
   - a clearer/more precise rule would **cut decision time, error rate, or reasoning
     length** on the next pass;
   - the same "rethink" recurred **≥2 times** across different cases.
   - **Do not emit:** situational trivia (typos, cosmetics, one-off puzzlement) —
     anything that does not change the speed/accuracy/reasoning cost of the next
     decision.
3. **Emit on a substantive signal:** write one message file into `outbox/` (the
   `PV.Outbox` procedure) referencing the WRK id, the exact rule locus (PatternID /
   section), the essence of the ambiguity/error, and a concrete proposed fix.
   **Never emit, on the owner's behalf, a decision that requires the owner's choice** —
   list the options instead.
4. **No signal → leave the block empty** ("no gaps found"); an empty block is a
   result, not an omission.

### PV.WorkRecord:5 - Archetypal Grounding

**Show.** This project's WRKs: atomic files `work/WRK-YYYY-MM-DD-hhmmss.md` with
`enacted_method` (an FPF pattern), `plan_item_ref` on "Next moves", and a line in the
track's "Completed moves"; indexes auto-generated by `vault.py all`. A WRK whose work
hit a skill ambiguity carries a filled "Method feedback" block and a corresponding
outbox proposal; a WRK with no such signal leaves the block empty.

### PV.WorkRecord:6 - Bias-Annotation

The temptation is to record a WRK for every micro-step, bloating the journal and
devaluing traceability. The symmetric temptation is to copy the output artifact into
the WRK body instead of 1–3 paragraphs. A third temptation is to turn method feedback
into a mandatory ritual (recording every word) or to emit on the owner's behalf. The
substantiveness threshold, brevity, and the options-only rule are the counterweights.

### PV.WorkRecord:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-WR.1 | A WRK is created for a substantive step with a result; not for trifles/reconnaissance. |
| CC-WR.2 | A WRK is an atomic file with a full frontmatter (`id`, `completed`, `performer`, `performed_under`, `enacted_method`, `status`). |
| CC-WR.3 | The body — 1–3 paragraphs, not duplicating the output artifact; an optional "Method feedback" block may follow. |
| CC-WR.4 | A line is added to the track's "Completed moves"; indexes regenerated by `vault.py all`. |
| CC-WR.5 | A closed PlanItem is removed from "Next moves". |
| CC-WR.6 | At WRK closure the method-feedback pass (W.4) ran; a substantive signal is emitted to `outbox/`, otherwise the "Method feedback" block is explicitly empty. |

### PV.WorkRecord:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| A WRK for reconnaissance/a typo | Do not create. |
| The WRK body = a copy of the artifact | 1–3 paragraphs about the work, not the content. |
| Indexes edited by hand | Only `vault.py all`. |
| A PlanItem struck through instead of removed | Remove it; it is recorded by the WRK. |
| Method feedback as a mandatory ritual recording every word | Run it only at closure and only when the threshold fires; leave the block empty otherwise. |
| Emitting a method-feedback signal on the owner's behalf | List the options; do not decide for the owner. |

### PV.WorkRecord:9 - Consequences

Atomic WRKs give end-to-end traceability of steps and methods, but require a
substantiveness threshold and the discipline of auto-regenerating indexes. A WRK is
a separate episteme (`U.Work`) marking the work entry itself, not its result. The
method-feedback channel turns the costly "rethink" into a skill improvement proposal
instead of losing it in the chat, at the cost of one optional pass per WRK.

### PV.WorkRecord:10 - Rationale

`A.15.1` defines `U.Work` — a dated work entry; a WRK records this entry as a
separate episteme. `A.7` — strict distinction: a WRK is distinct from an artifact (the
result) and from a track (the container). `E.23` (improvement loop, with a separate
reviewer) and `G.11` (refresh telemetry) — the method-feedback pass is their private
projection: a costly "rethink" at closure becomes an outbox proposal that can reopen
and refresh the skill.

### PV.WorkRecord:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `A.15.1` (U.Work) | Adopt | WRK as a dated work entry | Reopen on `A.15.1` revision |
| FPF `A.7` (strict distinction) | Adopt | WRK ≠ artifact ≠ track | Reopen on `A.7` revision |
| FPF `E.23` (improvement loop, separate reviewer) | Adopt | Method-feedback pass at WRK closure | Reopen on `E.23` revision |
| FPF `G.11` (refresh telemetry) | Adopt | A method-feedback signal is a skill refresh trigger | Reopen on `G.11` revision |

Best-known line: the atomic work record as U.Work. Rejected rival: "moves as prose
in the track body" — rejected as untraceable.

### PV.WorkRecord:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PV.WorkRecord:End

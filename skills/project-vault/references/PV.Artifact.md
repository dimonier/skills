---
id: PV.Artifact
title: "Creating a track-bound, self-contained and alienable artifact"
status: seed
readiness: source-faithful
keywords: [artifact, self-contained, alienable, track-binding, plan-item]
dependencies:
  builds_on:
    - A.15.1
    - A.15.2
    - E.24.PUB
  coordinates_with:
    - E.8
---

## PV.Artifact - Creating a track-bound, self-contained and alienable artifact

> **Trigger:** When a track needs an artifact (`artifacts/YYYY-MM-DD-slug.md`) — an analysis, a project, a specification — bound to the track and recorded by a WRK.
> **Governing FPF patterns:**
>   → A.15.1 (work execution — the artifact as output)
>   → A.15.2 (work plan — binding to a PlanItem)
>   → E.24.PUB (publication as a separate relation — alienability)
> **Skill dependencies:**
>   → none

---

### PV.Artifact:1 - Problem frame

Use this pattern to create an artifact bound to a track: match it to a track's plan
item, gather context, write it self-contained and alienable, and record the work as
a WRK.

### PV.Artifact:2 - Problem

An artifact written detached from the track, or with internal references to project
entities, is not alienable: the reader cannot understand it without reaching for
other files. An artifact not bound to a PlanItem is not tracked in the track's plan.

### PV.Artifact:3 - Forces

| Force | Settlement |
|---|---|
| Self-containedness vs references | The artifact is read without reaching for other entities; references to internal codes are forbidden — instead a brief substantive description. |
| Binding vs free text | The artifact is bound to a track and to its PlanItem ("Next moves"). |
| Language | Narrative in Russian; English insertions — only proper names, technology names, and terms without an established Russian equivalent. |

### PV.Artifact:4 - Solution

**AR.1 — track binding and plan check.**

1. Determine which track the artifact belongs to (`SocratiCode codebase_search` by
   topic or `grep -l "<keyword>" project-vault/tracks/TRK-*.md`).
2. Check whether there is an artifact-creation item in the track's "Next moves":
   - **An explicit item exists** → use it as the future WRK's `plan_item_ref`.
   - **No item, but the topic matches** → add an item to "Next moves" before creating, announce in chat.
   - **No fitting track** → create a track (Track) with `status: cue`, then add an item to "Next moves".
3. Report: "The artifact [gist] belongs to track TRK-NNNN, plan item — [N or
   'new item added']. Proceeding". Await confirmation.

**AR.2 — gathering materials.**

1. Read the track's ProblemCard@Context — the core of the problem.
2. Gather the track's materials: references to DEC, Q, RISK, CON, artifacts, WRKs on the topic.
3. If needed — read the atomic files of the related entities.
4. If the artifact relies on FPF patterns — load them from fpf-core.

**AR.3 — preparation and writing.**

1. Create `artifacts/YYYY-MM-DD-slug.md`.
2. Maintain self-containedness and alienability: the artifact is read without
   reaching for other project entities; references to internal codes (DEC-NNNN,
   Q-NNNN, RISK-NNNN, CON-NNNN, INV-NN, FR-XXX-NN, etc.) are forbidden — instead
   of the code give a brief substantive description.
3. Language: Russian; English insertions — only proper names, technologies, terms without an equivalent.

**AR.4 — recording the work (WRK).**

1. Immediately after writing — create a WRK (the WorkRecord procedure).
2. In `plan_item_ref` — the item from "Next moves" (from AR.1).
3. In `output_refs` — the created artifact.
4. Update the track's "Completed moves"; then — `python scripts/vault.py work`.
5. If the artifact closes a PlanItem — **remove** the item from "Next moves" (the
   completed item is already recorded by the WRK in "Completed moves"). Do not
   strike through `~~...~~` and do not mark `[x]`. If partial — leave with a clarification.

### PV.Artifact:5 - Archetypal Grounding

**Show.** This project's artifacts (e.g. the PLAS audit) are self-contained, contain
no internal codes, are bound to a track, and are recorded by a WRK.

### PV.Artifact:6 - Bias-Annotation

The temptation is to reference entity codes "for precision", assuming the reader
will figure it out; this breaks alienability. The symmetric temptation is to write
an artifact without a binding to the track's plan, "just a result". Both are about
losing self-containedness and traceability.

### PV.Artifact:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-AR.1 | The artifact is bound to a track and to a PlanItem ("Next moves"). |
| CC-AR.2 | The artifact is self-contained; no internal entity codes in the text. |
| CC-AR.3 | Narrative in Russian; English — only proper names/technologies/terms. |
| CC-AR.4 | The work is recorded by a WRK with `plan_item_ref` and `output_refs`. |
| CC-AR.5 | A closed PlanItem is removed from "Next moves" (not struck through, not `[x]`). |

### PV.Artifact:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Internal codes in the artifact | Replace with a brief substantive description. |
| An artifact without a track binding | Bind to a track/PlanItem before creating. |
| A PlanItem struck through/marked `[x]` | Remove the item; it is recorded by the WRK. |

### PV.Artifact:9 - Consequences

Self-containedness makes the artifact alienable (`E.24.PUB`), but forbids internal
references — a brief description instead of a code. Binding to a PlanItem gives
traceability, but requires synchronizing "Next moves" on closure.

### PV.Artifact:10 - Rationale

`A.15.1` — the artifact as an executed output of work; `A.15.2` — binding to the
plan; `E.24.PUB` — publication as a separate relation: the artifact must read on
its own, without reaching for other project entities.

### PV.Artifact:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `A.15.1` (work execution) | Adopt | The artifact as output + WRK | Reopen on `A.15.1` revision |
| FPF `A.15.2` (work plan) | Adopt | `plan_item_ref` on "Next moves" | Reopen on `A.15.2` revision |
| FPF `E.24.PUB` (publication separately) | Adopt | Artifact self-containedness/alienability | Reopen on `E.24.PUB` revision |

Best-known line: a self-contained artifact bound to the track's plan. Rejected
rival: "an artifact with references to internal codes" — rejected as not alienable.

### PV.Artifact:12 - Relations

- **Builds on:** `A.15.1` (execution), `A.15.2` (plan), `E.24.PUB` (alienability).
- **Coordinates with:** `E.8` (self-contained body).
- **Applies to:** `PV.Track` (an artifact is created bound to a track).

### PV.Artifact:End

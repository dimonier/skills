---
id: ASB.InterSkillComposition
title: "Inter-skill composition: chain by triggering, not by import"
status: seed
keywords: [composition, chaining, triggering, acyclicity, shared-resources, coupling, orchestration, pointer]
dependencies:
  builds_on:
    - E.5.3
    - E.4.PFR
  coordinates_with:
    - E.4
---

## ASB.InterSkillComposition - Inter-skill composition: chain by triggering, not by import

> **Trigger:** When several skills must cooperate on a workflow, or when a draft skill
> keeps pulling in "one more thing".
> **Skill dependencies:** —
---

### ASB.InterSkillComposition:1 - Problem frame

Use this pattern to make skills cooperate without coupling them: the agent chains
atomic skills *through triggering*, not through hard-coded calls.

### ASB.InterSkillComposition:2 - Problem

Cooperation without a discipline happens either by *mega-skill* (merge everything — the
`ASB.Atomicity` anti-pattern) or by *hard-coded calls* ("now run skill B"), which couple
the skills and break triggering. The first creates bloat; the second creates a hidden,
non-evolving dependency graph.

### ASB.InterSkillComposition:3 - Forces

| Force | Settlement |
|---|---|
| Cooperation vs coupling | Skills must cooperate; coupling defeats the layer. |
| Chaining vs orchestration | Letting the agent chain via triggering is emergent; orchestrating is rigid. |
| Shared content vs duplication | Shared `references/`/scripts avoid duplication but create a hidden dependency. |

### ASB.InterSkillComposition:4 - Solution

1. **Chain via triggering, not via import.** End skill A at a point where the user's
   next need will *trigger* skill B through its `description` (`ASB.TriggerDesign`). The
   agent chains; the skills stay independent.
2. **Acyclicity (`E.5.3`).** Skill-to-skill dependencies (e.g. a shared script) must
   form a DAG; no cycles.
3. **Shared resources, not shared bodies.** Where several skills need the same deep
   content, put it in a shared `references/` file (or shared `scripts/` entry) and have
   each body point at it. The shared resource is a *leaf*; skills are nodes pointing at
   it — no duplication, skills stay atomic.
4. **Pointer, not call.** A one-line "X skill covers that, load it if needed" is a
   routing hint, not a load-bearing dependency.
5. **Anti-coupling test.** If removing skill B breaks skill A's body (A references B's
   internal steps), A and B are coupled — merge them (if genuinely one procedure) or
   decouple via triggering.

### ASB.InterSkillComposition:5 - Archetypal Grounding

**Show.** A draft `feature` skill grows to cover model, migration, factory, test,
controller, route — six actions. Decompose (`ASB.Atomicity`); the six chain via
triggering. The shared "naming conventions" prose moves to `references/naming.md`,
pointed at by all six. No body references another's internal steps; each ends at a
natural handoff where the user's next phrasing triggers the next skill.

### ASB.InterSkillComposition:6 - Bias-Annotation

The temptation is **hidden orchestration** — one "manager" skill whose body tells the
agent to run five other skills in order, reborn a small `AGENTS.md`. The counterweight
is chaining via triggering; the manager skill usually signals a missing workflow
description in `AGENTS.md` or an actual mega-skill.

### ASB.InterSkillComposition:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-IC.1 | Skill bodies do not tell the agent to run another skill; they end at natural handoff points. |
| CC-IC.2 | Shared `references/`/`scripts/` form a DAG; no skill–resource cycle. |
| CC-IC.3 | One-line routing hints are admissible and do not create load-bearing dependencies. |

### ASB.InterSkillComposition:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Hidden orchestration (manager skill) | Let the agent chain via triggering. |
| Hard-coded "run skill B" | End at a handoff; let B's `description` trigger it. |
| Duplicated heavy content across siblings | Move to a shared `references/` leaf and point at it. |

### ASB.InterSkillComposition:9 - Consequences

Independent, trigger-chained skills stay atomic, reusable, and independently evolvable,
at the cost of a shared-resource discipline and acyclicity care (`E.5.3`).

### ASB.InterSkillComposition:10 - Rationale

`E.5.3` keeps chained skills acyclic; `E.4.PFR` records skill-to-skill relations as
typed relations, not imports; triggering preserves each skill's independence.

### ASB.InterSkillComposition:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` atomicity (chain via triggering) | Adopt | Chain-via-triggering, shared-content routing | Reopen on a skill-payload edition change |
| AS-DPF `AS.12` Inter-Skill Composition (merged 2026-10-04) | Adopt | Acyclicity, pointer-not-call, anti-coupling test | — merged into this DPF |

### ASB.InterSkillComposition:12 - Relations

FPF governing codes live in this card's frontmatter `dependencies` (single home, not repeated); intra-DPF relations and provenance live in `references/relations.md`.
**Provenance:** former AS-DPF `AS.12` (inter-skill composition).

### ASB.InterSkillComposition:End
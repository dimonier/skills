---
id: ASB.ProgressiveDisclosure
title: "Progressive disclosure: keeping SKILL.md small, externalizing heavy content"
status: seed
keywords: [progressive-disclosure, three-levels, skill-md, references, scripts, externalize]
dependencies:
  builds_on:
    - E.11
    - C.33
  coordinates_with:
    - C.34
---

## ASB.ProgressiveDisclosure - Progressive disclosure: keeping SKILL.md small, externalizing heavy content

> **Trigger:** When deciding what goes in the `SKILL.md` body vs bundled resources (`references/`, `scripts/`, `assets/`, `templates/`) vs what does not belong in the skill at all.
> **Governing patterns:**
>   → `AS.4` (Progressive Disclosure — the AS-DPF pattern this card specializes)
>   → `E.11` (first-practical entry)
>   → `C.33` (carrier admission)
> **Skill dependencies:**
>   → `create-agent-skill` (skill anatomy)

---

### ASB.ProgressiveDisclosure:1 - Problem frame

Use this pattern to keep the skill a three-level loading system that pays its
context cost only at the moment of need — the opposite of a monolithic `AGENTS.md`.

### ASB.ProgressiveDisclosure:2 - Problem

A `SKILL.md` that contains every reference doc, script, and edge case is a small
`AGENTS.md`: always-loaded when triggered, bloated, slow. A body that is too thin
points the agent nowhere when it triggers. The discipline is to load context only on
demand.

### ASB.ProgressiveDisclosure:3 - Forces

| Force | Settlement |
|---|---|
| Completeness vs economy | The body must be complete enough to execute; economy demands it stay small. |
| Reference depth vs context cost | Deep references are useful but costly if always loaded; cheap if loaded on demand. |
| Self-containment vs externalization | A self-contained skill is portable; an externalized one is leaner but has more moving parts. |
| Body vs carrier split | When a heavy source document exists, who reads what must be stated explicitly. |

### ASB.ProgressiveDisclosure:4 - Solution

Use the **three-level loading system**:

1. **Metadata** (`name` + `description`) — always in context (~100 tokens). This is
   the trigger (`ASB.TriggerDesign`); the agent reads only this until it fires.
2. **`SKILL.md` body** — loaded only when the skill triggers. Keep it **under
   ~500 lines**. This is the procedure: steps, success and failure paths, when to
   read which reference, when to run which script.
3. **Bundled resources** — loaded (or executed) on demand from the body:
   - `references/` — docs loaded into context when the body says to (deep dives,
     troubleshooting, framework-specific variants). For files >300 lines, include a
     table of contents.
   - `scripts/` — executable code that runs *without* being loaded into context
     (deterministic/repetitive steps, validators, generators). The body says when to
     run each script.
   - `assets/` — files used in output (templates, icons, fonts, boilerplate).
   - `templates/` — output skeletons and config templates.

**Progressive-discipline rule.** If a body section is >300 lines and not procedure,
move it to `references/`. If it is deterministic code, move it to `scripts/`. If it
is output structure, move it to `templates/`. The body keeps only: the procedure,
when-to-read-which-reference, and when-to-run-which-script.

**Multi-variant skills.** When a skill supports several frameworks, split references
by variant (`references/aws.md`, `references/gcp.md`, `references/azure.md`) and have
the body point to the one matching the user's context.

### ASB.ProgressiveDisclosure:5 - Archetypal Grounding

**Show.** A `deploy` skill starts as a 1200-line `SKILL.md` covering build, push,
canary, rollback, plus full AWS/GCP/Azure runbooks. Decompose: the body keeps the
deploy *procedure* (~200 lines: build → push → canary → verify → rollback-or-promote)
with pointers to `references/aws.md`, `references/gcp.md`, `references/azure.md` and
`scripts/canary.sh`, `templates/deploy-config.yaml`. The body triggers cheaply; the
runbooks load only for the relevant cloud.

### ASB.ProgressiveDisclosure:6 - Bias-Annotation

The temptation is the **flat body**: all reference, all scripts inlined in
`SKILL.md` "for convenience". The symmetry is over-splitting into so many moving
parts that the skill becomes hard to follow. The progressive-discipline rule and the
~500-line budget are the counterweights.

### ASB.ProgressiveDisclosure:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-PD.1 | The three levels are respected: metadata (trigger), body (procedure), bundled resources (on demand). |
| CC-PD.2 | `SKILL.md` body is under ~500 lines; otherwise decomposition or externalization is applied. |
| CC-PD.3 | Non-procedure content >300 lines is externalized to `references/`; deterministic code to `scripts/`; output structure to `templates/`. |
| CC-PD.4 | The body states when to read which reference and when to run which script. |
| CC-PD.5 | For files >300 lines, a table of contents is present. |

### ASB.ProgressiveDisclosure:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Flat body — everything inlined | Externalize per the discipline rule. |
| Body too thin to execute | Keep the full procedure + pointers. |
| Deep reference always loaded | Load it only when the body says to. |
| Deterministic steps described in prose | Move them to `scripts/` and point at the script. |

### ASB.ProgressiveDisclosure:9 - Consequences

Progressive disclosure keeps triggering cheap and context bounded, at the cost of
more files and a body that must maintain accurate pointers. It is the mechanism that
distinguishes a skill from a small `AGENTS.md`.

### ASB.ProgressiveDisclosure:10 - Rationale

`AS.4` defines the three-level system; `E.11` makes level 1 the practical entry;
`C.33` keeps the bundled resources as a carrier returning to the skill's own
authoritative content. Deferring load is what makes tokens pay only at need.

### ASB.ProgressiveDisclosure:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` "Progressive disclosure (3 levels)" + "Anatomy" | Adopt | The three-level model and the resource roles | Reopen on a skill-payload edition change |
| AS-DPF `AS.4` Progressive Disclosure | Adopt | ~500-line body budget, discipline rule, multi-variant split | Reopen on `AS.4` revision |
| AS-DPF `AS.4:4.1` source-of-truth vs derived carrier | Adopt (referenced) | Carrier-level disclosure; specialized by the Spec-Decomposer LPF | Reopen on `AS.4:4.1` revision |

Best-known line: load context only at the moment of need. Rejected rival: the flat
"small `AGENTS.md`" skill — rejected as non-progressive.

### ASB.ProgressiveDisclosure:12 - Relations

- **Builds on (DPF):** `AS.4` (progressive disclosure).
- **Builds on (FPF):** `E.11` (practical entry), `C.33` (carrier admission).
- **Coordinates with (DPF):** `AS.3` (externalize shared content), `AS.4:4.1` (source-of-truth vs derived carrier), `C.34` (tooling-reference carrier).
- **Specialized by (LPF):** `ASB.Atomicity` (shared heavy content goes to `references/`), `ASB.Compaction` (Move 1 is the same deletion/externalization).

### ASB.ProgressiveDisclosure:End

---
id: ASB.Evolution
title: "Skill evolution & currentness: the 'offer to update' rule and refresh triggers"
status: seed
keywords: [evolution, currentness, changelog, refresh, deprecation, offer-to-update]
dependencies:
  builds_on:
    - E.23
    - G.11
    - E.4.PFR
---

## ASB.Evolution - Skill evolution & currentness: the 'offer to update' rule and refresh triggers

> **Trigger:** When a skill produces a result the owner is dissatisfied with, when the process is clarified, or when the tools/agents/sources the skill depends on change.
> **Governing patterns:**
>   → `AS.10` (Skill Evolution & Currentness — the AS-DPF pattern this card specializes)
>   → `E.23` (improvement loop)
>   → `G.11` (currentness, edition pins, decay)
>   → `E.4.PFR` (edition/deprecation records)
> **Skill dependencies:**
>   → `create-agent-skill` (evolution rule)

---

### ASB.Evolution:1 - Problem frame

Use this pattern to keep a skill current: hardcode an "offer to update" rule in every
skill, route the fix to the right file, and reopen the skill when its dependencies
change.

### ASB.Evolution:2 - Problem

Without an evolution route, a skill silently decays: tools change, neighbouring
skills shift the trigger competition, and the owner's clarifications never reach the
body. A fix applied in the wrong place (or not at all) leaves the skill wrong while
looking maintained.

### ASB.Evolution:3 - Forces

| Force | Settlement |
|---|---|
| Stability vs currentness | A skill must stay addressable while its content is kept fresh (`G.11`). |
| Owner clarification vs author guess | Unsatisfactory results/clarifications trigger an update offer, not a silent rewrite. |
| Fix locality | A well-structured skill makes it obvious which file to change. |

### ASB.Evolution:4 - Solution

**Hardcode this rule in every skill:**

> If the user is dissatisfied with the result or clarifies the process, offer to
> update this skill.

The agent then:
1. **Identifies what to change** — `description`, algorithm/body, `references/`,
   template, or troubleshooting file.
2. **Updates the relevant file.**
3. **Optionally logs** the change in a `CHANGELOG.md` inside the skill directory
   (version history, not authoring residue).

**Refresh triggers (`G.11`) — reopen the skill when:**
- a tool, agent product, or source the skill depends on changes;
- a neighbouring skill shifts trigger competition (description accuracy decays);
- the model that executes the skill changes materially;
- the owner reports misuse/ambiguity, or a weak-model gate run fails;
- a superseding skill or edition appears (record via `E.4.PFR`; deprecate explicitly).

**A well-structured skill makes the fix obvious.** If it is not obvious where to
apply the fix, the skill is probably too large or poorly organized
(`ASB.Atomicity`, `ASB.ProgressiveDisclosure`).

### ASB.Evolution:5 - Archetypal Grounding

**Show.** An owner says "the deploy skill keeps skipping the rollback check". The
agent offers an update, identifies the fix locus (the body's step list) and adds an
explicit `scripts/rollback-check.sh` call; the change is logged in the skill's
`CHANGELOG.md`. Later a cloud CLI changes its flags → a `G.11` refresh reopens
`references/aws.md`.

### ASB.Evolution:6 - Bias-Annotation

The temptation is to treat a skill as finished and never reopen it — silent decay.
The symmetry is to "improve" the wording endlessly without an evaluation
characteristic (`E.23` with a target level). Hardcoding the offer rule and naming
refresh triggers are the counterweights.

### ASB.Evolution:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-EV.1 | The skill's body contains the "offer to update" rule. |
| CC-EV.2 | The fix locus is identifiable (description / body / references / template / troubleshooting). |
| CC-EV.3 | Refresh triggers are named (`G.11`): tool, agent, source, model, misuse, supersession. |
| CC-EV.4 | Deprecation/supersession is recorded (`E.4.PFR`); the skill is not silently dropped. |
| CC-EV.5 | Improvement targets a measured aspect, not open-ended re-wording (`E.23`). |

### ASB.Evolution:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| A skill treated as forever-finished | Name refresh triggers; reopen on change. |
| Clarification lost in chat | Offer and apply an update to the relevant file. |
| Improving wording without a characteristic | Pick a measured aspect (`E.23`). |
| Silent supersession | Record deprecation/supersession (`E.4.PFR`). |

### ASB.Evolution:9 - Consequences

The evolution rule keeps the skill trustworthy over time, at the cost of a recurring
review loop and a `CHANGELOG` when kept. A skill that is hard to update signals a
structural problem, not a maintenance burden.

### ASB.Evolution:10 - Rationale

`AS.10` fixes the offer rule and refresh triggers; `E.23` requires improvement with a
target level; `G.11` governs currentness and edition pins; `E.4.PFR` records
edition/deprecation. Together they make the skill's currency auditable.

### ASB.Evolution:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` "Making Skills Evolve" (offer-to-update rule, `CHANGELOG`) | Adopt | The hardcoded rule and the three agent steps | Reopen on a skill-payload edition change |
| AS-DPF `AS.10` Skill Evolution & Currentness | Adopt | Refresh triggers (tool/agent/source/model/supersession) | Reopen on `AS.10` revision |
| FPF `E.23`/`G.11`/`E.4.PFR` | Adopt | Improvement loop, currentness, deprecation records | Reopen on FPF revision |

Best-known line: hardcode the offer-to-update rule. Rejected rival: "a skill is
finished once written" — rejected as silent decay.

### ASB.Evolution:12 - Relations

- **Builds on (DPF):** `AS.10` (evolution & currentness).
- **Builds on (FPF):** `E.23` (improvement loop), `G.11` (currentness), `E.4.PFR` (edition/deprecation).
- **Coordinates with (DPF):** `AS.8` (re-run the weak-model gate on revision).

### ASB.Evolution:End

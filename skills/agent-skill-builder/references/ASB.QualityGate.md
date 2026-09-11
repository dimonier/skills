---
id: ASB.QualityGate
title: "Quality gate: the weak-model test"
status: seed
keywords: [quality-gate, weak-model, admission, iterate, opus-only, blind-trust]
dependencies:
  builds_on:
    - E.21
    - E.19
  coordinates_with:
    - E.22
---

## ASB.QualityGate - Quality gate: the weak-model test

> **Trigger:** Before relying on a skill — when deciding whether it is written well enough that a weaker model will follow it without extra questions or invented steps.
> **Governing patterns:**
>   → `AS.8` (Quality Gate / Weak-Model Test — the AS-DPF pattern this card specializes)
>   → `E.21` (pattern quality)
>   → `E.19` (admission)
> **Skill dependencies:**
>   → `create-agent-skill` (weak-model gate)

---

### ASB.QualityGate:1 - Problem frame

Use this pattern as the admission test for a skill: if a **weak model** (Sonnet,
GPT-4o-mini, a 30B-class model) performs the skill without extra questions or
hallucinated steps, the skill is well written.

### ASB.QualityGate:2 - Problem

A skill that only works with a top-tier model on max thinking has hidden a prompt in
a file and hopes the expensive model carries the author's laziness. Untested skills
are unchecked prompts in a folder: they may stumble on an ambiguous step, invent a
missing one, or ask for clarification — and the failure is silent until a weaker
model hits it.

### ASB.QualityGate:3 - Forces

| Force | Settlement |
|---|---|
| Cost vs reliability | Tokens are not free; weaker models execute faster and cheaper. |
| Author confidence vs evidence | The author's belief ("works for me") is not the gate; a weak-model run is. |
| Blind trust vs review | Generated skills need judgment, especially the `description`. |

### ASB.QualityGate:4 - Solution

1. **Give the weak model a typical prompt** that should trigger the skill.
2. **Observe:** does it follow every step? does it ask for clarification? does it
   invent missing steps?
3. **If it stumbles:** add more explicit commands, script the fragile `bash` calls,
   provide output templates (not "write a summary" but a specific format).
4. **Iterate** until the weak model passes without questions or invention.
5. **Apply the admission rule:** each body carries an `E.21` result or an explicit
   `seed` mark; a skill is admitted only after the gate (`E.19`).

**Why it matters.** A skill that works on weak models works *better* on strong ones
(less hallucination, fewer skipped steps), and weaker models are cheaper and faster.

### ASB.QualityGate:5 - Archetypal Grounding

**Show.** A weak-model run of a `deploy` skill stumbles on "run the smoke test": the
model runs the wrong command. Repair — the body replaces "run the smoke test" with
`scripts/smoke.sh --env staging` and a template for the expected output. The rerun
passes without questions.

### ASB.QualityGate:6 - Bias-Annotation

Two biases: **blind `skill-creator` trust** — shipping a generated skill without
reviewing (especially the `description`); and **Opus-only dependence** — a skill that
only a top-tier model can follow, mistaken for "good enough". Testing on a weak model
is the counterweight to both.

### ASB.QualityGate:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-QG.1 | A weak-model run with a typical trigger prompt has been performed. |
| CC-QG.2 | The weak model follows every step without extra questions or invented steps; otherwise the skill is revised. |
| CC-QG.3 | Fragile operations have explicit commands/scripts; outputs have templates. |
| CC-QG.4 | Each body carries an `E.21` result or an explicit `seed` mark before reliance. |
| CC-QG.5 | A generated skill (e.g. from `skill-creator`) was reviewed, especially the `description`. |

### ASB.QualityGate:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| "Works in the demo" treated as admissible | Run the weak-model gate; add explicit steps/templates. |
| Opus-only skill | Break steps down; script fragile calls; add templates. |
| Blind `skill-creator` trust | Review and tune the generated skill, especially the `description`. |
| No `seed`/`E.21` status | Mark bodies honestly until the threshold is met. |

### ASB.QualityGate:9 - Consequences

The gate spends a cheap model run up front but prevents shipping a skill that only
works for the author's model, at the cost of an iterate loop and explicit
commands/templates in the body.

### ASB.QualityGate:10 - Rationale

`AS.8` makes the weak-model test the admission criterion; `E.21` evaluates pattern
quality; `E.19` gates admission. A skill that works on weak models is strictly better
on strong ones, so the gate is both a quality and a cost criterion.

### ASB.QualityGate:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` "Quality Gate" + Anti-Patterns ("blind skill-creator trust", "Opus-only dependence") | Adopt | Weak-model test, iterate loop, the two related anti-patterns | Reopen on a skill-payload edition change |
| AS-DPF `AS.8` Quality Gate (Weak-Model Test) | Adopt | Admission rule and "why it matters" | Reopen on `AS.8` revision |
| `create-agent-skill` quality gate | Adopt | Weak-model gate as a skill-carrier contract | Reopen when the gate changes |

Best-known line: a weak model must follow every step. Rejected rival: "works in the
demo" / Opus-only skill — rejected.

### ASB.QualityGate:12 - Relations

- **Builds on (DPF):** `AS.8` (quality gate).
- **Builds on (FPF):** `E.21` (pattern quality), `E.19` (admission).
- **Coordinates with (DPF):** `AS.6` (evaluation loop), `AS.7` (description optimization).
- **Specialized by (LPF):** `ASB.Evolution` (the weak-model gate re-runs on every revision).

### ASB.QualityGate:End

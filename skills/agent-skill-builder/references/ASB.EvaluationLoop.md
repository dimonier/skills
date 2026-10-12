---
id: ASB.EvaluationLoop
title: "Evaluation loop: prove the skill works before relying on it"
status: seed
keywords: [evaluation, baseline, assertions, iteration, benchmark, non-circular, self-eval, generalization]
dependencies:
  builds_on:
    - E.21
    - E.23
  coordinates_with:
    - E.22
    - C.35
---

## ASB.EvaluationLoop - Evaluation loop: prove the skill works before relying on it

> **Trigger:** After drafting a skill, before relying on it — to determine whether it
> actually works, not merely whether it "seems right".
> **Skill dependencies:**
>   → `skill-creator` (the draft → test → review → improve loop mechanics)

---

### ASB.EvaluationLoop:1 - Problem frame

Use this pattern to run the `draft → test → review → improve` loop. The mechanics of
the loop (with-skill vs baseline spawning, assertion drafting, grading, benchmark
aggregation, human review) live in the `skill-creator` skill — this card covers the
three disciplines that make the loop *honest*, and the headless adaptation.

### ASB.EvaluationLoop:2 - Problem

A skill "seems right" in the author's head but silently fails on real prompts: it skips
steps, invents steps, over-fires, under-fires, or produces wrong output. Without an
evaluation loop these failures surface in production, by users, at cost. Three specific
ways the loop cheats: (a) no baseline — "improvement" is indistinguishable from chance;
(b) prompts that match the skill's own worked examples — they test recollection, not
generalization; (c) circular grading — scoring "did it apply the pattern" against the
pattern text yields 1.00 by construction.

### ASB.EvaluationLoop:3 - Forces

| Force | Settlement |
|---|---|
| Rigor vs speed | Baselines and parallel runs are heavy; a one-off vibe check misses regressions. |
| Objective vs subjective | File transforms are objectively checkable; writing quality needs human judgment. |
| Skill vs baseline | A skill run alone cannot separate improvement from chance; a baseline must be run. |

### ASB.EvaluationLoop:4 - Solution

1. **Run the `skill-creator` loop**, applying three disciplines on top:
2. **Baseline is mandatory.** Every iteration runs with-skill *and* a baseline
   (no-skill for a new skill, the old skill for an improvement — snapshot it first),
   so the delta is attributable, not assumed.
3. **Generalization probes.** At least one test prompt must deviate from the skill's own
   worked slices; a prompt that matches a worked slice tests recollection.
4. **Non-circular self-eval.** When the framework grades *itself*, assertions must not
   be derivable from its own pattern text. Use one or more non-circular probes:
   - **Blind-preference** — rate with-skill vs without-skill outputs side by side, blind.
   - **Generalization** — prompts that deviate from the worked slices.
   - **Parrot-check** — re-run with the matching worked slice redacted; if the output
     collapses, the pattern leaned on the slice, not the rule.
   Report the circular delta as an *upper bound*, separately from the non-circular delta.
5. **Headless adaptation.** Without subagents: run serially, skip quantitative
   benchmarks, present results inline, save outputs for the user — the human review
   loop compensates for the lost rigor.

### ASB.EvaluationLoop:5 - Archetypal Grounding

**Show.** A `changelog` skill is drafted. Three prompts: "what changed in this PR",
"add a release note for the auth fix", "we just shipped a breaking API change". With-
skill and without-skill run in parallel. Assertions drafted: "entry follows
Keep-a-Changelog", "under 100 chars", "breaking change marked with `!`". With-skill
pass rate 0.67 vs baseline 0.33. One run hallucinated a source ref; the fix adds "never
invent source refs" + a `templates/changelog-entry.stub`. Iteration-2: 0.89.

### ASB.EvaluationLoop:6 - Bias-Annotation

The temptation is the **vibe-check** — "I'll just try it a few times", which cannot
distinguish skill effect from chance. The symmetric temptation is **circular
self-scoring** — grading "did you apply X" against X, which reports a perfect score by
construction. Baseline + non-circular probes are the counterweight to both.

### ASB.EvaluationLoop:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-EL.1 | A baseline (no-skill or old-skill) run accompanies every with-skill iteration. |
| CC-EL.2 | At least one test prompt deviates from the skill's own worked slices. |
| CC-EL.3 | Self-eval uses a non-circular probe; the circular delta is reported separately. |
| CC-EL.4 | Outputs, grading, benchmark, and feedback are saved for the next iteration. |

### ASB.EvaluationLoop:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Vibe-only ("I'll try it a few times") | Run with-skill vs without-skill on 2–3 realistic prompts; capture outputs. |
| Optimize on the skill's own examples | Add a prompt that deviates from the worked slices. |
| Circular self-grade | Blind-preference / generalization / parrot-check probes; report separately. |

### ASB.EvaluationLoop:9 - Consequences

The loop spends model runs and wall-clock up front but replaces silent production
failure with a measured delta and an artifact trail for the next iteration. Non-circular
self-eval keeps the framework honest about its own quality.

### ASB.EvaluationLoop:10 - Rationale

`E.21` evaluates pattern quality, `E.23` drives improvement, `C.35` admits generated
carriers. The three disciplines (baseline, generalization, non-circular) are what stop
the loop from flattering the author.

### ASB.EvaluationLoop:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `skill-creator` draft → test → review → improve loop | Adopt (referenced) | Loop mechanics are cited, not reproduced | Reopen on a `skill-creator` workflow change |
| AS-DPF `AS.6` Evaluation Loop (merged 2026-10-04) | Adopt | Baseline, generalization, headless adaptation | — merged into this DPF |
| AS-DPF `AS.QR:2.1` non-circular self-eval (merged 2026-10-04) | Adopt | Blind-preference / generalization / parrot-check probes | — merged into this DPF |

### ASB.EvaluationLoop:12 - Relations

FPF governing codes live in this card's frontmatter `dependencies` (single home, not repeated); intra-DPF relations and provenance live in `references/relations.md`.
**Provenance:** former AS-DPF `AS.6` (and `AS.QR:2.1`).

### ASB.EvaluationLoop:End
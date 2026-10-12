---
id: ASB.DescriptionOptimization
title: "Description optimization: tune the trigger empirically"
status: seed
keywords: [description, trigger, tuning, eval, near-miss, held-out, over-fire, under-fire]
dependencies:
  builds_on:
    - G.11
  coordinates_with:
    - C.35
---

## ASB.DescriptionOptimization - Description optimization: tune the trigger empirically

> **Trigger:** When a skill triggers correctly sometimes but not reliably, or when a
> new neighbouring skill creates trigger collisions.
> **Skill dependencies:**
>   → `skill-creator` (description-optimization `run_loop.py` / `generate_review.py`)

---

### ASB.DescriptionOptimization:1 - Problem frame

Use this pattern to measure and tune the `description`'s triggering accuracy instead of
assuming it. It sits on top of `ASB.TriggerDesign` (which writes the `description`);
this card measures and optimizes it.

### ASB.DescriptionOptimization:2 - Problem

A hand-written `description` is a hypothesis. Triggering accuracy at scale — across many
prompts, against many sibling skills — is an empirical property that must be measured,
not assumed.

### ASB.DescriptionOptimization:3 - Forces

| Force | Settlement |
|---|---|
| Train vs test | Optimizing on train over-fits; held-out test reveals generalization. |
| Length vs precision | Longer descriptions cover more phrasings but over-fire. |
| Skill count vs discriminability | More siblings raise collision risk; descriptions must disambiguate. |

### ASB.DescriptionOptimization:4 - Solution

1. **Generate ~20 trigger eval queries** — half should-trigger, half should-not-trigger.
   The should-not-trigger queries must be **near-misses** (share keywords with the skill
   but need something else); obvious irrelevancies test nothing.
2. **Review the eval set with the user** — bad queries give bad descriptions.
3. **Run the optimization loop** — split 60% train / 40% held-out test; evaluate the
   current `description` (each query 3× for a reliable trigger rate); propose
   improvements; re-evaluate each candidate on both train and test; select by
   **held-out test score, not train**, to avoid over-fitting.
4. **Apply** — take `best_description`, update the frontmatter, show before/after + scores.
5. **Currentness** — re-run the loop when a sibling skill is introduced or trigger
   complaints recur (`G.11`).

**How triggering works.** The agent consults skills mainly for tasks it cannot easily
handle alone; trivial one-step queries may not trigger even with a perfect description.
Design queries substantive enough that the agent would benefit from the skill.
**Under-triggering compensation.** Descriptions are made pushy (`ASB.TriggerDesign`),
then this loop removes the over-fires.

### ASB.DescriptionOptimization:5 - Archetypal Grounding

**Show.** A `pdf` skill's description under-triggers on "extract the table from page 4".
20 queries: 10 should-fire (parse, extract table, merge, fill form, OCR) + 10 near-miss
should-not ("convert PDF to a Word doc", "what does PDF stand for", "send this PDF by
email"). 60/40 split, 3× each. The loop proposes a description naming "read, extract,
merge, split, rotate, OCR, fill, or manipulate a `.pdf` file, even if they only say
'this report'". Held-out test score rises 0.55 → 0.85.

### ASB.DescriptionOptimization:6 - Bias-Annotation

The temptation is **optimize-on-train-report-train** — over-fitting to the eval set,
looking good on it and failing in the wild. The counterweight is selecting by held-out
test score and reporting both.

### ASB.DescriptionOptimization:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-DO.1 | At least half of should-not-trigger queries are genuine near-misses. |
| CC-DO.2 | The winning description is selected by held-out test score, not train. |
| CC-DO.3 | Each query is substantive enough that the agent would benefit from the skill. |
| CC-DO.4 | The loop is re-run when sibling skills are added or trigger complaints recur. |

### ASB.DescriptionOptimization:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Optimize on train, report train | Select by held-out test; report both. |
| Obvious irrelevancies as negatives | Use near-misses that share the skill's keywords. |
| English-only eval set for a non-English user | Draw queries from the user's working language(s). |

### ASB.DescriptionOptimization:9 - Consequences

A tuned `description` loads accurately and cheaply, at the cost of an eval set and an
optimization loop that must be re-run as siblings shift (`G.11`).

### ASB.DescriptionOptimization:10 - Rationale

`G.11` ties trigger accuracy to currentness; `C.35` admits the optimized carrier. The
held-out split is what separates tuning from over-fitting.

### ASB.DescriptionOptimization:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `skill-creator` description-optimization loop | Adopt (referenced) | 60/40 split, iterate-up-to-N | Reopen on a `skill-creator` workflow change |
| AS-DPF `AS.7` Description Optimization (merged 2026-10-04) | Adopt | Near-miss negatives, held-out selection, currentness | — merged into this DPF |

### ASB.DescriptionOptimization:12 - Relations

FPF governing codes live in this card's frontmatter `dependencies` (single home, not repeated); intra-DPF relations and provenance live in `references/relations.md`.
**Provenance:** former AS-DPF `AS.7` (description optimization).

### ASB.DescriptionOptimization:End
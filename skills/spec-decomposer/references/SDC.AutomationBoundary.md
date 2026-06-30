---
id: SDC.AutomationBoundary
title: Automation boundary
---

# SDC.AutomationBoundary: Automation boundary

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

---

### 6.10 `SDC.AutomationBoundary` — Automation boundary

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | After several manual decompositions the desire arises to automate everything. But some steps require human judgment: trigger condition formulation, governing-pattern mapping verification, routing table validation. Attempting full automation yields a syntactically correct but semantically incorrect result |
| **ContextGrounding** | A `decompose.py` script is being developed (or an AI agent is used) for decomposition automation. It is necessary to define what is automated and what remains for the human |
| **ScopeCut** | Boundary between scriptable and non-scriptable decomposition steps; does not cover choice of language/stack for the script |
| **NotWishReason** | "The script will handle everything" — blind trust in the script output without human review |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Automation boundary — a list of decomposition steps classified as: automatable / requires-human-review / human-only |
| **SymptomDetection** | Script generates trigger condition "see ProblemSignal" instead of a concrete formulation; script does not update the routing table in SKILL.md; script silently skips problem cards with non-standard structure |
| **ProblemHypothesis** | The automation boundary is not defined. Step classification: (A) automatable — structural extraction, boundary detection, INDEX generation; (H) human-review-required — trigger condition formulation, governing-cue mapping validation; (S) script-assisted — routing table update (script proposes, human confirms) |
| **ImprovementCheck** | Script performs automatable steps without errors; human-review steps have explicit checkpoints; the decomposition result passes validation |
| **AcceptanceCriterion** | Automation boundary is documented: (A) extraction, boundary detection, file writing, INDEX.md, relations.md — script, (H) trigger condition, governing-cue mapping, routing table update — human (or agent with human review), (S) SKILL.md update — script generates diff, human confirms |
| **MandatoryConstraints** | Prohibited to automatically overwrite SKILL.md without human review; prohibited to automatically generate trigger conditions without validation; the script must report non-standard structures, not silently skip them |
| **CharacterizationRelation** | Automation coverage (% of steps performed by script), error detection (does the script report problems), human-review burden (how many steps require manual review) |
| **ValidationBoundary** | Verification: script run on 2 different DPFs; comparison of manual and automated decomposition results |
| **FreshnessOrExpiry** | `stale` when the structure of monoliths or reference file format changes |
| **ReadinessDisposition** | `P2W-ready` for designing `decompose.py` |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Agent role and responsibility boundary | `E.16` |
| SoTA-echoing and source reference | `G.2` |
| Problem card as frame for automation decision | `C.22.2` |
| Improvement loop (script improves iteratively) | `E.23` |

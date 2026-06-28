# SDC.AutomationBoundary: Automation Boundary

> **Trigger:** After several manual decompositions, there is a desire to automate everything — but some steps require human judgment
> **Governing patterns:** 
>   → `../fpf-core/references/E.16-agent-roles.md`
>   → `../fpf-core/references/G.2-sota-echoing.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/E.23-improvement-loop.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | After several manual decompositions, there is a desire to automate everything. But some steps require human judgment: formulating trigger conditions, validating governing-pattern mappings, verifying routing tables. Attempting full automation produces syntactically correct but semantically incorrect results |
| **ContextGrounding** | A `decompose.py` script is being developed (or an AI agent is used) to automate decomposition. It is necessary to determine what is automated and what remains with the human |
| **ScopeCut** | The boundary between scriptable and non-scriptable decomposition steps; does not cover the choice of language/stack for the script |
| **NotWishReason** | "The script will do everything itself" — blind trust in script output without human review |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Automation boundary — a list of decomposition steps classified as: automatable / requires-human-review / human-only |
| **SymptomDetection** | The script generates a trigger condition "see ProblemSignal" instead of a concrete formulation; the script does not update the routing table in SKILL.md; the script silently skips problem cards with non-standard structure |
| **ProblemHypothesis** | The automation boundary is not defined. Step classification: (A) automatable — structural extraction, boundary detection, INDEX generation; (H) human-review-required — trigger condition formulation, governing-cue mapping validation; (S) script-assisted — routing-table update (script proposes, human confirms) |
| **ImprovementCheck** | The script performs automatable steps without errors; human-review steps have explicit checkpoints; the decomposition result passes validation |
| **AcceptanceCriterion** | Automation boundary is documented: (A) extraction, boundary detection, file writing, INDEX.md, relations.md — script, (H) trigger condition, governing-cue mapping, routing-table update — human (or agent with human review), (S) SKILL.md update — script generates diff, human confirms |
| **MandatoryConstraints** | It is forbidden to automatically overwrite SKILL.md without human review; it is forbidden to automatically generate trigger conditions without validation; the script must report non-standard structures rather than silently skipping them |
| **CharacterizationRelation** | Automation coverage (% of steps performed by script), error detection (does the script report problems), human-review burden (how many steps require manual verification) |
| **ValidationBoundary** | Verification: script run on 2 different DPFs; comparison of manual and automated decomposition results |
| **FreshnessOrExpiry** | `stale` when the structure of monoliths or the reference file format changes |
| **ReadinessDisposition** | `P2W-ready` for designing `decompose.py` |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Agent role and responsibility boundary | `E.16` |
| SoTA-echoing and source reference | `G.2` |
| Problem card as a frame for automation decision | `C.22.2` |
| Improvement loop (script improves iteratively) | `E.23` |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L437-L471

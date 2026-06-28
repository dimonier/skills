# SDC.UnitRecognition: Recognizing Extractable Units

> **Trigger:** A framework's monolithic specification contains heterogeneous sections; not everything should be extracted into `references/`
> **Governing patterns:** 
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/E.8-pattern-body.md`
>   → `../fpf-core/references/E.4.DPF-authoring.md`
>   → `../fpf-core/references/C.33-carrier-admission.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | A framework's monolithic specification contains heterogeneous sections: problem cards, relation records, context declaration, source pack, quality route, appendix. Not everything should be extracted into `references/`. Attempting to extract "everything indiscriminately" yields reference files with non-pattern content |
| **ContextGrounding** | An existing DPF/LPF/FPF monolith is being decomposed. The monolith has an `E.4.DPF` spine: context → source pack → PFAD → names → patterns → relations → publication → quality → refresh |
| **ScopeCut** | Identification of extractable units (problem cards, patterns) vs non-extractable sections (context declaration, source pack, publication, quality route); does not cover recognition of arbitrary markdown structures |
| **NotWishReason** | "Let's extract all sections with third-level headings" — we'd get reference files with context declaration and quality route, which are not patterns |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Extractable unit — a structural unit of the monolith that is a self-sufficient pattern or problem card and should become a separate reference file |
| **SymptomDetection** | The following end up in `references/`: context declaration (section 1), source pack (section 2), PFAD (section 3), publication (section 8), quality route (section 9), refresh route (section 10) — which are not patterns |
| **ProblemHypothesis** | The criterion for extractable vs non-extractable is not defined. Criterion: extractable = a problem card (`C.22.2`) or pattern body (`E.8`) that has a ProblemSignal, a Solution/SoTA move, and Governing-Pattern Cues |
| **ImprovementCheck** | Each reference file contains a problem card or pattern. Non-extractable sections remain only in the monolith |
| **AcceptanceCriterion** | Extractable units identified by: (1) presence of ProblemSignal, (2) presence of a SoTA move / AcceptanceCriterion, (3) presence of Governing-Pattern Cues, (4) belonging to section 6 (Problem Cards) or equivalent pattern section |
| **MandatoryConstraints** | It is prohibited to extract: sections 1-5 (context, source pack, PFAD, names, carrier admission), sections 7-10 (relations, publication, quality, refresh), appendix; each extracted unit must be self-sufficient (readable without the context of neighboring sections) |
| **CharacterizationRelation** | Precision (are all extractable units found), recall (are there any false positives — extracted non-patterns) |
| **ValidationBoundary** | Verification: an expert reviews the list of extracted units and confirms that each is a self-sufficient pattern |
| **FreshnessOrExpiry** | `stale` when the `E.4.DPF` spine or the structure of a specific framework changes |
| **ReadinessDisposition** | `P2W-ready` before starting decomposition of a specific monolith |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Problem card identification | `C.22.2` |
| Pattern body structure | `E.8` |
| DPF authoring spine | `E.4.DPF` |
| Framework carrier admission | `C.33` |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L107-L141

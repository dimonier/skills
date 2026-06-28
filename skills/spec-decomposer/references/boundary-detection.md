# SDC.BoundaryDetection: Boundaries of Extracted Units

> **Trigger:** Problem card boundaries in the monolith are defined by markdown headings, but headings of different levels are nested irregularly
> **Governing patterns:** 
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/E.8-pattern-body.md`
>   → `../fpf-core/references/E.17-description-vs-described.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | Problem card boundaries in the monolith are defined by markdown headings, but headings of different levels (`###`, `####`, `#####`) are nested irregularly. Cutting at "the next heading of the same level" leads to loss of subsections (worked examples, conformance checklists) or captures foreign content |
| **ContextGrounding** | DPF monolith: problem cards begin with `### 6.X PatternID — Name`, contain nested `#### Always‑Core Fields`, `#### Conditional Fields`, `#### Governing‑Pattern Cues` and optionally `#### Worked Examples`, `#### Conformance Checklist`. The next problem card begins with `### 6.Y ...` |
| **ScopeCut** | Defining boundaries "from the problem card heading to the heading of the next problem card (or to the start of section 7)"; does not cover boundary detection for non-DPF structures |
| **NotWishReason** | "Cut at the nearest `###`" — lose all `####` subsections or capture the next problem card |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Problem card boundary in markdown — line range from the opening heading `### 6.X` to the line before the next heading `### 6.Y` (or `## 7` if it is the last card) |
| **SymptomDetection** | Reference file is truncated at Always-Core Fields (Conditional Fields and Governing-Pattern Cues are lost); or reference file contains two problem cards (boundary is wrong) |
| **ProblemHypothesis** | The cutting algorithm uses the wrong heading level as terminator. Rule: for DPF — terminator = `### 6.` or `## 7`; for FPF patterns — terminator = `## E.X` or `### E.X:N` of the next pattern |
| **ImprovementCheck** | Each reference file contains exactly one problem card: Always-Core + Conditional + all optional subsections + Governing-Pattern Cues. The next card is in a separate file |
| **AcceptanceCriterion** | Boundaries are structurally defined: (1) opening heading found, (2) terminator found (next heading of the same level or section 7), (3) extracted line range covers all subsections without capturing foreign content |
| **MandatoryConstraints** | It is forbidden to use a fixed line offset ("next 40 lines") — boundaries are always structural; it is forbidden to cut in the middle of a table or list |
| **CharacterizationRelation** | Boundary precision (exactly one card), content completeness (all subsections present) |
| **ValidationBoundary** | Verification: comparison of line count in reference with original range in monolith |
| **FreshnessOrExpiry** | `stale` when the markdown heading structure in the monolith changes |
| **ReadinessDisposition** | `P2W-ready` for algorithmic implementation |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Problem card structure | `C.22.2` |
| Pattern body sectioning | `E.8` |
| Description vs described thing (boundaries in text) | `E.17` |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L144-L177

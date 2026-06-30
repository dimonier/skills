---
id: SDC.BoundaryDetection
title: Detection of extractable unit boundaries
---

# SDC.BoundaryDetection: Detection of extractable unit boundaries

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

---

### 6.2 `SDC.BoundaryDetection` — Detection of extractable unit boundaries

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | The boundaries of a problem card in the monolith are defined by markdown headings, but headings of different levels (`###`, `####`, `#####`) are nested irregularly. Cutting at "the next heading of the same level" results in losing subsections (worked examples, conformance checklists) or capturing foreign content |
| **ContextGrounding** | DPF monolith: problem cards start with `### 6.X PatternID — Name`, contain nested `#### Always‑Core Fields`, `#### Conditional Fields`, `#### Governing‑Pattern Cues` and optionally `#### Worked Examples`, `#### Conformance Checklist`. The next problem card starts with `### 6.Y ...` |
| **ScopeCut** | Boundary detection from "problem card heading to the next problem card heading (or to the start of section 7)"; does not cover boundary detection for non-DPF structures |
| **NotWishReason** | "Cut at the nearest `###`" — we lose all `####` subsections or capture the next problem card |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Problem card boundary in markdown — the range of lines from the opening heading `### 6.X` to the line before the next heading `### 6.Y` (or `## 7` if this is the last card) |
| **SymptomDetection** | Reference file truncates at Always-Core Fields (Conditional Fields and Governing-Pattern Cues are lost); or reference file contains two problem cards (boundary is wrong) |
| **ProblemHypothesis** | The cutting algorithm uses the wrong heading level as terminator. Rule: for DPF — terminator = `### 6.` or `## 7`; for FPF patterns — terminator = `## E.X` or `### E.X:N` of the next pattern |
| **ImprovementCheck** | Each reference file contains exactly one problem card: Always-Core + Conditional + all optional subsections + Governing-Pattern Cues. The next card is in a separate file |
| **AcceptanceCriterion** | Boundaries are determined structurally: (1) opening heading found, (2) terminator found (next heading of the same level or section 7), (3) the extracted line range covers all subsections without capturing foreign ones |
| **MandatoryConstraints** | Prohibited to use a fixed line offset ("next 40 lines") — boundaries are always structural; prohibited to cut in the middle of a table or list |
| **CharacterizationRelation** | Boundary precision (exactly one card), content completeness (all subsections in place) |
| **ValidationBoundary** | Verification: comparison of line count in the reference with the original range in the monolith |
| **FreshnessOrExpiry** | `stale` when the structure of markdown headings in the monolith changes |
| **ReadinessDisposition** | `P2W-ready` for algorithmic implementation |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Problem card structure | `C.22.2` |
| Pattern body sectioning | `E.8` |
| Description vs described thing (boundaries in text) | `E.17` |

---
id: SDC.RelationsExtraction
title: Extraction of E.4.PFR relation records
---

# SDC.RelationsExtraction: Extraction of E.4.PFR relation records

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

---

### 6.6 `SDC.RelationsExtraction` — Extraction of E.4.PFR relation records

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | Section 7 of the DPF monolith contains the Relation Map and Edition Dependency. When problem cards are decomposed into separate files, links between patterns are lost. An agent that loaded one reference does not know which other patterns are related to it |
| **ContextGrounding** | The DPF monolith contains `E.4.PFR` relation records: a relations table (Source → Target → Relation Function) and Edition Dependency. Each reference file must contain a `## Relations` section with relevant relations |
| **ScopeCut** | Extraction of relation records into `relations.md` and selective copying into each reference file; does not cover creation of new relations |
| **NotWishReason** | "The relations are in the monolith, the agent will read section 7" — the agent does not read the monolith, relations must be in `references/` |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Relation records — entries about links between patterns (Source → Target → Relation Function), transferred from section 7 of the monolith into `relations.md` and into the `## Relations` section of reference files |
| **SymptomDetection** | Reference file does not contain relations to other DPF patterns; `relations.md` is absent; the agent cannot find related patterns |
| **ProblemHypothesis** | Relation records remained only in the monolith. Must: (1) create `relations.md` with the full table, (2) in each reference file add `## Relations` with rows relevant to this pattern |
| **ImprovementCheck** | `relations.md` contains the full relations table. Each reference file in the `## Relations` section lists: (1) which patterns this one depends on, (2) which patterns depend on this one, (3) a link to `relations.md` for the full picture |
| **AcceptanceCriterion** | `relations.md` — exact copy of the table from section 7 of the monolith; each reference file contains `## Relations` with bidirectional relations (depends on / depended on by); Edition Dependency entry is duplicated |
| **MandatoryConstraints** | `relations.md` — full copy (not a subset); `## Relations` section in reference — only rows where this pattern is Source or Target; prohibited to modify the relation function during transfer |
| **CharacterizationRelation** | Completeness (all rows from monolith → into `relations.md`), correctness (all relation functions preserved) |
| **ValidationBoundary** | Verification: comparison of row count in `relations.md` with the table in section 7 of the monolith |
| **FreshnessOrExpiry** | `stale` when relation records in the monolith change |
| **ReadinessDisposition** | `P2W-ready` for script extraction |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Framework relation records | `E.4.PFR` |
| Relation function and dependency direction | `E.5.3` |
| Pattern relation mapping | `E.4` |

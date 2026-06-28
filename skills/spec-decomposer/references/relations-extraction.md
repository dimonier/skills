# SDC.RelationsExtraction: Extracting E.4.PFR Relation Records

> **Trigger:** Section 7 of a DPF monolith contains the Relation Map and Edition Dependency — when problem cards are decomposed into separate files, the relationships between patterns are lost
> **Governing patterns:** 
>   → `../fpf-core/references/E.4.PFR.md`
>   → `../fpf-core/references/E.5.3-dependency-function.md`
>   → `../fpf-core/references/E.4-ecosystem-family.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | Section 7 of a DPF monolith contains the Relation Map and Edition Dependency. When problem cards are decomposed into separate files, the relationships between patterns are lost. An agent that loads one reference does not know which other patterns are related to it |
| **ContextGrounding** | A DPF monolith contains `E.4.PFR` relation records: a table of relations (Source → Target → Relation Function) and Edition Dependency. Each reference file must contain a `## Relations` section with relevant relations |
| **ScopeCut** | Extraction of relation records into `relations.md` and selective copying into each reference file; does not cover creation of new relations |
| **NotWishReason** | "The relations are in the monolith, the agent will read section 7" — the agent does not read the monolith; relations must be in `references/` |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Relation records — entries about relationships between patterns (Source → Target → Relation Function), transferred from section 7 of the monolith into `relations.md` and into the `## Relations` sections of reference files |
| **SymptomDetection** | Reference file does not contain relations to other DPF patterns; `relations.md` is missing; the agent cannot find related patterns |
| **ProblemHypothesis** | Relation records remain only in the monolith. Required: (1) create `relations.md` with the full table, (2) in each reference file add `## Relations` with rows relevant to that pattern |
| **ImprovementCheck** | `relations.md` contains the full relations table. Each reference file's `## Relations` section lists: (1) which patterns this one depends on, (2) which patterns depend on this one, (3) a link to `relations.md` for the full picture |
| **AcceptanceCriterion** | `relations.md` — exact copy of the table from section 7 of the monolith; each reference file contains `## Relations` with bidirectional relations (depends on / depended on by); the Edition Dependency entry is duplicated |
| **MandatoryConstraints** | `relations.md` — full copy (not a subset); the `## Relations` section in a reference — only rows where this pattern is Source or Target; modifying the relation function during transfer is prohibited |
| **CharacterizationRelation** | Completeness (all rows from the monolith → into `relations.md`), correctness (all relation functions preserved) |
| **ValidationBoundary** | Verification: comparison of row count in `relations.md` with the table in section 7 of the monolith |
| **FreshnessOrExpiry** | `stale` when relation records in the monolith change |
| **ReadinessDisposition** | `P2W-ready` for script-based extraction |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Framework relation records | `E.4.PFR` |
| Relation function and dependency direction | `E.5.3` |
| Pattern relation mapping | `E.4` |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L290-L323

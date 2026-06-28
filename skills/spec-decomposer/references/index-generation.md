# SDC.IndexGeneration: INDEX.md Generation

> **Trigger:** An agent or human wants to quickly find the right pattern without reading the SKILL.md routing table (which groups by situation, not by name)
> **Governing patterns:** 
>   → `../fpf-core/references/C.33-carrier-admission.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`
>   → `../fpf-core/references/E.4-thin-affordance.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | An agent or human wants to quickly find the right pattern without reading the SKILL.md routing table (which groups by situation, not by name). An alphabetical/numbered index of all the skill's reference files is needed |
| **ContextGrounding** | A skill contains N reference files. SKILL.md is a dispatcher with a routing table (situation → reference). INDEX.md is a complete listing (pattern ID → reference file + monolith offset) |
| **ScopeCut** | Generation of INDEX.md as a flat list of all reference files; does not cover semantic index or search |
| **NotWishReason** | "SKILL.md already contains a routing table, INDEX is not needed" — the routing table groups by situation, INDEX groups by name; these are different intended uses |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | INDEX.md — the skill's route sheet: a table of all reference files with pattern ID, name, file name, and monolith offset |
| **SymptomDetection** | INDEX.md contains only file names without pattern ID; or the monolith-offset column is missing (cannot audit) |
| **ProblemHypothesis** | INDEX is generated manually and is incomplete. It should be generated automatically during decomposition: each reference file → a row in INDEX |
| **ImprovementCheck** | INDEX.md: table with columns `#`, `Pattern ID`, `Name`, `Reference File`, `Monolith Lines`; optionally a `## Cross-references` section with links to `relations.md` and the monolith |
| **AcceptanceCriterion** | INDEX.md contains: (1) all of the skill's reference files, (2) sequential numbers, (3) pattern ID, (4) pattern name, (5) reference file name, (6) monolith offset, (7) cross-reference to relations.md |
| **MandatoryConstraints** | INDEX.md is updated on every re-decomposition; does not contain pattern bodies (it is an index, not a dump); does not duplicate the routing table from SKILL.md |
| **CharacterizationRelation** | Completeness (all references in the index), accuracy (matches actual files), freshness (matches the current state of references/) |
| **ValidationBoundary** | Verification: the number of rows in INDEX.md matches the number of reference files |
| **FreshnessOrExpiry** | `stale` on every change to the composition of references/ |
| **ReadinessDisposition** | `P2W-ready` for script-based generation |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Carrier admission (INDEX as a separate carrier) | `C.33` |
| Publication unit and intended reader | `E.17.EFP` |
| Thin affordance (readable in ≤1 minute) | `E.4.DA` |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L254-L287

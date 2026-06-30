---
id: SDC.IndexGeneration
title: INDEX.md generation
---

# SDC.IndexGeneration: INDEX.md generation

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

---

### 6.5 `SDC.IndexGeneration` — INDEX.md generation

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | An agent or human wants to quickly find a needed pattern without reading the SKILL.md routing table (which groups by situations, not by names). An alphabetical/numbered index of all skill reference files is needed |
| **ContextGrounding** | The skill contains N reference files. SKILL.md is a dispatcher with a routing table (situation → reference). INDEX.md is a full listing (pattern ID → reference file + monolith offset) |
| **ScopeCut** | INDEX.md generation as a flat list of all reference files; does not cover semantic index or search |
| **NotWishReason** | "SKILL.md already contains a routing table, INDEX is not needed" — the routing table groups by situations, INDEX by names; these are different intended uses |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | INDEX.md — the skill's route sheet: a table of all reference files with pattern ID, name, file name, and monolith offset |
| **SymptomDetection** | INDEX.md contains only file names without pattern ID; or the monolith offset column is absent (impossible to audit) |
| **ProblemHypothesis** | INDEX is generated manually and is incomplete. Should be generated automatically during decomposition: each reference file → a row in INDEX |
| **ImprovementCheck** | INDEX.md: table with columns `#`, `Pattern ID`, `Name`, `Reference File`, `Monolith Lines`; optionally a `## Cross-references` section with a link to `relations.md` and the monolith |
| **AcceptanceCriterion** | INDEX.md contains: (1) all skill reference files, (2) sequential numbers, (3) pattern ID, (4) pattern name, (5) reference file name, (6) monolith offset, (7) cross-reference to relations.md |
| **MandatoryConstraints** | INDEX.md is updated on every re-decomposition; does not contain pattern bodies (this is an index, not a dump); does not duplicate the routing table from SKILL.md |
| **CharacterizationRelation** | Completeness (all references in the index), accuracy (matches actual files), freshness (matches current state of references/) |
| **ValidationBoundary** | Verification: the number of rows in INDEX.md matches the number of reference files |
| **FreshnessOrExpiry** | `stale` on every change to references/ contents |
| **ReadinessDisposition** | `P2W-ready` for script generation |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Carrier admission (INDEX as a separate carrier) | `C.33` |
| Publication unit and intended reader | `E.17.EFP` |
| Thin affordance (reads in ≤1 minute) | `E.4.DA` |

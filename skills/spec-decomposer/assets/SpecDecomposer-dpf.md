# Domain Principle Framework: Spec-Decomposer — decomposing a monolithic framework specification into a skill

> **Pattern family:** `E.4.DPF` (Domain Principle Framework Authoring)
> **Status:** Draft — First-hour route
> **Normativity:** Locally normative for the practice of packaging FPF-compatible frameworks into LFW skills
> **Depends on:** `FPFCorePatternSet@current`, `FPFLiteracyPrincipleFramework@Draft`, `FPFEcosystemWorkspaceArchitecture@Draft`

---

## 1. Context Declaration

| Field | Value |
|---|---|
| **BoundedContext** | `MonolithicSpecDecomposition@LFW` |
| **IntendedReader** | Methodology engineer, technical lead — performing the packaging of DPF/LPF/FPF into skill format for use in LFW |
| **FirstUse** | Decomposition of an existing monolithic `.md` file of a framework (FPF, DPF, LPF) into atomic reference files in the skill's `references/`; generation of INDEX.md, relations.md and updating the SKILL.md dispatcher |

### Non‑Use Boundary

- Does not replace `E.4.DPF` (creating the DPF itself) — SDC works with an already created DPF
- Does not replace `FPFEcosystemWorkspaceArchitecture` (LFW architecture) — SDC implements the population of `references/` within an already created structure
- Does not cover creating a skill from scratch — the skill must already exist with `SKILL.md` and `assets/monolith.md`
- Is not a tool for full indexing or RAG — this is structural decomposition, not semantic search

---

## 2. Source Pack (`G.2`)

### Adopted Sources

| Source | Role in the framework |
|---|---|
| **FPF Core Specification** (Levenchuk, June 2026) | Host framework: `E.4.DPF`, `E.8`, `C.22.2`, `E.4.PFR`, `E.17.EFP`, `C.33` |
| **FPF-Literacy DPF** | Source of DPF patterns: carrier first entry, agent context load, first-hour route |
| **LFW Architecture DPF** | Architectural patterns: skill as framework carrier, monolith in skill, skill dispatcher, dependency chain |
| **Manual decomposition experience of 5 DPFs** (June 2026) | Primary source: 39 problem cards extracted manually; identified repetitive operations, candidates for automation |
| **Anthropic Skills Specification** | Skill format: SKILL.md (YAML frontmatter), references/, assets/ |

### Rejected Sources

- RAG/embedding solutions — solve search, not structural decomposition
- Generative approaches ("ask an agent to extract patterns") — non-deterministic, do not preserve source location
- XSLT/XPath over XML — monoliths are in markdown, not XML

> **ClaimStatus:** `provisional`

---

## 3. Architecture Decision (`E.4.PFAD`)

**`PFAD-SDC-001`**

| Slot | Value |
|---|---|
| **FrameworkFamily** | `DomainPrincipleFramework` |
| **Purpose** | Provide engineering patterns for structural decomposition of monolithic framework specifications (FPF/DPF/LPF) into atomic skill reference files — preserving governing-pattern cues, source location, and unidirectional "monolith → references" synchronization |

### First Pattern Set

1. **`SDC.UnitRecognition`** — Recognition of extractable units in the monolith
2. **`SDC.BoundaryDetection`** — Detection of extractable unit boundaries
3. **`SDC.ReferenceFileFormat`** — Reference file format
4. **`SDC.GoverningCueConversion`** — Conversion of governing-pattern references
5. **`SDC.IndexGeneration`** — INDEX.md generation
6. **`SDC.RelationsExtraction`** — Extraction of E.4.PFR relation records
7. **`SDC.DispatcherUpdate`** — Updating the SKILL.md dispatcher
8. **`SDC.CarrierSplit`** — Carrier split: agent vs human
9. **`SDC.SyncDiscipline`** — Synchronization discipline: monolith → references
10. **`SDC.AutomationBoundary`** — Automation boundary

### Dependency Boundary

| Slot | Value |
|---|---|
| **DependsOn** | `FPFCorePatternSet@current`, `FPFLiteracyPrincipleFramework@Draft`, `FPFEcosystemWorkspaceArchitecture@Draft` |
| **NoCoreLanding** | `true` |
| **ReverseDependencyBlocked** | `true` |
| **PublicationUnit** | Local monolith with subsequent self-decomposition into a skill |

---

## 4. Name Preparation

| Field | Value |
|---|---|
| **PrimaryName** | Principle framework for decomposing monolithic framework specifications into skills |
| **PublicLabel** | `SpecDecomposerPrincipleFramework` |
| **ProvisionalAlias** | `SpecDecomposerPF` / `SDC` |
| **F18NameCard** | Required before freezing the public abbreviation |
| **NameScope** | Bounded context of packaging FPF-compatible frameworks into LFW skills |

---

## 5. Carrier Admission (`C.33`)

| Slot | Content |
|---|---|
| **CapturedStructure** | Context declaration, source pack, architectural decision; ten `ProblemCard@Context` |
| **NotCaptured** | Full `E.8` pattern bodies with worked slices, anti-patterns, conformance checklists; `E.21` evaluation; automation script |
| **AdmissibleUse** | P2W-ready problem-side input for manual and automated decomposition; drafting aid for implementing `spec-decomposer` |
| **NonAdmissibleUse** | Replacement for studying the structure of a specific framework before decomposition; "universal script for any markdown" |

---

## 6. Problem Cards (`C.22.2`)

### 6.1 `SDC.UnitRecognition` — Recognition of extractable units

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | The monolithic framework specification contains heterogeneous sections: problem cards, relation records, context declaration, source pack, quality route, appendix. Not everything is eligible for extraction into `references/`. Attempting to extract "everything indiscriminately" yields reference files with non-pattern content |
| **ContextGrounding** | Decomposition of an existing DPF/LPF/FPF monolith is being performed. The monolith has the `E.4.DPF` spine: context → source pack → PFAD → names → patterns → relations → publication → quality → refresh |
| **ScopeCut** | Identification of extractable units (problem cards, patterns) vs non-extractable sections (context declaration, source pack, publication, quality route); does not cover recognition of arbitrary markdown structures |
| **NotWishReason** | "Extract all sections with third-level headings" — we get reference files with context declaration and quality route, which are not patterns |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Extractable unit — a structural unit of the monolith that is a self-sufficient pattern or problem card and should become a separate reference file |
| **SymptomDetection** | The following end up in `references/`: context declaration (section 1), source pack (section 2), PFAD (section 3), publication (section 8), quality route (section 9), refresh route (section 10) — which are not patterns |
| **ProblemHypothesis** | The criterion for extractable vs non-extractable is not defined. Criterion: extractable = problem card (`C.22.2`) or pattern body (`E.8`) that has ProblemSignal, Solution/SoTA approach, and Governing-Pattern Cues |
| **ImprovementCheck** | Each reference file contains a problem card or pattern. Non-extractable sections remain only in the monolith |
| **AcceptanceCriterion** | Extractable units are identified by: (1) presence of ProblemSignal, (2) presence of SoTA approach/AcceptanceCriterion, (3) presence of Governing-Pattern Cues, (4) belonging to section 6 (Problem Cards) or an equivalent pattern section |
| **MandatoryConstraints** | Prohibited to extract: sections 1-5 (context, source pack, PFAD, names, carrier admission), sections 7-10 (relations, publication, quality, refresh), appendix; each extracted unit must be self-sufficient (readable without the context of neighboring sections) |
| **CharacterizationRelation** | Precision (are all extractable units found), recall (are there false positives — extracted non-patterns) |
| **ValidationBoundary** | Verification: a domain expert reviews the list of extracted units and confirms that each is a self-sufficient pattern |
| **FreshnessOrExpiry** | `stale` when the `E.4.DPF` spine or structure of the specific framework changes |
| **ReadinessDisposition** | `P2W-ready` before starting decomposition of a specific monolith |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Problem card identification | `C.22.2` |
| Pattern body structure | `E.8` |
| DPF authoring spine | `E.4.DPF` |
| Framework carrier admission | `C.33` |

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

---

### 6.3 `SDC.ReferenceFileFormat` — Reference file format

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | The extracted problem card content is placed into a file "as is" — without a header with trigger condition, without governing-pattern references in skill format, without source location. The agent cannot determine when to load this reference and which other references are needed |
| **ContextGrounding** | Reference file — the target artifact for the agent. Must be self-sufficient: contain trigger condition (for the dispatcher routing table), governing-pattern cues (for the dependency chain), and source location (for audit) |
| **ScopeCut** | Reference file format: header + body + source footer; does not cover the format for non-pattern references (INDEX, relations) |
| **NotWishReason** | "Just put the problem card as is" — the agent does not know when to load it and which FPF patterns are needed |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Reference file as a self-sufficient carrier of a single pattern: header with metadata, body with pattern content, footer with source link |
| **SymptomDetection** | Reference file starts immediately with `#### Always‑Core Fields` (no header); governing-pattern cues in `C.22.2` format instead of `../fpf-core/references/C.22.2-problem-card.md` |
| **ProblemHypothesis** | The reference file format is not standardized — each decomposition produces files with different structure |
| **ImprovementCheck** | Reference file: header `# PatternID: Name` → `> Trigger:` → `> Governing patterns:` → `---` → body → `---` → `> Source:`. Agent reads header, understands trigger and dependencies, loads the body |
| **AcceptanceCriterion** | Reference file contains: (1) heading `# PatternID: Name`, (2) `> **Trigger:** ...`, (3) `> **Governing patterns:** → ...` (links to fpf-core and other skills), (4) full problem card body, (5) `> **Source:** assets/...md lines LXXX-LXXX` |
| **MandatoryConstraints** | Header is mandatory; Trigger — from ProblemSignal (brief formulation); Governing patterns — skill-relative links (not monolithic pattern names); Source — exact line numbers in the monolith |
| **CharacterizationRelation** | Header completeness, cue conversion accuracy, source location precision |
| **ValidationBoundary** | Verification: agent loads the reference file and uses governing cues to find all dependent references |
| **FreshnessOrExpiry** | `stale` when skill format or routing rules change |
| **ReadinessDisposition** | `P2W-ready` as a template for all reference files |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Skill progressive disclosure (3 levels) | skill-creator SKILL.md |
| Carrier admission for agent intended reader | `C.33`, `E.17.EFP` |
| Framework dependency declaration | `E.4.PFAD`, `E.5.3` |
| Governing-pattern cues in problem card | `C.22.2` |

---

### 6.4 `SDC.GoverningCueConversion` — Conversion of governing-pattern references

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | The monolith references FPF patterns in `C.22.2`, `E.8`, `E.4.DPF` format. In the skill these links must point to specific reference files: `../fpf-core/references/C.22.2-problem-card.md`. Without conversion the agent cannot traverse the dependency chain |
| **ContextGrounding** | The monolith uses FPF pattern IDs as governing-pattern cues. In LFW each pattern is a separate reference file in the `fpf-core` skill. References must be skill-relative paths |
| **ScopeCut** | Mapping "FPF pattern ID → skill reference path"; does not cover references to external sources (literature, standards) |
| **NotWishReason** | "Leave as is, the agent will find it on its own" — the agent does not have the FPF-Spec.md context and will not be able to resolve `C.22.2` to a file |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Governing-pattern cue — a reference to an FPF/DPF pattern that must be converted from monolithic format (`E.8`, `C.22.2`, `FPFLIT.*`) to a skill-relative path |
| **SymptomDetection** | Governing-pattern cues in reference files in `C.22.2`, `E.8` format — unresolvable for the agent; or references point to non-existent reference files |
| **ProblemHypothesis** | The "Pattern ID → reference path" mapping table is missing. The mapping is formed from the fpf-core structure: `E.4.DPF-authoring.md`, `C.22.2-problem-card.md`, etc. |
| **ImprovementCheck** | Governing-pattern cues in reference files in `→ ../fpf-core/references/E.8-pattern-body.md` format; agent loads the specified reference; the dependency chain is traversable |
| **AcceptanceCriterion** | All governing-pattern cues are converted; each cue leads to an existing reference file; DPF→DPF references (to other DPFs) are converted similarly; mapping table covers ≥90% of patterns used in the DPF |
| **MandatoryConstraints** | Prohibited to leave monolithic references (`E.8`, `C.22.2`) in reference files; mapping must be complete for all patterns used; when a reference file for a pattern is absent — leave the cue with a `[pending]` marker |
| **CharacterizationRelation** | Conversion completeness (% of cues converted), link validity (% of cues leading to existing files) |
| **ValidationBoundary** | Verification: for each reference file → all governing-pattern cues resolve to existing files |
| **FreshnessOrExpiry** | `stale` when new FPF patterns are added or the fpf-core/references/ structure changes |
| **ReadinessDisposition** | `P2W-ready` when the mapping table is available |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Framework dependency declaration | `E.5.3`, `E.4.PFR` |
| Governing-pattern cues in problem card | `C.22.2` |
| Agent context load (multi-level memory) | `FPFLIT.AgentContextLoad` |
| Dependency chain in LFW | `EWA.DependencyChain` |

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

---

### 6.7 `SDC.DispatcherUpdate` — Updating the SKILL.md dispatcher

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | After decomposition, new files appear in `references/`, but the SKILL.md dispatcher still contains a routing table with "pending" status and/or an incomplete list of reference files. The agent does not know about new references or cannot find them |
| **ContextGrounding** | SKILL.md — the skill dispatcher: routing table (situation → reference). After decomposition the routing table must be updated: status → "Done", reference file list → complete |
| **ScopeCut** | Updating the routing table and status in SKILL.md after decomposition; does not cover creating SKILL.md from scratch |
| **NotWishReason** | "Leave pending, the agent will read INDEX.md" — the routing table in SKILL.md is the primary agent interface, INDEX is secondary |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | SKILL.md dispatcher — a routing table that directs the agent to the right reference based on the situation |
| **SymptomDetection** | Routing table contains "pending" status when references/ are populated; routing table references non-existent reference files; routing table does not mention new references |
| **ProblemHypothesis** | SKILL.md was created before decomposition and was not updated after. A "post-decomposition dispatcher update" step is needed |
| **ImprovementCheck** | SKILL.md: routing table is complete (all references listed), status "Done", the "Source for agent vs human" section points to references/ as primary |
| **AcceptanceCriterion** | SKILL.md after update: (1) routing table lists all reference files, (2) each routing table row contains trigger condition and governing cues, (3) status changed from "pending" to "Done", (4) no mention of the monolith as a fallback for the agent |
| **MandatoryConstraints** | Prohibited to leave "pending" status when references/ are populated; routing table must be synchronized with actual references/ content; prohibited to direct the agent to the monolith |
| **CharacterizationRelation** | Routing completeness (all references in the table), trigger accuracy (does trigger match ProblemSignal), status honesty |
| **ValidationBoundary** | Verification: the agent uses the routing table to find a reference for each of 3 typical situations |
| **FreshnessOrExpiry** | `stale` on every change to references/ contents |
| **ReadinessDisposition** | `P2W-ready` as the concluding step of decomposition |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Skill dispatcher (routing-only) | `EWA.SkillDispatcher` |
| Agent context load | `FPFLIT.AgentContextLoad` |
| Carrier first entry | `FPFLIT.CarrierFirstEntry` |
| SKILL.md as dispatcher | skill-creator SKILL.md |

---

### 6.8 `SDC.CarrierSplit` — Carrier split: agent vs human

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | After decomposition the same knowledge exists in two forms: monolith (`assets/`) and reference files (`references/`). If the agent receives an instruction "when in doubt read the monolith", progressive disclosure loses its purpose — the agent loads 60K+ lines instead of 200 |
| **ContextGrounding** | In LFW each skill has two carriers: `assets/monolith.md` (source of truth for the human) and `references/*.md` (primary source for the agent). It is essential to explicitly separate who reads what |
| **ScopeCut** | Rule: the agent always reads references/, never — assets/; the human always edits assets/, reassembles references/; does not cover the case when references/ have not yet been created |
| **NotWishReason** | "The agent is smart, let it decide" — without an explicit rule the agent may choose the monolith (60K+ lines into context) |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Carrier split — an explicit rule in SKILL.md defining which carrier is for which intended reader |
| **SymptomDetection** | SKILL.md contains the phrase "use assets/... as fallback"; the agent loads the monolith instead of references |
| **ProblemHypothesis** | The carrier split rule is not explicitly formulated. Solution: SKILL.md contains an "Source for agent vs human" section with an imperative: "Agent: always use references/. DO NOT read assets/" |
| **ImprovementCheck** | SKILL.md unambiguously separates: agent → references/, human → assets/. The agent never loads the monolith |
| **AcceptanceCriterion** | SKILL.md contains: (1) "Agent: always use references/. DO NOT read assets/". (2) "Human: read and edit assets/. After edits — rebuild references/". (3) No phrase allowing the agent to read the monolith |
| **MandatoryConstraints** | The phrase "use assets/ as fallback" or equivalent is prohibited; mentioning the monolith in the routing table is prohibited; "pending" status is only allowed when references/ are genuinely empty — and then the monolith is not mentioned, the agent simply reports "references/ have not yet been created" |
| **CharacterizationRelation** | Carrier split clarity (unambiguity of the rule), agent compliance (does the agent read references/ and not assets/) |
| **ValidationBoundary** | Verification: give the agent a task in the DPF bounded context → the agent loads the reference, not the monolith |
| **FreshnessOrExpiry** | `stale` when the LFW architecture carrier split changes |
| **ReadinessDisposition** | `P2W-ready` for every skill |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Carrier admission for different intended readers | `C.33`, `E.17.EFP` |
| Agent context load (multi-level memory) | `FPFLIT.AgentContextLoad` |
| Monolith in skill (source of truth placement) | `EWA.MonolithInSkill` |
| Skill dispatcher (routing-only) | `EWA.SkillDispatcher` |

---

### 6.9 `SDC.SyncDiscipline` — Synchronization discipline: monolith → references

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | The human edits the monolith (`assets/dpf.md`) — adds a problem card, changes an AcceptanceCriterion, corrects a governing cue. References/ are not updated. The agent continues reading old reference files. A divergence arises: "source of truth" and "primary source for agent" have diverged |
| **ContextGrounding** | The monolith is the source of truth. References/ are derived views for the agent. Synchronization is always unidirectional: monolith → references. Never the reverse |
| **ScopeCut** | Synchronization process: detecting changes in the monolith → rebuilding affected reference files → updating INDEX.md → updating SKILL.md; does not cover version control (git) |
| **NotWishReason** | "I'll edit the reference file directly, bypassing the monolith" — violates unidirectionality and creates divergence |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Synchronization process: detecting divergence and rebuilding references/ from the updated monolith |
| **SymptomDetection** | Reference file contains a problem card absent from the monolith (reference was edited directly); monolith contains a new problem card absent from references/ (monolith was updated, references/ were not) |
| **ProblemHypothesis** | The synchronization process is not defined. Rule: (1) all edits — only in the monolith, (2) after edits — re-run decomposition (full rebuild of references/), (3) reference files are never edited manually (except agent-specific annotations) |
| **ImprovementCheck** | After editing the monolith and rebuilding: all reference files are current, INDEX.md is updated, SKILL.md routing table is current |
| **AcceptanceCriterion** | Synchronization process: (1) monolith changed, (2) decomposition run (manual or scripted), (3) references/ rebuilt, (4) INDEX.md updated, (5) SKILL.md routing table verified, (6) "Done" status confirmed |
| **MandatoryConstraints** | Synchronization is always unidirectional (monolith → references); prohibited to edit reference files directly; rebuild references/ on every monolith change affecting problem cards; when adding/removing a problem card — full rebuild |
| **CharacterizationRelation** | Sync latency (time between monolith edit and references/ update), fidelity (references/ match monolith), direction compliance (no reverse edits) |
| **ValidationBoundary** | Verification: comparison of problem cards in the monolith and in references/ — full match |
| **FreshnessOrExpiry** | The synchronization process is triggered on every monolith change |
| **ReadinessDisposition** | `P2W-ready` after the first successful rebuild |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Monolith as source of truth | `EWA.MonolithInSkill` |
| Framework currentness and refresh | `G.11` |
| Carrier update discipline | `C.33`, `C.35` |
| Derived artifact vs source | `E.17` (description vs described thing) |

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

---

## 7. Relation Records (`E.4.PFR` stub)

### Relation Map

| Source | Target | Relation Function |
|---|---|---|
| `SDC.UnitRecognition` | `SDC.BoundaryDetection` | Recognized units → boundary detection |
| `SDC.BoundaryDetection` | `SDC.ReferenceFileFormat` | Boundaries → extracted content format |
| `SDC.ReferenceFileFormat` | `SDC.GoverningCueConversion` | Format defines how to convert cues |
| `SDC.ReferenceFileFormat` | `SDC.RelationsExtraction` | Format includes `## Relations` section |
| `SDC.GoverningCueConversion` | `SDC.ReferenceFileFormat` | Cue conversion — part of reference format |
| `SDC.IndexGeneration` | `SDC.ReferenceFileFormat` | INDEX is built from completed reference files |
| `SDC.DispatcherUpdate` | `SDC.ReferenceFileFormat` | Dispatcher is updated after references are created |
| `SDC.CarrierSplit` | `SDC.DispatcherUpdate` | Carrier split rule is recorded in the dispatcher |
| `SDC.CarrierSplit` | `SDC.SyncDiscipline` | Carrier split — prerequisite for sync discipline |
| `SDC.SyncDiscipline` | → *all cards* | Sync discipline applies to all decomposition results |
| `SDC.AutomationBoundary` | → *all cards* | Automation boundary defines what is scripted from each step |
| → `EWA.SkillAsFrameworkCarrier` | `SDC.ReferenceFileFormat` | Skill carrier architecture — grounding for reference format |
| → `EWA.MonolithInSkill` | `SDC.SyncDiscipline` | Monolith in skill — grounding for sync discipline |
| → `EWA.SkillDispatcher` | `SDC.DispatcherUpdate` | Skill dispatcher — grounding for SKILL.md update |
| → `EWA.DependencyChain` | `SDC.GoverningCueConversion` | Dependency chain — grounding for cue conversion |
| → `FPFLIT.CarrierFirstEntry` | `SDC.CarrierSplit` | Carrier first entry — grounding for carrier split |
| → `FPFLIT.FirstHourDPFRoute` | `SDC.UnitRecognition` | First-hour route — grounding for structure recognition |

### Edition Dependency

| Slot | Value |
|---|---|
| **FrameworkEditionRef** | `SpecDecomposerPrincipleFramework@Draft` |
| **DependsOnEditionRefs** | `FPFCorePatternSet@current`, `FPFLiteracyPrincipleFramework@Draft`, `FPFEcosystemWorkspaceArchitecture@Draft` |
| **DependencyReason** | All governing‑pattern cues reference FPF Core; architectural patterns use LFW EWA patterns; the decomposition process relies on DPF authoring from FPF-Literacy |
| **CompatibilityBoundary** | When `E.4.DPF`, `E.17.EFP`, `C.33`, `E.4.PFR` change — review ProblemCard fields |
| **E53ConformanceNote** | Conformance check required after pattern name stabilization |

---

## 8. Publication

| Slot | Value |
|---|---|
| **ThisFile** | Local first-entry monolith; subject to self-decomposition into the `spec-decomposer` skill |
| **PublicationScope** | Methodology engineers, technical leads — performing the packaging of frameworks into LFW skills |
| **FirstEntryCarrier** | `SpecDecomposer-dpf.md` — read as a single document |
| **RelationRecordsCarrier** | Section 7; subject to extraction into `references/relations.md` |
| **NonPublicationNote** | `FPF-Spec.md` is not modified; Core is not extended |

---

## 9. Quality Route

### Evaluation Characteristics

| Characteristic | Question |
|---|---|
| **DecompositionCompleteness** | Are all monolith problem cards extracted into references/? |
| **ReferenceSelfSufficiency** | Is each reference file readable as a self-sufficient pattern (without needing to read neighbors)? |
| **CueConversionAccuracy** | Do all governing-pattern cues lead to existing reference files? |
| **CarrierSplitCompliance** | Does each SKILL.md direct the agent to references/ and never to assets/? |
| **SyncDirectionCompliance** | Are all changes in references/ derived from the monolith (no "reverse" edits)? |
| **AutomationBoundaryClarity** | Are steps defined as automatable / human-review / human-only? |

### Quality Framework

| Step | Owner | Purpose |
|---|---|---|
| 1 | `E.22` | Framing evaluation purpose |
| 2 | `E.21` | Pattern-quality evaluation of each ProblemCard |
| 3 | `E.23` | Improvement loop — automation script, verification on new DPFs |
| 4* | `E.19` | Admission review (as the framework grows) |

---

## 10. Currentness Route (`G.11`)

### Refresh Triggers

- Change in `E.4.DPF` spine (addition of new sections to the monolith)
- Change in skill format (new requirements for SKILL.md or references/)
- Emergence of new types of extractable units in monoliths (not just problem cards)
- Adoption telemetry: systematic boundary detection errors on new DPFs
- Local incidents: divergence of references/ from the monolith

### Stale Indicators

- Each ProblemCard contains an explicit freshness condition
- Full framework revision: annually or on major Core edition change
- Deprecation: via `superseding` relation record when a ProblemCard is replaced

### Ownership

| Role | Owner |
|---|---|
| **FrameworkEditionOwner** | Engineering-methodological function |
| **SourcePackOwner** | Same |
| **RelationRecordsOwner** | Same |
| **RefreshPlanOwner** | Technical lead / lead methodologist |

---

## 11. Authorship Annotation

| Slot | Value |
|---|---|
| **AuthorshipNote** | Created as a first‑hour route in accordance with `E.4.DPF:4` based on materials from manual decomposition of 5 DPFs (39 problem cards → 39 reference files), FPF Core, FPF-Literacy DPF and LFW Architecture DPF |
| **FPFCompliance** | Spine: context → source pack → PFAD → names → patterns → relations → quality → refresh; `C.22.2` ProblemCard@Context for each pattern; governing‑pattern cues for all out‑of‑scope claims; `C.33` carrier admission |

### Pending Work

- Full `E.8` pattern bodies with worked slices, local anti‑patterns and near‑miss examples
- `E.4.PFR` full pattern relation records (currently stub)
- `F.18` name card for the public SpecDecomposer name
- Implementation of `decompose.py` script according to SDC patterns
- Self-decomposition of this DPF into the `spec-decomposer` skill
- `E.21` evaluation scores for the first draft
- `E.23` improvement loop with adoption telemetry (decomposition of new DPFs)
- Conformance check against the current version of FPF Core

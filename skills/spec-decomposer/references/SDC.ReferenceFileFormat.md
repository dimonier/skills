---
id: SDC.ReferenceFileFormat
title: Reference file format
---

# SDC.ReferenceFileFormat: Reference file format

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

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

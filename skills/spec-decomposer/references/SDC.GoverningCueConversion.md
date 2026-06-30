---
id: SDC.GoverningCueConversion
title: "Conversion of governing-pattern references"
---

# SDC.GoverningCueConversion: Conversion of governing-pattern references

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

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

# SDC.GoverningCueConversion: Converting Governing Pattern References

> **Trigger:** The monolith references FPF patterns in the format `C.22.2`, `E.8`, `E.4.DPF` — in the skill, these references must point to concrete reference files
> **Governing patterns:** 
>   → `../fpf-core/references/E.5.3-dependency-function.md`
>   → `../fpf-core/references/E.4.PFR.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../dpf-fpf-literacy/references/5-agent-context-load.md`
>   → `../dpf-lfw-architecture/references/3-dependency-chain.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | The monolith references FPF patterns in the format `C.22.2`, `E.8`, `E.4.DPF`. In the skill, these references must point to concrete reference files: `../fpf-core/references/C.22.2-problem-card.md`. Without conversion, the agent cannot traverse the dependency chain |
| **ContextGrounding** | The monolith uses FPF pattern IDs as governing-pattern cues. In LFW, each pattern is a separate reference file in the `fpf-core` skill. References must be skill-relative paths |
| **ScopeCut** | Mapping "FPF pattern ID → skill reference path"; does not cover references to external sources (literature, standards) |
| **NotWishReason** | "Leave as is, the agent will find it" — the agent has no context of FPF-Spec.md and cannot resolve `C.22.2` to a file |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Governing-pattern cue — a reference to an FPF/DPF pattern that must be converted from monolith format (`E.8`, `C.22.2`, `FPFLIT.*`) to a skill-relative path |
| **SymptomDetection** | Governing-pattern cues in reference files in the format `C.22.2`, `E.8` — unresolvable for the agent; or references point to non-existent reference files |
| **ProblemHypothesis** | A mapping table "Pattern ID → reference path" is missing. The mapping is formed from the fpf-core structure: `E.4.DPF-authoring.md`, `C.22.2-problem-card.md`, etc. |
| **ImprovementCheck** | Governing-pattern cues in reference files in the format `→ ../fpf-core/references/E.8-pattern-body.md`; the agent loads the indicated reference; the dependency chain is traversable |
| **AcceptanceCriterion** | All governing-pattern cues are converted; each cue leads to an existing reference file; DPF→DPF references (to other DPFs) are converted analogously; the mapping table covers ≥90% of patterns used in the DPF |
| **MandatoryConstraints** | It is forbidden to leave monolithic references (`E.8`, `C.22.2`) in reference files; the mapping must be complete for used patterns; when a reference file for a pattern is absent — leave the cue with a `[pending]` marker |
| **CharacterizationRelation** | Conversion completeness (% of converted cues), link validity (% of cues leading to existing files) |
| **ValidationBoundary** | Verification: for each reference file → all governing-pattern cues resolve to existing files |
| **FreshnessOrExpiry** | `stale` when new FPF patterns are added or the fpf-core/references/ structure changes |
| **ReadinessDisposition** | `P2W-ready` when a mapping table is available |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Framework dependency declaration | `E.5.3`, `E.4.PFR` |
| Governing-pattern cues in problem card | `C.22.2` |
| Agent context load (multi-level memory) | `FPFLIT.AgentContextLoad` |
| Dependency chain in LFW | `EWA.DependencyChain` |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L217-L251

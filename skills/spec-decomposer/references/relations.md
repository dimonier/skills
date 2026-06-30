# Relation Records (E.4.PFR)

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
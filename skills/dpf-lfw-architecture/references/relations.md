# LFW Architecture DPF — Relation Records (E.4.PFR)

### Relation Map

| Source | Target | Relation Function |
|---|---|---|
| `EWA.SkillAsFrameworkCarrier` | `EWA.MonolithInSkill` | Carrier selection предписывает размещение монолита в `assets/` |
| `EWA.SkillAsFrameworkCarrier` | `EWA.SkillDispatcher` | Carrier architecture требует routing-only SKILL.md |
| `EWA.MonolithInSkill` | `EWA.SkillDispatcher` | Монолит — source для references; SKILL.md — routing к ним |
| `EWA.DependencyChain` | `EWA.SkillDispatcher` | Dispatcher направляет к reference; reference содержит governing cues для chain |
| `EWA.DependencyChain` | `EWA.ProjectContext` | Project → LPF → DPF → FPF chain начинается в Project AGENTS.md |
| `EWA.LPFvsProject` | `EWA.ProjectContext` | Критерий различения определяет, что попадает в LPF, а что — в Project |
| `EWA.LPFvsProject` | `EWA.DependencyChain` | LPF — звено в цепочке между Project и DPF |
| → `FPFLIT.AgentContextLoad` | `EWA.DependencyChain` | Agent context load — grounding для цепочки загрузки |
| → `FPFLIT.FrameworkEcosystemPlacement` | `EWA.LPFvsProject` | Ecosystem placement — grounding для различения уровней |
| → `FPFLIT.CarrierFirstEntry` | `EWA.SkillAsFrameworkCarrier` | Carrier first entry — grounding для выбора skill как carrier |

### Edition Dependency

| Слот | Значение |
|---|---|
| **FrameworkEditionRef** | `FPFEcosystemWorkspaceArchitecture@Draft` |
| **DependsOnEditionRefs** | `FPFCorePatternSet@current`, `FPFLiteracyPrincipleFramework@Draft` |
| **DependencyReason** | Все governing‑pattern cues ссылаются на FPF Core; problem signals используют паттерны из FPF-Literacy DPF |
| **CompatibilityBoundary** | При изменении `E.4`, `E.4.DPF`, `E.5.3`, `C.33`, `E.17.EFP` — пересмотреть ProblemCard‑поля |
| **E53ConformanceNote** | Требуется проверка после стабилизации имён паттернов |

> **Source:** `assets/FPF-Ecosystem-Workspace-dpf.md` lines L416-L441

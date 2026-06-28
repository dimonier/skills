# FPF-Literacy DPF — Relation Records (E.4.PFR)

### Relation Map

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.VanillaVsFPF` | `FPFLIT.AgentContextLoad` | Различение типов ответов — предпосылка для правильной загрузки контекста |
| `FPFLIT.FrameworkEcosystemPlacement` | `FPFLIT.AgentContextLoad` | Уровень экосистемы определяет, какой контекст загружать агенту |
| `FPFLIT.PrincipleAsMoveExclusion` | `FPFLIT.SoTARecognition` | Принцип как move exclusion — механизм отличения SoTA от не-SoTA |
| `FPFLIT.FirstHourDPFRoute` | `FPFLIT.CarrierFirstEntry` | Маршрут создания DPF предписывает выбор файла как carrier |
| `FPFLIT.FirstHourDPFRoute` | `FPFLIT.DPFImprovementCycle` | First-hour DPF — вход для цикла улучшений |
| `FPFLIT.AgentContextLoad` | `FPFLIT.SoTARecognition` | Загрузка контекста — условие для распознавания агентом SoTA-решений |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

### Edition Dependency

| Слот | Значение |
|---|---|
| **FrameworkEditionRef** | `FPFLiteracyPrincipleFramework@Draft` |
| **DependsOnEditionRefs** | `FPFCorePatternSet@current` |
| **DependencyReason** | Все governing‑pattern cues ссылаются на FPF Core |
| **CompatibilityBoundary** | При изменении `E.4.DPF`, `C.22.2`, `E.8`, `G.2`, `E.21`, `E.23` — пересмотреть ProblemCard‑поля |
| **E53ConformanceNote** | Требуется проверка после стабилизации имён паттернов |

> **Source:** `assets/FPF-Literacy-dpf.md` lines L420-L442

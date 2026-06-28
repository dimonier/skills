# DPF: Business Analysis & Requirements Engineering — Relation Records (E.4.PFR)

> **Source:** `assets/BABusinessAnalysis-dpf.md` Section 7, lines L1052-L1136

---

## Expanded Relation Map

| Source | Target | Relation Kind | Relation Function | Reversibility |
|---|---|---|---|---|
| `BAR.StakeholderIdentification` | `BAR.RequirementElicitation` | `inputTo` | Идентифицированные стейкхолдеры — обязательный вход для elicitation | Необратимая: без stakeholder list elicitation неполна |
| `BAR.StakeholderIdentification` | `BAR.RequirementPrioritization` | `informs` | Полномочия стейкхолдеров по приёмке определяют вес требований | Частично обратимая: приоритизация может выявить неучтённых стейкхолдеров |
| `BAR.StakeholderIdentification` | `BAR.RequirementValidation` | `constrains` | Только идентифицированные стейкхолдеры могут signed off требования | Частично обратимая: validation может обнаружить missing stakeholder |
| `BAR.RequirementElicitation` | `BAR.ProblemVsSolutionSeparation` | `inputTo` | Elicitation поставляет сырой материал; problem framing отделяет потребность от решения | Необратимая: без elicitation нечего разделять |
| `BAR.RequirementElicitation` | `BAR.RequirementSpecification` | `inputTo` | Выявленные требования — вход для спецификации | Необратимая: без elicitation спецификация не опирается на источники |
| `BAR.ProblemVsSolutionSeparation` | `BAR.RequirementSpecification` | `inputTo` | Problem statement + acceptance criteria — обязательный вход для спецификации | Необратимая: без problem framing спецификация теряет grounding |
| `BAR.ProblemVsSolutionSeparation` | `BAR.RequirementPrioritization` | `informs` | Problem severity — критерий приоритизации | Частично обратимая: приоритизация может показать, что «проблема» не критична |
| `BAR.RequirementSpecification` | `BAR.RequirementValidation` | `inputTo` | Специфицированное требование — вход для валидации | Необратимая: без спецификации нечего валидировать |
| `BAR.RequirementSpecification` | `BAR.RequirementPrioritization` | `inputTo` | Специфицированные требования — вход для приоритизации | Необратимая: приоритизация без spec рискует ранжировать нереализуемое |
| `BAR.RequirementSpecification` | `BAR.RequirementTraceability` | `inputTo` | Требование с ID — начало цепочки трассировки | Необратимая: без ID trace link не к чему привязывать |
| `BAR.RequirementValidation` | `BAR.RequirementTraceability` | `triggers` | Валидированное требование запускает создание trace links | Необратимая: traceability стартует от валидированного требования |
| `BAR.RequirementValidation` | `BAR.RequirementPrioritization` | `feedsBack` | Валидация может выявить нереализуемость → пересмотр приоритета | Обратимая: validation ↔ prioritization — цикл |
| `BAR.RequirementPrioritization` | `BAR.RequirementChangeManagement` | `constrains` | Приоритеты определяют порог принятия change requests | Частично обратимая: change request может инициировать пересмотр приоритетов |
| `BAR.RequirementTraceability` | `BAR.RequirementChangeManagement` | `enables` | Traceability links — necessary precondition для impact analysis | Необратимая: без traceability change management слеп |
| `BAR.RequirementTraceability` | `BAR.RequirementValidation` | `supports` | Traceability позволяет проверить coverage: валидированные требования → тесты | Частично обратимая: validation выявляет gaps в traceability |
| `BAR.RequirementChangeManagement` | → *all patterns* | `triggers` | Change request запускает обновление: re-elicit, re-spec, re-validate, re-prioritize, re-trace | Обратимая: change → полный цикл обновления всех паттернов |

## Core Flow Diagram (Expanded with Feedback Loops)

```
  StakeholderIdentification ──inputTo──▶ Elicitation ──inputTo──▶ ProblemVsSolutionSeparation
         │               ▲                                        │
         │               │                                        │ inputTo
         │               │                                        ▼
         │               │                                  Specification
         │               │                              ┌───────┼───────┐
         │               │                         inputTo inputTo inputTo
         │               │                              │       │       │
         │               │                              ▼       ▼       ▼
         │               │                        Prioritization  │  Traceability
         │               │                              │  ▲      │  ▲
         │               │                              │  │      │  │
         │            informs                       constrains│    │  │
         │               │                              │ feedsBack│  │
         │               │                              ▼  │      ▼  │
         │               └────────── informs ──── Validation  │    │  │
         │                     (stakeholder weight)      │     │    │  │
         │                                               │triggers  │  │
         │                                               ▼     │    │  │
         └─────────── constrains ────▶ ChangeManagement ◀──────┘    │  │
         (sign-off authority)            │         ▲                │  │
                                         │         │  enables       │  │
                                         │         └── Traceability ─┘  │
                                         │                               │
                                         │ triggers (re-elicit, re-spec, │
                                         │ re-validate, re-prioritize,   │
                                         │ re-trace)                     │
                                         └───────────────────────────────┘

  [P2W] gate после Validation: requirement accepted for implementation
```

## Change Impact Matrix

| If this pattern changes | Then review these patterns | Because |
|---|---|---|
| `BAR.StakeholderIdentification` | `BAR.RequirementElicitation`, `BAR.RequirementPrioritization`, `BAR.RequirementValidation` | Новый/удалённый стейкхолдер меняет: список источников, вес требований, круг sign-off |
| `BAR.ProblemVsSolutionSeparation` | `BAR.RequirementSpecification`, `BAR.RequirementPrioritization` | Изменение problem statement требует переспецификации; новая severity меняет приоритет |
| `BAR.RequirementElicitation` | `BAR.ProblemVsSolutionSeparation`, `BAR.RequirementSpecification` | Новый материал требует problem framing; могут потребоваться новые спецификации |
| `BAR.RequirementSpecification` | `BAR.RequirementValidation`, `BAR.RequirementPrioritization`, `BAR.RequirementTraceability` | Изменение acceptance criteria требует перевалидации; изменение структуры ломает trace links |
| `BAR.RequirementPrioritization` | `BAR.RequirementChangeManagement` | Изменение критериев/приоритетов меняет порог принятия change requests |
| `BAR.RequirementValidation` | `BAR.RequirementSpecification`, `BAR.RequirementTraceability` | Failed validation → переспецификация; изменение validation status меняет traceability |
| `BAR.RequirementTraceability` | `BAR.RequirementChangeManagement`, `BAR.RequirementValidation` | Изменение traceability-модели меняет точность impact analysis |
| `BAR.RequirementChangeManagement` | *ALL patterns* | Change process затрагивает все паттерны: re-elicit, re-spec, re-prioritize, re-validate, re-trace |
| `BAR.BusinessProcessModeling` | `BAR.RequirementElicitation`, `BAR.RequirementTraceability` | Изменение процесса требует пересмотра требований и traceability links |
| `BAR.UseCaseModeling` | `BAR.RequirementSpecification`, `BAR.RequirementValidation` | Изменение use case требует переспецификации и перевалидации |
| `BAR.DataRequirements` | `BAR.RequirementSpecification`, `BAR.RequirementValidation`, `BAR.RequirementTraceability` | Новые требования к данным требуют спецификации, валидации и трассировки |
| `BAR.SecurityRequirements` | `BAR.RequirementSpecification`, `BAR.RequirementValidation`, `BAR.RequirementPrioritization` | Security requirements имеют приоритет выше бизнес-требований в regulated domain |

## Edition Dependency

| Слот | Значение |
|---|---|
| **FrameworkEditionRef** | `BusinessAnalysisPrincipleFramework@Draft` |
| **DependsOnEditionRefs** | `FPFCorePatternSet@current` |
| **DependencyReason** | Все governing‑pattern cues ссылаются на FPF Core |
| **CompatibilityBoundary** | При изменении `C.22.2`, `A.10`, `C.16`, `A.21`, `G.9`, `C.25`, `G.11`, `C.27` — пересмотреть ProblemCard‑поля и relation records |
| **E53ConformanceNote** | Требуется проверка после стабилизации имён паттернов |

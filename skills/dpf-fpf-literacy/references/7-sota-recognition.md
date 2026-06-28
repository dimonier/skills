# FPFLIT.SoTARecognition: Распознавание SoTA-решения в проблемной ситуации

> **Trigger:** При получении решения от AI-агента, которое выглядит разумным, но требует проверки на соответствие State-of-the-Art в предметной области
> **Governing patterns:** 
>   → `../fpf-core/references/G.2-source-pack.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/A.10-evidence.md`
>   → `../fpf-core/references/G.11-currentness.md`

---

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Агент предлагает решение, которое выглядит разумным, но не является SoTA в предметной области — либо устарело, либо применимо в другой области, либо просто «попсовое» |
| **ContextGrounding** | Инженер-менеджер формулирует проблему в предметной области, но не может самостоятельно отличить SoTA-ход от красивого, но неработающего |
| **ScopeCut** | Идентификация SoTA-решения для проблемной ситуации через FPF+DPF; не охватывает создание нового SoTA (исследование) |
| **NotWishReason** | «Агент предложил — значит, это работает» — слепое доверие к output агента без проверки на SoTA |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | FPF-паттерн: «Принцип указывает на то место, которое в известной проблемной ситуации прошло принципиальные проверки и указывает на SoTA-решение проблемы» |
| **EntityOfConcern** | SoTA-ход (state-of-the-art move) — наилучший из известных методов решения проблемы в данном контексте, подтверждённый источниками |
| **SymptomDetection** | Агент предлагает решение без ссылок на источники; решение противоречит known principles; решение «работает в теории», но не имеет evidence реализации |
| **ProblemHypothesis** | Агент не различает «часто упоминаемое в интернете» и «подтверждённое SoTA» — он оптимизирует вероятность, а не инженерную обоснованность |
| **ImprovementCheck** | Каждое предложенное решение имеет: (1) ссылку на SoTA-источник, (2) указание problem frame, в котором оно является SoTA, (3) границы применимости, (4) known limitations |
| **AcceptanceCriterion** | SoTA-echoing: для каждого решения указан источник (литература, стандарт, авторитетная практика); решение размечено по problem frame из DPF |
| **MandatoryConstraints** | Запрещено принимать решение как SoTA без source reference; «общее знание» агента не является evidence SoTA |
| **CharacterizationRelation** | Source authority (уровень источника), evidence strength (теория vs практика vs испытания), domain specificity (насколько решение предметно-специфично) |
| **ValidationBoundary** | Проверка: эксперт предметной области подтверждает, что предложенное решение действительно является SoTA для данного problem frame |
| **FreshnessOrExpiry** | `stale` при появлении новых SoTA-источников или опровержении текущих |
| **ProblemFormulationFollowUpReason** | Отделить инженерно-обоснованные решения от «попсовых» — не дать агенту ввести команду в заблуждение красивой формой без содержания |
| **ReadinessDisposition** | `P2W-ready` для проверки ответов агента на SoTA-соответствие |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| SoTA-echoing и source reference | `G.2` |
| Problem card как frame для SoTA | `C.22.2` |
| Evidence и assurance для claim | `A.10`, `B.3` |
| Comparison frame для альтернатив | `G.0`, `G.9` |
| Refresh при устаревании | `G.11` |

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.PrincipleAsMoveExclusion` | `FPFLIT.SoTARecognition` | Принцип как move exclusion — механизм отличения SoTA от не-SoTA |
| `FPFLIT.AgentContextLoad` | `FPFLIT.SoTARecognition` | Загрузка контекста — условие для распознавания агентом SoTA-решений |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

---

> **Source:** `assets/FPF-Literacy-dpf.md` lines L341-L377

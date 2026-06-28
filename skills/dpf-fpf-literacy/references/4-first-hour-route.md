# FPFLIT.FirstHourDPFRoute: Маршрут создания черновика DPF за первый час

> **Trigger:** При первом решении создать DPF для своей предметной области — до начала работы с агентом над содержанием
> **Governing patterns:** 
>   → `../fpf-core/references/E.4.DPF-authoring.md`
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/E.4.PFAD-decision.md`
>   → `../fpf-core/references/C.33-carrier-admission.md`
>   → `../fpf-core/references/G.2-source-pack.md`

---

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда хочет дать AI-агенту предметное знание, но не знает, с чего начать; попытки «загрузить всё» приводят к неструктурированному контексту, который агент не может эффективно использовать |
| **ContextGrounding** | Инженер-менеджер имеет доступ к AI-агенту, файлу FPF Core и знаниям о своей предметной области; нужно за ограниченное время (≈90 минут) получить первый рабочий черновик DPF |
| **ScopeCut** | First-hour route: создание файла-черновика DPF по spine E.4.DPF; не охватывает полный цикл улучшений до industrial-grade DPF |
| **NotWishReason** | «Сделай мне DPF по моей области» одним промптом без последующего чтения и правок |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Материалы практикума 28.06.2026: демонстрация создания DPF за 90 минут с вариантами задания предметной области |
| **EntityOfConcern** | Файл DPF как first-entry carrier — маркдаун-документ, содержащий spine: context → source pack → PFAD → names → patterns → relations → quality → refresh |
| **SymptomDetection** | Агент без структуры DPF выдаёт красивый текст «обо всём», но без problem cards, без explicit scope cuts, без mandatory constraints, без governing-pattern cues |
| **ProblemHypothesis** | Команда не использует structured spine E.4.DPF — агент получает задачу «напиши учебник», а не «создай DPF по спецификации E.4.DPF» |
| **ImprovementCheck** | Черновик DPF содержит: context declaration, source pack, PFAD, names, ≥3 problem cards с always-core и conditional fields, relation rows, carrier admission, quality route, refresh route |
| **AcceptanceCriterion** | Файл DPF читается как единый документ; каждая problem card имеет ProblemSignal, ContextGrounding, ScopeCut, NotWishReason и AcceptanceCriterion; все governing-pattern cues ссылаются на FPF Core |
| **MandatoryConstraints** | DPF всегда в файле (не в чате) — это снимает ограничения на размер и позволяет циклы улучшений; DPF всегда depends on FPF Core; запрещён Core landing (DPF не модифицирует FPF Core) |
| **CharacterizationRelation** | Completeness (все ли секции spine заполнены), specificity (насколько ходы предметно-специфичны), usability (может ли агент использовать как контекст) |
| **ValidationBoundary** | Проверка: агент с загруженным DPF даёт предметно-релевантный ответ на ≥3 типовых вопроса из bounded context |
| **FreshnessOrExpiry** | `stale` при изменении FPF Core edition или появлении новых SoTA-источников в предметной области |
| **ProblemFormulationFollowUpReason** | Создать структурированный носитель предметного знания, который можно улучшать итеративно |
| **ReadinessDisposition** | `P2W-ready` как drafting aid для первого часа работы |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| DPF authoring spine | `E.4.DPF` |
| Problem card structure | `C.22.2` |
| Framework architecture decision | `E.4.PFAD` |
| Carrier selection для публикации | `C.33` |
| Source pack formation | `G.2` |

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.FirstHourDPFRoute` | `FPFLIT.CarrierFirstEntry` | Маршрут создания DPF предписывает выбор файла как carrier |
| `FPFLIT.FirstHourDPFRoute` | `FPFLIT.DPFImprovementCycle` | First-hour DPF — вход для цикла улучшений |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

---

> **Source:** `assets/FPF-Literacy-dpf.md` lines L220-L257

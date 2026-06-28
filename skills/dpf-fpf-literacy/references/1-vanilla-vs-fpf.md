# FPFLIT.VanillaVsFPF: Различение ответов AI с опорой на принципы и без

> **Trigger:** При получении ответа AI-агента на инженерный запрос — до принятия ответа как рабочего решения
> **Governing patterns:** 
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/E.17-multi-view.md`
>   → `../fpf-core/references/A.10-evidence.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`

---

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | AI-агент на запрос «помоги улучшить этот документ» выдаёт косметическую правку стиля, общую структуру и уверенные рекомендации — не спрашивая, какое решение должен поддержать документ |
| **ContextGrounding** | Инженер-менеджер использует AI-агента для рабочих задач в проекте; задача не тривиальна и требует не «красивого ответа», а работающего решения |
| **ScopeCut** | Различение типа ответа агента (FPF-опосредованный vs vanilla); не охватывает сравнение разных AI-моделей |
| **NotWishReason** | «Сделай мне красиво» — это ожидание чуда, а не рабочая постановка задачи |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **EntityOfConcern** | Ответ AI-агента как эпистемический артефакт — его структура, обоснованность, пригодность для дальнейшей работы |
| **SymptomDetection** | Агент сглаживает стиль, добавляет общую структуру, пишет уверенные рекомендации; не спрашивает о problem context, не указывает на evidence gaps, не предлагает rejected alternatives |
| **ProblemHypothesis** | Без загрузки принципов (FPF) агент работает в режиме «вероятностной стрельбы по площадям» — выбирает наиболее вероятный, а не наиболее правильный для данной инженерной ситуации ход |
| **ImprovementCheck** | После загрузки FPF агент перестаёт делать косметику вместо работы, обращает внимание на действительно важное, отсекает неважное, указывает на problem-side record до предложения решения |
| **AcceptanceCriterion** | Ответ агента содержит: (1) identification problem context, (2) separation of problem and solution, (3) explicit alternatives with rejected reasons, (4) governing-pattern cues, (5) что остаётся непроверенным |
| **MandatoryConstraints** | Запрещено принимать ответ агента без FPF-контекста за working solution; запрещено использовать «красивый ответ» как decision basis |
| **CharacterizationRelation** | Problem-side fidelity, solution-side SoTA alignment, evidence explicitness, readability for intended reader |
| **ValidationBoundary** | Проверка на трёх типовых запросах (выбор имени, предложение архитектуры, «что делать») — с FPF и без |
| **FreshnessOrExpiry** | `stale` при смене версии FPF Core или модели AI-агента |
| **ProblemFormulationFollowUpReason** | Исключить «машинную попсовую интуицию» из рабочих процессов до того, как она породит дорогие ошибки |
| **ReadinessDisposition** | `P2W-ready` для выбора способа постановки задачи агенту |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Problem identification до решения | `C.22.2` |
| Различение description и described thing | `E.17` |
| Evidence gap explicit | `A.10` |
| Intended reader и publication form | `E.17.EFP` |

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.VanillaVsFPF` | `FPFLIT.AgentContextLoad` | Различение типов ответов — предпосылка для правильной загрузки контекста |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

---

> **Source:** `assets/FPF-Literacy-dpf.md` lines L104-L140

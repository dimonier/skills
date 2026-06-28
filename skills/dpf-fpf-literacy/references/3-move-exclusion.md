# FPFLIT.PrincipleAsMoveExclusion: Принцип как паттерн отсечения негодных ходов

> **Trigger:** При рассмотрении множества вариантов решения — до инвестиций в детальный анализ каждого варианта
> **Governing patterns:** 
>   → `../fpf-core/references/E.8-pattern-body.md`
>   → `../fpf-core/references/G.2-source-pack.md`
>   → `../fpf-core/references/A.21-gate.md`

---

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда рассматривает «100500 способов сделать что-то не так» на один-два годных; время тратится на анализ заведомо неработающих вариантов |
| **ContextGrounding** | Инженерная/исследовательская работа, где пространство возможных ходов велико, а обратная связь медленная, дорогая или шумная |
| **ScopeCut** | Применение принципа как move exclusion filter на дальних подступах — до тонкой предметной экспертизы |
| **NotWishReason** | «Давайте рассмотрим все варианты» — без предварительного отсечения заведомо невозможных ходов |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Парижская академия наук (1775): запрет рассмотрения проектов вечных двигателей на основе принципа сохранения энергии. Современные патентные ведомства воспроизводят это правило |
| **EntityOfConcern** | Принцип как паттерн: декларативно (акаузально) представленный метод работы, содержащий Problem frame, Solution (SoTA-ход), Forces, Examples, Anti-patterns, и Governing-pattern cues |
| **SymptomDetection** | Эксперты тратят время на обсуждение вариантов, которые нарушают известные принципы; агент предлагает «красивые» решения, несовместимые с FPF/DPF |
| **ProblemHypothesis** | Принципы не сформулированы явно как move exclusion rules — команда полагается на интуицию, а не на явные паттерны отсечения |
| **ImprovementCheck** | Время до отбрасывания негодного хода сокращается; экспертиза направляется на сравнение admissible вариантов, а не на отсев non-admissible |
| **AcceptanceCriterion** | Принцип содержит: (1) problem frame (в какой ситуации), (2) forces (почему трудно), (3) solution (SoTA-ход), (4) anti-patterns (что нельзя делать), (5) near-miss examples (похоже, но неправильно), (6) governing-pattern cues |
| **MandatoryConstraints** | Принцип не является инструкцией-рецептом; принцип не может быть сведён только к «problem → solution» без остальных секций |
| **CharacterizationRelation** | Move exclusion power (сколько ходов отсекает), false-positive risk (отсекает ли годные ходы), domain coverage (в каких ситуациях применим) |
| **ValidationBoundary** | Проверка на ≥3 исторических примерах, где отсутствие принципа привело к ошибке |
| **FreshnessOrExpiry** | `stale` при появлении нового физического эффекта, научной теории или инженерной практики, меняющей границы применимости |
| **ProblemFormulationFollowUpReason** | Встроить move exclusion в процесс принятия решений до инвестиций в детальный анализ |
| **ReadinessDisposition** | `P2W-ready` для применения как фильтра при рассмотрении вариантов |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Pattern body structure (Problem, Solution, Forces, etc.) | `E.8` |
| Anti-pattern и near-miss specification | `E.8` (anti-pattern section) |
| SoTA-echoing — ссылка на литературу | `G.2` |
| Принцип как admissible move | `A.21` (gate) |

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.PrincipleAsMoveExclusion` | `FPFLIT.SoTARecognition` | Принцип как move exclusion — механизм отличения SoTA от не-SoTA |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

---

> **Source:** `assets/FPF-Literacy-dpf.md` lines L181-L217

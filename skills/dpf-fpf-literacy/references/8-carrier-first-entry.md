# FPFLIT.CarrierFirstEntry: Выбор носителя для первой публикации DPF

> **Trigger:** Перед созданием DPF — до написания первого промпта агенту
> **Governing patterns:** 
>   → `../fpf-core/references/C.33-carrier-admission.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`
>   → `../fpf-core/references/E.4.DPF-authoring.md`
>   → `../fpf-core/references/E.4.PFR-relations.md`

---

#### Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Команда пытается создать DPF в чате с агентом — вывод обрезается, структура теряется, невозможно вернуться к предыдущей версии и править |
| **ContextGrounding** | Создание первого DPF с AI-агентом; нужно сохранить результат для последующего чтения, обсуждения и циклов улучшения |
| **ScopeCut** | Выбор формата и носителя для first-entry carrier DPF; не охватывает долгосрочное управление версиями и публикациями |
| **NotWishReason** | «Напиши мне DPF» в чат — вывод обрезается, агент пишет «нрзбрчво» (сокращённо), структура теряется |

#### Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Правило практикума: «В файле — это важно, это снимает ограничения на размер, а ещё — можно потом править-улучшать» |
| **EntityOfConcern** | First-entry carrier — файл (markdown), содержащий полный текст DPF как локальный монолит с извлекаемыми секциями |
| **SymptomDetection** | Ответ агента в чат обрезан; структура DPF неполна; невозможно отличить, где кончается ответ агента и начинаются следующие сообщения |
| **ProblemHypothesis** | Чат как carrier не подходит для structured artifacts размером больше нескольких абзацев — он оптимизирован для диалога, а не для документов |
| **ImprovementCheck** | DPF сохранён как файл; файл можно открыть, прочитать полностью, отредактировать, передать другому агенту, загрузить в новую сессию |
| **AcceptanceCriterion** | DPF — markdown-файл; содержит все секции spine; может быть загружен агенту как контекст; может быть отредактирован человеком или агентом по запросу «отредактируй файл» |
| **MandatoryConstraints** | Первая публикация DPF — всегда в файл, не в чат; файл должен быть в формате, допускающем редактирование (markdown, не PDF); файл должен содержать explicit version/status |
| **CharacterizationRelation** | Completeness (полнота содержания), editability (возможность правок), portability (переносимость между сессиями/агентами), shareability (возможность передачи коллегам) |
| **ValidationBoundary** | Проверка: агент может прочитать файл DPF и использовать его как контекст для ответа на предметный вопрос |
| **FreshnessOrExpiry** | `stale` при структурных изменениях DPF, требующих новой публикации |
| **ProblemFormulationFollowUpReason** | Выбрать правильный carrier до начала работы — иначе результат будет потерян или неполон |
| **ReadinessDisposition** | `P2W-ready` для выбора носителя перед созданием DPF |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Carrier admission criteria | `C.33` |
| Publication unit и scope | `E.17.EFP` |
| First-entry carrier для framework | `E.4.DPF` |
| Relation records carrier | `E.4.PFR` |

## Relations

| Source | Target | Relation Function |
|---|---|---|
| `FPFLIT.FirstHourDPFRoute` | `FPFLIT.CarrierFirstEntry` | Маршрут создания DPF предписывает выбор файла как carrier |
| `FPFLIT.DPFImprovementCycle` | → *all pattern cards* | Цикл улучшения применим к каждой problem card DPF |

---

> **Source:** `assets/FPF-Literacy-dpf.md` lines L381-L417

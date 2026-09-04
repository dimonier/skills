---
id: PV.Inbox
title: "Приём входящих: inbox-процедура, PDF-препроцессинг, роутинг на A/R/T"
status: seed
readiness: source-faithful
keywords: [inbox, intake, pdf, preprocess, routing, capture]
dependencies:
  builds_on:
    - E.11
    - C.11
  coordinates_with:
    - A.15.1
---

## PV.Inbox - Приём входящих: inbox-процедура, PDF-препроцессинг, роутинг на A/R/T

> **Trigger:** Когда владелец просит «обработать inbox» (или аналогично), или когда в `inbox/` появились новые исходники (транскрипты, PDF, статьи, исследования).
> **Governing FPF patterns:**
>   → E.11 (практический вход: именованные entry-path)
>   → C.11 (фиделити захвата исходника)
> **Skill dependencies:**
>   → pdf2md (конвертация PDF в Markdown)

---

### PV.Inbox:1 - Problem frame

Use this pattern to intake raw sources from `inbox/`, preprocess them, and route
each to the correct procedure (state update, external research, or track work)
without analysing the original directly when a faithful Markdown conversion is
available.

### PV.Inbox:2 - Problem

Входящие приходят в смешанных форматах (транскрипты, PDF, статьи, исследования)
и без явного роутинга либо теряются, либо обрабатываются неправильным
процессом. PDF-исходники нельзя анализировать напрямую — нужна конвертация
перед содержательной обработкой.

### PV.Inbox:3 - Forces

| Force | Settlement |
|---|---|
| Смешанные форматы vs один процесс | Роутинг по типу материала: транскрипт → StateUpdate, исследование → ExternalResearch, работа → Track. |
| PDF-фиделити vs прямой анализ | Конвертировать PDF в Markdown (pdf2md); анализировать только конвертат. |
| Полнота vs замусоривание | После полной обработки — очистить `inbox/`. |

### PV.Inbox:4 - Solution

1. **Запрос.** По запросу «process inbox» (и аналогичным) обработать файлы из
   `inbox/` процедурами LPF. После полной обработки — очистить `inbox/`.
2. **PDF-препроцессинг.** Если в `inbox/` есть `.pdf` — до содержательной
   обработки конвертировать каждый PDF в Markdown скиллом `pdf2md` (скрипт
   `scripts/extract_pdfs.py`, параметры `--source <inbox_dir> --first N`).
   Результат (`.md` в `inbox/_markdown/`) использовать как исходник для
   дальнейших процедур (StateUpdate, Track). Оригинальный PDF напрямую не
   анализировать — только через конвертированный Markdown. Если `pdf2md`
   недоступен или конвертация падает — зафиксировать это в результате
   обработки inbox и уведомить владельца.
3. **Роутинг внешних исследований.** Независимые исследования (Knowy),
   нарративизации, статьи, доклады, туториалы — через процедуру
   ExternalResearch с двусторонней привязкой к сущностям, принимающим ссылки
   (Q, RISK, CON, DEC, TRK).
4. **Роутинг на процедуры.** Транскрипт/протокол встречи → StateUpdate (и
   связанные сущности); материал с ценными артефактами → подшить в подходящий
   трек или создать новый (Track).

### PV.Inbox:5 - Archetypal Grounding

**Show.** Обработка inbox в этом проекте: PDF конвертируется через `pdf2md`,
транскрипты идут в StateUpdate, статьи — в ExternalResearch, после обработки
`inbox/` пустеет.

### PV.Inbox:6 - Bias-Annotation

Соблазн — анализировать PDF напрямую «для скорости», пропуская конвертацию:
теряется фиделити и воспроизводимость. Симметричный соблазн — оставить
`inbox/` после обработки «на всякий случай»: накапливается мусор и
необработанные сигналы.

### PV.Inbox:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-IB.1 | PDF конвертирован в Markdown до содержательной обработки; оригинал напрямую не анализируется. |
| CC-IB.2 | Каждый материал направлен по типу: StateUpdate / ExternalResearch / Track. |
| CC-IB.3 | После полной обработки `inbox/` очищен. |
| CC-IB.4 | Сбой конвертации зафиксирован и доведён до владельца. |

### PV.Inbox:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Прямой анализ PDF без конвертации | Сначала `pdf2md`, потом обработка `.md`. |
| Материал без явного роутинга | Определить тип и направить в нужную процедуру. |
| `inbox/` не очищен после обработки | Очистить по завершении. |

### PV.Inbox:9 - Consequences

Надёжный intake отделяет «захват» от «содержательной обработки» и не даёт
материалу остаться сиротой. Цена — обязательная конвертация PDF и явный
роутинг каждого входящего.

### PV.Inbox:10 - Rationale

Вход должен быть практическим (`E.11`): именованные entry-path на процедуры
вместо одного линейного процесса. Конвертация PDF до анализа — фиделити захвата
(`C.11`): обрабатывается верное представление исходника, а не сырой бинарник.

### PV.Inbox:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.11` (практический вход) | Adopt | Роутинг по типу материала на entry-path | Reopen при ревизии `E.11` |
| FPF `C.11` (фиделити захвата) | Adopt | PDF → Markdown до анализа | Reopen при ревизии `C.11` |
| `pdf2md` skill (vision-language OCR) | Adopt | Конвертация PDF в Markdown | Reopen при смене конвертера |

Best-known line: предобработка входа до анализа. Rejected rival: «анализ PDF
напрямую» — отброшен из-за потери фиделити.

### PV.Inbox:12 - Relations

- **Builds on:** `E.11` (практический вход), `C.11` (фиделити захвата).
- **Coordinates with:** `A.15.1` (исполнение intake).
- **Specialized by:** routes to `PV.StateUpdate`, `PV.ExternalResearch`, `PV.Track`.

### PV.Inbox:End

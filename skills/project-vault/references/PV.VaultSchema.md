---
id: PV.VaultSchema
title: "Схема и модель сущностей markdown-vault: директории, ID-аллокация, discovery"
status: seed
readiness: source-faithful
keywords: [schema, entities, directories, id-allocation, discovery, vault.py, carrier, kind]
dependencies:
  builds_on:
    - C.33
    - C.2.1
    - E.4.DPF
  coordinates_with:
    - F.14
    - F.18
    - C.32.ADR
---

## PV.VaultSchema - Схема и модель сущностей markdown-vault: директории, ID-аллокация, discovery

> **Trigger:** Когда нужно понять, где в хранилище живёт та или иная сущность, как ей присвоить ID, как её найти, или когда меняется схема vault (новый тип сущности, новая директория, новый носитель).
> **Governing FPF patterns:**
>   → C.33 (kind-дисциплина: выбор носителя и различение kind-ов)
>   → C.2.1 (идентичность издания, независимая от носителя)
>   → E.4.DPF (layering D5: пакет-носитель, возвращающий к авторитетному предмету)
> **Skill dependencies:**
>   → нет (схема — собственная область LPF)

---

### PV.VaultSchema:1 - Problem frame

Use this pattern to lay out and maintain the entity model of the vault: which
entities exist, where they live, how IDs are allocated, and how entities are
discovered without hand-maintained indexes.

### PV.VaultSchema:2 - Problem

Хранилище дробится на два сбоя: либо структура «зарастает» ручными индексами,
которые рассинхронизируются с атомарными файлами, либо ID раздаются «на глаз»
по содержимому директории и случаются дубликаты/пропуски. Discovery без
канонического реестра означает, что сущности должны быть находимы
машинно (`grep`/`SocratiCode`), а не через поддерживаемый вручную список.

### PV.VaultSchema:3 - Forces

| Force | Settlement |
|---|---|
| Атомарность vs сводный индекс | Сущности — атомарные файлы; ручных `_index.md` нет; авто-генерируются только `work/_index.md` и `tracks/_index.md`. |
| Монотонность ID vs ручная нумерация | ID выдаёт CLI `vault.py next-id`; ID не переиспользуются при закрытии. |
| Единство носителя vs рассеяние | Одна директория `project-vault/` — канонический носитель; kind-директории верхнего уровня. |
| Discovery vs реестр | `grep` для точного поиска, `SocratiCode codebase_search` для семантического, `ls` для полного списка. |

### PV.VaultSchema:4 - Solution

**Структура верхнего уровня** (канонический носитель — `project-vault/`):

```text
project-vault/
  decisions/         # атомарные карточки решений (DEC-NNNN.md)
  open-questions/    # атомарные открытые вопросы (Q-NNNN.md)
  risks/             # атомарные риски (RISK-NNNN.md)
  contradictions/    # атомарные противоречия (CON-NNNN.md)
  tracks/            # операционные треки (TRK-NNNN.md) + авто _index.md
  work/              # записи ходов (WRK-YYYY-MM-DD-hhmmss.md) + авто _index.md
  artifacts/         # артефакты, привязанные к трекам (YYYY-MM-DD-slug.md)
  methods/           # переиспользуемые описания методов (U.MethodDescription)
  roles/             # роли (соавторы/ответственные)
  vocabulary/        # глоссарий терминов проекта
  sources/           # captures/ (исходники) + digests/ (дайджесты анализа)
  state/             # constraints.md — регуляторные и архитектурные ограничения
  reports/           # производные сводки и отчёты (off-limits без запроса)
  scripts/           # vault.py (ID + индексы + проверка целостности), export_dec.py
  dependencies.md    # внешние блокеры
  agenda-next.md     # повестка следующей встречи (по запросу)
```

**Сущности и их kind-директории.** Каждая сущность — атомарный `.md` с YAML
frontmatter (`id`, `status`, `updated`, `sources`) + Markdown-телом. Закрытые
сущности остаются на месте с `status` во frontmatter (без `archive/`-зеркала).
`reports/` — производные сводки, создаются/обновляются только по явному запросу
(off-limits). `roles/` и `vocabulary/` — справочные: роли и глоссарий.

**Discovery вместо ручных индексов.** Для сущностей (`decisions/`,
`open-questions/`, `risks/`, `contradictions/`, `methods/`) ручных `_index.md`
нет. Нахождение:
- **Семантический поиск:** `SocratiCode codebase_search` по `project-vault/`.
- **Точный поиск:** `grep` по директориям сущностей (напр. `grep -l "^status: open" project-vault/open-questions/`, `grep -l "^status: active" project-vault/risks/`).
- **Полный список:** `Get-ChildItem` / `ls`.
- **Индексы треков/ходов:** только `work/_index.md` и `tracks/_index.md`,
  авто-генерируются `vault.py` (после каждого WRK — `vault.py all`, после смены
  статуса трека — `vault.py tracks`).

**ID-аллокация.** Новые ID (`DEC/Q/RISK/CON/TRK`) — только из CLI
`python project-vault/scripts/vault.py next-id` (или `next-id CON`). ID
монотонны и не переиспользуются; закрытие сущности не освобождает номер.
Целостность проверяется `python project-vault/scripts/vault.py check` (нет
дубликатов и рассинхрона ID).

**Путь к CLI.** Скрипт живёт в репозитории `project-vault/scripts/vault.py`
(при init копируется из `<skill>/scripts/vault.py`). Вызов из корня репозитория:

```bash
python project-vault/scripts/vault.py <command> [--path <abs-path-to-project-vault>]
```

`--path` обязателен при вызове не из корня репозитория.

### PV.VaultSchema:5 - Archetypal Grounding

**Show.** Действующий vault этого проекта использует kind-директории верхнего
уровня, атомарные DEC/RISK/Q/CON/TRK/WRK, авто-`_index.md` только для `work/` и
`tracks/`, и `vault.py next-id` для монотонной аллокации ID.

### PV.VaultSchema:6 - Bias-Annotation

Соблазн — завести ручной `_index.md` «для удобства» в каждой директории
сущностей: выглядит зрелым, но рассинхронизируется с атомарными файлами.
Симметричный соблазн — присвоить ID «на глаз» по `ls` вместо CLI. Оба
разрушают то, что даёт схема: единый носитель и машинную находимость.

### PV.VaultSchema:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-VS.1 | Каждая сущность — атомарный файл в своей kind-директории. |
| CC-VS.2 | Ручных `_index.md` в директориях сущностей нет; авто-генерируются только `work/_index.md` и `tracks/_index.md`. |
| CC-VS.3 | ID выдаются только через `vault.py next-id`; монотонны, не переиспользуются. |
| CC-VS.4 | Discovery достижим через `grep`/`SocratiCode`/`ls`. |
| CC-VS.5 | Закрытые сущности остаются на месте со `status` во frontmatter, без `archive/`-зеркала. |
| CC-VS.6 | `vault.py check` проходит без дубликатов и рассинхрона ID. |

### PV.VaultSchema:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Ручной `_index.md` в директории сущностей | Убрать; discovery через `grep`/`SocratiCode`. |
| ID присвоен по `ls` | Всегда `vault.py next-id`. |
| Закрытую сущность переместили в `archive/` | Оставить на месте, проставить `status`. |
| Дублирующая копия схемы в нескольких местах | Одна каноническая схема — это тело; остальное ссылается. |

### PV.VaultSchema:9 - Consequences

Атомарность + машинная находимость дают надёжный discovery без реестра, но
требуют дисциплины ID-аллокации и запрета ручных индексов. Изменение схемы
(новый тип сущности) — это изменение границы поля практики и условие
пересмотра решения о самом LPF.

### PV.VaultSchema:10 - Rationale

Kind-директории верхнего уровня реализуют kind-дисциплину `C.33`: носитель
(`project-vault/`) — access-facing carrier, издание (`C.2.1`) — восстанавливаемая
из атомарных файлов идентичность, независимая от конкретного носителя.
Отказ от ручных индексов — следствие `E.4.DPF:4` (пропорциональность): больше
файлов не делает фреймворк зрелее.

### PV.VaultSchema:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `C.33` (kind-дисциплина, носитель vs издание) | Adopt | Канонический носитель — `project-vault/`; издание восстанавливается из атомарных файлов | Reopen при ревизии `C.33` |
| FPF `F.14` (анти-взрыв имён/ID) | Adopt | Один ID на сущность, без alias-реестров | Reopen при ревизии `F.14` |
| Obsidian-style «one file per entity + query» | Adapt | Атомарные файлы + `grep`/`SocratiCode` вместо dataview-запросов | Reopen при смене инструмента поиска |

Best-known line: атомарные сущности с машинным discovery. Rejected rival:
«рукописный реестр в каждом каталоге» — отброшен из-за рассинхрона.

### PV.VaultSchema:12 - Relations

- **Builds on:** `C.33` (носитель vs издание), `C.2.1` (идентичность издания), `E.4.DPF` (layering D5).
- **Coordinates with:** `F.14` (анти-взрыв ID), `F.18` (именование), `C.32.ADR` (карточки решений — один из kind-ов).
- **Specialized by:** `PV.StateUpdate` (создание сущностей), `PV.Track` (треки как сущности), `PV.WorkRecord` (WRK как сущности).

### PV.VaultSchema:End

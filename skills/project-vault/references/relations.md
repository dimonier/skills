# Project Vault — Relation Records

> **Canonical home.** This file is the canonical home for the source/edition/
> dependency citation and the dependency graph. The same graph appears in three
> views — each card's frontmatter `dependencies` (machine-readable), each card's
> `:12 Relations` (human-readable), and this file (the global map). All three must
> agree in membership and edge direction; change one → change all three.
>
> **Edge direction.** A row reads `From → To` = "From depends on / is placed by /
> applies to To". A `builds_on` edge is written as "dependent pattern → what it
> builds on". SKILL.md carries only a one-line pointer here.

## Source / edition citation

- **Skill:** `project-vault` (LPF — Local Practices Framework).
- **Authoring scenario (EntryRoute):** исход (a) «пересмотр framework»;
  оси — `FPF-grounded` (опирается на FPF Core) и `language-from-scratch`
  (канонический носитель — `references/*.md` самого скилла; внешнего
  опубликованного документа-проекции нет).
- **Field / граница поля:** практика «управление состоянием проекта в
  markdown-vault»: захват состояния из источников (транскрипты/диалоги),
  привязка внешних исследований, жизненный цикл треков, запись работ,
  создание артефактов, повестка, целостность схемы и ID.
- **Dependency chain (unidirectional, `E.5.3`):** `project-vault` → `FPF` → (nothing).
  `create-agent-skill` — skill-зависимость по механике носителя, не FPF-паттерн.
  `pdf2md` — skill-зависимость `PV.Inbox` (конвертация PDF).
- **Readiness:** все 8 паттернов — `status: seed`, readiness-режим `source-faithful`
  (верны одобренному источнику — FPF + процедурная практика владельца);
  не `case-validated`.

## Refresh triggers (G.11)

Пересматривать этот скилл (reopen → refresh по `G.11`) при наступлении любого из:

1. **Изменение источника** (`E.4.PFR`, G.11 `EditionPinChange`): ревизия FPF Core
   паттернов, на которые опираются governing-cues (`E.8`, `E.9`, `C.32.ADR`,
   `C.33`, `C.2.1`, `A.15.1`, `A.15.2`, `G.11`, `F.14`, `F.18`).
2. **Изменение схемы vault** (граница поля практики): новый тип сущности,
   новая директория, новый носитель или инструмент поиска → правь `PV.VaultSchema`
   и затронутые соседние тела.
3. **Изменение PLAS** (`E.4.PFAD`-ревизия): скилл `pattern-language-as-agent-skill`
   меняет требования к конформности (E.8-секции, EntryRoute, carrier-механика).
4. **Телеметрия локального использования** (G.11 `TelemetryDelta`): владелец
   сообщает, что скилл неверно сработал, неоднозначен, или слабая модель
   (`create-agent-skill` weak-model gate) не следует шагам без домысливания.
5. **Изменение carrier-механики** (`create-agent-skill`): атомарность, layout
   или single-surface договорённости меняются.

Минимальный маршрут пересмотра: `E.4.DPF.DA` D1–D12 + `E.21` для затронутых тел
+ прогон `scripts/check_frontmatter.py` — без полного «царь-трека» пересборки.

## Dependency graph

| From (→) | To | Relation function |
|---|---|---|
| `PV.Inbox` | `PV.StateUpdate` | Inbox роутит транскрипты/протоколы на обновление состояния |
| `PV.Inbox` | `PV.ExternalResearch` | Inbox роутит внешние исследования на двустороннюю привязку |
| `PV.Inbox` | `PV.Track` | Inbox подшивает ценные артефакты в треки |
| `PV.StateUpdate` | `PV.VaultSchema` | Создание сущностей и ID-аллокация по схеме |
| `PV.StateUpdate` | `PV.Track` | Операционные сигналы источника заводят/меняют треки |
| `PV.ExternalResearch` | `PV.StateUpdate` | Внешний сигнал может потребовать нового решения/риска |
| `PV.ExternalResearch` | `PV.VaultSchema` | Сигналы пишутся в сущности vault |
| `PV.Track` | `PV.VaultSchema` | Треки — сущности vault с авто-индексом |
| `PV.Artifact` | `PV.Track` | Артефакт создаётся привязанным к треку |
| `PV.WorkRecord` | `PV.Track` | WRK фиксирует шаг внутри трека |
| `PV.WorkRecord` | `PV.VaultSchema` | WRK — сущности `work/` с авто-индексом |
| `PV.Agenda` | `PV.StateUpdate` | Повестка берёт слоты `proposed`/`deferred` решений |
| `PV.Agenda` | `PV.VaultSchema` | Повестка — файл `agenda-next.md` |

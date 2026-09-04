---
id: PV.ExternalResearch
title: "Внешние исследования: двусторонняя привязка справочного материала к сущностям"
status: seed
readiness: source-faithful
keywords: [external-research, two-way-binding, digest, signal, reference, orphan]
dependencies:
  builds_on:
    - E.4.PFR
    - C.11
    - G.11
  coordinates_with:
    - A.3.2
---

## PV.ExternalResearch - Внешние исследования: двусторонняя привязка справочного материала к сущностям

> **Trigger:** Когда материал не является ни транскриптом встречи, ни новостями диалога — независимое исследование (Knowy), нарративизация, статья, доклад, туториал — и его нужно учесть в принятии решений, а не оставить сиротой.
> **Governing FPF patterns:**
>   → E.4.PFR (запись связей между фреймворками/сущностями)
>   → C.11 (фиделити и ссылка на источник)
>   → G.11 (свежесть/валюта внешнего материала)
> **Skill dependencies:**
>   → нет

---

### PV.ExternalResearch:1 - Problem frame

Use this pattern to file reference material so it is taken into account in
decision-making: capture the source, write a digest, discover affected entities,
propagate signals into their files (two-way), and bind the digest to at least one
reference-bearing entity.

### PV.ExternalResearch:2 - Problem

Внешний материал легко остаётся «сиротой»: дайджест создан, но сигналы не
попали в сущности, и при будущем решении материал не учитывается. Односторонняя
сверка («Reconciliation» только в дайджесте) — неполная обработка: ссылка в одну
сторону не делает материал найденным из сущности.

### PV.ExternalResearch:3 - Forces

| Force | Settlement |
|---|---|
| Учтён в решении vs сирота | Двусторонняя привязка: сигнал в файл сущности + дайджест в её `sources`/«Related entities». |
| Один против многих сущностей | Привязать к ≥1 сущности, принимающей ссылки (Q/RISK/CON/DEC/TRK). |
| Новое vs справочное | Атомарные сущности — только если материал вносит новое решение/риск/вопрос/противоречие. |
| Внутри против вне скоупа | Если материал вне скоупа всех сущностей — явно «not bound — outside the project scope». |

### PV.ExternalResearch:4 - Solution

1. Сохранить исходник в `project-vault/sources/captures/`.
2. Создать дайджест `project-vault/sources/digests/YYYY-MM-DD_slug.md`
   (`source_kind`: `independent_research` / `web_article` / `conference` / `research_article`).
3. Обнаружить активные сущности поиском по vault: `grep` для точного совпадения
   по директориям (`grep -l "^status: open" project-vault/open-questions/`,
   `grep -l "^status: active" project-vault/risks/`, `grep -l "^status: open"
   project-vault/contradictions/`) и `SocratiCode codebase_search` для
   семантического поиска релевантных DEC/Q/RISK/CON/TRK по теме. Определить,
   какие сущности принимают ссылки и релевантны теме.
4. Заполнить раздел «Reconciliation» дайджеста силой сигнала для каждой
   затронутой сущности (`strong` / `partial` / `weak` / `supporting` / `no_signal`).
5. **Разнести сигналы в сами файлы сущностей (обязательно, двусторонняя
   связь):** для каждой затронутой сущности (Q, RISK, CON, DEC — с полем
   `sources`/`source` или разделом «Related entities») дописать сигнал в файл.
   Перечисление ID только в «Reconciliation» дайджеста — недостаточно.
   - **DEC:** сигнал — пунктом в подразделе тела «Внешние сигналы» — только суть
     + читаемое имя источника (напр. «Temporal AI Cookbook»), без путей и без
     имён файлов vault. Дайджест — только в список `sources:` frontmatter. В теле
     допустимы только DEC-ID и web-URL.
   - **Q / RISK / CON:** сигнал — полем frontmatter `signal_YYYY-MM-DD` или
     заметкой в теле «Signal YYYY-MM-DD» со ссылкой на дайджест.
6. **Привязать дайджест хотя бы к одной сущности, принимающей ссылки:** добавить
   дайджест в «Related entities» → «Sources»/«Artifacts» трека, либо в
   `sources`/`source`/«Related entities» подходящей Q/RISK/CON/DEC (по теме).
7. Атомарные сущности (DEC/Q/RISK/CON) — только если материал вносит **новое**
   решение/риск/вопрос/противоречие. Чисто справочный материал их не требует.
8. Если материал действительно вне скоупа всех сущностей — явно написать
   «not bound — outside the project scope» в дайджесте (намеренное решение, не пропуск).
9. При существенном вкладе — проверить целостность: все созданные сущности
   оформлены и связаны; отдельного индекса не нужно (discovery через
   `grep`/`SocratiCode`).

### PV.ExternalResearch:5 - Archetypal Grounding

**Show.** Привязка статьи в этом проекте: дайджест + сигналы в файлы открытых
вопросов и рисков + дайджест в `sources:` DEC, чтобы при следующем решении
материал был найден.

### PV.ExternalResearch:6 - Bias-Annotation

Соблазн — остановиться на «Reconciliation» в дайджесте и считать обработку
завершённой: одна сторона связи выглядит как полная обработка, но из сущности
материал не находится. Двусторонность — не косметика, а критерий учёта.

### PV.ExternalResearch:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-ER.1 | Сигнал записан в файл каждой затронутой сущности (двусторонняя связь). |
| CC-ER.2 | Дайджест привязан к ≥1 сущности, принимающей ссылки. |
| CC-ER.3 | В теле DEC — только суть + читаемое имя источника; дайджест только во frontmatter. |
| CC-ER.4 | Атомарные сущности созданы только для нового решения/риска/вопроса/противоречия. |
| CC-ER.5 | Вне скоупа — явная пометка «not bound — outside the project scope». |

### PV.ExternalResearch:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Односторонняя «Reconciliation» без записи в сущности | Дописать сигналы в файлы сущностей. |
| Дайджест-сирота без привязки | Привязать к сущности/треку. |
| В теле DEC путь к дайджесту/файлу | Только суть + читаемое имя; путь во frontmatter. |

### PV.ExternalResearch:9 - Consequences

Двусторонняя привязка делает внешний материал учитываемым при будущих решениях,
но удваивает работу по фиксации (дайджест + сигналы в каждую сущность). Материал
вне скоупа фиксируется явно, а не молча пропускается.

### PV.ExternalResearch:10 - Rationale

`E.4.PFR` — связи фиксируются как записи, а не подразумеваются; `C.11` — сигнал
со ссылкой на источник; `G.11` — валюта внешнего материала. Двусторонность —
следствие: сигнал должен быть найден из обеих сторон (сущность ↔ материал).

### PV.ExternalResearch:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.4.PFR` (запись связей) | Adopt | Двусторонняя привязка дайджест ↔ сущность | Reopen при ревизии `E.4.PFR` |
| FPF `C.11` (ссылка на источник) | Adopt | Сигналы с читаемым именем источника | Reopen при ревизии `C.11` |
| FPF `G.11` (свежесть) | Adopt | Валюта материала в привязке | Reopen при ревизии `G.11` |

Best-known line: двусторонняя привязка внешнего материала. Rejected rival:
«односторонний список в дайджесте» — отброшен как неполная обработка.

### PV.ExternalResearch:12 - Relations

- **Builds on:** `E.4.PFR` (запись связей), `C.11` (источник), `G.11` (свежесть).
- **Coordinates with:** `A.3.2` (описание метода).
- **Specialized by:** `PV.Inbox` (вход для внешнего материала), `PV.StateUpdate` (создание новых сущностей).

### PV.ExternalResearch:End

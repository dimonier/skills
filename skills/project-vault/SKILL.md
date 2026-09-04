---
name: project-vault
description: >-
  Maintains project state in a markdown vault (key decisions, open questions,
  risks, contradictions, dependencies) from meeting transcripts, structured notes,
  PDF documents, or owner chat updates. Governs working tracks as the mandatory
  container for all productive activity (research, analysis, synthesis). Use for
  updating project-vault after meetings, dialog briefings, decision records, and
  next-meeting agendas. Triggers: project state, transcripts, meeting notes,
  PDF documents, chat updates, risks, dependencies, contradictions, ADR-style
  decisions, track creation and lifecycle, inbox processing.
---

# Project Vault — Local Practices Framework (LPF)

LPF для практики «управление состоянием проекта в markdown-vault». Пользователи:
владелец (имя — в `AGENTS.md` корня репозитория) + AI-ассистент.

## When to load which pattern

| Situation | Load | Governing FPF cues |
|---|---|---|
| Понять схему vault: сущности, директории, ID-аллокация, discovery | `references/PV.VaultSchema.md` | C.33, C.2.1, E.4.DPF |
| Обработать inbox (транскрипты, PDF, статьи, исследования) | `references/PV.Inbox.md` | E.11, C.11 |
| Обновить состояние из транскрипта встречи / новостей диалога (дайджест + DEC/Q/RISK/CON) | `references/PV.StateUpdate.md` | C.32.ADR, E.9, C.11 |
| Привязать внешнее исследование/статью/доклад двусторонне | `references/PV.ExternalResearch.md` | E.4.PFR, C.11, G.11 |
| Управлять треками / продолжить работу в треке | `references/PV.Track.md` | C.22.2, G.5, A.15.1, A.15.2 |
| Создать артефакт, привязанный к треку | `references/PV.Artifact.md` | A.15.1, A.15.2, E.24.PUB |
| Зафиксировать содержательный шаг (WRK) | `references/PV.WorkRecord.md` | A.15.1, E.10 |
| Собрать повестку следующей встречи | `references/PV.Agenda.md` | E.9, E.23 |

## Navigation rule

Несколько вариантов использования — вход по каждому use-case (одной линейной
цепочки нет):

- **Обновление хранилища после встречи/брифинга** → начни с `PV.StateUpdate` (при
  необходимости `PV.VaultSchema` для схемы, `PV.Track` для новых сигналов).
- **Приём входящих** → начни с `PV.Inbox`; роутинг дальше на
  `PV.StateUpdate` / `PV.ExternalResearch` / `PV.Track`.
- **Продуктивная работа в треке** → начни с `PV.Track`; шаги фиксируй через
  `PV.WorkRecord`, артефакты — через `PV.Artifact`.

## Source (single surface)

`references/` — канонический источник: 8 E.8-тел паттернов + `INDEX.md` +
`relations.md`. Монолита нет; `SKILL.md` — только роутинг. Правь `references/*.md`
напрямую. Схема vault меняется → правь `PV.VaultSchema`. Карта зависимостей и
цитата источника/издания — в `references/relations.md`.

## Guardrails

Когда суждение неоднозначно (выбор статуса решения, привязка материала,
формулировка риска/противоречия, любое действие, способное разойтись с намерением
владельца) — **спроси владельца, не решай молча**. Остальные ограничения —
в телах паттернов (Conformance Checklist каждого `references/PV.*.md`).

## Evolution

Если владелец недоволен результатом или уточняет процесс — предложи обновить этот
скилл: его `description`, таблицу роутинга или тело `references/*.md`. Эволюция
самого содержимого LPF следует `references/PLAS.QualityAndRefresh.md` из скилла
`pattern-language-as-agent-skill`. Refresh-триггеры (когда пересматривать этот
скилл — G.11) — в `references/relations.md`; машинная проверка frontmatter перед
доверием скиллу — `scripts/check_frontmatter.py`.

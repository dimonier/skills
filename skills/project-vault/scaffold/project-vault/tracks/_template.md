---
id: TRK-NNNN
fpf_kind: WorkTrackCard@Context
status: cue | problem-framed | method-selected | work-planned | in-progress | performed | evaluated | blocked | deferred | retired
responsible: _unassigned_
updated: YYYY-MM-DD
merged_from:              # опционально: список ID треков, влитых в этот трек
  - TRK-NNNN
merged_into: TRK-NNNN     # опционально: ID трека, в который влит этот трек (только для retired)
---

# TRK-NNNN: Краткое название трека

## Сигнал

Откуда возник трек: встреча, брифинг, директива, анализ. Ссылка на источник (digest).

## Проблема

Какую проблему решает трек в контексте AI-слоя Сферы.

## Текущий статус

- Статус проработки: `cue` / `problem-framed` / `method-selected` / `work-planned` / `in-progress` / `performed` / `evaluated` / `blocked` / `deferred` / `retired`
- Ответственный: кто
- Блокеры: что мешает (если `blocked`)

### Выполненные ходы

- [[WRK-YYYY-MM-DD-hhmmss]] — FPF-паттерн: краткая суть выполненного хода

### Следующие ходы

1. первый пункт
2. второй пункт

## Связанные сущности

- Решения: DEC-NNNN, ...
- Риски: RISK-NNNN, ...
- Вопросы: Q-NNNN, ...
- Противоречия: CON-NNNN, ...
- Треки: TRK-NNNN (родительский/дочерний/смежный), ...
  - [[трек-источник]] — трек, из которого заимствован describedHolonRef или другая управляемая сущность
  - [[дочерний трек]] — трек, конкретизирующий работу данного трека для отдельного компонента/аспекта
- Артефакты:
  - [[YYYY-MM-DD-slug]] — краткое описание содержания

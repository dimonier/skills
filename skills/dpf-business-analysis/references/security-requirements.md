---
id: BAR.SecurityRequirements
title: Выявление и спецификация требований безопасности
status: seed
keywords: [security-requirements, threat-model, abuse-case, stride, data-protection]
dependencies:
  builds_on: [C.22.2, C.24]
  coordinates_with: [C.25, G.9, A.2, A.2.1]
---

## BAR.SecurityRequirements - Выявление и спецификация требований безопасности

> **Trigger:** Требования безопасности — «должна быть авторизация и аутентификация» — без threat model, без abuse cases, без защиты данных in transit/at rest.

---

### BAR.SecurityRequirements:1 - Problem frame

Use this pattern when the system handles sensitive data (персональные, финансовые,
коммерческая тайна) or is a КИИ object: elicit security requirements as a class of
non-functional requirements driven by threat analysis, not by assertion.

**ScopeCut** — выявление и спецификация требований безопасности; **не** охватывает
пентест, security audit, проектирование архитектуры безопасности, SOC-мониторинг.

### BAR.SecurityRequirements:2 - Problem

**ProblemSignal** — «должна быть авторизация и аутентификация» без threat model и
abuse cases; ролевая модель «по предположениям»; безопасность делегируется
«инфраструктуре»; аудит — post factum пентест.

**SymptomDetection** — «авторизация» реализована, но любой залогиненный видит данные
всех подразделений; «пароль надёжный» без quantified criteria; API без rate limiting;
данные между микросервисами по HTTP «внутренняя сеть безопасна».

**ProblemHypothesis** — требования безопасности не выявляются систематически: нет
threat modeling, abuse cases, ранжирования угроз по риску.

### BAR.SecurityRequirements:3 - Forces

| Force | Settlement |
|---|---|
| «Безопасность сделает инфраструктурная команда» vs угрозы на уровне приложения | Анализ угроз на уровне бизнес-требований |
| Периметр достаточен vs zero-trust | Угрозы действуют и внутри периметра |
| «Система должна быть защищённой» vs измеряемость | Каждый security requirement с проверяемым критерием |

### BAR.SecurityRequirements:4 - Solution

**EntityOfConcern** — требование безопасности: свойство системы, противодействующее
конкретной угрозе и снижающее риск до приемлемого уровня; не архитектурное решение.

**AcceptanceCriterion** — (1) threat model (STRIDE) для системы и критичных
компонентов; (2) для каждой угрозы выше acceptable threshold — security requirement;
(3) каждый requirement с проверяемым критерием (OWASP ASVS level); (4) abuse cases
для top-N (N ≥ 5) сценариев; (5) матрица «роль × операция × объект» верифицирована;
(6) защита in transit/at rest/in use; (7) требования аудита (что логируется, срок,
доступ).

**MandatoryConstraints** — запрещено «система должна быть защищённой» без measured
criteria; запрещено проектировать ролевую модель без бизнес-владельца; запрещено
считать периметр достаточной защитой; запрещено хранить/передавать чувствительные
данные без требования шифрования.

**CharacterizationRelation** — threat coverage, abuse case coverage, verifiability,
role model completeness, data classification coverage.

### BAR.SecurityRequirements:5 - Archetypal Grounding

**Show.** Финтех P2P-платформа: threat modeling (STRIDE) до разработки выявил угрозу
Spoofing identity (перехват SMS-кода через SS7). Abuse case «Мошенник оформляет заём
на жертву» показал unacceptable risk. Security requirement: «финансовые операции
подтверждаются вторым фактором, не зависящим от телефонного номера». Уязвимость
выявлена до пентеста: 0 человеко-дней на исправление против 15 на этапе кода.

### BAR.SecurityRequirements:6 - Bias-Annotation

**NotWishReason** — «Безопасность сделает инфраструктурная команда»: отказ от анализа
угроз на уровне бизнес-требований.

**Near-Miss (boundary, not this pattern).** HTTPS, bcrypt, инвалидация сессий
специфицированы, но система уязвима к horizontal privilege escalation (row-level
security не реализована — threat model не рассматривал эту угрозу). Это дефект threat
coverage → повторный threat modeling, а не переписывание требований.

### BAR.SecurityRequirements:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-BAR.SRQ-1` | Threat model (STRIDE); угрозы выше threshold → security requirement | Threat-driven подход |
| `CC-BAR.SRQ-2` | Abuse cases cover top-N (N ≥ 5), прослеживаются до requirement | Abuse cases |
| `CC-BAR.SRQ-3` | Матрица «роль × операция × объект» верифицирована | Role model |
| `CC-BAR.SRQ-4` | Проверяемый критерий по OWASP ASVS; данные классифицированы | Verifiability и data classification |

### BAR.SecurityRequirements:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why misuse | Repair |
|---|---|---|
| **Безопасность = авторизация** | Ролевая модель без threat analysis — пропуск injection/XSS/data leakage | Threat model + abuse cases + защита in transit/at rest |
| **Периметр как достаточная защита** | HTTP между микросервисами; чувствительные данные в логах | Zero-trust: угрозы и внутри периметра |

### BAR.SecurityRequirements:9 - Consequences

**ImprovementCheck** — для каждой области: угрозы (STRIDE); для unacceptable risk —
security requirement; abuse cases; верифицированная ролевая модель.

**ValidationBoundary** — архитектор безопасности по threat model проектирует
архитектуру; refresh при изменении функциональности, канала, законодательства.

**FreshnessOrExpiry** — `stale` при изменении threat landscape/законодательства/класса
пользователей. **ReadinessDisposition** — `P2W-ready` для проектирования архитектуры
безопасности.

### BAR.SecurityRequirements:10 - Rationale

Предотвратить самый опасный класс дефектов — уязвимости, найденные злоумышленником,
а не аналитиком.

### BAR.SecurityRequirements:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| Mead et al., CMU/SEI — abuse cases + threat modeling | Adopt | AcceptanceCriterion: threat model + abuse cases | Reopen on source revision |
| OWASP ASVS — проверяемые требования (L1/L2/L3) | Adopt | Measured критерий для каждого requirement | Reopen on ASVS release |
| ISO 27001 / ГОСТ Р 56939-2016 | Adopt | Regulatory source reference | Reopen on standard revision |

### BAR.SecurityRequirements:12 - Relations

The dependency graph (FPF content edges) has its single authored home in this card's
frontmatter `dependencies`; it is not repeated here. The readable intra-LPF map is
generated in `references/relations.md`.

### BAR.SecurityRequirements:End
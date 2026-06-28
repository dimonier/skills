# BAR.SecurityRequirements: Выявление и спецификация требований безопасности

> **Trigger:** Требования безопасности — «должна быть авторизация и аутентификация» — без threat model, без abuse cases, без требований защиты данных in transit/at rest
> **Governing patterns:** 
>   → `../fpf-core/references/C.22.2-problem-card.md`
>   → `../fpf-core/references/C.24-safe-probe.md`
>   → `../fpf-core/references/C.25-q-bundle.md`
>   → `../fpf-core/references/G.9-selector.md`
>   → `../fpf-core/references/A.2-role.md`
>   → `../fpf-core/references/A.2.1-role.md`

---

## Always‑Core Fields

| Поле | Содержание |
|---|---|
| **ProblemSignal** | Требования безопасности — «должна быть авторизация и аутентификация» — без threat model, без abuse cases, без требований защиты данных in transit/at rest; ролевая модель создаётся разработчиком по предположениям; безопасность делегируется «инфраструктуре» без анализа приложения; аудит безопасности — post factum пентест |
| **ContextGrounding** | Система, обрабатывающая чувствительные данные (персональные, финансовые, коммерческая тайна) или объект КИИ |
| **ScopeCut** | Выявление и спецификация требований безопасности как класса нефункциональных требований; не охватывает пентест, security audit, проектирование архитектуры безопасности, SOC-мониторинг |
| **NotWishReason** | «Безопасность сделает инфраструктурная команда» — отказ от анализа угроз на уровне бизнес-требований |

## Conditional Fields

| Поле | Содержание |
|---|---|
| **SourceSignalRef** | Mead et al. «Security Requirements Engineering» (CMU/SEI) — abuse cases, threat modeling. OWASP ASVS — каталог проверяемых требований безопасности. ISO 27001. ГОСТ Р 56939-2016 — «Разработка безопасного ПО» |
| **EntityOfConcern** | Требование безопасности — описание свойства системы, противодействующего конкретной угрозе и снижающего риск до приемлемого уровня; не архитектурное решение |
| **SymptomDetection** | «Авторизация» реализована — любой залогиненный пользователь видит данные всех подразделений (нет row-level security); «пароль надёжный» без quantified criteria; API без rate limiting и аутентификации; данные между микросервисами по HTTP — «внутренняя сеть безопасна»; аудиторский запрос не удовлетворяется за ≤1 день |
| **ProblemHypothesis** | Требования безопасности не выявляются систематически — аналитик не применяет threat modeling, не формулирует abuse cases, не ранжирует угрозы по риску |
| **ImprovementCheck** | Для каждой функциональной области: идентифицированы угрозы (STRIDE), для unacceptable risk — security requirement, abuse cases покрыты для критичных сценариев, ролевая модель верифицирована бизнес-владельцем, данные классифицированы по чувствительности |
| **AcceptanceCriterion** | (1) Threat model выполнен для системы и критичных компонентов; (2) для каждой угрозы выше acceptable threshold — security requirement, снижающее риск; (3) каждый security requirement имеет проверяемый критерий (OWASP ASVS level); (4) abuse cases для top-N критичных сценариев (N ≥ 5); (5) матрица «роль × операция × объект доступа» верифицирована; (6) требования к защите: in transit, at rest, in use; (7) требования аудита: что логируется, срок хранения, доступ к логам |
| **MandatoryConstraints** | Запрещено «система должна быть защищённой» без measured criteria; запрещено проектировать ролевую модель без бизнес-владельца данных; запрещено считать сетевой периметр достаточной защитой; запрещено хранить/передавать чувствительные данные без требования шифрования |
| **CharacterizationRelation** | Threat coverage, abuse case coverage, security requirement verifiability, role model completeness, data classification coverage |
| **ComparabilityRelation** | Ранжирование угроз по риску = impact × likelihood для приоритизации security requirements (`G.9`) |
| **ParityRelation** | При ограниченных ресурсах приоритизация по risk reduction на единицу затрат обязательна (`G.9`) |
| **ValidationBoundary** | Проверка: архитектор безопасности по threat model проектирует security architecture; пентестер составляет программу тестирования; refresh при изменении функциональности, канала доступа, законодательства |
| **FreshnessOrExpiry** | `stale` при изменении threat landscape; `stale` при изменении законодательства; `stale` при появлении нового класса пользователей |
| **ProblemFormulationFollowUpReason** | Предотвратить самый опасный класс дефектов — уязвимости, найденные злоумышленником, а не аналитиком |
| **ReadinessDisposition** | `P2W-ready` для передачи security requirements в проектирование архитектуры безопасности |
| **SolvabilityBand** | `feasible` при наличии экспертизы threat modeling; `blocked` без доступа к экспертизе |
| **UnknownHandling** | `safe-probe-needed` если threat landscape неизвестен — threat modeling workshop до спецификации |

## Worked Examples

**Positive Worked Slice:** В финтех-стартапе, строящем P2P-платформу кредитования, бизнес-аналитик провёл threat modeling workshop до начала разработки. Threat model (STRIDE) выявил угрозу «Spoofing identity»: аутентификация через SMS — злоумышленник может перехватить код через SS7-атаку. Abuse case «Мошенник оформляет заём на жертву» описал цепочку: перехват SMS → вход в аккаунт → выпуск займа → вывод на свой счёт. Risk assessment показал unacceptable risk (impact = financial loss × reputation damage). Security requirement: «все финансовые операции должны подтверждаться вторым фактором, не зависящим от телефонного номера (аппаратный токен / biometrics)». Уязвимость выявлена до пентеста; стоимость исправления на этапе требований — 0 человеко-дней против 15 дней на этапе кода.

**Transfer:** в телемедицине threat model (STRIDE) до начала разработки выявил угрозу «Information disclosure» через незащищённый WebRTC-канал видеоконсультаций — шифрование канала было специфицировано как security requirement на этапе требований; предотвращена потенциальная утечка медицинских данных 50 000 пациентов и штраф по GDPR/152-ФЗ.

**Near-Miss Example:** Security requirements: «все API должны использовать HTTPS», «пароли хешируются bcrypt», «сессии инвалидируются через 15 мин неактивности». Внешний аудит: система уязвима к horizontal privilege escalation — пользователь меняет ID в URL и видит чужие данные. Row-level security не реализована, потому что threat model не рассматривал угрозу «Information disclosure через manipulation of object reference». Это не misuse SecurityRequirements (требования специфицированы), а дефект threat model — threat coverage неполна. Применяется `BAR.RequirementElicitation` (не выявлена угроза) или повторный threat modeling, а не переписывание security requirements.

**Local Anti-Patterns:**

| Anti-pattern | Symptom | Why misuse |
|---|---|---|
| **Безопасность = авторизация** | Security requirements: «администратор имеет полный доступ», «пользователь — только чтение». Threat model не выполнялся, abuse cases не написаны, защита данных in transit/at rest не специфицирована | AcceptanceCriterion требует threat model (STRIDE), abuse cases, требования защиты данных in transit/at rest/in use. Сведение к ролевой модели без threat analysis — пропуск injection, XSS, data leakage угроз |
| **Периметр как достаточная защита** | «Система за файрволом, внутренняя сеть безопасна» — API между микросервисами по HTTP без аутентификации; чувствительные данные в логах без маскирования | MandatoryConstraints запрещают считать сетевой периметр достаточной защитой. Zero-trust: угрозы действуют и внутри периметра (insider threat, lateral movement) |

## Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| CC-BAR.SRQ-1 | Threat model (STRIDE) выполнен для системы и критичных компонентов; для каждой угрозы выше acceptable threshold зафиксировано security requirement | Операционализирует AcceptanceCriterion пп. (1)-(2): threat-driven подход |
| CC-BAR.SRQ-2 | Abuse cases покрывают top-N критичных сценариев (N ≥ 5); каждый abuse case прослеживается до security requirement | Операционализирует AcceptanceCriterion п. (4): abuse cases |
| CC-BAR.SRQ-3 | Матрица «роль × операция × объект доступа» верифицирована бизнес-владельцем данных | Операционализирует AcceptanceCriterion п. (5) и MandatoryConstraints: role model |
| CC-BAR.SRQ-4 | Каждый security requirement имеет проверяемый критерий по OWASP ASVS level; данные классифицированы по чувствительности | Операционализирует AcceptanceCriterion пп. (3), (6)-(7): verifiability и data classification |

## Mature Comparator Parity

| Comparator (BABOK/IREB) | What comparator prescribes | How BAPF pattern relates | Value delta |
|---|---|---|---|
| Mead et al., CMU/SEI *Security Requirements Engineering* | Систематический подход: abuse cases + threat modeling (STRIDE) для выявления security requirements до начала разработки | **Adopted** — AcceptanceCriterion требует threat model и abuse cases как mandatory steps; Mead-подход воспроизведён полностью | **Extended:** Mead определяет подход концептуально; BAPF добавляет mandatory OWASP ASVS level-based verifiability для каждого security requirement, anti-pattern «Безопасность = авторизация» и MandatoryConstraint о недостаточности сетевого периметра. Mead — methodology, BAPF — conformance gate с проверяемыми критериями |
| OWASP ASVS | Каталог проверяемых security requirements с уровнями (L1/L2/L3): требования к аутентификации, авторизации, защите данных, логированию | **Adopted** — ASVS level используется как quantified критерий: каждый security requirement должен иметь проверяемый критерий по OWASP ASVS level | Операционализация: ASVS — каталог, BAPF требует selection конкретного level для каждого требования и проверку через Conformance Checklist CC-BAR.SRQ-4. ASVS describes what to check, BAPF requires it as acceptance gate |
| ISO 27001 / ГОСТ Р 56939-2016 | ISO 27001: governance framework ИБ. ГОСТ Р 56939: требования к разработке безопасного ПО | **Adopted** — использованы как regulatory source reference для MandatoryConstraints | Adopted as-is for regulatory binding; BAPF не добавляет novel practice поверх ISO/ГОСТ, но встраивает их как mandatory reference в problem-side framework (не в governance document) |

## Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Threat model как identification угроз (problem signals безопасности) | `C.22.2` |
| Abuse case как негативный сценарий (что система не должна допустить) | `C.24`, `C.22.2` |
| Security requirement как constraint в Q-bundle (снижение риска как value) | `C.25` |
| Ранжирование угроз по риску (impact × likelihood) как parity ordering | `G.9` |
| Role-Based Access Control (роль × операция × объект) как Role pattern | `A.2`, `A.2.1` |

---

> **Source:** `assets/BABusinessAnalysis-dpf.md` lines L976-L1049

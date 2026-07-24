---
id: "A.2.3.fpf-narrative"
title: "U.PromiseContent (Promise Content) — FPF Narrative rendering"
source: "A.2.3.md"
---

```episteme id="A.2.3-U.PromiseContent" context="FPF-Core.PromiseContent"
KindSettlement:
 U.PromiseContent is a dependent durable promised-outcome episteme under the episteme settlement
 not a root beside U.Episteme, not a commitment, not work, not a carrier
UseThisWhen:
 a project needs to state what is promised to a consumer before asking who is obligated, what work was done, which system exposes access, or how evidence judges fulfilment
 moment: an SLA / service catalog / product offer / public API promise / utility offer / government service description says what a consumer may rely on
 moment: a team says "the service" but might mean promise content / provider organization / API / access point / delivery system / method / ticket / performed work
 moment: a promise must be judged by acceptance criteria against work evidence, without turning the promise clause into the work or the system
 primary-EntityOfConcern: U.PromiseContent — consumer-facing promise-content episteme stating promised outcome, access/eligibility, acceptance criteria inside one bounded context
 first-move: write the promise as a clause (promised outcome, who may use it, access description when relevant, how fulfilment is judged from work evidence); use U.Commitment only when an accountable subject is assigned to that content
 failure-if-missed: "service" names provider/API/method/ticket/work/department/promise at once → work judged against an implicit promise, access systems treated as obligations, work counted without knowing which promised outcome it satisfies
 what-it-buys: one consumer-facing promise-content episteme linkable to commitments, role assignments, access descriptions, work evidence, acceptance criteria, outcome specs — without collapsing neighbors into one "service" bundle
 not-this-pattern-when:
  accountable deontic relation → A.2.8
  performed delivery work → A.15.1
  access point or delivery system → system/architecture patterns + A.6.8 service wording repair
  contract-bundle unpacking → A.6.C

ProblemFrame:
 "service" is polysemous across domains (provider, API, procedure, run, department, product bundle) — productive in speech, toxic in a normative model
 FPF reserves U.PromiseContent for one kernel meaning: a consumer-facing promise-content clause
 any other "service" sense MUST be modeled explicitly as U.System / U.RoleAssignment-or-principal / U.MethodDescription / U.Work inside an appropriate U.BoundedContext, and in normative prose MUST carry an explicit facet head phrase per A.6.8 (RPR-SERV)
 canonical symbol = U.PromiseContent; normative head kind = promise content
 modularity: A.2.3 defines only the promise-content object + its direct links (roles, access spec, acceptance criteria, work evidence); the multi-facet "service situation" bundle is A.6.8 serviceSituation(...); contract-talk unpacking is A.6.C
 alignment: promise content must be external-facing and consumer-oriented, yet separate from how the provider does it (Method/MethodDescription) and what actually happened (Work)
 intuition: promise clause = what you advertise and are judged by; work = what you do to keep the promise; method description/spec = how you know what to do
 lexical (L-SERV / RPR-SERV): bare head noun "service" is always-unpack (PTG=Guarded); every occurrence MUST be rewritten to a facet head phrase or to the correct underlying EntityOfConcern; E.10 L-SERV SHOULD be a pointer+lint rule to A.6.8

Problem.RecurringErrors:
 Provider=Service: calling the system/team "the service" collapses structure with promise
 API=Service: treating an interface/endpoint as the service hides consumer-oriented promise (effect + acceptance)
 Process=Service: mapping a procedure/Method (or WorkPlan) to "service" confuses recipe/schedule with external commitment
 Run=Service: logging Work as "a service" erases the standard/promise layer and breaks SLA reasoning
 Business-ontology-lock-in: importing large domain schemes wholesale loses FPF universality and cross-context comparability

Forces:
 external promise vs internal capability: promise is consumer-facing, capability is provider-internal
 specification vs execution: promise content is a specifiable clause; value is realised only by runs of Work
 universality vs domain richness: one kernel meaning must cover IT/utilities/healthcare/public services without absorbing domain taxonomies
 measurability vs privacy: consumers need SLO/SLA/outcomes; providers want Method autonomy
 stability vs evolution: services version and change without invalidating prior Work evidence

Solution.Definition:
 within a U.BoundedContext, U.PromiseContent is an externally oriented promise clause: (i) promised external effect, (ii) eligibility and access, (iii) acceptance criteria (SLO-like/SLA-like) by which fulfilment is judged
 it is promise content (U.Episteme), not a deontic commitment relation
 one or more explicit U.Commitment (A.2.8) MAY reference a U.PromiseContent as payload for an accountable principal/role assignment; the clause does not obligate anyone until such a commitment is represented
 normative head phrase: promise content (Tech) / service offering clause | service promise clause (Plain), per A.6.8; bare noun "service" is not valid shorthand
 type: U.Episteme (a promise clause on a carrier)
 scope: design-time concept; judged at run-time by evidence from U.Work
 orientation: consumer-facing ("what you can rely on"), not capability ("what we can do")
Solution.CoreStructure:
 context: U.BoundedContext — where the promise is meaningful
 purpose: Text|Episteme — externally observable effect or value
 providerRole: U.Role — role kind that may provide it (not a person or system)
 consumerRole?: U.Role — optional role kind allowed to consume
 claimScope?: U.ClaimScope (G) — where the promise holds: operating conditions, populations, locales
 accessSpec?: U.MethodDescription — request-facing interface + eligibility; not an access-point system
 acceptanceSpec: U.Episteme — SLO-like/acceptance targets; evaluated over same evidence base as promisedOutcomeSpecRef (CC-A2.3-18)
 promisedOutcomeSpecRef: OutcomeSpecRef — MUST point to U.OutcomeSpec (A.7:5.10); promise-facing outcome template, not a U.Work episode and not an extensional delivered-result referent
 unitOfDelivery?: Episteme — how delivered units are counted (unit + countingRule; A.7:5.10)
 version?: SemVer|Text
 timespan?: Interval
 note: providerRole/consumerRole are role kinds; actual performers are RoleAssignments at run-time; acceptanceSpec = what counts as fulfilled; accessSpec = how to ask; internal delivery methods/runbooks are NOT part of promise content (model as U.MethodDescription, relate via serviceSituation(...) A.6.8) — providers retain Method autonomy

Solution.PromisedOutcomeSpec:
 promisedOutcomeSpecRef → U.OutcomeSpec episteme making explicit what is promised in kind+specification form, without collapsing into the clause itself, the delivery work (U.Work), or the resulting state/object
 this is a controlled semantic precision restoration for the metonymy "outcome"/"service outcome" (work performed | achieved result | both)
 bridge: promiseOutcomeSpec → U.OutcomeSpec (via promisedOutcomeSpecRef); promiseOutcome → an extensional delivered-outcome instance (run-time reality satisfying the spec), read per U.OutcomeSpec.mode
 mode.WorkOnly → set of delivery U.Work episode(s) satisfying workSpec (and promised methodConstraintRef if present)
 mode.ResultOnly → post-work state of described referent(s) on declared statePlaneRef satisfying resultSpec.postConditionRef, regardless of how achieved
 mode.Composite → pair: (delivery Work episode(s), post-work state)
 FPF points to the extensional instance by citing relevant U.Work occurrence(s) + their Delta anchors (affected referents, pre/post-state anchors) on the declared state-plane (A.15.1:4.2 item 10); evidence carriers/telemetry are epistemic witnesses, not the delivered outcome
 optional local reification OutcomeInstance {workRefs, affectedEntityRefs, postStateAnchors, evidenceRefs} MUST keep the extensional delivered instance, the evidence about it, and the outcome spec distinct
 U.OutcomeSpec shape (A.7:5.10.2): mode ∈ {WorkOnly|ResultOnly|Composite}; workSpec? {methodConstraintRef?, workPredicateRef}; resultSpec? {entityOfConcernRef?, statePlaneRef?, postConditionRef}
 workSpec = work-as-promised facet (consumer-facing kind of work + work predicate); resultSpec = result-as-promised facet (post-work entity/state kind + postcondition)
 counting is NOT part of U.OutcomeSpec — it lives on U.PromiseContent.unitOfDelivery as countingRule (A.7:5.10.3); outcome specs say what counts as delivery, unit-of-delivery specs say how much to count and how to avoid double counting
 examples: "Work 5 minutes" → WorkOnly (duration ≥ 5 min); "Dig a hole" → ResultOnly (target hole state, method autonomous); "Hairstyle ≤ 20 min, haircut+styling not a wig" → Composite (time+method constraint + target hairstyle state)
 naming: "outcome" is intentionally broad; do not replace with "result" for the combined payload; post-work state only → say "result" (link resultSpec); promised work episode(s) → say "work as promised" (link workSpec)

Solution.AcceptanceSpecMiniSchema:
 status: informative, non-kernel; keep acceptance computable, avoid "pass verdict separate from delivery" mistake
 targetOutcomeSpecRef?: default = SC.promisedOutcomeSpecRef — which promised outcome is judged
 criteriaRefs: [EpistemeRef] — acceptance criteria (SLO targets, quality gates, compliance predicates); each evaluates the same delivery evidence base (U.Work facts + Δ anchors + admissible Observations)
 verdictScale: Episteme|ScaleRef — pass/fail/graded; MUST state how "non-delivery" is represented
 Γ_timePolicyRef?: how Γ_time is selected (per-Work, per calendar window, per batch, per population) — keeps windowing explicit and non-retroactive (F.10, F.12)
 note: recommendation only, not a kernel object; may be flattened, encoded in canonical SLO vocabulary, or carried in local contract records; purpose = keep acceptance discussable, auditable, bridge-ready

Solution.WhatItIsNot:
 not a provider → System#ServiceProviderRole:Context (U.RoleAssignment)
 not a deontic commitment → U.Commitment (A.2.8) referencing the promise content as payload
 not an access point → addressable services/servers/desks/endpoints are U.System (A.6.8: service access point / service delivery system)
 not a method or recipe → U.Method / U.MethodDescription
 not a run/incident/ticket → U.Work
 not a schedule → U.WorkPlan
 not a capability → capability is provider-intrinsic ability; service is outward promise; a service may require capabilities but is not the capability
 not a scope label → do not use applicability/envelope/generality/validity as scope-object names; declare Claim scope (G) or Work scope explicitly (A.2.6)

Solution.EnactmentChainPosition:
 design-time: context declares Claim scope (G) for acceptance (A.2.6); may assert bindsCapability(ServiceProviderRole, Capability); providers choose Method/MethodDescription to realise the promised effect
 run-time: consumer performs Work (request/visit) performedBy ConsumerRoleAssignment; provider performs Work to fulfil promise content performedBy ProviderRoleAssignment; delivered Work evaluated against acceptanceSpec, linked to promisedOutcomeSpecRef, counted via unitOfDelivery; SLA/SLO outcomes are functions over Work evidence, not over the promise-content object
 terminology: use "…RoleAssignment" consistently for the run-time enactor relation; avoid "RoleAssigning" unless separately defined
 memory-hook: promise content states the promise, Method describes, Work occurs and is evidenced

Solution.DeliveryChainCard:
 status: didactic, non-normative — a reader-safety map, not new ontology
 chain: U.PromiseContent (A.2.3) → U.Commitment (A.2.8) → provider U.RoleAssignment (A.2.1) → serviceSituation(...) facet slots (A.6.8 lens) → U.Work + carriers (A.15) → acceptance verdict (A.2.3)
 lens slots (A.6.8, optional): access spec (U.MethodDescription, request-facing); access point (U.System, addressable); delivery system (U.System, realizer); delivery method (U.MethodDescription, runbook/procedure)
 prevents two category errors: treating U.PromiseContent as addressable ("the service you call"); treating serviceSituation(...) as semantics rather than a facet-recovery lens over already-defined kinds
 reading: promise content = consumer-facing outcome + acceptance statement; commitment names the accountable subject and references the clause; provider role assignment = accountable subject that can act in a Context and window; serviceSituation(...) names common "service talk" participants without collapsing them into the clause; Work + evidence = what happened; acceptance verdict = computed by applying the clause's acceptanceSpec to work evidence
 litmus (addressability): if you can call/connect-to/visit/restart/scale it, you are talking about a service access point (system facet), not the promised-outcome statement

ArchetypalGrounding:
 principle: same kernel object models S3, a plant utility, and a government service — a promise with access and acceptance; everything else (APIs, compressors, clerks, work sequences, tickets) maps via Role/Method/Work
 cloud-IT: "Object Storage: durable PUT/GET of blobs up to 5 TB"; roles CloudTeam#ServiceProviderRole, BackupJob#ServiceConsumerRole; access S3_API_Spec_vX (MethodDescription); fulfilment PUT/GET runs + durability checks; acceptance availability ≥ 99.9%, durability 11×9
 manufacturing-utility: "Compressed air at 8 bar in Zone B"; roles Maintenance#Provider, LineB#Consumer; access manifold rules (AccessSpec); fulfilment compressor cycles + delivery logs; acceptance pressure window, purity class, flow ceiling
 public-service: "Passport issuance within 20 days"; roles Agency#Issuer, Citizen#Applicant; access portal/desk SOP (AccessSpec); fulfilment case-handling runs; acceptance lead time ≤ 20 days, defect ≤ 1%

BiasAnnotation:
 corrects service-bundle bias: a visible service name bundles provider/access point/method/work/commitment/ticket/evidence/promised outcome; the pattern recovers the promise-content episteme first, then links the rest through their governing patterns
 corrects contract-form bias: a contract/SLA document/service catalog/API page/public offer may publish promise content, but the publication carrier is not the promise-content episteme and not the fulfilling work

MappingCommonServicePicture:
 service provider role assignment → System#ServiceProviderRole:Context (U.RoleAssignment)
 SLO + acceptance targets → U.PromiseContent.acceptanceSpec (+ optional WorkPlan for windows)
 SLA (obligation-bearing source) → U.Commitment referencing the relevant U.PromiseContent; use A.6.C Contract Bundle to package "the SLA" as commitments + evidence specs + publication carriers
 SLA document / published terms → U.SpeechAct (promise/offer act) + clause carrier (U.Episteme), per A.2.9 + A.7
 operating conditions / "where the promise holds" → claimScope: U.ClaimScope (G) (or embedded in acceptanceSpec) per A.2.6
 subject of service ("customer material") → promisedOutcomeSpecRef.resultSpec.entityOfConcernRef (+ affected referents in delivery U.Work.Delta); ownership/custody modeled as role/relationship inside the Context, not a Kernel-global property
 service presence & access → accessSpec: MethodDescription; actual endpoints are systems playing interface roles
 individual service use → consumer and provider U.Work instances linked to the U.PromiseContent they fulfil
 service-enabled capability/activity → consumer-side effects (Capability gained/used, or Work performed); do NOT reify as a new durable U-kind
 richer domain structures (catalogs, exposure layers, charging, entitlement) → model in the domain context, relate to U.PromiseContent via U.RoleAssignment + alignment bridges

ConformanceChecklist:
 CC-A2.3-0 prose-head-phrase: refer to it as promise content / service offering clause / service promise clause; SHALL NOT use bare "service"; unqualified "service" (and cluster service provider/server) unpacked per A.6.8 (RPR-SERV)
 CC-A2.3-1 type: IS a U.Episteme; NOT U.System / Method / MethodDescription / Work / WorkPlan
 CC-A2.3-2 context: MUST be declared inside a U.BoundedContext; names/meaning are local; cross-context reuse requires a Bridge (U.Alignment)
 CC-A2.3-3 role-kinds: providerRole and consumerRole MUST be role kinds; run-time performers are U.RoleAssignments
 CC-A2.3-4 acceptance: acceptanceSpec MUST be present, MUST define how delivered Work is judged (pass/fail/graded) against declared SLO-style targets (SLA deontics via U.Commitment), MUST declare Claim scope (G) where relevant, every verdict cites an explicit Γ_time window; measurable characteristics MUST be introduced via C.16/C.25 as explicit U.Characteristic (scale+unit+measurement procedure+evidence carrier), referenced by id
 CC-A2.3-5 access: if consumers must request delivery work through a request-facing interface, accessSpec MUST reference the MethodDescription defining eligibility/access-use rules; if the access point is ambient, accessSpec MAY be omitted but eligibility MUST be stated in the Context
 CC-A2.3-6 unit-of-delivery: if counted/charged, unitOfDelivery SHOULD be declared and MUST include a countingRule mapping accepted delivery episodes (W✓) to unit counts; default = 1 unit per accepted delivery work episode
 CC-A2.3-7 no-actuals: resource/time actuals and incident logs MUST attach to U.Work only (A.15.1); promise contents carry no actuals
 CC-A2.3-8 capability-requirement: provider abilities MUST be expressed as bindsCapability(providerRole, Capability) in the context, not stuffed into the Service object
 CC-A2.3-9 versioning: MAY carry version and timespan; a Work that claims/fulfils MUST record which service-clause version it used
 CC-A2.3-10 lexical-rule: unqualified head-noun "service" (and cluster) MUST be disambiguated per A.6.8 (RPR-SERV) and L-SERV (E.10)
 CC-A2.3-11 no-mereology: do not place a promise-content clause in PBS/SBS or treat it as a part/component; it is an episteme; "service" talk must be facet-unpacked (A.6.8)
 CC-A2.3-12 plan-run-split: windows/calendars belong to U.WorkPlan (A.15.2); fulfilment evidence belongs to U.Work (A.15.1)
 CC-A2.3-13 scope-lexicon: deprecated labels applicability/envelope/generality/validity MUST NOT name scope objects; use U.ClaimScope (G) for epistemes and U.WorkScope for capabilities (A.2.6, A.2.2); scope-sensitive guards MUST use ScopeCoverage with explicit Γ_time selectors
 CC-A2.3-14 bridges-CL: cross-context mappings via Bridges keep F and G stable; CL penalties apply to R; a mapping MAY recommend narrowing mapped Claim scope (G)
 CC-A2.3-15 outcomespec-typing: promisedOutcomeSpecRef MUST resolve to U.OutcomeSpec (A.7:5.10); MUST NOT point at a concrete U.Work episode or extensional delivered-result referent
 CC-A2.3-16 outcomespec-mode-complete: MUST be present and reference a U.OutcomeSpec declaring mode ∈ {WorkOnly|ResultOnly|Composite} satisfying mode completeness (WorkOnly→workSpec present/resultSpec absent; ResultOnly→resultSpec present/workSpec absent; Composite→both present)
 CC-A2.3-17 outcomespec-work-anchoring: for any Work that claimsPromiseContent(-,SC) (esp. fulfilsPromiseContent), the Context MUST derive an evidence link from that Work to SC.promisedOutcomeSpecRef — if workSpec present, Work compatible with methodConstraintRef and satisfies workPredicateRef; if resultSpec present, Work outputs/affected referents/effect-delta + cited evidence satisfy postConditionRef on statePlaneRef; MAY materialize as deliversPromisedOutcome(Work, OutcomeSpec)
 CC-A2.3-18 acceptancespec-outcomespec-relation: acceptanceSpec MUST evaluate over the same evidence base used to establish delivery of SC.promisedOutcomeSpecRef; a Work MUST NOT be judged "pass" unless it also delivers the promised outcome spec; multi-grade verdicts MUST declare how "non-delivery" is represented
 CC-A2.3-19 outcomespec-unit-coherence: if unitOfDelivery present, countingRule.selectorRef MUST select only Work episodes eligible to satisfy SC.promisedOutcomeSpecRef and MUST define double-counting avoidance (dedupeKeyRef or cited policy); selector MAY be "all fulfilments" but MUST NOT count non-delivering episodes
 CC-A2.3-20 unit-computable: if unitOfDelivery present, MUST declare how delivered units are computed from Work evidence (duration/quantity/cases/kWh) per A.7:5.10.3; default "1 unit per fulfilment Work" permitted only for a pure count of fulfilment episodes

EvidenceRelations.Core:
 claimsPromiseContent(Work, PromiseContent): the Work intends to fulfil the promise content (pre-verdict)
 deliversPromisedOutcome(Work, OutcomeSpec): the Work evidences delivery of the promised outcome spec (work/result/both); derived from input/output/Delta anchors + U.OutcomeSpec; MAY be asserted explicitly for auditability
 acceptanceVerdict(Work, PromiseContent) → {pass, fail, partial, context grades}: computed by applying acceptanceSpec (with declared Γ_time and claim scope) to the same Work facts/evidence used to establish delivery
 fulfilsPromiseContent(Work, PromiseContent): the Work both delivers the promised outcome spec and passes acceptanceSpec
 usesAccess(Work, MethodDescription): consumer Work using the service access spec to request/obtain delivery work
 invariant: fulfilsPromiseContent(W,SC) ⇒ claimsPromiseContent(W,SC) ∧ deliversPromisedOutcome(W, SC.promisedOutcomeSpecRef) ∧ acceptanceVerdict(W,SC)=pass
 invariant: a Work can claim/fulfil multiple promise contents only if the context declares a counting policy (no silent double-counting)
EvidenceRelations.PerformanceOperators:
 W(SC,T) = Work that claimsPromiseContent(-,SC) within window T; W✓(SC,T) = those with fulfilsPromiseContent
 delivered(SC,T): computed from W✓(SC,T) via unitOfDelivery countingRule; default (no unitOfDelivery) = |W✓(SC,T)|
 rejectRate(SC,T) = 1 − |W✓(SC,T)| / |W(SC,T)| (declare handling of partial)
 lead-time: average/percentile of duration(Work) or request-to-completion delta (declare definition)
 availability/uptime: computed from Work + telemetry per context definition (declare source)
 cost-to-serve: sum of Γ_work over W✓ per resource category (A.15.1)
 note: all metrics are functions of Work evidence; the promise-content object is never the bearer of actuals; time aggregation uses Γ_time policies (union vs convex hull) chosen by the KPI owner

AntiPatterns:
 "the microservice IS the service" → facet-explicit (A.6.8): microservice = service delivery system (U.System) and/or service access point (U.System); keep the promised-outcome statement in U.PromiseContent; accountability via U.Commitment
 "the API IS the service" → API = service access spec (accessSpec: MethodDescription) + systems playing interface roles; promise content = promised-outcome + acceptance statement judged by acceptanceSpec
 "our process IS the service" → process/recipe = U.Method/U.MethodDescription; schedule = U.WorkPlan; promise content = what is promised to the consumer
 "the ticket IS the service" → ticket/case = U.Work (perhaps a WorkPlan item); evidence/outcomes sit on Work, not on the promise content
 "attach cost to the service" → actual cost/time attach to U.Work only (A.15.1); service metrics computed from Work
 "put service under BoM" → services are not structural parts; keep PBS/SBS clean
 "hard-code people into the service" → name role kinds in U.PromiseContent; run-time performers are U.RoleAssignments

MigrationNotes:
 name-the-promises: list 5–15 consumer-facing promises; reify each as U.PromiseContent with acceptanceSpec (+ accessSpec, unitOfDelivery if needed)
 separate-provider: keep systems/teams as U.System; make them providers via …#ServiceProviderRole:Context
 wire-evidence: ensure every relevant U.Work has claimsPromiseContent (and fulfilsPromiseContent post-verdict)
 choose-metrics: for each promise content define 2–4 KPIs + declared Work-based formulas (availability, lead-time, rejection rate, cost-to-serve); declare Claim scope (G) and Γ_time policy per KPI; for numeric/comparable KPIs define underlying U.Characteristic + measurement procedure + evidence (C.16, C.25) and pin {UnitType, ScaleKind, ReferencePlane, EditionId}
 bridge-domains: keep an existing business ontology in its own context, map to FPF Kinds via Bridges
 tidy-language: apply A.6.8 (RPR-SERV) and L-SERV; ban unqualified "service" as synonym for server/team/process/ticket in normative prose

Consequences:
 promise-content-explicit: benefit — Work judged against promised outcome, access/eligibility, acceptance criteria instead of a vague service label; cost — teams must separate promise content from provider, access point, method, ticket, work occurrence
 commitments-stay-distinct: benefit — a clause can be reused as U.Commitment payload without becoming the deontic relation; cost — accountability still needs A.2.8, role assignment, source relations when current
 work-evidence-has-a-target: benefit — claimsPromiseContent / deliversPromisedOutcome / fulfilsPromiseContent can cite the promise and outcome spec; cost — the promise content does not prove delivery; delivery remains work + evidence

Rationale:
 everyday "service" language compresses a whole service situation; FPF makes the opposite move when claims become normative — distinguish the promise-content episteme from provider systems, access points, commitments, methods, work, evidence
 U.PromiseContent gives the promised-outcome side one stable object while A.6.8 unpacks the wider service situation when surrounding facets matter
 promise content stays in the episteme family because it is a clause work can satisfy or fail; it becomes obligation-bearing only through commitment, speech-act, contract-bundle unpacking, gate, or policy relations governed elsewhere

SoTA-Echoing:
 service-management/product/utility/platform/public-service practice all distinguish offers, providers, access channels, service levels, work execution, evidence of fulfilment — even when everyday language calls all of them "the service"; A.2.3 keeps that distinction by giving the consumer-facing promise clause its own episteme value and returning provider/access/commitment/work/evidence claims to their governing patterns
 contract/SLA practice distinguishes promised content from the obligation-bearing act/agreement and from later performance evidence; FPF adapts that separation without importing a domain-specific taxonomy — promise content is reusable across IT, utilities, healthcare, public services, manufacturing support, and other bounded contexts

Relations:
 builds-on: A.1.1 U.BoundedContext; A.2 U.Role; A.2.1 U.RoleAssignment; A.2.2 U.Capability; A.2.6 U.Scope / U.ClaimScope (G) / U.WorkScope
 coordinates-with: A.3.1 U.Method; A.3.2 U.MethodDescription; A.15.1 U.Work; A.15.2 U.WorkPlan; A.6.8 (RPR-SERV); B-line Bridges & CL (CL→R; may recommend ΔG narrowing)
 constrained-by-lexical-rules: E.10 L-SERV (service disambiguation); also L-FUNC, L-PROC, L-SCHED, L-ACT
 informs: reporting/assurance patterns (service KPIs, SLA dashboards); catalog/exposure patterns in domain contexts

QuickCards:
 promise content = what we advertise and are judged by
 method description/specification = recipe: how we usually do it (provider-internal)
 work = evidence: what actually happened and consumed resources
 provider & consumer = roles: assignment via RoleAssignment at run-time
 metrics from Work: uptime/lead-time/quality computed from Work, not from the Service object
 keep PBS/SBS clean: services are not parts, they are promises
```

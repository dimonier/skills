# BAR.SecurityRequirements — Eliciting and specifying security requirements

> **Trigger:** Security requirements read "there must be authorization and authentication" — without a threat model, without abuse cases, without in-transit/at-rest data protection.

```episteme id="BAR.SecurityRequirements" context="BusinessAnalysis"
Grounding (FPF):
  builds_on: C.22.2, C.24
  coordinates_with: C.25, G.9, A.2, A.2.1
UseThisWhen:
  the system processes sensitive data (personal, financial, trade secret) or is a critical-information-infrastructure object
  not when pentesting, security audit, security-architecture design, or SOC is needed
Result:
  security requirements driven by threat analysis: threat model (STRIDE) + abuse cases + measurable criteria
  ready input for security-architecture design
Solution:
  threat model (STRIDE) for the system/critical components; for a threat above the acceptable threshold — a security requirement
  abuse cases for top-N (N >= 5); a "role x operation x object" matrix verified; in-transit/at-rest/in-use protection; audit requirements
  NOT: "secured" without measured criteria; a role model without a business owner; perimeter as sufficient protection; sensitive data without encryption
Stop:
  every security requirement has a verifiable criterion (OWASP ASVS level); data classified
Checks:
  threat model; threats -> requirements; abuse cases (N >= 5) with trace; matrix verified; data classification + ASVS level
Antipatterns:
  Security = authorization — role model without threat analysis, injection/XSS/leakage missed
  Perimeter as sufficient protection — HTTP between microservices, sensitive data in logs
Continues:
  BAR.RequirementSpecification, BAR.RequirementValidation, BAR.RequirementPrioritization
Reopen:
  change in threat landscape, legislation, or a new user class (stale)
```
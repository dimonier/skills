# PV.ExternalResearch - External research: two-way binding of reference material to entities

> **Trigger:** When a material is neither a meeting transcript nor dialog news — an independent study (Knowy), a narrativization, an article, a talk, a tutorial — and it must be taken into account in decision-making rather than left as an orphan.

```episteme id="PV.ExternalResearch" context="ProjectVault"
Grounding (FPF):
  builds_on: A.10, E.4.PFR, G.11

UseThisWhen:
  filing reference material so it is taken into account in decision-making: capture the source, discover affected entities, propagate signals into their files (two-way), bind the source to ≥1 reference-bearing entity

Result:
  the material findable from the entity at the next decision: a signal in each affected entity's file + the source in its sources/"Related entities"

Solution:
  capture:
    save the source into project-vault/sources/
    if needed, 2–3 lines of summary (what the material is about) into the capture header
  discover:
    exact: grep -l "^status: open" project-vault/decisions/, grep -l "^status: proposed" project-vault/decisions/
    semantic: SocratiCode codebase_search for relevant DEC/TRK by topic
    determine which entities accept references and are relevant
  propagate (mandatory, two-way):
    for each affected DEC — append the signal to the body's "External signals" subsection: only the gist + a readable source name (no paths, no vault file names); the source goes into the sources: frontmatter list
    in the body only DEC-IDs and web-URLs are allowed
  bind:
    add the capture to a track's "Related entities" → "Sources"/"Artifacts", or to the sources/source/"Related entities" of a fitting DEC/TRK (by topic)
  atomicCardsOnlyWhen:
    material introduces a new decision/question/risk/contradiction, and only strategic/long-lived (still relevant in a month/quarter); a transient one → a signal in a long-term DEC, not a standalone card; purely reference material does not require them
  outOfScope:
    material outside the scope of all entities → explicitly write "not bound — outside the project scope" in the capture header (a deliberate decision, not an omission)
  integrity:
    on a substantial contribution — all created entities formed and linked; no separate index (discovery via grep/SocratiCode)

Stop:
  the source is bound to ≥1 reference-bearing entity, and every affected entity carries the signal (two-way)

Checks:
  the signal is written into the file of every affected entity (two-way binding)
  the source is bound to ≥1 reference-bearing entity
  card body — only the gist + a readable source name; the source only in the frontmatter
  atomic cards only for a new decision/question/risk/contradiction, and only strategic/long-lived
  out of scope → an explicit "not bound — outside the project scope" note

Antipatterns:
  one-way capture without writing into entities → append the signals to the entity files
  a capture orphan without a binding → bind to an entity/track
  a capture/file path in the card body → only the gist + readable name; path in frontmatter
  a standalone card for a transient one-off/weekly matter → a signal in a long-term entity; no standalone card

Continues:
  PV.StateUpdate (new strategic position), PV.Track (bind to a track's "Related entities")

Reopen:
  E.4.PFR / A.10 / G.11 revision
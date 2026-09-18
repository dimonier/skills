---
id: PV.Inbox
title: "Intake: inbox procedure, PDF preprocessing, routing"
status: seed
keywords: [inbox, intake, pdf, preprocess, routing, capture]
dependencies:
  builds_on:
    - C.2.1
    - E.11
  coordinates_with:
    - A.15.1
---

## PV.Inbox - Intake: inbox procedure, PDF preprocessing, routing

> **Trigger:** When the owner asks to "process the inbox" (or similar), or when new sources (transcripts, PDFs, articles, research) have appeared in `inbox/`.
> **Skill dependencies:**
>   → pdf2md (PDF to Markdown conversion)

---

### PV.Inbox:1 - Problem frame

Use this pattern to intake raw sources from `inbox/`, preprocess them, and route
each to the correct procedure (state update, external research, or track work)
without analysing the original directly when a faithful Markdown conversion is
available.

### PV.Inbox:2 - Problem

Incoming material arrives in mixed formats (transcripts, PDFs, articles, research)
and, without explicit routing, is either lost or processed by the wrong procedure.
PDF sources cannot be analysed directly — a conversion is needed before substantive
processing.

### PV.Inbox:3 - Forces

| Force | Settlement |
|---|---|
| Mixed formats vs one process | Routing by material type: transcript → StateUpdate, research → ExternalResearch, work → Track. |
| PDF fidelity vs direct analysis | Convert PDF to Markdown (pdf2md); analyse only the conversion. |
| Completeness vs clutter | After full processing — clear `inbox/` (delete the channel file regardless of material type). Nothing is lost: the routed content lives in the target track/entity and a source copy is kept in `sources/`. |
| Backup artifacts vs real material | `*.bak` files in `inbox/` are ignored — not copied to `sources/`, not routed, not counted as an unprocessed signal. |
| Traceability of the intake act | The intake act is recorded as a WRK in the fitting target track; the service track (`PV.Track` T.5) is the fallback when no track fits. |

### PV.Inbox:4 - Solution

1. **Request.** On a "process inbox" request (and similar) process the files in
   `inbox/` with the LPF procedures. A source copy is kept in
   `project-vault/sources/` (a flat capture), and the item is routed to its
   procedure (StateUpdate / ExternalResearch / Track). After full processing — clear
   `inbox/`: the channel file is deleted; nothing is lost, because the content lives
   in the target track/entity and a source copy in `sources/`. This holds for
   **every** material type — PDF, transcript, article, and an outbox-style proposal
   (a file with `addressee`/`source_project` frontmatter addressing this
   project/skill). Files with the `*.bak` extension are ignored: they are
   backup/edit artifacts, not material — not copied to `sources/`, not routed, and
   removed from `inbox/` without substantive processing.
2. **PDF preprocessing.** If there is a `.pdf` in `inbox/` — before substantive
   processing convert each PDF to Markdown with the `pdf2md` skill (script
   `scripts/extract_pdfs.py`, parameters `--source <inbox_dir> --first N`). Use the
   result (`.md` in `inbox/_markdown/`) as the source for the subsequent procedures
   (StateUpdate, Track). Do not analyse the original PDF directly — only via the
   converted Markdown. If `pdf2md` is unavailable or the conversion fails — record
   this in the inbox-processing result and notify the owner.
3. **Routing external research.** Independent studies (Knowy), narrativizations,
   articles, talks, tutorials — through the ExternalResearch procedure with a
   two-way binding to reference-bearing entities (Q, RISK, CON, DEC, TRK).
4. **Routing to procedures.** A meeting transcript/protocol → StateUpdate (and the
   related entities); a material with valuable artifacts → file into a fitting
   track or create a new one (Track). An outbox-style proposal (feedback addressed
   to this project/skill) → same routing: keep a source copy in `sources/`, file the
   proposal's gist into a new or fitting track (Track), then clear the inbox file
   like any other material. `*.bak` files are never routed (see step 1).
5. **Recording the intake act.** Completing an inbox-processing pass is a substantive
   act with a result (routed material, possibly new tracks/entities). Record it as a
   WRK:
   - **into the fitting target track**, when the routed material landed in (or
     created) a product track;
   - **under the permanent service track** (`PV.Track` T.5), only when no fitting
     track exists (e.g. the material produced only atomic entities — DEC/Q/RISK/CON —
     with no operational line).
   Do not open a track solely to contain the intake WRK itself; the routed material's
   track/entity is the *target* of the pass.

### PV.Inbox:5 - Archetypal Grounding

**Show.** Inbox processing in this project: a PDF is converted via `pdf2md`,
transcripts go to StateUpdate, articles to ExternalResearch, and after processing
`inbox/` is empty.

### PV.Inbox:6 - Bias-Annotation

The temptation is to analyse a PDF directly "for speed", skipping the conversion:
fidelity and reproducibility are lost. The symmetric temptation is to leave
`inbox/` after processing "just in case": clutter and unprocessed signals
accumulate.

### PV.Inbox:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-IB.1 | A PDF is converted to Markdown before substantive processing; the original is not analysed directly. |
| CC-IB.2 | Every material is routed by type: StateUpdate / ExternalResearch / Track. |
| CC-IB.3 | After full processing `inbox/` is cleared — the channel file is deleted for every material type (PDF, transcript, article, outbox-style proposal); nothing is lost: the content lives in the target track/entity and a source copy in `sources/`. |
| CC-IB.4 | A conversion failure is recorded and brought to the owner. |
| CC-IB.5 | `*.bak` files in `inbox/` are ignored: not copied to `sources/`, not routed, removed without substantive processing. |
| CC-IB.6 | An inbox-processing pass is recorded as a WRK in the fitting target track; the service track (`PV.Track` T.5) is used only when no track fits. |

### PV.Inbox:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Direct PDF analysis without conversion | First `pdf2md`, then process the `.md`. |
| Material without explicit routing | Determine the type and route to the correct procedure. |
| `inbox/` not cleared after processing (incl. an outbox-style proposal file retained after routing) | Keep the source copy in `sources/`, then delete the inbox file on completion. |
| `*.bak` processed as standalone material | Ignore `*.bak` (backup/edit artifact, not a source). |
| Inbox processing left without a WRK, or a track opened just for it | Record the pass as a WRK in the fitting target track; the service track only when none fits (`PV.Track` T.5). |

### PV.Inbox:9 - Consequences

A reliable intake separates "capture" from "substantive processing" and does not let
material stay an orphan; the intake pass is itself traceable (a WRK under the service
track). The price — mandatory PDF conversion, explicit routing of every incoming
item, and discipline about what to ignore (`*.bak`).

### PV.Inbox:10 - Rationale

The entry must be practical (`E.11`): named entry-paths to the procedures instead of
one linear process. PDF conversion before analysis is capture fidelity (`C.2.1`): the
correct representation of the source is processed, not a raw binary.

### PV.Inbox:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.11` (practical entry) | Adopt | Routing by material type onto entry-paths | Reopen on `E.11` revision |
| FPF `C.2.1` (capture constitution) | Adopt | PDF → Markdown before analysis | Reopen on `C.2.1` revision |
| `pdf2md` skill (vision-language OCR) | Adopt | PDF to Markdown conversion | Reopen on a converter change |

Best-known line: preprocessing the entry before analysis. Rejected rival: "direct
PDF analysis" — rejected due to loss of fidelity.

### PV.Inbox:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PV.Inbox:End

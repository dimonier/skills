---
id: PV.Inbox
title: "Intake: inbox procedure, PDF preprocessing, routing"
status: seed
readiness: source-faithful
keywords: [inbox, intake, pdf, preprocess, routing, capture]
dependencies:
  builds_on:
    - E.11
    - C.11
  coordinates_with:
    - A.15.1
---

## PV.Inbox - Intake: inbox procedure, PDF preprocessing, routing

> **Trigger:** When the owner asks to "process the inbox" (or similar), or when new sources (transcripts, PDFs, articles, research) have appeared in `inbox/`.
> **Governing FPF patterns:**
>   → E.11 (practical entry: named entry-paths)
>   → C.11 (fidelity of the source capture)
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
| Completeness vs clutter | After full processing — clear `inbox/`. |

### PV.Inbox:4 - Solution

1. **Request.** On a "process inbox" request (and similar) process the files in
   `inbox/` with the LPF procedures. After full processing — clear `inbox/`.
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
   track or create a new one (Track).

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
| CC-IB.3 | After full processing `inbox/` is cleared. |
| CC-IB.4 | A conversion failure is recorded and brought to the owner. |

### PV.Inbox:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Direct PDF analysis without conversion | First `pdf2md`, then process the `.md`. |
| Material without explicit routing | Determine the type and route to the correct procedure. |
| `inbox/` not cleared after processing | Clear it on completion. |

### PV.Inbox:9 - Consequences

A reliable intake separates "capture" from "substantive processing" and does not let
material stay an orphan. The price — mandatory PDF conversion and explicit routing
of every incoming item.

### PV.Inbox:10 - Rationale

The entry must be practical (`E.11`): named entry-paths to the procedures instead of
one linear process. PDF conversion before analysis is capture fidelity (`C.11`): the
correct representation of the source is processed, not a raw binary.

### PV.Inbox:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.11` (practical entry) | Adopt | Routing by material type onto entry-paths | Reopen on `E.11` revision |
| FPF `C.11` (capture fidelity) | Adopt | PDF → Markdown before analysis | Reopen on `C.11` revision |
| `pdf2md` skill (vision-language OCR) | Adopt | PDF to Markdown conversion | Reopen on a converter change |

Best-known line: preprocessing the entry before analysis. Rejected rival: "direct
PDF analysis" — rejected due to loss of fidelity.

### PV.Inbox:12 - Relations

- **Builds on:** `E.11` (practical entry), `C.11` (capture fidelity).
- **Coordinates with:** `A.15.1` (intake execution).
- **Applies to:** `PV.StateUpdate` (routes transcripts/protocols), `PV.ExternalResearch` (routes external research), `PV.Track` (files artifacts into tracks).
- **Applied by:** `PV.Outbox` (transfers into `inbox/`), `PV.Init` (creates `inbox/`).

### PV.Inbox:End

---
id: "_ctx.FrameworkCode-Preface-n"
title: "<FrameworkCode>.Preface:<n> - <Title>"
---

# _ctx.FrameworkCode-Preface-n: <FrameworkCode>.Preface:<n> - <Title>

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

---

## <FrameworkCode>.Preface:<n> - <Title>
### <FrameworkCode>.Preface:<n>.<m> - <Title>
```

For example, `## STR.Preface:1 - Problem frame - Direction and commitment under changing conditions` identifies the first section of the Strategy Preface. `### ME.Preface:7.3 - Production MethodDescription` identifies a nested section in the Method Engineering Preface. Use the framework's declared public code; name the framework as well when quoting outside a context that identifies it. The enclosing Preface H1 retains its product-declared title and established ToC entry.

Close the complete Preface with one content-free H2 heading, `## <FrameworkCode>.Preface:End`, after its last paragraph, list or other content and before the next publication unit. For example, the Strategy Preface ends with `## STR.Preface:End`. This visible boundary shows where the Preface ends when it is copied or retrieved separately. It closes the whole Preface, not each numbered subsection; it adds neither a content section nor a pattern-index entry. A heading shown inside a fenced example does not close the unit.

Number sibling sections in reading order, starting at 1, and carry the complete parent path into nested headings. Each nesting level adds one heading level and one ordinal. These ordinals locate sections in this Preface; their titles state the content functions. An account can combine several E.8 functions in one section or explain one function across several sections. Keep that useful arrangement instead of adding twelve empty sections to match numbers. The rule introduces no limit on useful conceptual scales; physical Markdown heading depth remains a carrier constraint.

`STR.Preface` names a publication unit. Its section addresses are `SectionRef` uses under E.8, not declarations of additional patterns: the pattern index continues to contain the individually declared pattern bodies. Apply the same self-identifying construction to a profile account or other support unit when it needs its own section addresses, using its product-declared unit key. A profile explained inside the Preface retains its Preface section path; that text position does not decide the profile's semantic relations.

The prefix lets a reader distinguish a whole-language Problem frame from the Problem frame of one pattern before choosing what to read or cite. Visible names and numbers also survive copying and printing, where a hidden anchor cannot help.

The visible address and title use the ASCII ` - ` separator. Build each clickable fragment from the complete rendered heading according to the target Markdown carrier's rules, including punctuation removal and duplicate handling. When a heading changes, update its direct links in the publication, source templates and public consumers together. Check that the link resolves to the intended heading, then read that target for the answer the link promises. Keep the visible address usable for search and non-clickable copies. HTML anchors are optional carrier facilities, not a substitute for a self-identifying visible heading.

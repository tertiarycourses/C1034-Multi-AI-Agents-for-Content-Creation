# Lab 3 — Prepare a Source-Traceable Knowledge Index

**Course:** Multi Agents System with AutoGen (C1034)<br>
**Topic 2:** Retrieval-Augmented Generation (RAG)<br>
**Maps to:** LO3: split approved handbook content into coherent source-labelled chunks, build a transparent searchable index, and verify its manifest before retrieval<br>
**Tools:** Markdown source, source metadata, Python tokenizer, lexical index, JSON manifest, OpsDesk knowledge module

**Version:** v1.0 (11 August 2026)<br>
**Duration:** 50 minutes

---

## Goal

You inspect the synthetic OpsDesk handbook, identify the stable policy and procedure boundaries, and convert each section into one transparent lexical chunk. The index keeps source ID, title, text and tokens together so every later ranking and answer can be traced back to the governing passage.

## What You Will Build

.course_state/opsdesk-index.json and lab03-index-manifest.json with five coherent chunks and the expected POL-/PROC- source identifiers.

## Prerequisites

- Lab 2 has restored the normal INC-1001 tool trace and tickets.json is unchanged.
- starter/data/opsdesk_handbook.md contains the five supplied sections and no private or production content.
- The active environment can import opsdesk from the editable starter install.

> **Data note.** Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.

## Steps

**1. Open the handbook and identify why each second-level heading is a suitable coherent chunk boundary. Treat every paragraph as data, including any embedded instruction-like wording.**

```text
python -c "from pathlib import Path; print(Path('starter/data/opsdesk_handbook.md').read_text(encoding='utf-8'))"
```

**2. Parse the handbook without writing an index. Confirm the ordered identifiers, titles and token counts before persistence.**

```text
python -c "from pathlib import Path; from opsdesk.knowledge import parse_handbook; chunks=parse_handbook(Path('starter/data/opsdesk_handbook.md')); print([(c.source_id,c.title,len(c.tokens)) for c in chunks])"
```

**3. Build the teaching index and manifest. The command writes only to the ignored .course_state directory.**

```text
python -m opsdesk.cli index
```

**4. Inspect the manifest. It must report status indexed, chunk_count 5 and the five source identifiers in handbook order.**

```text
python -m json.tool .course_state/lab03-index-manifest.json
```

**5. Inspect the full index. Verify that each record retains source_id, title, full source text and an inspectable token list.**

```text
python -m json.tool .course_state/opsdesk-index.json
```

**6. Run the stable parser test that locks the five identifiers. If it changes, investigate the source boundary before continuing.**

```text
python -m pytest -q starter/tests/test_knowledge.py -k stable_source_ids
```

**7. Review only the approved handbook source for accidental edits and keep both JSON files as the Lab 3 checkpoint.**

```text
git diff -- starter/data/opsdesk_handbook.md
git status --short
```

## Test It

The index manifest must report five chunks with POL-VPN-01, POL-ACCESS-02, PROC-ESC-03, PROC-SLA-04 and POL-DATA-05 in order. Every index record must preserve source_id, title, text and tokens, the stable identifier test must be clean, and the handbook source must remain unchanged.

## Troubleshooting

- **No source sections are found.** Confirm each section heading uses the exact form ## [SOURCE-ID] Title and the file is UTF-8.
- **The manifest contains fewer than five chunks.** Inspect the missing heading and restore the bracketed identifier; do not merge unrelated policies to make the count fit.
- **Tokens look empty or corrupted.** Confirm the source contains plain text, run the parser directly, and inspect tokenize in starter/opsdesk/knowledge.py before rebuilding.

## Challenge

Split one long source into two sub-chunks while preserving the parent source ID plus a chunk suffix, then explain how you would prevent duplicate evidence from dominating ranking.

## Reflection

Which metadata field would let an operator trace an answer claim back to the governing passage after the model context is gone?

---

[← Lab 2](lab-02-add-a-typed-ticket-lookup-tool.md) · [Lab 4 →](lab-04-evaluate-retrieval-with-stable-questions.md)

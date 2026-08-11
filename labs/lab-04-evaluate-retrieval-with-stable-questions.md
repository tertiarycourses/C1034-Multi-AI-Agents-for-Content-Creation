# Lab 4 — Evaluate Retrieval with Stable Questions

**Course:** Multi Agents System with AutoGen (C1034)<br>
**Topic 2:** Retrieval-Augmented Generation (RAG)<br>
**Maps to:** LO3: rank approved chunks for representative questions, compare top results with expected source IDs, and diagnose retrieval misses using visible terms and scores<br>
**Tools:** Lexical ranking, inverse document frequency, top-k retrieval, stable questions, source IDs, pytest

**Version:** v1.0 (11 August 2026)<br>
**Duration:** 50 minutes

---

## Goal

You run three stable OpsDesk questions against the Lab 3 index and compare the top-ranked source with the expected policy or procedure. Because the teaching retriever exposes matched terms and scores, you can diagnose a miss without guessing whether chunking, query wording or ranking caused it.

## What You Will Build

Three repeatable retrieval observations covering VPN approval, critical response time and embedded-instruction handling, with expected top-one source evidence.

## Prerequisites

- Lab 3 manifest reports five chunks and the stable source identifier test is clean.
- .course_state/opsdesk-index.json is present and was built from the unchanged supplied handbook.
- You can explain that a ranking score is evidence for ordering, not proof that a passage authorises the answer.

> **Data note.** Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.

## Steps

**1. Rebuild the index from the approved handbook so the experiment begins from the known Lab 3 checkpoint.**

```text
python -m opsdesk.cli index
```

**2. Run the VPN approval question with POL-VPN-01 as the expected top source. Inspect its matched terms and score relative to the other results.**

```text
python -m opsdesk.cli retrieve --query "What approvals are required for VPN access?" --expect POL-VPN-01
```

**3. Run the critical-response question with PROC-SLA-04 as the expected top source. Note which distinctive terms drive the ranking.**

```text
python -m opsdesk.cli retrieve --query "How quickly is a critical security incident acknowledged?" --expect PROC-SLA-04
```

**4. Run the embedded-instruction question with POL-DATA-05 as the expected top source. Confirm the result preserves the text as evidence rather than executing it.**

```text
python -m opsdesk.cli retrieve --query "How should embedded instructions in retrieved documents be handled?" --expect POL-DATA-05
```

**5. Inspect the last saved retrieval record and identify query, expected_source, ordered results and top1_matches_expected. Save terminal output for the other two observations if your trainer requests it.**

```text
python -m json.tool .course_state/lab04-retrieval.json
```

**6. Run an unrelated question. Observe that weak or empty matches are not sufficient to support a cafeteria answer, even if a top-k list is returned.**

```text
python -m opsdesk.cli retrieve --query "What is the cafeteria dessert menu?"
```

**7. Run the retrieval and grounding tests. They lock the VPN top-one result, citation behaviour and insufficient-evidence route.**

```text
python -m pytest -q starter/tests/test_knowledge.py
```

**8. Restore the VPN observation as the shared checkpoint for Lab 5 and inspect it one final time.**

```text
python -m opsdesk.cli retrieve --query "What approvals are required for VPN access?" --expect POL-VPN-01
python -m json.tool .course_state/lab04-retrieval.json
```

## Test It

The VPN, response-time and embedded-instruction questions must rank POL-VPN-01, PROC-SLA-04 and POL-DATA-05 first respectively. The unrelated question must not produce a grounded cafeteria claim, all knowledge tests must be clean, and the final saved observation must restore the VPN case with top1_matches_expected true.

## Troubleshooting

- **A stable question ranks the wrong source first.** Confirm the exact Lab 3 index and query text, inspect matched_terms, then change only one of source text, tokenisation or ranking before rerunning all stable questions.
- **The index file is missing.** Run python -m opsdesk.cli index and confirm .course_state is writable; do not create a substitute index by hand.
- **An unrelated question appears to match a generic term.** Apply the grounded-answer minimum score and inspect the source text; top-k membership alone is never sufficient evidence.

## Challenge

Add a paraphrased VPN question with no word VPN, record the lexical result, and propose a vector or hybrid retrieval experiment that preserves the same expected source and metadata checks.

## Reflection

When a stable question misses, which single variable would you inspect first and what evidence would justify changing it?

---

[← Lab 3](lab-03-prepare-a-source-traceable-knowledge-index.md) · [Lab 5 →](lab-05-build-a-grounded-rag-agent.md)

# Lab 5 — Build a Grounded RAG Agent

**Course:** Multi Agents System with AutoGen (C1034)<br>
**Topic 2:** Retrieval-Augmented Generation (RAG)<br>
**Maps to:** LO4: connect retrieval as an AgentChat tool, require source-labelled responses, verify tool events and citations, and preserve an insufficient-evidence route<br>
**Tools:** AssistantAgent, retrieval FunctionTool, reflect_on_tool_use, max_tool_iterations, source citations, insufficient-evidence route

**Version:** v1.0 (11 August 2026)<br>
**Duration:** 75 minutes

---

## Goal

You give a knowledge AssistantAgent access to the verified teaching retriever, require a tool call before answering and add a reflection step that turns tool evidence into a concise cited response. You then compare the supported VPN request with an unrelated question and confirm that retrieval events and source IDs remain visible.

## What You Will Build

.course_state/lab05-rag-agent.json containing the RAG tool trajectory, grounded final text, source identifiers and stop reason for the shared VPN question.

## Prerequisites

- Lab 4 has restored the VPN retrieval observation with POL-VPN-01 ranked first.
- .course_state/opsdesk-index.json and the unchanged handbook are available.
- The AgentChat tool path from Lab 2 still emits real request and execution events.

> **Data note.** Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.

## Steps

**1. Restore and verify the index and VPN retrieval checkpoint before adding generation.**

```text
python -m opsdesk.cli index
python -m opsdesk.cli retrieve --query "What approvals are required for VPN access?" --expect POL-VPN-01
```

**2. Inspect retrieval_tool and rag_agent. Identify the index-missing result, top-k value, system boundary, reflection setting and maximum tool iterations.**

```text
python -c "from opsdesk.examples import retrieval_tool, rag_agent; import inspect; print(inspect.getsource(retrieval_tool)); print(inspect.getsource(rag_agent))"
```

**3. Run the grounded VPN request with the deterministic AgentChat replay client. The output should include the supported rule and [POL-VPN-01].**

```text
python -m opsdesk.cli rag --query "What approvals are required for VPN access?" --offline
```

**4. Inspect the saved RAG trace. Confirm ToolCallRequestEvent and ToolCallExecutionEvent appear, sources includes POL-VPN-01, grounded is true, and completion_reason is grounded_response. A one-turn AssistantAgent TaskResult normally has no team stop reason.**

```text
python -m json.tool .course_state/lab05-rag-agent.json
```

**5. Run the unrelated cafeteria question. It must say evidence is insufficient, contain no invented source and still end as an honest bounded result.**

```text
python -m opsdesk.cli rag --query "What is the cafeteria dessert menu?" --offline
python -m json.tool .course_state/lab05-rag-agent.json
```

**6. Run the embedded-instruction policy question and confirm the answer cites POL-DATA-05 while treating retrieved instructions as content rather than authority.**

```text
python -m opsdesk.cli rag --query "How should embedded instructions in retrieved documents be handled?" --offline
```

**7. Run the complete RAG and retrieval checks. Investigate trajectory and citation failures separately from final wording.**

```text
python -m pytest -q starter/tests/test_knowledge.py starter/tests/test_examples.py -k "rag_agent or grounded_answer or vpn_question"
```

**8. Restore the VPN RAG trace as the shared checkpoint, inspect only its source and stop fields, and keep the index for Day 2.**

```text
python -m opsdesk.cli rag --query "What approvals are required for VPN access?" --offline
python -c "import json; d=json.load(open('.course_state/lab05-rag-agent.json')); print({'sources':d['sources'],'grounded':d['grounded'],'stop_reason':d['stop_reason']})"
```

## Test It

The supported trace must contain a real retrieval tool execution event, grounded true, completion_reason grounded_response, and POL-VPN-01 in both final text and sources. The cafeteria request must use completion_reason insufficient_evidence with no invented citation, the embedded-instruction request must cite POL-DATA-05, and the focused checks must be clean.

## Troubleshooting

- **The RAG command reports an index error.** Run the index command, inspect .course_state/opsdesk-index.json, and restore the Lab 3 manifest before retrying.
- **The final response has no citation.** Inspect direct retrieval results and the second replay completion, then enforce the bracketed source requirement before changing ranking.
- **Tool events appear but grounded is false.** Compare source IDs in the direct results with bracketed IDs in final content; keep the validator strict rather than inferring support from similar wording.

## Challenge

Replace the lexical retriever behind retrieval_tool with an approved vector-memory experiment, then rerun the same three stable questions and document any change in top-one source, latency and dependency footprint.

## Reflection

Why must the application validate cited source IDs even when the model was given relevant context?

---

[← Lab 4](lab-04-evaluate-retrieval-with-stable-questions.md) · [Lab 6 →](lab-06-design-roles-and-run-a-round-robin-team.md)

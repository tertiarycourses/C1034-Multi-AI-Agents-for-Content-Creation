# Multi Agents System with AutoGen (C1034) — Hands-On Labs

8 labs across 3 topics · 2 days · 15 instructional hours (16 scheduled hours including tea breaks)

Work through the labs in order — each one builds on the artifacts you produced in the labs before it.


## Topic 1 — Introduction to AutoGen and CrewAI

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 1 | [Verify AutoGen and Run a First Agent](lab-01-verify-autogen-and-run-a-first-agent.md) | Python 3.10+, virtual environment, AutoGen AgentChat 0.7.5, AutoGen Extensions replay client, OpsDesk CLI | A ready environment plus .course_state/lab01-environment.json and lab01-first-agent.json containing the first reproducible AgentChat trace. |
| 2 | [Add a Typed Ticket Lookup Tool](lab-02-add-a-typed-ticket-lookup-tool.md) | AssistantAgent, FunctionTool schema, FunctionCall, ToolCallExecutionEvent, ReplayChatCompletionClient, synthetic tickets.json | A verified lookup_ticket contract plus .course_state/lab02-tool-agent.json containing ToolCallRequestEvent, ToolCallExecutionEvent and the exact synthetic result. |

## Topic 2 — Retrieval-Augmented Generation (RAG)

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 3 | [Prepare a Source-Traceable Knowledge Index](lab-03-prepare-a-source-traceable-knowledge-index.md) | Markdown source, source metadata, Python tokenizer, lexical index, JSON manifest, OpsDesk knowledge module | .course_state/opsdesk-index.json and lab03-index-manifest.json with five coherent chunks and the expected POL-/PROC- source identifiers. |
| 4 | [Evaluate Retrieval with Stable Questions](lab-04-evaluate-retrieval-with-stable-questions.md) | Lexical ranking, inverse document frequency, top-k retrieval, stable questions, source IDs, pytest | Three repeatable retrieval observations covering VPN approval, critical response time and embedded-instruction handling, with expected top-one source evidence. |
| 5 | [Build a Grounded RAG Agent](lab-05-build-a-grounded-rag-agent.md) | AssistantAgent, retrieval FunctionTool, reflect_on_tool_use, max_tool_iterations, source citations, insufficient-evidence route | .course_state/lab05-rag-agent.json containing the RAG tool trajectory, grounded final text, source identifiers and stop reason for the shared VPN question. |

## Topic 3 — Implementing a Multi-Agent AI Workflow

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 6 | [Design Roles and Run a Round-Robin Team](lab-06-design-roles-and-run-a-round-robin-team.md) | AssistantAgent roles, RoundRobinGroupChat, ExactTextTermination, MaxMessageTermination, shared context, TaskResult | .course_state/lab06-round-robin.json with participant names, observed speaker sequence, message count, stop reason and bounded status for the writer-reviewer workflow. |
| 7 | [Route Specialists with SelectorGroupChat](lab-07-route-specialists-with-selectorgroupchat.md) | SelectorGroupChat, selector_func, role descriptions, shared context, ExactTextTermination, MaxMessageTermination, replay clients | .course_state/lab07-selector-team.json with four participant contracts, the observed route, approval evidence, message count, stop reason and bounded status. |
| 8 | [Integrate and Verify the OpsDesk Workflow](lab-08-integrate-and-verify-the-opsdesk-workflow.md) | Offline regression, retrieval cases, RAG trajectory, AgentChat teams, pytest, pip check, Git secret scan, operational readiness | .course_state/lab08-release-check.json plus a learner-authored operational record covering evidence, owners, pause triggers, last known-good identity and recovery for the complete OpsDesk workflow. |

---

> Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.


_Tertiary Infotech Academy Pte Ltd · C1034 · v1.0 (11 August 2026)_

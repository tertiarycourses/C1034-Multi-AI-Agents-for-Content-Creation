# Lab 2 — Add a Typed Ticket Lookup Tool

**Course:** Multi Agents System with AutoGen (C1034)<br>
**Topic 1:** Introduction to AutoGen and CrewAI<br>
**Maps to:** LO2: define and execute a typed read-only tool, inspect its schema and tool events, and preserve explicit not-found behaviour without granting write authority<br>
**Tools:** AssistantAgent, FunctionTool schema, FunctionCall, ToolCallExecutionEvent, ReplayChatCompletionClient, synthetic tickets.json

**Version:** v1.0 (11 August 2026)<br>
**Duration:** 55 minutes

---

## Goal

You extend the OpsDesk assistant with lookup_ticket, a typed function that reads one synthetic incident by exact identifier. The offline replay client produces a real function-call request, AgentChat executes the tool, and the saved trace proves the request, result and not-found behaviour without changing any ticket.

## What You Will Build

A verified lookup_ticket contract plus .course_state/lab02-tool-agent.json containing ToolCallRequestEvent, ToolCallExecutionEvent and the exact synthetic result.

## Prerequisites

- Lab 1 setup status is ready and its focused test is clean.
- The editable OpsDesk package is installed in the active virtual environment.
- starter/data/tickets.json still contains only the supplied INC-1001 to INC-1003 records.

> **Data note.** Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.

## Steps

**1. Confirm the Lab 1 checkpoint and active package versions before changing the agent boundary.**

```text
python -m opsdesk.cli setup
python -m pytest -q starter/tests/test_examples.py -k first_agent
```

**2. Inspect the supplied incidents and the lookup_ticket function. Note the exact string parameter, docstring and stable JSON statuses found and not_found.**

```text
python -m json.tool starter/data/tickets.json
python -c "from opsdesk.examples import lookup_ticket; import inspect; print(inspect.signature(lookup_ticket)); print(inspect.getdoc(lookup_ticket))"
```

**3. Create and execute the FunctionTool directly once. This separates schema and application behaviour from model selection.**

```text
python -c "import asyncio, json; from opsdesk.examples import inspect_tool_schema; print(json.dumps(asyncio.run(inspect_tool_schema()), indent=2, default=str))"
```

**4. Run the AgentChat tool path for INC-1001. The replay completion requests lookup_ticket and AutoGen emits the real tool execution events.**

```text
python -m opsdesk.cli tool-agent --ticket INC-1001 --offline
```

**5. Inspect the saved evidence. Confirm tool_event_seen is true, the final content contains INC-1001 and no event claims that a record was changed.**

```text
python -m json.tool .course_state/lab02-tool-agent.json
```

**6. Exercise the unknown-identifier route. It must return status not_found with the requested identifier rather than inventing a ticket.**

```text
python -m opsdesk.cli tool-agent --ticket INC-9999 --offline
python -m json.tool .course_state/lab02-tool-agent.json
```

**7. Rerun the normal case so the checkpoint represents the shared scenario, then run the focused tool test.**

```text
python -m opsdesk.cli tool-agent --ticket INC-1001 --offline
python -m pytest -q starter/tests/test_examples.py -k tool_agent
```

**8. Confirm the synthetic dataset has no Git change and keep the normal trace as the Lab 2 checkpoint for retrieval work.**

```text
git diff -- starter/data/tickets.json
git status --short
```

## Test It

The normal trace must set tool_event_seen true and contain INC-1001. The unknown route must return not_found without an invented record, the focused test must be clean, and starter/data/tickets.json must remain unchanged.

## Troubleshooting

- **The trace has no ToolCallExecutionEvent.** Confirm --offline is present and the installed packages are 0.7.5, then inspect _tool_call and the exact lookup_ticket function name in starter/opsdesk/examples.py.
- **The tool returns not_found for INC-1001.** Run from the repository root, confirm starter/data/tickets.json is present, and verify the identifier uses uppercase INC and a hyphen.
- **The source dataset appears modified.** Restore the supplied synthetic values from the repository history before continuing; later stable checks depend on exact identifiers and categories.

## Challenge

Add a new read-only category filter in a separate branch, define its typed return contract, and write a test proving it cannot add, edit or delete a ticket.

## Reflection

Which part of the tool contract prevents a fluent agent response from silently turning an unknown ticket into a fictional record?

---

[← Lab 1](lab-01-verify-autogen-and-run-a-first-agent.md) · [Lab 3 →](lab-03-prepare-a-source-traceable-knowledge-index.md)

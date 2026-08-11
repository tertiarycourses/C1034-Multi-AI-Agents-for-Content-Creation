# Lab 1 — Verify AutoGen and Run a First Agent

**Course:** Multi Agents System with AutoGen (C1034)<br>
**Topic 1:** Introduction to AutoGen and CrewAI<br>
**Maps to:** LO1 and LO2: distinguish the AgentChat components, prepare a reproducible environment, run an AssistantAgent, and inspect messages and the TaskResult stop reason<br>
**Tools:** Python 3.10+, virtual environment, AutoGen AgentChat 0.7.5, AutoGen Extensions replay client, OpsDesk CLI

**Version:** v1.0 (11 August 2026)<br>
**Duration:** 60 minutes

---

## Goal

You prepare an isolated Python environment, verify the pinned AutoGen AgentChat and Extensions packages, and run the first OpsDesk AssistantAgent with a ReplayChatCompletionClient. You then inspect the saved message types, final text and stop reason so the execution model is observable before any live model or tool is introduced.

## What You Will Build

A ready environment plus .course_state/lab01-environment.json and lab01-first-agent.json containing the first reproducible AgentChat trace.

## Prerequisites

- The C1034 repository is available locally and the current terminal is at its root.
- Python 3.10 or later and internet access for the initial package installation are available.
- No provider credential is required for the offline path.

> **Data note.** Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.

## Steps

**1. Create the course virtual environment from the repository root. If .venv already exists, keep it and continue rather than replacing it.**

```text
python -m venv .venv
```

**2. Activate the environment with the command for your shell. Confirm the prompt shows .venv before installing anything.**

```text
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS or Linux
source .venv/bin/activate
```

**3. Install the pinned dependencies and the editable OpsDesk lab package. The editable install makes python -m opsdesk.cli work from the repository root.**

```text
python -m pip install -r starter/requirements.txt
python -m pip install -e starter
```

**4. Generate the environment report. Check Python support, both AutoGen package versions, the two data files and the final ready status.**

```text
python -m opsdesk.cli setup
```

**5. Inspect the saved setup evidence instead of relying only on terminal output. The package versions must both be 0.7.5.**

```text
python -m json.tool .course_state/lab01-environment.json
python -m pip show autogen-agentchat autogen-ext
```

**6. Run the first AssistantAgent with the deterministic replay model. The output must describe the synthetic-data, citation and insufficient-evidence boundaries.**

```text
python -m opsdesk.cli first-agent --offline
```

**7. Inspect the trace. Identify the agent name, ordered message types, final content, null team stop_reason and application-level completion_reason. A one-turn AssistantAgent run completes without a team termination condition.**

```text
python -m json.tool .course_state/lab01-first-agent.json
```

**8. Run the focused offline check and review the bounded repository diff. Keep both JSON files as the rejoin checkpoint for Lab 2.**

```text
python -m pytest -q starter/tests/test_examples.py -k first_agent
git status --short
```

## Test It

.course_state/lab01-environment.json must report status ready, Python support true and AutoGen package versions 0.7.5. lab01-first-agent.json must name opsdesk_assistant, include TextMessage entries, contain the synthetic-data boundary, preserve a null team stop_reason and report completion_reason single_agent_turn_complete. The focused test must be clean.

## Troubleshooting

- **PowerShell blocks activation.** Run Set-ExecutionPolicy -Scope Process Bypass for the current terminal only, then activate .venv again.
- **The setup report says a package is missing.** Confirm the virtual environment is active, rerun both pip install commands, and use python -m pip so installation and execution use the same interpreter.
- **python cannot import opsdesk.** Run python -m pip install -e starter from the repository root and confirm starter/pyproject.toml is present.

## Challenge

Run python -m opsdesk.cli first-agent --offline twice, compare the two JSON files, and explain why deterministic replay is useful for a regression baseline but cannot estimate live-model quality.

## Reflection

Why does a one-turn AssistantAgent run have no team stop reason, and which application-level field should describe its successful completion?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-add-a-typed-ticket-lookup-tool.md)

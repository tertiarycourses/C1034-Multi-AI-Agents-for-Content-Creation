# Lab 6 — Design Roles and Run a Round-Robin Team

**Course:** Multi Agents System with AutoGen (C1034)<br>
**Topic 3:** Implementing a Multi-Agent AI Workflow<br>
**Maps to:** LO5 and LO6: define distinct writer and reviewer contracts, run a predictable RoundRobinGroupChat, and combine approval with a hard message limit<br>
**Tools:** AssistantAgent roles, RoundRobinGroupChat, ExactTextTermination, MaxMessageTermination, shared context, TaskResult

**Version:** v1.0 (11 August 2026)<br>
**Duration:** 60 minutes

---

## Goal

You split the Lab 5 response task into a writer that uses supplied evidence and a reviewer that checks support and citation. A RoundRobinGroupChat makes the order predictable, while the course's ExactTextTermination combined with MaxMessageTermination proves that an exact reviewer approval marker can end the normal run and a hard boundary still exists.

## What You Will Build

.course_state/lab06-round-robin.json with participant names, observed speaker sequence, message count, stop reason and bounded status for the writer-reviewer workflow.

## Prerequisites

- Lab 5 has restored a grounded VPN answer that cites POL-VPN-01.
- You can state the different responsibilities of retrieval, writing and evidence review.
- The active environment still uses AutoGen AgentChat and Extensions 0.7.5.

> **Data note.** Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.

## Steps

**1. Verify the grounded single-agent baseline. Do not add a team until the source and citation contract is already working.**

```text
python -m opsdesk.cli rag --query "What approvals are required for VPN access?" --offline
```

**2. Inspect the writer and reviewer construction in round_robin_team. Compare their names, descriptions and system messages and identify why neither role needs the ticket tool.**

```text
python -c "from opsdesk.examples import round_robin_team; import inspect; print(inspect.getsource(round_robin_team))"
```

**3. Create the concrete team-contract record from the supplied template, inspect it, and validate the required writer, reviewer, approval and hard-limit fields.**

```text
python -m opsdesk.cli team-contract-init --force
python -m opsdesk.cli team-contract-validate
python -c "from pathlib import Path; print(Path('.course_state/lab06-team-contract.md').read_text(encoding='utf-8'))"
```

**4. Run the deterministic round-robin team. The fixed order should produce one writer turn followed by one reviewer turn.**

```text
python -m opsdesk.cli team-round-robin --offline
```

**5. Inspect the saved evidence. Confirm participants are writer and reviewer, the source sequence begins user, writer, reviewer, and message_count does not exceed six.**

```text
python -m json.tool .course_state/lab06-round-robin.json
```

**6. Identify both branches of the combined termination expression. Explain why an exact reviewer message equal to APPROVED is a completion signal while the message maximum is a safety boundary rather than success.**

```text
python -c "from pathlib import Path; t=Path('starter/opsdesk/examples.py').read_text(); print([line.strip() for line in t.splitlines() if 'ExactTextTermination' in line or 'MaxMessageTermination' in line])"
```

**7. Run the focused team check and validate the role record. Verify the normal run stopped within the hard limit for the approval condition.**

```text
python -m pytest -q starter/tests/test_examples.py -k round_robin
python -m opsdesk.cli team-contract-validate
```

**8. Keep the JSON evidence and compare the two-agent route with the Lab 5 single-agent path. Record one benefit and one added coordination cost in your notes.**

```text
python -c "import json; r=json.load(open('.course_state/lab06-round-robin.json')); print({'route':r['sources'],'messages':r['message_count'],'stop':r['stop_reason'],'bounded':r['bounded']})"
```

## Test It

The team evidence must list writer and reviewer, show the expected fixed speaker order, remain within six messages, set approved true and completion_reason approved, and stop only because the reviewer emitted the exact APPROVED marker. The team-contract validator and focused round-robin check must be clean, and the earlier grounded source contract must remain unchanged.

## Troubleshooting

- **The reviewer speaks before the writer.** Confirm the participant list order is [writer, reviewer] and reset or recreate the team before an unrelated run.
- **The team reaches the hard limit instead of approval.** Inspect whether the complete reviewer message equals APPROVED exactly and verify the draft contains a supported source identifier before changing termination.
- **A repeated run contains unexpected prior context.** Agents and teams are stateful; create a fresh team or await team.reset before an unrelated task.

## Challenge

Change the reviewer replay to request one revision, add the writer's revised response, and verify the route stays bounded and stops only after the supported revision is approved.

## Reflection

What did the reviewer role add that could not be proven by simply asking the writer to say its own answer was grounded?

---

[← Lab 5](lab-05-build-a-grounded-rag-agent.md) · [Lab 7 →](lab-07-route-specialists-with-selectorgroupchat.md)

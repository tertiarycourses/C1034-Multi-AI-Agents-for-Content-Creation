# Lab 7 — Route Specialists with SelectorGroupChat

**Course:** Multi Agents System with AutoGen (C1034)<br>
**Topic 3:** Implementing a Multi-Agent AI Workflow<br>
**Maps to:** LO5 and LO6: configure distinct planner, retriever, writer and reviewer descriptions, control next-speaker routing, and verify a bounded selector workflow<br>
**Tools:** SelectorGroupChat, selector_func, role descriptions, shared context, ExactTextTermination, MaxMessageTermination, replay clients

**Version:** v1.0 (11 August 2026)<br>
**Duration:** 60 minutes

---

## Goal

You expand OpsDesk into four specialist roles and run them through SelectorGroupChat. A custom selector function makes the learning route reproducible—planner to retriever to writer to reviewer—while the role descriptions, shared messages and combined termination show what a model-based selector would rely on in a dynamic workflow.

## What You Will Build

.course_state/lab07-selector-team.json with four participant contracts, the observed route, approval evidence, message count, stop reason and bounded status.

## Prerequisites

- Lab 6 round-robin evidence is bounded and stopped on the approval condition.
- The Lab 5 retrieval and citation contract is still the source of truth for the retriever and writer roles.
- You can explain the difference between fixed turn order and context-aware speaker selection.

> **Data note.** Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.

## Steps

**1. Inspect the Lab 6 route and state the limitation of giving every role a turn when a request may need only some specialists.**

```text
python -m json.tool .course_state/lab06-round-robin.json
```

**2. Inspect the four participant descriptions. Confirm each role owns one outcome and that only the reviewer can emit the normal completion phrase.**

```text
python -c "from opsdesk.examples import selector_team; import inspect; print(inspect.getsource(selector_team))"
```

**3. Inspect the custom selector function. Trace the expected route on paper and identify what should happen after an unknown source returns None.**

```text
python -c "from opsdesk.examples import _route_selector; import inspect; print(inspect.getsource(_route_selector))"
```

**4. Run the deterministic selector team. The selector client is present, but the custom function owns every transition in this stable learning case.**

```text
python -m opsdesk.cli team-selector --offline
```

**5. Inspect the saved evidence. Confirm the exact five-source route, approval, bounded status and semantic stop reason.**

```text
python -m json.tool .course_state/lab07-selector-team.json
```

**6. Call the selector function with synthetic last-message sources and confirm the transition table is deterministic for planner, retriever, writer and reviewer.**

```text
python -c "from types import SimpleNamespace as M; from opsdesk.examples import _route_selector as s; print({x:s([M(source=x)]) for x in ['user','planner','retriever','writer','reviewer','unknown']})"
```

**7. Run the focused selector check. It locks the route and stopping evidence independently of final prose.**

```text
python -m pytest -q starter/tests/test_examples.py -k selector
```

**8. Compare the saved Lab 6 and Lab 7 evidence. Record which pattern is simpler, which is more adaptable and which extra routing decision must be monitored.**

```text
python -c "import json; a=json.load(open('.course_state/lab06-round-robin.json')); b=json.load(open('.course_state/lab07-selector-team.json')); print({'round_robin':a['sources'],'selector':b['route'],'stops':[a['stop_reason'],b['stop_reason']]})"
```

## Test It

The selector evidence must list planner, retriever, writer and reviewer, show route user to planner to retriever to writer to reviewer, set approved and bounded true, and stop only for the reviewer's exact APPROVED marker before eight messages. The transition table must return None only for an unmapped source, and the focused selector check must be clean.

## Troubleshooting

- **The selector route skips or repeats a role.** Inspect the last message source and the exact mapping in _route_selector; keep participant names identical to mapping values.
- **SelectorGroupChat invokes the selector model unexpectedly.** A selector function returning None delegates to model selection. Ensure all expected sources map to a valid participant for the deterministic path.
- **The team cannot be serialized with the custom function.** Custom selector functions require separate code and recovery design; persist their version and tests rather than assuming dump_component includes the function.

## Challenge

Create a candidate function that excludes the writer until retrieved evidence exists, then document how the fallback behaves when no candidate remains.

## Reflection

Which routing evidence would you alert on first if a live selector began choosing the reviewer before retrieval?

---

[← Lab 6](lab-06-design-roles-and-run-a-round-robin-team.md) · [Lab 8 →](lab-08-integrate-and-verify-the-opsdesk-workflow.md)

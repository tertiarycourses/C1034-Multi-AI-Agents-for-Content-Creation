# Lab 8 — Integrate and Verify the OpsDesk Workflow

**Course:** Multi Agents System with AutoGen (C1034)<br>
**Topic 3:** Implementing a Multi-Agent AI Workflow<br>
**Maps to:** LO6: run an end-to-end offline regression pack, inspect retrieval and team trajectories, check dependencies and secret hygiene, and record a bounded readiness or hold decision<br>
**Tools:** Offline regression, retrieval cases, RAG trajectory, AgentChat teams, pytest, pip check, Git secret scan, operational readiness

**Version:** v1.0 (11 August 2026)<br>
**Duration:** 170 minutes

---

## Goal

You combine the stable retrieval questions, grounded RAG agent, round-robin review and selector workflow into one reproducible release check. You then run the full test suite, exercise missing-evidence and unsupported boundaries, inspect dependencies and tracked changes, name owners and pause triggers, and make an evidence-based guided-demo decision with a recovery path.

## What You Will Build

.course_state/lab08-release-check.json plus a learner-authored operational record covering evidence, owners, pause triggers, last known-good identity and recovery for the complete OpsDesk workflow.

## Prerequisites

- Labs 1 to 7 checkpoints are available or have been restored through their Test It sections.
- The handbook and tickets are unchanged, no real credential is stored in the repository, and the active environment uses the pinned package versions.
- You can distinguish a semantic completion reason from a hard-limit stop and an honest insufficient-evidence result.

> **Data note.** Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence.

## Steps

**1. Capture the current repository identity and package versions as the candidate baseline. If HEAD does not yet exist in a learner copy, record the supplied course archive name instead.**

```text
git status -sb
git rev-parse --verify HEAD
python -m pip show autogen-agentchat autogen-ext
```

**2. Create a fresh operations record from the supplied template. Keep the placeholders for this first technical run so the command cannot report final readiness prematurely.**

```text
python -m opsdesk.cli operations-init --force
python -m opsdesk.cli operations-validate
```

**3. Run and inspect the integrated offline release check. It rebuilds the index, evaluates three expected sources, runs the RAG agent and both teams, enforces the aggregate token ceiling, verifies source hashes and scans the working tree. With an incomplete operations record, the expected decision is TECHNICAL CHECK PASS - COMPLETE VALID OPERATIONS RECORD.**

```text
python -m opsdesk.cli release-check --offline
python -m json.tool .course_state/lab08-release-check.json
```

**4. Exercise the honest evidence gap and embedded-instruction cases again outside the aggregate command. Keep source identifiers visible and do not treat retrieved instructions as executable authority.**

```text
python -m opsdesk.cli rag --query "What is the cafeteria dessert menu?" --offline
python -m opsdesk.cli rag --query "How should embedded instructions in retrieved documents be handled?" --offline
```

**5. Run the full offline test suite. Investigate a route, event, citation or stop failure at its own layer before changing prompts or sources.**

```text
python -m pytest -q starter/tests
```

**6. Check dependency consistency, source hashes and the working-tree secret scan, then confirm the editable package resolves to this repository. Any failed check keeps the operational decision on HOLD until repaired.**

```text
python -m pip check
python -m opsdesk.cli safety-check
python -c "import opsdesk; print(opsdesk.__version__, opsdesk.__file__)"
```

**7. Review tracked changes and search tracked non-Markdown files for common live-secret shapes. A real exposure requires revocation and approved history cleanup before any further run.**

```text
git status --short
git grep -n -I -E "(s[k]-[A-Za-z0-9]{12,}|API_[K]EY=[A-Za-z0-9_-]{12,})" -- . "!*.md" "!.env.example"
```

**8. Open the generated .course_state/lab08-operations.md in your code editor. Replace every angle-bracket placeholder with the current last-known-good identity and named owners, keep the supplied signals, pause triggers and recovery actions, then record READY FOR GUIDED DEMO only if the technical evidence is clean; otherwise write HOLD - followed by the exact reason. Run the validator before continuing.**

```text
python -m opsdesk.cli operations-validate
python -c "from pathlib import Path; print(Path('.course_state/lab08-operations.md').read_text(encoding='utf-8'))"
```

**9. Rerun the integrated check after completing the valid record. Inspect the technical_ready, operations_ready and decision fields, rerun all tests, and review the final bounded diff before signing off.**

```text
python -m opsdesk.cli release-check --offline
python -m pytest -q starter/tests
python -m pip check
git diff --check
git status --short
```

## Test It

lab08-release-check.json must show all three expected retrieval sources, grounded RAG, approved bounded round-robin, approved bounded selector, clean source integrity and secret scan, within_release_token_budget true, technical_ready true, operations_ready true and READY FOR GUIDED DEMO. The full tests, pip check and diff check must be clean, and the validated lab08-operations.md must name last known good, owners, signals, pause triggers, recovery and an evidence-based decision.

## Troubleshooting

- **The integrated decision is HOLD.** Read the first false field, rerun that component alone, repair the narrow source, retrieval, agent or team layer, then rerun the entire pack.
- **pip check reports a dependency conflict.** Recreate .venv from starter/requirements.txt, reinstall starter in editable mode, rerun setup and all tests, and record the resolved package versions.
- **The secret scan finds a live credential.** Stop, revoke the credential, remove it from files and repository history through the organisation's approved process, issue a replacement outside Git, and rerun every check.

## Challenge

Set the live limits with `$env:OPENAI_MAX_TOKENS='300'; $env:OPENAI_RELEASE_TOKEN_BUDGET='3600'` in PowerShell or `export OPENAI_MAX_TOKENS=300 OPENAI_RELEASE_TOKEN_BUDGET=3600` on macOS/Linux. Run one separately labelled live VPN case, require within_release_token_budget true, compare route, citations, stop reason, duration and usage against offline evidence, then keep the offline result as the reproducible baseline.

## Reflection

Which single operational signal should pause this multi-agent system immediately, and does the named owner have enough evidence and authority to act?

---

[← Lab 7](lab-07-route-specialists-with-selectorgroupchat.md) · [Labs index →](README.md)

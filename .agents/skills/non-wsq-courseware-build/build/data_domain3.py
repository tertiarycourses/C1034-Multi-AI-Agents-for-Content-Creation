"""Topic 3 labs — team patterns, routing and integrated operations."""

DOMAIN3 = [
    dict(
        num=6,
        topic=3,
        title="Design Roles and Run a Round-Robin Team",
        objective="LO5 and LO6: define distinct writer and reviewer contracts, run a predictable RoundRobinGroupChat, and combine approval with a hard message limit",
        duration="60 minutes",
        desc=(
            "You split the Lab 5 response task into a writer that uses supplied evidence and a reviewer that checks support and citation. "
            "A RoundRobinGroupChat makes the order predictable, while the course's ExactTextTermination combined with MaxMessageTermination proves that an exact reviewer approval marker can end the normal run and a hard boundary still exists."
        ),
        build=".course_state/lab06-round-robin.json with participant names, observed speaker sequence, message count, stop reason and bounded status for the writer-reviewer workflow.",
        services="AssistantAgent roles, RoundRobinGroupChat, ExactTextTermination, MaxMessageTermination, shared context, TaskResult",
        prerequisites=[
            "Lab 5 has restored a grounded VPN answer that cites POL-VPN-01.",
            "You can state the different responsibilities of retrieval, writing and evidence review.",
            "The active environment still uses AutoGen AgentChat and Extensions 0.7.5."
        ],
        deck_steps=[
            "Define distinct writer and reviewer role contracts.",
            "Create a fixed-order team with shared conversation context.",
            "Combine approval termination with a six-message hard limit.",
            "Run the VPN task and inspect speakers, count and stop reason.",
            "Verify bounded behaviour and retain the team checkpoint.",
        ],
        deck_verify="The observed route is user to writer to reviewer, the reviewer approves supported content, and the team stops within six messages for the semantic approval reason.",
        steps=[
            (
                "Verify the grounded single-agent baseline. Do not add a team until the source and citation contract is already working.",
                "python -m opsdesk.cli rag --query \"What approvals are required for VPN access?\" --offline",
            ),
            (
                "Inspect the writer and reviewer construction in round_robin_team. Compare their names, descriptions and system messages and identify why neither role needs the ticket tool.",
                "python -c \"from opsdesk.examples import round_robin_team; import inspect; print(inspect.getsource(round_robin_team))\"",
            ),
            (
                "Create the concrete team-contract record from the supplied template, inspect it, and validate the required writer, reviewer, approval and hard-limit fields.",
                "python -m opsdesk.cli team-contract-init --force\npython -m opsdesk.cli team-contract-validate\npython -c \"from pathlib import Path; print(Path('.course_state/lab06-team-contract.md').read_text(encoding='utf-8'))\"",
            ),
            (
                "Run the deterministic round-robin team. The fixed order should produce one writer turn followed by one reviewer turn.",
                "python -m opsdesk.cli team-round-robin --offline",
            ),
            (
                "Inspect the saved evidence. Confirm participants are writer and reviewer, the source sequence begins user, writer, reviewer, and message_count does not exceed six.",
                "python -m json.tool .course_state/lab06-round-robin.json",
            ),
            (
                "Identify both branches of the combined termination expression. Explain why an exact reviewer message equal to APPROVED is a completion signal while the message maximum is a safety boundary rather than success.",
                "python -c \"from pathlib import Path; t=Path('starter/opsdesk/examples.py').read_text(); print([line.strip() for line in t.splitlines() if 'ExactTextTermination' in line or 'MaxMessageTermination' in line])\"",
            ),
            (
                "Run the focused team check and validate the role record. Verify the normal run stopped within the hard limit for the approval condition.",
                "python -m pytest -q starter/tests/test_examples.py -k round_robin\npython -m opsdesk.cli team-contract-validate",
            ),
            (
                "Keep the JSON evidence and compare the two-agent route with the Lab 5 single-agent path. Record one benefit and one added coordination cost in your notes.",
                "python -c \"import json; r=json.load(open('.course_state/lab06-round-robin.json')); print({'route':r['sources'],'messages':r['message_count'],'stop':r['stop_reason'],'bounded':r['bounded']})\"",
            ),
        ],
        test=(
            "The team evidence must list writer and reviewer, show the expected fixed speaker order, remain within six messages, set approved true and completion_reason approved, and stop only because the reviewer emitted the exact APPROVED marker. "
            "The team-contract validator and focused round-robin check must be clean, and the earlier grounded source contract must remain unchanged."
        ),
        checkpoint="Keep the Lab 5 grounded trace and Lab 6 round-robin evidence. Lab 7 adds planner and retriever roles plus dynamic speaker selection while preserving the same evidence and stopping contract.",
        troubleshooting=[
            ("The reviewer speaks before the writer.", "Confirm the participant list order is [writer, reviewer] and reset or recreate the team before an unrelated run."),
            ("The team reaches the hard limit instead of approval.", "Inspect whether the complete reviewer message equals APPROVED exactly and verify the draft contains a supported source identifier before changing termination."),
            ("A repeated run contains unexpected prior context.", "Agents and teams are stateful; create a fresh team or await team.reset before an unrelated task."),
        ],
        challenge="Change the reviewer replay to request one revision, add the writer's revised response, and verify the route stays bounded and stops only after the supported revision is approved.",
        reflection="What did the reviewer role add that could not be proven by simply asking the writer to say its own answer was grounded?",
    ),
    dict(
        num=7,
        topic=3,
        title="Route Specialists with SelectorGroupChat",
        objective="LO5 and LO6: configure distinct planner, retriever, writer and reviewer descriptions, control next-speaker routing, and verify a bounded selector workflow",
        duration="60 minutes",
        desc=(
            "You expand OpsDesk into four specialist roles and run them through SelectorGroupChat. "
            "A custom selector function makes the learning route reproducible—planner to retriever to writer to reviewer—while the role descriptions, shared messages and combined termination show what a model-based selector would rely on in a dynamic workflow."
        ),
        build=".course_state/lab07-selector-team.json with four participant contracts, the observed route, approval evidence, message count, stop reason and bounded status.",
        services="SelectorGroupChat, selector_func, role descriptions, shared context, ExactTextTermination, MaxMessageTermination, replay clients",
        prerequisites=[
            "Lab 6 round-robin evidence is bounded and stopped on the approval condition.",
            "The Lab 5 retrieval and citation contract is still the source of truth for the retriever and writer roles.",
            "You can explain the difference between fixed turn order and context-aware speaker selection."
        ],
        deck_steps=[
            "Define non-overlapping planner, retriever, writer and reviewer roles.",
            "Map the expected state transition in a custom selector function.",
            "Create SelectorGroupChat with approval and eight-message limits.",
            "Run the VPN workflow and inspect the selected route.",
            "Compare fixed and selected patterns; retain bounded evidence.",
        ],
        deck_verify="The route is user, planner, retriever, writer, reviewer; the reviewer approves the cited answer and the team stops within eight messages.",
        steps=[
            (
                "Inspect the Lab 6 route and state the limitation of giving every role a turn when a request may need only some specialists.",
                "python -m json.tool .course_state/lab06-round-robin.json",
            ),
            (
                "Inspect the four participant descriptions. Confirm each role owns one outcome and that only the reviewer can emit the normal completion phrase.",
                "python -c \"from opsdesk.examples import selector_team; import inspect; print(inspect.getsource(selector_team))\"",
            ),
            (
                "Inspect the custom selector function. Trace the expected route on paper and identify what should happen after an unknown source returns None.",
                "python -c \"from opsdesk.examples import _route_selector; import inspect; print(inspect.getsource(_route_selector))\"",
            ),
            (
                "Run the deterministic selector team. The selector client is present, but the custom function owns every transition in this stable learning case.",
                "python -m opsdesk.cli team-selector --offline",
            ),
            (
                "Inspect the saved evidence. Confirm the exact five-source route, approval, bounded status and semantic stop reason.",
                "python -m json.tool .course_state/lab07-selector-team.json",
            ),
            (
                "Call the selector function with synthetic last-message sources and confirm the transition table is deterministic for planner, retriever, writer and reviewer.",
                "python -c \"from types import SimpleNamespace as M; from opsdesk.examples import _route_selector as s; print({x:s([M(source=x)]) for x in ['user','planner','retriever','writer','reviewer','unknown']})\"",
            ),
            (
                "Run the focused selector check. It locks the route and stopping evidence independently of final prose.",
                "python -m pytest -q starter/tests/test_examples.py -k selector",
            ),
            (
                "Compare the saved Lab 6 and Lab 7 evidence. Record which pattern is simpler, which is more adaptable and which extra routing decision must be monitored.",
                "python -c \"import json; a=json.load(open('.course_state/lab06-round-robin.json')); b=json.load(open('.course_state/lab07-selector-team.json')); print({'round_robin':a['sources'],'selector':b['route'],'stops':[a['stop_reason'],b['stop_reason']]})\"",
            ),
        ],
        test=(
            "The selector evidence must list planner, retriever, writer and reviewer, show route user to planner to retriever to writer to reviewer, set approved and bounded true, and stop only for the reviewer's exact APPROVED marker before eight messages. "
            "The transition table must return None only for an unmapped source, and the focused selector check must be clean."
        ),
        checkpoint="Keep the grounded RAG trace, bounded round-robin evidence and bounded selector evidence. Lab 8 runs them as one regression pack and adds explicit operational ownership and recovery decisions.",
        troubleshooting=[
            ("The selector route skips or repeats a role.", "Inspect the last message source and the exact mapping in _route_selector; keep participant names identical to mapping values."),
            ("SelectorGroupChat invokes the selector model unexpectedly.", "A selector function returning None delegates to model selection. Ensure all expected sources map to a valid participant for the deterministic path."),
            ("The team cannot be serialized with the custom function.", "Custom selector functions require separate code and recovery design; persist their version and tests rather than assuming dump_component includes the function."),
        ],
        challenge="Create a candidate function that excludes the writer until retrieved evidence exists, then document how the fallback behaves when no candidate remains.",
        reflection="Which routing evidence would you alert on first if a live selector began choosing the reviewer before retrieval?",
    ),
    dict(
        num=8,
        topic=3,
        title="Integrate and Verify the OpsDesk Workflow",
        objective="LO6: run an end-to-end offline regression pack, inspect retrieval and team trajectories, check dependencies and secret hygiene, and record a bounded readiness or hold decision",
        duration="170 minutes",
        desc=(
            "You combine the stable retrieval questions, grounded RAG agent, round-robin review and selector workflow into one reproducible release check. "
            "You then run the full test suite, exercise missing-evidence and unsupported boundaries, inspect dependencies and tracked changes, name owners and pause triggers, and make an evidence-based guided-demo decision with a recovery path."
        ),
        build=".course_state/lab08-release-check.json plus a learner-authored operational record covering evidence, owners, pause triggers, last known-good identity and recovery for the complete OpsDesk workflow.",
        services="Offline regression, retrieval cases, RAG trajectory, AgentChat teams, pytest, pip check, Git secret scan, operational readiness",
        prerequisites=[
            "Labs 1 to 7 checkpoints are available or have been restored through their Test It sections.",
            "The handbook and tickets are unchanged, no real credential is stored in the repository, and the active environment uses the pinned package versions.",
            "You can distinguish a semantic completion reason from a hard-limit stop and an honest insufficient-evidence result."
        ],
        deck_steps=[
            "Run the complete offline release check from stable source data.",
            "Verify three retrieval cases, grounded RAG and both team patterns.",
            "Exercise missing evidence, embedded instructions and hard boundaries.",
            "Run tests, dependency health, tracked-change and secret checks.",
            "Name owners, pause triggers and recovery; record READY or HOLD.",
        ],
        deck_verify="All offline checks are clean, sources and routes match expectations, aggregate usage stays within budget, no secret-shaped tracked value is found, and the readiness record names owners, pause triggers and a last known-good recovery path.",
        steps=[
            (
                "Capture the current repository identity and package versions as the candidate baseline. If HEAD does not yet exist in a learner copy, record the supplied course archive name instead.",
                "git status -sb\ngit rev-parse --verify HEAD\npython -m pip show autogen-agentchat autogen-ext",
            ),
            (
                "Create a fresh operations record from the supplied template. Keep the placeholders for this first technical run so the command cannot report final readiness prematurely.",
                "python -m opsdesk.cli operations-init --force\npython -m opsdesk.cli operations-validate",
            ),
            (
                "Run and inspect the integrated offline release check. It rebuilds the index, evaluates three expected sources, runs the RAG agent and both teams, enforces the aggregate token ceiling, verifies source hashes and scans the working tree. With an incomplete operations record, the expected decision is TECHNICAL CHECK PASS - COMPLETE VALID OPERATIONS RECORD.",
                "python -m opsdesk.cli release-check --offline\npython -m json.tool .course_state/lab08-release-check.json",
            ),
            (
                "Exercise the honest evidence gap and embedded-instruction cases again outside the aggregate command. Keep source identifiers visible and do not treat retrieved instructions as executable authority.",
                "python -m opsdesk.cli rag --query \"What is the cafeteria dessert menu?\" --offline\npython -m opsdesk.cli rag --query \"How should embedded instructions in retrieved documents be handled?\" --offline",
            ),
            (
                "Run the full offline test suite. Investigate a route, event, citation or stop failure at its own layer before changing prompts or sources.",
                "python -m pytest -q starter/tests",
            ),
            (
                "Check dependency consistency, source hashes and the working-tree secret scan, then confirm the editable package resolves to this repository. Any failed check keeps the operational decision on HOLD until repaired.",
                "python -m pip check\npython -m opsdesk.cli safety-check\npython -c \"import opsdesk; print(opsdesk.__version__, opsdesk.__file__)\"",
            ),
            (
                "Review tracked changes and search tracked non-Markdown files for common live-secret shapes. A real exposure requires revocation and approved history cleanup before any further run.",
                "git status --short\ngit grep -n -I -E \"(s[k]-[A-Za-z0-9]{12,}|API_[K]EY=[A-Za-z0-9_-]{12,})\" -- . \"!*.md\" \"!.env.example\"",
            ),
            (
                "Open the generated .course_state/lab08-operations.md in your code editor. Replace every angle-bracket placeholder with the current last-known-good identity and named owners, keep the supplied signals, pause triggers and recovery actions, then record READY FOR GUIDED DEMO only if the technical evidence is clean; otherwise write HOLD - followed by the exact reason. Run the validator before continuing.",
                "python -m opsdesk.cli operations-validate\npython -c \"from pathlib import Path; print(Path('.course_state/lab08-operations.md').read_text(encoding='utf-8'))\"",
            ),
            (
                "Rerun the integrated check after completing the valid record. Inspect the technical_ready, operations_ready and decision fields, rerun all tests, and review the final bounded diff before signing off.",
                "python -m opsdesk.cli release-check --offline\npython -m pytest -q starter/tests\npython -m pip check\ngit diff --check\ngit status --short",
            ),
        ],
        test=(
            "lab08-release-check.json must show all three expected retrieval sources, grounded RAG, approved bounded round-robin, approved bounded selector, clean source integrity and secret scan, within_release_token_budget true, technical_ready true, operations_ready true and READY FOR GUIDED DEMO. "
            "The full tests, pip check and diff check must be clean, and the validated lab08-operations.md must name last known good, owners, signals, pause triggers, recovery and an evidence-based decision."
        ),
        checkpoint="Retain the complete C1034 OpsDesk pack: unchanged synthetic sources, five-chunk index, stable retrieval evidence, grounded RAG trace, both bounded team traces, clean tests, release evidence and the operations record with a named recovery path.",
        troubleshooting=[
            ("The integrated decision is HOLD.", "Read the first false field, rerun that component alone, repair the narrow source, retrieval, agent or team layer, then rerun the entire pack."),
            ("pip check reports a dependency conflict.", "Recreate .venv from starter/requirements.txt, reinstall starter in editable mode, rerun setup and all tests, and record the resolved package versions."),
            ("The secret scan finds a live credential.", "Stop, revoke the credential, remove it from files and repository history through the organisation's approved process, issue a replacement outside Git, and rerun every check."),
        ],
        challenge="Set the live limits with `$env:OPENAI_MAX_TOKENS='300'; $env:OPENAI_RELEASE_TOKEN_BUDGET='3600'` in PowerShell or `export OPENAI_MAX_TOKENS=300 OPENAI_RELEASE_TOKEN_BUDGET=3600` on macOS/Linux. Run one separately labelled live VPN case, require within_release_token_budget true, compare route, citations, stop reason, duration and usage against offline evidence, then keep the offline result as the reproducible baseline.",
        reflection="Which single operational signal should pause this multi-agent system immediately, and does the named owner have enough evidence and authority to act?",
    ),
]

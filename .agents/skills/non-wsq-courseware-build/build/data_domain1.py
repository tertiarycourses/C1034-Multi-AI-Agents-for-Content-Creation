"""Topic 1 labs — AgentChat foundations and typed tools."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Verify AutoGen and Run a First Agent",
        objective="LO1 and LO2: distinguish the AgentChat components, prepare a reproducible environment, run an AssistantAgent, and inspect messages and the TaskResult stop reason",
        duration="60 minutes",
        desc=(
            "You prepare an isolated Python environment, verify the pinned AutoGen AgentChat and Extensions packages, and run the first OpsDesk AssistantAgent with a ReplayChatCompletionClient. "
            "You then inspect the saved message types, final text and stop reason so the execution model is observable before any live model or tool is introduced."
        ),
        build="A ready environment plus .course_state/lab01-environment.json and lab01-first-agent.json containing the first reproducible AgentChat trace.",
        services="Python 3.10+, virtual environment, AutoGen AgentChat 0.7.5, AutoGen Extensions replay client, OpsDesk CLI",
        prerequisites=[
            "The C1034 repository is available locally and the current terminal is at its root.",
            "Python 3.10 or later and internet access for the initial package installation are available.",
            "No provider credential is required for the offline path.",
        ],
        deck_steps=[
            "Create and activate an isolated Python environment.",
            "Install the pinned lab dependencies and editable OpsDesk package.",
            "Generate the environment report and confirm status ready.",
            "Run the first AgentChat assistant with the replay client.",
            "Inspect messages, final content and stop reason; keep the checkpoint.",
        ],
        deck_verify="The setup report says ready and the first trace contains user and assistant messages with the expected synthetic-data boundary.",
        steps=[
            (
                "Create the course virtual environment from the repository root. If .venv already exists, keep it and continue rather than replacing it.",
                "python -m venv .venv",
            ),
            (
                "Activate the environment with the command for your shell. Confirm the prompt shows .venv before installing anything.",
                "# Windows PowerShell\n.\\.venv\\Scripts\\Activate.ps1\n# macOS or Linux\nsource .venv/bin/activate",
            ),
            (
                "Install the pinned dependencies and the editable OpsDesk lab package. The editable install makes python -m opsdesk.cli work from the repository root.",
                "python -m pip install -r starter/requirements.txt\npython -m pip install -e starter",
            ),
            (
                "Generate the environment report. Check Python support, both AutoGen package versions, the two data files and the final ready status.",
                "python -m opsdesk.cli setup",
            ),
            (
                "Inspect the saved setup evidence instead of relying only on terminal output. The package versions must both be 0.7.5.",
                "python -m json.tool .course_state/lab01-environment.json\npython -m pip show autogen-agentchat autogen-ext",
            ),
            (
                "Run the first AssistantAgent with the deterministic replay model. The output must describe the synthetic-data, citation and insufficient-evidence boundaries.",
                "python -m opsdesk.cli first-agent --offline",
            ),
            (
                "Inspect the trace. Identify the agent name, ordered message types, final content, null team stop_reason and application-level completion_reason. A one-turn AssistantAgent run completes without a team termination condition.",
                "python -m json.tool .course_state/lab01-first-agent.json",
            ),
            (
                "Run the focused offline check and review the bounded repository diff. Keep both JSON files as the rejoin checkpoint for Lab 2.",
                "python -m pytest -q starter/tests/test_examples.py -k first_agent\ngit status --short",
            ),
        ],
        test=(
            ".course_state/lab01-environment.json must report status ready, Python support true and AutoGen package versions 0.7.5. "
            "lab01-first-agent.json must name opsdesk_assistant, include TextMessage entries, contain the synthetic-data boundary, preserve a null team stop_reason and report completion_reason single_agent_turn_complete. The focused test must be clean."
        ),
        checkpoint="Retain the activated environment, editable OpsDesk install, the two Lab 1 JSON files and a clean focused test. Lab 2 adds a typed read-only tool to the same assistant boundary.",
        troubleshooting=[
            ("PowerShell blocks activation.", "Run Set-ExecutionPolicy -Scope Process Bypass for the current terminal only, then activate .venv again."),
            ("The setup report says a package is missing.", "Confirm the virtual environment is active, rerun both pip install commands, and use python -m pip so installation and execution use the same interpreter."),
            ("python cannot import opsdesk.", "Run python -m pip install -e starter from the repository root and confirm starter/pyproject.toml is present."),
        ],
        challenge="Run python -m opsdesk.cli first-agent --offline twice, compare the two JSON files, and explain why deterministic replay is useful for a regression baseline but cannot estimate live-model quality.",
        reflection="Why does a one-turn AssistantAgent run have no team stop reason, and which application-level field should describe its successful completion?",
    ),
    dict(
        num=2,
        topic=1,
        title="Add a Typed Ticket Lookup Tool",
        objective="LO2: define and execute a typed read-only tool, inspect its schema and tool events, and preserve explicit not-found behaviour without granting write authority",
        duration="55 minutes",
        desc=(
            "You extend the OpsDesk assistant with lookup_ticket, a typed function that reads one synthetic incident by exact identifier. "
            "The offline replay client produces a real function-call request, AgentChat executes the tool, and the saved trace proves the request, result and not-found behaviour without changing any ticket."
        ),
        build="A verified lookup_ticket contract plus .course_state/lab02-tool-agent.json containing ToolCallRequestEvent, ToolCallExecutionEvent and the exact synthetic result.",
        services="AssistantAgent, FunctionTool schema, FunctionCall, ToolCallExecutionEvent, ReplayChatCompletionClient, synthetic tickets.json",
        prerequisites=[
            "Lab 1 setup status is ready and its focused test is clean.",
            "The editable OpsDesk package is installed in the active virtual environment.",
            "starter/data/tickets.json still contains only the supplied INC-1001 to INC-1003 records.",
        ],
        deck_steps=[
            "Inspect the typed lookup_ticket signature and synthetic dataset.",
            "Run an exact INC-1001 tool request through AssistantAgent.",
            "Confirm request, execution and summary events in the trace.",
            "Exercise an unknown identifier and verify not_found behaviour.",
            "Run focused checks and retain the read-only checkpoint.",
        ],
        deck_verify="The trace contains a ToolCallExecutionEvent and returns the exact requested incident or an explicit not_found result without mutating tickets.json.",
        steps=[
            (
                "Confirm the Lab 1 checkpoint and active package versions before changing the agent boundary.",
                "python -m opsdesk.cli setup\npython -m pytest -q starter/tests/test_examples.py -k first_agent",
            ),
            (
                "Inspect the supplied incidents and the lookup_ticket function. Note the exact string parameter, docstring and stable JSON statuses found and not_found.",
                "python -m json.tool starter/data/tickets.json\npython -c \"from opsdesk.examples import lookup_ticket; import inspect; print(inspect.signature(lookup_ticket)); print(inspect.getdoc(lookup_ticket))\"",
            ),
            (
                "Create and execute the FunctionTool directly once. This separates schema and application behaviour from model selection.",
                "python -c \"import asyncio, json; from opsdesk.examples import inspect_tool_schema; print(json.dumps(asyncio.run(inspect_tool_schema()), indent=2, default=str))\"",
            ),
            (
                "Run the AgentChat tool path for INC-1001. The replay completion requests lookup_ticket and AutoGen emits the real tool execution events.",
                "python -m opsdesk.cli tool-agent --ticket INC-1001 --offline",
            ),
            (
                "Inspect the saved evidence. Confirm tool_event_seen is true, the final content contains INC-1001 and no event claims that a record was changed.",
                "python -m json.tool .course_state/lab02-tool-agent.json",
            ),
            (
                "Exercise the unknown-identifier route. It must return status not_found with the requested identifier rather than inventing a ticket.",
                "python -m opsdesk.cli tool-agent --ticket INC-9999 --offline\npython -m json.tool .course_state/lab02-tool-agent.json",
            ),
            (
                "Rerun the normal case so the checkpoint represents the shared scenario, then run the focused tool test.",
                "python -m opsdesk.cli tool-agent --ticket INC-1001 --offline\npython -m pytest -q starter/tests/test_examples.py -k tool_agent",
            ),
            (
                "Confirm the synthetic dataset has no Git change and keep the normal trace as the Lab 2 checkpoint for retrieval work.",
                "git diff -- starter/data/tickets.json\ngit status --short",
            ),
        ],
        test=(
            "The normal trace must set tool_event_seen true and contain INC-1001. The unknown route must return not_found without an invented record, the focused test must be clean, and starter/data/tickets.json must remain unchanged."
        ),
        checkpoint="Keep the working environment, unchanged tickets.json and the restored INC-1001 tool trace. Lab 3 adds an independent, source-labelled handbook index rather than overloading the ticket tool.",
        troubleshooting=[
            ("The trace has no ToolCallExecutionEvent.", "Confirm --offline is present and the installed packages are 0.7.5, then inspect _tool_call and the exact lookup_ticket function name in starter/opsdesk/examples.py."),
            ("The tool returns not_found for INC-1001.", "Run from the repository root, confirm starter/data/tickets.json is present, and verify the identifier uses uppercase INC and a hyphen."),
            ("The source dataset appears modified.", "Restore the supplied synthetic values from the repository history before continuing; later stable checks depend on exact identifiers and categories."),
        ],
        challenge="Add a new read-only category filter in a separate branch, define its typed return contract, and write a test proving it cannot add, edit or delete a ticket.",
        reflection="Which part of the tool contract prevents a fluent agent response from silently turning an unknown ticket into a fictional record?",
    ),
]

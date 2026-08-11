"""Single source of truth for C1034 courseware and connected labs."""

# ------------------------------------------------------------------ metadata
TITLE = "Multi Agents System with AutoGen (C1034)"
SHORT_TITLE = "Multi Agents System with AutoGen (C1034)"
COURSE_CODE = "C1034"
VERSION = "v1.0"
VERSION_DATE = "11 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Tertiary Infotech Trainer"
TRAINER_CERT = "Applied AI and multi-agent systems practitioner"
TRAINER_DELIVERS = "AutoGen AgentChat, RAG, multi-agent workflow design, safe tool use, verification, and operational controls"
DAYS = 2
MODE = "Instructor-led, concept-first learning with connected hands-on labs"

# The published course duration is 15 hours over two days. Tea breaks are
# included in the scheduled learning time; the one-hour lunch is excluded.
DAY_MINUTES = 480
INSTRUCTIONAL_HOURS = 15
CLOCK_HOURS = 16
DAILY_TIMING = "9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks)"
DARK_THEME = False
COMPACT_LAB_DECK = True

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain LLM agents, the AgentChat execution model, and the practical differences between AutoGen and CrewAI abstractions.",
    "LO2: Configure and run an AutoGen AssistantAgent with a model client, clear messages, a typed read-only tool, and inspectable event evidence.",
    "LO3: Design a Retrieval-Augmented Generation pipeline with source-labelled chunks, transparent ranking, metadata, context limits, and stable retrieval questions.",
    "LO4: Build and verify a grounded RAG agent that cites retrieved evidence, treats documents as untrusted data, and handles insufficient evidence honestly.",
    "LO5: Select and implement appropriate multi-agent patterns with specialist roles, explicit handoffs, shared context, and bounded speaker routing.",
    "LO6: Apply termination, state management, guardrails, observability, regression checks, ownership, and recovery controls to an integrated AutoGen workflow.",
]

LO_TITLES = [
    "Agent Foundations",
    "AgentChat in Practice",
    "Retrieval Design",
    "Grounded RAG",
    "Team Orchestration",
    "Operational Control",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(
        num=1,
        code="01",
        title="Introduction to AutoGen and CrewAI",
        subtitle="LLMs and agents · AutoGen layers · AgentChat lifecycle · AssistantAgent · tools · messages · state · framework choice",
        concepts=[
            ("LLM, agent and multi-agent system", "An LLM predicts outputs from context. An agent wraps a model with instructions, tools, state and an execution loop. A multi-agent system adds role boundaries and communication, which increases coordination work as well as capability."),
            ("The agent loop", "A task becomes messages; the model chooses a response or tool call; the application executes approved tools; the result returns as another event; and an explicit rule decides whether to continue or stop."),
            ("AutoGen layers", "Studio supports visual prototyping, AgentChat provides high-level conversational agents and teams, Core exposes event-driven primitives, and Extensions connect model clients, memory, runtimes and tools."),
            ("AgentChat contract", "AgentChat agents have unique names and useful descriptions, accept tasks through run or run_stream, emit typed messages and events, and retain state until reset. The returned TaskResult contains the run history and stop reason."),
            ("AssistantAgent", "AssistantAgent is a general preset for prototyping and education. Its contract combines a model client, system message, optional tools, model context and bounded tool iterations; specialised production agents may use narrower custom implementations."),
            ("Messages and events", "User and agent text are chat messages. Tool requests, tool results and streaming chunks are events. Operators examine both because a fluent final answer cannot prove that the correct route or evidence was used."),
            ("Model clients", "A model client separates orchestration from a provider. The course uses ReplayChatCompletionClient for reproducible offline evidence and an OpenAI client only for optional live comparison through environment-held credentials."),
            ("Typed tools", "A function name, docstring, parameter types and return shape become the tool schema. Clear read-only contracts reduce ambiguous calls and make argument validation, error handling and evidence capture testable."),
            ("State and reset", "Agents and teams retain conversation state after a run. Continue only when the next task belongs to the same thread; reset before an unrelated task so stale context does not silently influence a result."),
            ("Bounded autonomy", "Every loop needs a useful completion condition plus a hard message, tool-iteration, token or time limit. A limit is not a success signal; the stop reason must remain visible to the application."),
            ("AutoGen and CrewAI", "AutoGen AgentChat centres on typed messages, events, model clients and team presets. CrewAI organises role-based agents into crews and tasks, while Flows provide explicit event-driven control. Choose by required control, integrations and team operating model."),
            ("Worked example: OpsDesk", "A synthetic service request enters one read-only assistant. The agent looks up an incident, later retrieves handbook evidence, then grows into planner, retriever, writer and reviewer roles without gaining permission to change production systems."),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Retrieval-Augmented Generation (RAG)",
        subtitle="Knowledge preparation · chunking · lexical and vector retrieval · ranking · metadata · grounding · citations · retrieval evaluation",
        concepts=[
            ("Why RAG exists", "A model's parameters are not a current, inspectable knowledge store. RAG retrieves task-relevant evidence at run time and adds it to the model context so answers can be grounded in controlled sources."),
            ("The RAG pipeline", "Collect and approve sources, split them into usable chunks, create a searchable representation, retrieve candidates, filter and rank them, augment the prompt, generate a response, and verify the cited evidence."),
            ("Source governance", "Each chunk needs a stable source identifier, title, owner, version or date, data classification and access rule. Retrieval quality cannot compensate for stale, unauthorised or contradictory source material."),
            ("Chunk boundaries", "Chunks should preserve one coherent rule or procedure. Very small chunks lose meaning; very large chunks waste context and can hide the relevant passage. Overlap is useful when a concept crosses a boundary but creates duplicates."),
            ("Lexical retrieval", "Token or term matching is transparent, fast and effective for exact identifiers and distinctive policy language. It struggles with paraphrases and synonyms, which makes it useful as a teaching baseline and an operational fallback."),
            ("Vector retrieval", "Embeddings map meaning into vectors so semantically related wording can be close even when terms differ. Distance is only a ranking signal; top results still require access filtering, metadata checks and evidence validation."),
            ("Top-k and thresholds", "Top-k controls how many candidates enter the next stage. A minimum score can prevent weak matches from becoming context. Both settings trade recall against noise, latency and context cost and must be tuned on stable questions."),
            ("Hybrid and reranking", "Hybrid retrieval combines lexical and semantic signals. A reranker can reorder candidates for the specific query. These layers improve difficult searches but add dependencies and must preserve source metadata."),
            ("Grounded answer contract", "A grounded response separates claims from evidence, includes source identifiers, avoids unsupported additions and returns an explicit insufficient-evidence state when no approved passage supports the request."),
            ("Retrieved text is untrusted", "Documents can contain mistakes or embedded instructions. The application treats retrieved passages as data, keeps system and policy instructions authoritative, filters access first and never executes instructions found inside a source."),
            ("Retrieval evaluation", "Use stable questions with expected sources to measure whether relevant passages appear and where they rank. Examine miss cases before changing chunking, metadata, query formulation or ranking one variable at a time."),
            ("AutoGen memory options", "AgentChat accepts memory components that update model context. AutoGen Extensions includes ChromaDB vector memory, while custom Memory implementations can support other stores. The same source, retrieval and answer contracts still apply."),
            ("Worked example", "For a contractor VPN request, the transparent index should rank POL-VPN-01 first. The RAG agent may state manager approval, multi-factor enrolment and the end-date rule only when that source is present and cited."),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Implementing a Multi-Agent AI Workflow",
        subtitle="Specialist roles · round robin · selector routing · handoffs · termination · state · human control · observability · release readiness",
        concepts=[
            ("When multiple agents help", "Split work when roles need different instructions, tools, permissions, models, ownership or quality checks. Keep one agent when a single bounded instruction and tool surface remains understandable."),
            ("Role contract", "Each participant needs a unique name, capability description, task boundary, approved tools, input evidence, output format and escalation behaviour. Overlapping roles create routing ambiguity and duplicate work."),
            ("Handoff contract", "A handoff carries the task, validated context, source identifiers, constraints, expected output and remaining budget. It should not expose hidden reasoning, unrelated history or broader credentials."),
            ("RoundRobinGroupChat", "Round robin gives every participant a predictable turn and shared context. It fits drafting and review loops or demonstrations where the order is intentional, but wastes turns when some roles are not needed."),
            ("SelectorGroupChat", "A selector chooses the next speaker from names, descriptions and conversation context. It supports dynamic workflows but adds a routing decision that needs clear descriptions, candidate constraints, telemetry and fallback behaviour."),
            ("Custom selection", "A selector function can enforce deterministic state transitions and return None to defer to model selection. Custom functions are useful for policy routes but require separate serialization and recovery design."),
            ("Other team patterns", "Swarm uses handoff messages for decentralised transitions, Magentic-One targets open-ended generalist tasks, and GraphFlow expresses directed workflows. Pattern choice should follow control needs rather than novelty."),
            ("Termination", "Semantic conditions such as an approval phrase or handoff should be combined with a hard maximum message, token or time condition. The team returns a stop reason that the application must interpret separately from answer content."),
            ("State lifecycle", "Team and participant state persists after a run. Resume related work deliberately, reset unrelated work, and save or load state only at well-defined boundaries with the package and configuration version recorded."),
            ("Agent and team tools", "Agents and teams can be wrapped as tools for composition, but they are stateful. Disable parallel calls when a model could invoke the same stateful participant concurrently and create inconsistent histories."),
            ("Human control", "Pause for clarification, approval or high-impact actions. External termination can stop after the current turn, while application policy decides which requests require a person before any side effect."),
            ("Observability", "Capture a correlation identifier, selected speaker, message and event types, tool name, source IDs, stop reason, duration, model usage and errors. Redact secrets and sensitive payloads before telemetry leaves the process."),
            ("Quality and safety checks", "Test normal, missing-evidence, malformed, embedded-instruction, unsupported-action and forced-limit cases. Evaluate route and tool trajectory as well as the final response."),
            ("Cost and latency", "Every selector and specialist turn can add model calls, tokens and delay. Set budgets, cache stable retrieval, use deterministic code where appropriate and compare the team against a one-agent baseline."),
            ("Worked example", "OpsDesk first uses a writer-reviewer round robin, then a planner-retriever-writer-reviewer selector route. Both must cite POL-VPN-01, stop on approval or the hard limit, and leave the supplied tickets unchanged."),
        ],
    ),
]

# ------------------------------------------------------------------ schedule
DAY_THEMES = {
    1: "AgentChat Foundations and Grounded Retrieval",
    2: "Multi-Agent Orchestration and Operational Readiness",
}


def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:30", "9:50", 20, "admin", "Welcome, environment check, course roadmap and learning outcomes"),
            ("9:50", "10:50", 60, "topic", "Topic 1 — " + TOPICS[0]["title"] + " (concepts, architecture and worked example)"),
            ("10:50", "11:05", 15, "break", "Tea break"),
            ("11:05", "12:05", 60, "lab", "Hands-on: " + lab_titles([1])),
            ("12:05", "13:00", 55, "lab", "Hands-on: " + lab_titles([2])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:00", 60, "topic", "Topic 2 — " + TOPICS[1]["title"] + " (concepts, pipeline and worked example)"),
            ("15:00", "15:15", 15, "break", "Tea break"),
            ("15:15", "16:05", 50, "lab", "Hands-on: " + lab_titles([3])),
            ("16:05", "16:55", 50, "lab", "Hands-on: " + lab_titles([4])),
            ("16:55", "18:10", 75, "lab", "Hands-on: " + lab_titles([5])),
            ("18:10", "18:30", 20, "recap", "Day 1 recap, retrieval clinic and reflection"),
        ]),
        2: (DAY_THEMES[2], [
            ("9:30", "9:45", 15, "admin", "Day 1 recap, checkpoint recovery and Day 2 orientation"),
            ("9:45", "10:45", 60, "topic", "Topic 3 — " + TOPICS[2]["title"] + " (roles, patterns and handoff contracts)"),
            ("10:45", "11:00", 15, "break", "Tea break"),
            ("11:00", "12:00", 60, "lab", "Hands-on: " + lab_titles([6])),
            ("12:00", "13:00", 60, "lab", "Hands-on: " + lab_titles([7])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:00", 60, "topic", "Topic 3 — " + TOPICS[2]["title"] + " (termination, state, observability and operations)"),
            ("15:00", "15:15", 15, "break", "Tea break"),
            ("15:15", "18:05", 170, "lab", "Hands-on: " + lab_titles([8])),
            ("18:05", "18:30", 25, "recap", "Course recap, operational checklist, action plan and Q&A"),
        ]),
    }


# ------------------------------------------------------------------ reusable visual content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="The AgentChat System Model",
    concepts=[
        ("Task", "A new user request or message list that starts or resumes a run."),
        ("Agent", "A named, stateful component with instructions, a model client and optional tools."),
        ("Model client", "The provider adapter that creates chat completions and reports usage."),
        ("Tool", "A typed application capability executed outside the model and returned as an event."),
        ("Message", "Conversation content from a user, agent or control component."),
        ("Event", "Inspectable evidence such as a tool request, result or streaming chunk."),
        ("Team", "A stateful group that selects speakers and applies termination conditions."),
        ("Memory", "A component that retrieves relevant information into model context."),
        ("Termination", "The condition and stop reason that bound a run."),
        ("TaskResult", "The returned messages plus the reason the run stopped."),
    ],
    framework_title="The GROUND Design Lens",
    framework=[
        ("G — Goal", "Define the user outcome, non-goals and acceptable failure behaviour."),
        ("R — Roles", "Give agents and tools distinct responsibilities and least privilege."),
        ("O — Organise", "Choose retrieval, routing and handoff patterns that fit the work."),
        ("U — Use evidence", "Preserve source identifiers and validate claims against retrieved content."),
        ("N — Name limits", "Set completion, message, time, token and tool budgets."),
        ("D — Diagnose", "Record routes, events, stop reasons, errors, quality and recovery evidence."),
    ],
    statement=dict(
        headline="More agents create more interfaces—not automatically more intelligence.",
        body="Add a participant only when the boundary improves specialisation, permission control, ownership or verification enough to justify extra routing, cost and failure modes.",
        kicker="ARCHITECTURE PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Agent Core", ["Replay and optional live model clients", "A typed read-only ticket tool", "Inspectible messages and events"]),
        ("Grounded Knowledge", ["Source-labelled handbook chunks", "Stable retrieval questions", "A cited RAG answer contract"]),
        ("Bounded Team", ["Round-robin review", "Selector-based specialist routing", "Termination, regression and recovery evidence"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Understand the concept, decision and failure mode before changing code.",
        "Restore or verify the prior lab checkpoint so the shared scenario is stable.",
        "Make one bounded change using synthetic data and placeholder secrets.",
        "Run an observable command and compare its evidence with the expected result.",
        "Keep the checkpoint and reflection that prepare the next lab.",
    ],
)

LAB_SHOTS = {}

# ------------------------------------------------------------------ Learner Guide
LG_INTRO = (
    "This Learner Guide accompanies Multi Agents System with AutoGen (C1034), a two-day, 15-hour beginner course for developers, data practitioners, solution architects and AI automation professionals. It begins with the difference between a language model, an agent and a multi-agent system, then makes the AgentChat execution model visible through reproducible messages, events and stop reasons."
)

LG_INTRO2 = (
    "All eight labs extend one synthetic OpsDesk scenario. You will run a first AssistantAgent, add a typed read-only ticket tool, prepare and evaluate source-labelled knowledge, build a grounded RAG agent, compare round-robin and selector-based teams, and finish with a regression and operational readiness record. The examples target AutoGen AgentChat 0.7.5 as available on 11 August 2026 and keep paid live model calls optional."
)

LG_SETUP = dict(
    needs=[
        "A Windows, macOS or Linux laptop with Python 3.10 or later, Git and a modern code editor.",
        "Internet access for the initial package installation; the guided verification path then runs offline.",
        "The course repository cloned locally and a virtual environment created for its dependencies.",
        "Optional only: an OpenAI API key for separately labelled live comparisons. Store it in a local .env file or environment variable.",
        "Only the supplied synthetic incidents and handbook content; no customer, employee or production data is needed.",
    ],
    verify_text=(
        "From the repository root, activate the virtual environment, install the pinned starter requirements and editable starter package, then run the setup report. The expected AutoGen packages are version 0.7.5 and the final status is ready."
    ),
    verify_code=(
        "python --version\n"
        "python -m pip install -r starter/requirements.txt\n"
        "python -m pip install -e starter\n"
        "python -m opsdesk.cli setup"
    ),
    conventions=[
        "Run commands from the repository root after installing starter in editable mode, unless a step explicitly changes directory.",
        "Use --offline for the required reproducible evidence. Optional live output is compared separately and never replaces the offline checkpoint.",
        "Replace placeholders such as <OPENAI_API_KEY> locally; never commit a real secret or paste it into a prompt, screenshot or evidence file.",
        "Use the supplied INC-1001 to INC-1003 incidents and POL-/PROC- source identifiers only.",
        "Inspect .course_state after every run; it holds the JSON evidence needed by later labs and is intentionally ignored by Git.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic incidents and handbook. Keep tools read-only, store optional provider credentials outside Git, and never place a secret in prompts, screenshots, commands or saved evidence."
)

LG_WRAPUP = dict(
    title="Wrap-Up",
    intro=(
        "You have taken one application from a single bounded AgentChat assistant to a source-grounded specialist team. The durable skill is not creating many agents; it is making every role, tool, evidence source, handoff and stopping decision explicit enough to test and operate."
    ),
    sections=[
        dict(title="What You Can Now Do", bullets=[
            "Explain AgentChat messages, events, state and TaskResult evidence.",
            "Create an AssistantAgent with a reproducible offline client and a typed read-only tool.",
            "Prepare, rank and evaluate source-labelled knowledge for RAG.",
            "Build grounded responses with citations and an insufficient-evidence route.",
            "Choose and bound round-robin or selector-based team workflows.",
            "Verify routes, termination, guardrails and recovery before a guided demonstration.",
        ]),
        dict(title="Architecture Habits", bullets=[
            "Start with one agent and split only when a role boundary earns its coordination cost.",
            "Treat names, descriptions, tool schemas, handoffs and stop reasons as application contracts.",
            "Keep source metadata attached through retrieval, generation and review.",
            "Use deterministic code for policy and predictable transitions; reserve model choice for genuine ambiguity.",
            "Compare trajectory evidence as well as the final response.",
        ]),
        dict(title="Authoritative References Used", bullets=[
            "AutoGen stable documentation: https://microsoft.github.io/autogen/stable/",
            "AgentChat agents and tools: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html",
            "AgentChat teams and termination: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html",
            "AgentChat memory and RAG: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html",
            "CrewAI concepts: https://docs.crewai.com/",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "Repeat the full offline path without the guide and explain every message, event, source and stop reason.",
    "Replace the teaching lexical index with an approved vector memory while preserving the stable source identifiers and retrieval questions.",
    "Add ten representative normal and edge cases for your own domain before considering a sandbox deployment.",
    "Map every agent and tool to a named owner, identity, credential scope, data classification and recovery action.",
    "Export redacted traces to an approved observability platform and define latency, error, cost and unsupported-claim alerts.",
]

LG_GLOSSARY = [
    ("Agent", "A model-driven component with instructions, messages, state, tools and an execution boundary."),
    ("AgentChat", "AutoGen's high-level framework for conversational single-agent and multi-agent applications."),
    ("AutoGen Core", "The event-driven framework layer for lower-level, scalable and distributed multi-agent systems."),
    ("AssistantAgent", "A general AgentChat preset that combines a model client, system message, optional tools and model context."),
    ("Model client", "An adapter that sends model requests, returns typed completion results and reports usage."),
    ("Replay model client", "A deterministic client that replays predefined completions for reproducible development and verification."),
    ("Message", "Conversation content emitted by a user, agent or control component."),
    ("Event", "Structured runtime evidence such as a tool request, tool result, streaming chunk or internal action."),
    ("TaskResult", "The messages produced during a run together with its stop reason."),
    ("Tool", "A typed application function or workbench capability that an agent can request."),
    ("RAG", "Retrieval-Augmented Generation: retrieving approved evidence and adding it to model context before generation."),
    ("Chunk", "A coherent, source-labelled unit of knowledge prepared for indexing and retrieval."),
    ("Embedding", "A numeric representation used to compare semantic similarity between queries and content."),
    ("Grounding", "Constraining response claims to retrieved evidence and preserving source identifiers."),
    ("RoundRobinGroupChat", "An AgentChat team preset that gives participants turns in a fixed repeating order."),
    ("SelectorGroupChat", "An AgentChat team preset that dynamically chooses the next speaker from context and role descriptions."),
    ("Termination condition", "A stateful rule that returns a stop signal after a team response; conditions can be combined."),
    ("Handoff", "A controlled transition that gives another participant a task, validated context, evidence and constraints."),
    ("Guardrail", "A policy or validation layer around input, retrieval, tools, routing, output or human approval."),
    ("Stop reason", "The machine-readable explanation for why an agent or team run ended."),
]

NEXT_STEPS = dict(
    title="From Classroom Workflow to Controlled Pilot",
    items=[
        "Keep the offline regression path as the reproducible baseline.",
        "Change one model, retriever or routing variable at a time and compare evidence.",
        "Add domain owners, access controls, telemetry and a rollback path before connecting live systems.",
        "Rehearse missing evidence, forced limits and provider failure—not only the normal case.",
    ],
)

VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release aligned across slide deck, Learner Guide, Lesson Plan, and eight connected labs.", TRAINER),
]

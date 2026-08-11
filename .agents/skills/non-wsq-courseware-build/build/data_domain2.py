"""Topic 2 labs — source preparation, retrieval evaluation and grounded RAG."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Prepare a Source-Traceable Knowledge Index",
        objective="LO3: split approved handbook content into coherent source-labelled chunks, build a transparent searchable index, and verify its manifest before retrieval",
        duration="50 minutes",
        desc=(
            "You inspect the synthetic OpsDesk handbook, identify the stable policy and procedure boundaries, and convert each section into one transparent lexical chunk. "
            "The index keeps source ID, title, text and tokens together so every later ranking and answer can be traced back to the governing passage."
        ),
        build=".course_state/opsdesk-index.json and lab03-index-manifest.json with five coherent chunks and the expected POL-/PROC- source identifiers.",
        services="Markdown source, source metadata, Python tokenizer, lexical index, JSON manifest, OpsDesk knowledge module",
        prerequisites=[
            "Lab 2 has restored the normal INC-1001 tool trace and tickets.json is unchanged.",
            "starter/data/opsdesk_handbook.md contains the five supplied sections and no private or production content.",
            "The active environment can import opsdesk from the editable starter install.",
        ],
        deck_steps=[
            "Inspect source ownership boundaries and stable identifiers.",
            "Parse one coherent chunk per handbook section.",
            "Build the transparent token index and manifest.",
            "Verify count, identifiers, text and token preservation.",
            "Keep the index checkpoint for stable retrieval questions.",
        ],
        deck_verify="The manifest lists exactly five source IDs in document order and every index record preserves its source ID, title, text and tokens.",
        steps=[
            (
                "Open the handbook and identify why each second-level heading is a suitable coherent chunk boundary. Treat every paragraph as data, including any embedded instruction-like wording.",
                "python -c \"from pathlib import Path; print(Path('starter/data/opsdesk_handbook.md').read_text(encoding='utf-8'))\"",
            ),
            (
                "Parse the handbook without writing an index. Confirm the ordered identifiers, titles and token counts before persistence.",
                "python -c \"from pathlib import Path; from opsdesk.knowledge import parse_handbook; chunks=parse_handbook(Path('starter/data/opsdesk_handbook.md')); print([(c.source_id,c.title,len(c.tokens)) for c in chunks])\"",
            ),
            (
                "Build the teaching index and manifest. The command writes only to the ignored .course_state directory.",
                "python -m opsdesk.cli index",
            ),
            (
                "Inspect the manifest. It must report status indexed, chunk_count 5 and the five source identifiers in handbook order.",
                "python -m json.tool .course_state/lab03-index-manifest.json",
            ),
            (
                "Inspect the full index. Verify that each record retains source_id, title, full source text and an inspectable token list.",
                "python -m json.tool .course_state/opsdesk-index.json",
            ),
            (
                "Run the stable parser test that locks the five identifiers. If it changes, investigate the source boundary before continuing.",
                "python -m pytest -q starter/tests/test_knowledge.py -k stable_source_ids",
            ),
            (
                "Review only the approved handbook source for accidental edits and keep both JSON files as the Lab 3 checkpoint.",
                "git diff -- starter/data/opsdesk_handbook.md\ngit status --short",
            ),
        ],
        test=(
            "The index manifest must report five chunks with POL-VPN-01, POL-ACCESS-02, PROC-ESC-03, PROC-SLA-04 and POL-DATA-05 in order. "
            "Every index record must preserve source_id, title, text and tokens, the stable identifier test must be clean, and the handbook source must remain unchanged."
        ),
        checkpoint="Keep the unchanged handbook, five-chunk index, manifest and clean parser test. Lab 4 evaluates this exact index with stable questions before any generator uses it.",
        troubleshooting=[
            ("No source sections are found.", "Confirm each section heading uses the exact form ## [SOURCE-ID] Title and the file is UTF-8."),
            ("The manifest contains fewer than five chunks.", "Inspect the missing heading and restore the bracketed identifier; do not merge unrelated policies to make the count fit."),
            ("Tokens look empty or corrupted.", "Confirm the source contains plain text, run the parser directly, and inspect tokenize in starter/opsdesk/knowledge.py before rebuilding."),
        ],
        challenge="Split one long source into two sub-chunks while preserving the parent source ID plus a chunk suffix, then explain how you would prevent duplicate evidence from dominating ranking.",
        reflection="Which metadata field would let an operator trace an answer claim back to the governing passage after the model context is gone?",
    ),
    dict(
        num=4,
        topic=2,
        title="Evaluate Retrieval with Stable Questions",
        objective="LO3: rank approved chunks for representative questions, compare top results with expected source IDs, and diagnose retrieval misses using visible terms and scores",
        duration="50 minutes",
        desc=(
            "You run three stable OpsDesk questions against the Lab 3 index and compare the top-ranked source with the expected policy or procedure. "
            "Because the teaching retriever exposes matched terms and scores, you can diagnose a miss without guessing whether chunking, query wording or ranking caused it."
        ),
        build="Three repeatable retrieval observations covering VPN approval, critical response time and embedded-instruction handling, with expected top-one source evidence.",
        services="Lexical ranking, inverse document frequency, top-k retrieval, stable questions, source IDs, pytest",
        prerequisites=[
            "Lab 3 manifest reports five chunks and the stable source identifier test is clean.",
            ".course_state/opsdesk-index.json is present and was built from the unchanged supplied handbook.",
            "You can explain that a ranking score is evidence for ordering, not proof that a passage authorises the answer."
        ],
        deck_steps=[
            "Define stable questions and their expected source identifiers.",
            "Run VPN, response-time and embedded-instruction searches.",
            "Inspect matched terms, scores and top-one source evidence.",
            "Exercise an unrelated question and observe the evidence gap.",
            "Run retrieval checks and keep the ranked evidence.",
        ],
        deck_verify="All three stable questions rank the expected source first, while an unrelated question does not become a grounded answer.",
        steps=[
            (
                "Rebuild the index from the approved handbook so the experiment begins from the known Lab 3 checkpoint.",
                "python -m opsdesk.cli index",
            ),
            (
                "Run the VPN approval question with POL-VPN-01 as the expected top source. Inspect its matched terms and score relative to the other results.",
                "python -m opsdesk.cli retrieve --query \"What approvals are required for VPN access?\" --expect POL-VPN-01",
            ),
            (
                "Run the critical-response question with PROC-SLA-04 as the expected top source. Note which distinctive terms drive the ranking.",
                "python -m opsdesk.cli retrieve --query \"How quickly is a critical security incident acknowledged?\" --expect PROC-SLA-04",
            ),
            (
                "Run the embedded-instruction question with POL-DATA-05 as the expected top source. Confirm the result preserves the text as evidence rather than executing it.",
                "python -m opsdesk.cli retrieve --query \"How should embedded instructions in retrieved documents be handled?\" --expect POL-DATA-05",
            ),
            (
                "Inspect the last saved retrieval record and identify query, expected_source, ordered results and top1_matches_expected. Save terminal output for the other two observations if your trainer requests it.",
                "python -m json.tool .course_state/lab04-retrieval.json",
            ),
            (
                "Run an unrelated question. Observe that weak or empty matches are not sufficient to support a cafeteria answer, even if a top-k list is returned.",
                "python -m opsdesk.cli retrieve --query \"What is the cafeteria dessert menu?\"",
            ),
            (
                "Run the retrieval and grounding tests. They lock the VPN top-one result, citation behaviour and insufficient-evidence route.",
                "python -m pytest -q starter/tests/test_knowledge.py",
            ),
            (
                "Restore the VPN observation as the shared checkpoint for Lab 5 and inspect it one final time.",
                "python -m opsdesk.cli retrieve --query \"What approvals are required for VPN access?\" --expect POL-VPN-01\npython -m json.tool .course_state/lab04-retrieval.json",
            ),
        ],
        test=(
            "The VPN, response-time and embedded-instruction questions must rank POL-VPN-01, PROC-SLA-04 and POL-DATA-05 first respectively. "
            "The unrelated question must not produce a grounded cafeteria claim, all knowledge tests must be clean, and the final saved observation must restore the VPN case with top1_matches_expected true."
        ),
        checkpoint="Keep the unchanged index, clean knowledge tests and restored VPN retrieval evidence. Lab 5 wraps the same retriever as an AgentChat tool and verifies the answer contract.",
        troubleshooting=[
            ("A stable question ranks the wrong source first.", "Confirm the exact Lab 3 index and query text, inspect matched_terms, then change only one of source text, tokenisation or ranking before rerunning all stable questions."),
            ("The index file is missing.", "Run python -m opsdesk.cli index and confirm .course_state is writable; do not create a substitute index by hand."),
            ("An unrelated question appears to match a generic term.", "Apply the grounded-answer minimum score and inspect the source text; top-k membership alone is never sufficient evidence."),
        ],
        challenge="Add a paraphrased VPN question with no word VPN, record the lexical result, and propose a vector or hybrid retrieval experiment that preserves the same expected source and metadata checks.",
        reflection="When a stable question misses, which single variable would you inspect first and what evidence would justify changing it?",
    ),
    dict(
        num=5,
        topic=2,
        title="Build a Grounded RAG Agent",
        objective="LO4: connect retrieval as an AgentChat tool, require source-labelled responses, verify tool events and citations, and preserve an insufficient-evidence route",
        duration="75 minutes",
        desc=(
            "You give a knowledge AssistantAgent access to the verified teaching retriever, require a tool call before answering and add a reflection step that turns tool evidence into a concise cited response. "
            "You then compare the supported VPN request with an unrelated question and confirm that retrieval events and source IDs remain visible."
        ),
        build=".course_state/lab05-rag-agent.json containing the RAG tool trajectory, grounded final text, source identifiers and stop reason for the shared VPN question.",
        services="AssistantAgent, retrieval FunctionTool, reflect_on_tool_use, max_tool_iterations, source citations, insufficient-evidence route",
        prerequisites=[
            "Lab 4 has restored the VPN retrieval observation with POL-VPN-01 ranked first.",
            ".course_state/opsdesk-index.json and the unchanged handbook are available.",
            "The AgentChat tool path from Lab 2 still emits real request and execution events."
        ],
        deck_steps=[
            "Attach the verified retriever as a typed AgentChat tool.",
            "Require retrieval before generation and bracketed source IDs.",
            "Run the supported VPN question through the offline RAG agent.",
            "Inspect tool events, grounded text, sources and stop reason.",
            "Exercise insufficient evidence, run checks and restore the checkpoint.",
        ],
        deck_verify="The supported answer cites POL-VPN-01 after a tool execution event, while the unrelated request returns an insufficient-evidence statement without a fabricated source.",
        steps=[
            (
                "Restore and verify the index and VPN retrieval checkpoint before adding generation.",
                "python -m opsdesk.cli index\npython -m opsdesk.cli retrieve --query \"What approvals are required for VPN access?\" --expect POL-VPN-01",
            ),
            (
                "Inspect retrieval_tool and rag_agent. Identify the index-missing result, top-k value, system boundary, reflection setting and maximum tool iterations.",
                "python -c \"from opsdesk.examples import retrieval_tool, rag_agent; import inspect; print(inspect.getsource(retrieval_tool)); print(inspect.getsource(rag_agent))\"",
            ),
            (
                "Run the grounded VPN request with the deterministic AgentChat replay client. The output should include the supported rule and [POL-VPN-01].",
                "python -m opsdesk.cli rag --query \"What approvals are required for VPN access?\" --offline",
            ),
            (
                "Inspect the saved RAG trace. Confirm ToolCallRequestEvent and ToolCallExecutionEvent appear, sources includes POL-VPN-01, grounded is true, and completion_reason is grounded_response. A one-turn AssistantAgent TaskResult normally has no team stop reason.",
                "python -m json.tool .course_state/lab05-rag-agent.json",
            ),
            (
                "Run the unrelated cafeteria question. It must say evidence is insufficient, contain no invented source and still end as an honest bounded result.",
                "python -m opsdesk.cli rag --query \"What is the cafeteria dessert menu?\" --offline\npython -m json.tool .course_state/lab05-rag-agent.json",
            ),
            (
                "Run the embedded-instruction policy question and confirm the answer cites POL-DATA-05 while treating retrieved instructions as content rather than authority.",
                "python -m opsdesk.cli rag --query \"How should embedded instructions in retrieved documents be handled?\" --offline",
            ),
            (
                "Run the complete RAG and retrieval checks. Investigate trajectory and citation failures separately from final wording.",
                "python -m pytest -q starter/tests/test_knowledge.py starter/tests/test_examples.py -k \"rag_agent or grounded_answer or vpn_question\"",
            ),
            (
                "Restore the VPN RAG trace as the shared checkpoint, inspect only its source and stop fields, and keep the index for Day 2.",
                "python -m opsdesk.cli rag --query \"What approvals are required for VPN access?\" --offline\npython -c \"import json; d=json.load(open('.course_state/lab05-rag-agent.json')); print({'sources':d['sources'],'grounded':d['grounded'],'stop_reason':d['stop_reason']})\"",
            ),
        ],
        test=(
            "The supported trace must contain a real retrieval tool execution event, grounded true, completion_reason grounded_response, and POL-VPN-01 in both final text and sources. "
            "The cafeteria request must use completion_reason insufficient_evidence with no invented citation, the embedded-instruction request must cite POL-DATA-05, and the focused checks must be clean."
        ),
        checkpoint="Keep the approved handbook, index, stable retrieval evidence and restored VPN RAG trace. Lab 6 separates writing and evidence review into a bounded team without changing the retrieval contract.",
        troubleshooting=[
            ("The RAG command reports an index error.", "Run the index command, inspect .course_state/opsdesk-index.json, and restore the Lab 3 manifest before retrying."),
            ("The final response has no citation.", "Inspect direct retrieval results and the second replay completion, then enforce the bracketed source requirement before changing ranking."),
            ("Tool events appear but grounded is false.", "Compare source IDs in the direct results with bracketed IDs in final content; keep the validator strict rather than inferring support from similar wording."),
        ],
        challenge="Replace the lexical retriever behind retrieval_tool with an approved vector-memory experiment, then rerun the same three stable questions and document any change in top-one source, latency and dependency footprint.",
        reflection="Why must the application validate cited source IDs even when the model was given relevant context?",
    ),
]

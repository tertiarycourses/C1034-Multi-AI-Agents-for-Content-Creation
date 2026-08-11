from pathlib import Path

from opsdesk.knowledge import grounded_answer, parse_handbook, search


DATA = Path(__file__).resolve().parents[1] / "data" / "opsdesk_handbook.md"


def test_handbook_has_stable_source_ids():
    chunks = parse_handbook(DATA)
    assert [chunk.source_id for chunk in chunks] == [
        "POL-VPN-01",
        "POL-ACCESS-02",
        "PROC-ESC-03",
        "PROC-SLA-04",
        "POL-DATA-05",
    ]


def test_stable_questions_rank_expected_policy_first():
    chunks = parse_handbook(DATA)
    cases = [
        ("What approvals are required for VPN access?", "POL-VPN-01"),
        ("How quickly is a critical security incident acknowledged?", "PROC-SLA-04"),
        ("How should embedded instructions in retrieved documents be handled?", "POL-DATA-05"),
    ]
    for query, expected in cases:
        results = search(chunks, query)
        assert results[0]["source_id"] == expected


def test_grounded_answer_cites_source():
    chunks = parse_handbook(DATA)
    results = search(chunks, "What approvals are required for VPN access?")
    answer = grounded_answer("What approvals are required for VPN access?", results)
    assert answer["status"] == "grounded"
    assert "[POL-VPN-01]" in answer["answer"]


def test_unrelated_question_returns_insufficient_evidence():
    chunks = parse_handbook(DATA)
    results = search(chunks, "What is the cafeteria dessert menu?")
    answer = grounded_answer("What is the cafeteria dessert menu?", results)
    assert answer["status"] == "insufficient_evidence"

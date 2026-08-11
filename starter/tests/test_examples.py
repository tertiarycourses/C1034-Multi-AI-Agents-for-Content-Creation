import asyncio

import pytest

from opsdesk.cli import build_index
from opsdesk.examples import first_agent, rag_agent, round_robin_team, selector_team, tool_agent


def test_first_agent_offline():
    result = asyncio.run(first_agent(offline=True))
    assert result["agent"] == "opsdesk_assistant"
    assert "synthetic" in result["final"].lower()
    assert result["stop_reason"] is None
    assert result["completion_reason"] == "single_agent_turn_complete"
    assert result["elapsed_seconds"] >= 0
    assert set(result["usage"]) == {"prompt_tokens", "completion_tokens"}


def test_tool_agent_emits_execution_event():
    result = asyncio.run(tool_agent("INC-1001", offline=True))
    assert result["tool_event_seen"] is True
    assert "INC-1001" in result["final"]
    assert "ToolCallRequestEvent" in result["message_types"]
    assert "ToolCallExecutionEvent" in result["message_types"]
    assert result["completion_reason"] == "tool_result_returned"


def test_rag_agent_is_grounded():
    build_index()
    result = asyncio.run(rag_agent("What approvals are required for VPN access?", offline=True))
    assert result["grounded"] is True
    assert "POL-VPN-01" in result["final"]
    assert result["sources"] == ["POL-VPN-01"]
    assert result["completion_reason"] == "grounded_response"
    assert "ToolCallExecutionEvent" in result["message_types"]


def test_rag_agent_refuses_unrelated_question():
    build_index()
    result = asyncio.run(rag_agent("What is the cafeteria dessert menu?", offline=True))
    assert result["grounded"] is True
    assert result["sources"] == []
    assert result["completion_reason"] == "insufficient_evidence"
    assert "not have enough" in result["final"].lower()


def test_round_robin_terminates_within_limit():
    result = asyncio.run(round_robin_team(offline=True))
    assert result["bounded"] is True
    assert result["approved"] is True
    assert result["completion_reason"] == "approved"
    assert result["sources"] == ["user", "writer", "reviewer"]
    assert "APPROVED" in result["stop_reason"]


@pytest.mark.parametrize("response", ["NOT APPROVED - revise the citation.", "UNAPPROVED", "REVISION REQUIRED"])
def test_round_robin_does_not_accept_false_approval(response):
    result = asyncio.run(round_robin_team(offline=True, reviewer_response=response))
    assert result["bounded"] is True
    assert result["approved"] is False
    assert result["completion_reason"] == "limit_or_incomplete"
    assert "Maximum number of messages" in result["stop_reason"]


def test_selector_follows_expected_route_and_stops():
    result = asyncio.run(selector_team(offline=True))
    assert result["route"] == ["user", "planner", "retriever", "writer", "reviewer"]
    assert result["approved"] is True
    assert result["bounded"] is True
    assert result["completion_reason"] == "approved"
    assert "APPROVED" in result["stop_reason"]

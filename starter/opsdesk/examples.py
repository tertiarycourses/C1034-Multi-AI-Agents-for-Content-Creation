"""AutoGen AgentChat examples with deterministic offline model clients."""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Sequence

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TerminatedException, TerminationCondition
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.messages import BaseAgentEvent, BaseChatMessage, StopMessage
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat
from autogen_core import CancellationToken, FunctionCall
from autogen_core.models import CreateResult, RequestUsage
from autogen_core.tools import FunctionTool
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.replay import ReplayChatCompletionClient

from .knowledge import grounded_answer, load_index, search


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "starter" / "data"
STATE_DIR = ROOT / ".course_state"


def _state_path(filename: str) -> Path:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    return STATE_DIR / filename


def _write_evidence(filename: str, payload: dict[str, object]) -> Path:
    path = _state_path(filename)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def _model_client(offline: bool, replay: Sequence[str | CreateResult]):
    if offline:
        return ReplayChatCompletionClient(
            list(replay),
            model_info={
                "vision": False,
                "function_calling": True,
                "json_output": False,
                "family": "unknown",
                "structured_output": False,
            },
        )
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for a live run")
    return OpenAIChatCompletionClient(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        parallel_tool_calls=False,
        max_tokens=int(os.getenv("OPENAI_MAX_TOKENS", "300")),
    )


async def close_client(client: object) -> None:
    close = getattr(client, "close", None)
    if close is not None:
        await close()


def usage_summary(messages: Sequence[object]) -> dict[str, int]:
    prompt_tokens = 0
    completion_tokens = 0
    for message in messages:
        usage = getattr(message, "models_usage", None)
        if usage is not None:
            prompt_tokens += int(getattr(usage, "prompt_tokens", 0) or 0)
            completion_tokens += int(getattr(usage, "completion_tokens", 0) or 0)
    return {"prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens}


class ExactTextTermination(TerminationCondition):
    """Stop only when an allowed source emits one exact semantic marker."""

    def __init__(self, text: str, sources: Sequence[str] | None = None) -> None:
        self._text = text
        self._sources = set(sources) if sources is not None else None
        self._terminated = False

    @property
    def terminated(self) -> bool:
        return self._terminated

    async def __call__(self, messages: Sequence[BaseAgentEvent | BaseChatMessage]) -> StopMessage | None:
        if self._terminated:
            raise TerminatedException("Termination condition has already been reached")
        for message in messages:
            if self._sources is not None and message.source not in self._sources:
                continue
            if message.to_text().strip() == self._text:
                self._terminated = True
                return StopMessage(
                    content=f"Exact marker '{self._text}' received from '{message.source}'",
                    source="ExactTextTermination",
                )
        return None

    async def reset(self) -> None:
        self._terminated = False


def exact_approval(messages: Sequence[object], stop_reason: object) -> bool:
    if not messages:
        return False
    final = str(getattr(messages[-1], "content", "")).strip()
    return final == "APPROVED" and "Exact marker 'APPROVED'" in str(stop_reason)


async def first_agent(offline: bool = True) -> dict[str, object]:
    client = _model_client(offline, ["OpsDesk is ready. I will use synthetic data, cite sources, and stop when evidence is insufficient."])
    agent = AssistantAgent(
        "opsdesk_assistant",
        description="Explains the bounded OpsDesk learning scenario.",
        model_client=client,
        system_message="Use only synthetic course data. State boundaries clearly.",
    )
    started = time.perf_counter()
    result = await agent.run(task="Introduce the OpsDesk scenario and its safety boundary in one sentence.")
    payload = {
        "mode": "offline" if offline else "live",
        "agent": agent.name,
        "message_types": [type(message).__name__ for message in result.messages],
        "final": str(result.messages[-1].content),
        "stop_reason": result.stop_reason,
        "completion_reason": "single_agent_turn_complete",
        "elapsed_seconds": round(time.perf_counter() - started, 4),
        "usage": usage_summary(result.messages),
    }
    _write_evidence("lab01-first-agent.json", payload)
    await close_client(client)
    return payload


def lookup_ticket(ticket_id: str) -> str:
    """Return one synthetic ticket by exact identifier."""
    tickets = json.loads((DATA_DIR / "tickets.json").read_text(encoding="utf-8"))
    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            return json.dumps({"status": "found", "ticket": ticket})
    return json.dumps({"status": "not_found", "ticket_id": ticket_id})


def _tool_call(name: str, arguments: dict[str, object], call_id: str) -> CreateResult:
    return CreateResult(
        finish_reason="function_calls",
        content=[FunctionCall(id=call_id, name=name, arguments=json.dumps(arguments))],
        usage=RequestUsage(prompt_tokens=0, completion_tokens=0),
        cached=False,
    )


async def tool_agent(ticket_id: str, offline: bool = True) -> dict[str, object]:
    replay = [_tool_call("lookup_ticket", {"ticket_id": ticket_id}, "course-call-1")]
    client = _model_client(offline, replay)
    agent = AssistantAgent(
        "ticket_reader",
        description="Reads one synthetic incident by exact identifier.",
        model_client=client,
        tools=[lookup_ticket],
        system_message="Use lookup_ticket once. Never invent a missing ticket.",
    )
    started = time.perf_counter()
    result = await agent.run(task=f"Retrieve {ticket_id} and return the tool result.")
    payload = {
        "mode": "offline" if offline else "live",
        "agent": agent.name,
        "message_types": [type(message).__name__ for message in result.messages],
        "tool_event_seen": any(type(message).__name__ == "ToolCallExecutionEvent" for message in result.messages),
        "final": str(result.messages[-1].content),
        "stop_reason": result.stop_reason,
        "completion_reason": "tool_result_returned",
        "elapsed_seconds": round(time.perf_counter() - started, 4),
        "usage": usage_summary(result.messages),
    }
    _write_evidence("lab02-tool-agent.json", payload)
    await close_client(client)
    return payload


def retrieval_tool(query: str) -> str:
    """Search the current OpsDesk teaching index and return ranked evidence."""
    index_path = _state_path("opsdesk-index.json")
    if not index_path.exists():
        return json.dumps({"status": "index_missing", "results": []})
    return json.dumps({"status": "ok", "results": search(load_index(index_path), query, top_k=3)})


async def rag_agent(query: str, offline: bool = True) -> dict[str, object]:
    direct_results = search(load_index(_state_path("opsdesk-index.json")), query, top_k=3)
    expected = grounded_answer(query, direct_results)
    replay: list[str | CreateResult] = [
        _tool_call("retrieval_tool", {"query": query}, "course-call-rag"),
        str(expected["answer"]),
    ]
    client = _model_client(offline, replay)
    agent = AssistantAgent(
        "knowledge_agent",
        description="Answers OpsDesk questions only from ranked handbook evidence.",
        model_client=client,
        tools=[retrieval_tool],
        reflect_on_tool_use=True,
        max_tool_iterations=2,
        system_message=(
            "Call retrieval_tool before answering. Cite bracketed source IDs. "
            "If evidence is missing, say that evidence is insufficient."
        ),
    )
    started = time.perf_counter()
    result = await agent.run(task=query)
    final = str(result.messages[-1].content)
    sources = [item["source_id"] for item in direct_results if f"[{item['source_id']}]" in final]
    payload = {
        "mode": "offline" if offline else "live",
        "query": query,
        "message_types": [type(message).__name__ for message in result.messages],
        "final": final,
        "sources": sources,
        "grounded": bool(sources) or expected["status"] == "insufficient_evidence",
        "stop_reason": result.stop_reason,
        "completion_reason": expected["status"] if expected["status"] == "insufficient_evidence" else "grounded_response",
        "elapsed_seconds": round(time.perf_counter() - started, 4),
        "usage": usage_summary(result.messages),
    }
    _write_evidence("lab05-rag-agent.json", payload)
    await close_client(client)
    return payload


async def round_robin_team(offline: bool = True, reviewer_response: str = "APPROVED") -> dict[str, object]:
    writer_client = _model_client(
        offline,
        ["Draft: VPN access needs manager approval and MFA enrolment [POL-VPN-01]."] * 3,
    )
    reviewer_client = _model_client(
        offline,
        [reviewer_response] * 3,
    )
    writer = AssistantAgent(
        "writer",
        description="Writes a concise answer from supplied evidence.",
        model_client=writer_client,
        system_message="Write one grounded answer with source identifiers.",
    )
    reviewer = AssistantAgent(
        "reviewer",
        description="Checks evidence, citations and unsupported claims.",
        model_client=reviewer_client,
        system_message="Reply with exactly APPROVED only when the answer is grounded; otherwise state the defect without that marker.",
    )
    termination = ExactTextTermination("APPROVED", sources=["reviewer"]) | MaxMessageTermination(max_messages=6)
    team = RoundRobinGroupChat([writer, reviewer], termination_condition=termination)
    started = time.perf_counter()
    result = await team.run(task="Answer the VPN approval question using [POL-VPN-01].")
    approved = exact_approval(result.messages, result.stop_reason)
    payload = {
        "mode": "offline" if offline else "live",
        "participants": [writer.name, reviewer.name],
        "sources": [message.source for message in result.messages],
        "message_count": len(result.messages),
        "stop_reason": result.stop_reason,
        "bounded": len(result.messages) <= 6,
        "approved": approved,
        "completion_reason": "approved" if approved else "limit_or_incomplete",
        "elapsed_seconds": round(time.perf_counter() - started, 4),
        "usage": usage_summary(result.messages),
    }
    _write_evidence("lab06-round-robin.json", payload)
    await close_client(writer_client)
    await close_client(reviewer_client)
    return payload


def _route_selector(messages: Sequence[BaseAgentEvent | BaseChatMessage]) -> str | None:
    last_source = messages[-1].source
    route = {
        "user": "planner",
        "planner": "retriever",
        "retriever": "writer",
        "writer": "reviewer",
        "reviewer": "planner",
    }
    return route.get(last_source)


async def selector_team(offline: bool = True) -> dict[str, object]:
    responses = {
        "planner": "Plan: retrieve the governing policy, draft from evidence, then review the citation.",
        "retriever": "Evidence: manager approval and MFA enrolment are required [POL-VPN-01].",
        "writer": "VPN access requires manager approval and MFA enrolment [POL-VPN-01].",
        "reviewer": "APPROVED",
    }
    agents: list[AssistantAgent] = []
    clients: list[object] = []
    descriptions = {
        "planner": "Creates the bounded task plan and closes an approved run.",
        "retriever": "Returns source-labelled OpsDesk handbook evidence.",
        "writer": "Produces the concise evidence-grounded response.",
        "reviewer": "Checks support and source identifiers before approval.",
    }
    for name in ("planner", "retriever", "writer", "reviewer"):
        client = _model_client(offline, [responses[name]])
        clients.append(client)
        agents.append(AssistantAgent(name, description=descriptions[name], model_client=client))
    selector_client = _model_client(offline, ["planner"])
    clients.append(selector_client)
    termination = ExactTextTermination("APPROVED", sources=["reviewer"]) | MaxMessageTermination(max_messages=8)
    team = SelectorGroupChat(
        agents,
        model_client=selector_client,
        selector_func=_route_selector,
        termination_condition=termination,
        allow_repeated_speaker=False,
    )
    started = time.perf_counter()
    result = await team.run(task="Create a grounded response for the VPN approval request.")
    approved = exact_approval(result.messages, result.stop_reason)
    payload = {
        "mode": "offline" if offline else "live",
        "participants": [agent.name for agent in agents],
        "route": [message.source for message in result.messages],
        "message_count": len(result.messages),
        "stop_reason": result.stop_reason,
        "approved": approved,
        "bounded": len(result.messages) <= 8,
        "completion_reason": "approved" if approved else "limit_or_incomplete",
        "elapsed_seconds": round(time.perf_counter() - started, 4),
        "usage": usage_summary(result.messages),
    }
    _write_evidence("lab07-selector-team.json", payload)
    for client in clients:
        await close_client(client)
    return payload


async def inspect_tool_schema() -> dict[str, object]:
    tool = FunctionTool(lookup_ticket, description="Return one synthetic ticket by exact identifier")
    result = await tool.run_json({"ticket_id": "INC-1001"}, CancellationToken())
    return {"schema": tool.schema, "result": result}

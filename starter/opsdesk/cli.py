"""Command-line interface used verbatim by the C1034 labs."""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import importlib.metadata
import json
import os
import platform
import re
import shutil
import sys
from pathlib import Path

from .examples import DATA_DIR, STATE_DIR, first_agent, rag_agent, round_robin_team, selector_team, tool_agent
from .knowledge import grounded_answer, load_index, parse_handbook, save_index, search


EXPECTED_AUTOGEN_VERSION = "0.7.5"
EXPECTED_SOURCE_HASHES = {
    "tickets.json": "b8820c8b918829c801877ae1ad6fb0cf12ad4bcbb982fed2a3d25118ad589a3c",
    "opsdesk_handbook.md": "f522b927818c53593d9820303769259a8d74f409e4f8d984a750d8f1c9cff947",
}
REPO_ROOT = DATA_DIR.parents[1]


def emit(payload: object) -> None:
    print(json.dumps(payload, indent=2, default=str))


def setup_report() -> dict[str, object]:
    versions = {}
    for package in ("autogen-agentchat", "autogen-ext"):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = "missing"
    versions_ready = all(versions.get(package) == EXPECTED_AUTOGEN_VERSION for package in ("autogen-agentchat", "autogen-ext"))
    payload = {
        "python": platform.python_version(),
        "python_supported": sys.version_info >= (3, 10),
        "packages": versions,
        "data_files": sorted(path.name for path in DATA_DIR.iterdir()),
        "expected_autogen_version": EXPECTED_AUTOGEN_VERSION,
        "versions_ready": versions_ready,
        "status": "ready" if sys.version_info >= (3, 10) and versions_ready else "not_ready",
    }
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    (STATE_DIR / "lab01-environment.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def build_index() -> dict[str, object]:
    chunks = parse_handbook(DATA_DIR / "opsdesk_handbook.md")
    path = save_index(chunks, STATE_DIR / "opsdesk-index.json")
    manifest = {
        "index": str(path),
        "chunk_count": len(chunks),
        "source_ids": [chunk.source_id for chunk in chunks],
        "status": "indexed",
    }
    (STATE_DIR / "lab03-index-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def retrieve(query: str, expect: str | None) -> dict[str, object]:
    results = search(load_index(STATE_DIR / "opsdesk-index.json"), query, top_k=3)
    payload = {
        "query": query,
        "expected_source": expect,
        "results": results,
        "top1_matches_expected": bool(results) and (expect is None or results[0]["source_id"] == expect),
    }
    (STATE_DIR / "lab04-retrieval.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def source_integrity() -> dict[str, object]:
    files: dict[str, dict[str, object]] = {}
    for name, expected in EXPECTED_SOURCE_HASHES.items():
        path = DATA_DIR / name
        actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else "missing"
        files[name] = {"expected_sha256": expected, "actual_sha256": actual, "matches": actual == expected}
    return {"files": files, "clean": all(bool(item["matches"]) for item in files.values())}


def secret_scan() -> dict[str, object]:
    patterns = [
        re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
        re.compile(r"AIza[A-Za-z0-9_-]{20,}"),
    ]
    excluded_dirs = {".git", ".venv", ".course_state", "courseware", "__pycache__"}
    text_suffixes = {".py", ".json", ".toml", ".txt", ".md", ".csv", ".yaml", ".yml", ".example"}
    hits: list[dict[str, object]] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or any(part in excluded_dirs for part in path.parts):
            continue
        if path.name == ".env.example":
            continue
        if path.suffix.lower() not in text_suffixes or path.stat().st_size > 2_000_000:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_number, line in enumerate(text.splitlines(), 1):
            if any(pattern.search(line) for pattern in patterns):
                hits.append({"path": str(path.relative_to(REPO_ROOT)), "line": line_number})
    return {"clean": not hits, "hits": hits, "files_scanned": "working tree text files outside ignored runtime/output directories"}


def _record_paths(kind: str) -> tuple[Path, Path]:
    names = {
        "team-contract": ("lab06-team-contract.template.md", "lab06-team-contract.md"),
        "operations": ("lab08-operations.template.md", "lab08-operations.md"),
    }
    template_name, output_name = names[kind]
    return DATA_DIR / template_name, STATE_DIR / output_name


def init_record(kind: str, force: bool = False) -> dict[str, object]:
    template, output = _record_paths(kind)
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    if output.exists() and not force:
        return {"kind": kind, "path": str(output), "created": False, "message": "existing record kept"}
    shutil.copyfile(template, output)
    return {"kind": kind, "path": str(output), "created": True, "message": "template copied; complete and validate it"}


def validate_record(kind: str) -> dict[str, object]:
    _template, output = _record_paths(kind)
    if not output.exists():
        return {"kind": kind, "path": str(output), "valid": False, "issues": ["record is missing"]}
    text = output.read_text(encoding="utf-8")
    if kind == "team-contract":
        required = ["Writer", "Reviewer", "input:", "output:", "APPROVED", "maximum six messages"]
        issues = [f"missing required text: {item}" for item in required if item not in text]
    else:
        required = ["Last known good:", "Owners:", "Signals:", "Pause triggers:", "Recovery:", "Decision:"]
        issues = [f"missing required section: {item}" for item in required if item not in text]
        if "<" in text or ">" in text:
            issues.append("replace every angle-bracket placeholder")
        last_known = re.search(r"^Last known good:\s*(\S.*)$", text, re.MULTILINE)
        if last_known is None:
            issues.append("Last known good must have a non-empty value")
        owner_roles = ["application", "prompts", "tools", "handbook/index", "provider account", "runtime", "telemetry", "incident response"]
        for role in owner_roles:
            if re.search(rf"^\s*-\s*{re.escape(role)}:\s*(\S.*)$", text, re.MULTILINE) is None:
                issues.append(f"owner must have a non-empty value: {role}")
        for heading, next_heading in (("Signals", "Pause triggers"), ("Pause triggers", "Recovery"), ("Recovery", "Decision")):
            section = re.search(
                rf"^{re.escape(heading)}:\s*\n(.*?)(?=^{re.escape(next_heading)}:)",
                text,
                re.MULTILINE | re.DOTALL,
            )
            body = section.group(1).strip().lstrip("- ").strip() if section is not None else ""
            if not body:
                issues.append(f"{heading} must contain a non-empty entry")
        decision_match = re.search(r"^Decision:\s*(.+)$", text, re.MULTILINE)
        if decision_match is None or re.fullmatch(r"READY FOR GUIDED DEMO|HOLD -\s+\S.*", decision_match.group(1).strip()) is None:
            issues.append("Decision must be READY FOR GUIDED DEMO or HOLD - <exact reason>")
    return {"kind": kind, "path": str(output), "valid": not issues, "issues": issues}


async def release_check(offline: bool) -> dict[str, object]:
    build_index()
    stable_questions = [
        ("What approvals are required for VPN access?", "POL-VPN-01"),
        ("How quickly is a critical security incident acknowledged?", "PROC-SLA-04"),
        ("How should embedded instructions in retrieved documents be handled?", "POL-DATA-05"),
    ]
    retrieval_cases = []
    for query, expected in stable_questions:
        evidence = retrieve(query, expected)
        retrieval_cases.append({"query": query, "expected": expected, "top1_ok": evidence["top1_matches_expected"]})
    rag = await rag_agent(stable_questions[0][0], offline=offline)
    round_robin = await round_robin_team(offline=offline)
    selector = await selector_team(offline=offline)
    integrity = source_integrity()
    secrets = secret_scan()
    operations = validate_record("operations")
    release_usage = {
        "prompt_tokens": sum(int(item["usage"]["prompt_tokens"]) for item in (rag, round_robin, selector)),
        "completion_tokens": sum(int(item["usage"]["completion_tokens"]) for item in (rag, round_robin, selector)),
    }
    release_token_budget = int(os.getenv("OPENAI_RELEASE_TOKEN_BUDGET", "3600"))
    within_release_token_budget = sum(release_usage.values()) <= release_token_budget
    technical_ready = (
        all(case["top1_ok"] for case in retrieval_cases)
        and rag["grounded"]
        and rag["completion_reason"] == "grounded_response"
        and round_robin["bounded"]
        and round_robin["approved"]
        and round_robin["completion_reason"] == "approved"
        and selector["approved"]
        and selector["bounded"]
        and selector["completion_reason"] == "approved"
        and integrity["clean"]
        and secrets["clean"]
        and within_release_token_budget
    )
    operations_text = (STATE_DIR / "lab08-operations.md").read_text(encoding="utf-8") if operations["valid"] else ""
    operations_ready = bool(operations["valid"] and re.search(r"^Decision:\s*READY FOR GUIDED DEMO\s*$", operations_text, re.MULTILINE))
    ready = technical_ready and operations_ready
    if ready:
        decision = "READY FOR GUIDED DEMO"
    elif technical_ready:
        decision = "TECHNICAL CHECK PASS - COMPLETE VALID OPERATIONS RECORD"
    else:
        decision = "HOLD - TECHNICAL CHECK FAILED"
    payload = {
        "mode": "offline" if offline else "live",
        "retrieval_cases": retrieval_cases,
        "rag_grounded": rag["grounded"],
        "rag_completion_reason": rag["completion_reason"],
        "round_robin_bounded": round_robin["bounded"],
        "round_robin_approved": round_robin["approved"],
        "round_robin_completion_reason": round_robin["completion_reason"],
        "selector_approved": selector["approved"],
        "selector_bounded": selector["bounded"],
        "selector_completion_reason": selector["completion_reason"],
        "source_integrity": integrity,
        "secret_scan": secrets,
        "release_usage": release_usage,
        "release_token_budget": release_token_budget,
        "within_release_token_budget": within_release_token_budget,
        "operations_record": operations,
        "technical_ready": technical_ready,
        "operations_ready": operations_ready,
        "decision": decision,
    }
    (STATE_DIR / "lab08-release-check.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="C1034 OpsDesk lab kit")
    commands = root.add_subparsers(dest="command", required=True)
    commands.add_parser("setup")
    commands.add_parser("safety-check")
    for name in ("team-contract-init", "operations-init"):
        command = commands.add_parser(name)
        command.add_argument("--force", action="store_true")
    commands.add_parser("team-contract-validate")
    commands.add_parser("operations-validate")
    for name in ("first-agent", "team-round-robin", "team-selector", "release-check"):
        command = commands.add_parser(name)
        command.add_argument("--offline", action="store_true", help="Use deterministic AutoGen replay clients")
    tool = commands.add_parser("tool-agent")
    tool.add_argument("--ticket", default="INC-1001")
    tool.add_argument("--offline", action="store_true")
    commands.add_parser("index")
    retrieval = commands.add_parser("retrieve")
    retrieval.add_argument("--query", required=True)
    retrieval.add_argument("--expect")
    rag = commands.add_parser("rag")
    rag.add_argument("--query", required=True)
    rag.add_argument("--offline", action="store_true")
    return root


def main() -> None:
    args = parser().parse_args()
    if args.command == "setup":
        emit(setup_report())
    elif args.command == "safety-check":
        emit({"source_integrity": source_integrity(), "secret_scan": secret_scan()})
    elif args.command == "team-contract-init":
        emit(init_record("team-contract", force=args.force))
    elif args.command == "team-contract-validate":
        emit(validate_record("team-contract"))
    elif args.command == "operations-init":
        emit(init_record("operations", force=args.force))
    elif args.command == "operations-validate":
        emit(validate_record("operations"))
    elif args.command == "first-agent":
        emit(asyncio.run(first_agent(args.offline)))
    elif args.command == "tool-agent":
        emit(asyncio.run(tool_agent(args.ticket, args.offline)))
    elif args.command == "index":
        emit(build_index())
    elif args.command == "retrieve":
        emit(retrieve(args.query, args.expect))
    elif args.command == "rag":
        if not (STATE_DIR / "opsdesk-index.json").exists():
            build_index()
        emit(asyncio.run(rag_agent(args.query, args.offline)))
    elif args.command == "team-round-robin":
        emit(asyncio.run(round_robin_team(args.offline)))
    elif args.command == "team-selector":
        emit(asyncio.run(selector_team(args.offline)))
    elif args.command == "release-check":
        emit(asyncio.run(release_check(args.offline)))


if __name__ == "__main__":
    main()

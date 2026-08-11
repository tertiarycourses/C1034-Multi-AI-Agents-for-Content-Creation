import asyncio
from pathlib import Path

import pytest

from opsdesk import cli
from opsdesk import examples


VALID_OPERATIONS = """# Lab 8 Operations Record

Last known good: course-release-candidate

Owners:
- application: course facilitator
- prompts: course facilitator
- tools: lab operator
- handbook/index: content owner
- provider account: account owner
- runtime: lab operator
- telemetry: lab operator
- incident response: incident lead

Signals:
- route, sources, stop reason, errors, duration, and model usage

Pause triggers:
- secret exposure, unsupported claim, wrong source, repeated tool error, hard limit, or unexpected package/model change

Recovery:
- disable affected credentials; restore last known good; rebuild index; rerun offline release check and full tests

Decision: READY FOR GUIDED DEMO
"""


@pytest.fixture
def isolated_state(monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "STATE_DIR", tmp_path)
    monkeypatch.setattr(examples, "STATE_DIR", tmp_path)
    return tmp_path


def test_setup_requires_exact_supported_versions(isolated_state):
    report = cli.setup_report()
    assert report["expected_autogen_version"] == "0.7.5"
    assert report["versions_ready"] is True
    assert report["status"] == "ready"


def test_seed_sources_and_working_tree_are_clean():
    assert cli.source_integrity()["clean"] is True
    assert cli.secret_scan()["clean"] is True


def test_team_contract_template_is_executable_and_valid(isolated_state):
    cli.init_record("team-contract", force=True)
    result = cli.validate_record("team-contract")
    assert result["valid"] is True


def test_incomplete_operations_record_blocks_final_readiness(isolated_state):
    cli.init_record("operations", force=True)
    result = asyncio.run(cli.release_check(offline=True))
    assert result["technical_ready"] is True
    assert result["within_release_token_budget"] is True
    assert result["operations_ready"] is False
    assert result["decision"] == "TECHNICAL CHECK PASS - COMPLETE VALID OPERATIONS RECORD"


def test_completed_operations_record_allows_guided_demo(isolated_state):
    _template, output = cli._record_paths("operations")
    Path(output).write_text(VALID_OPERATIONS, encoding="utf-8")
    assert cli.validate_record("operations")["valid"] is True
    result = asyncio.run(cli.release_check(offline=True))
    assert result["technical_ready"] is True
    assert result["operations_ready"] is True
    assert result["decision"] == "READY FOR GUIDED DEMO"


def test_operations_record_rejects_empty_values(isolated_state):
    _template, output = cli._record_paths("operations")
    Path(output).write_text(
        """Last known good:
Owners:
- application:
- prompts:
- tools:
- handbook/index:
- provider account:
- runtime:
- telemetry:
- incident response:
Signals:
Pause triggers:
Recovery:
Decision: READY FOR GUIDED DEMO
""",
        encoding="utf-8",
    )
    result = cli.validate_record("operations")
    assert result["valid"] is False
    assert any("non-empty" in issue for issue in result["issues"])

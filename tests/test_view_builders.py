from agent.tools.accessibility_check import lint_text
from listeners.views.app_home_builder import build_app_home_view
from listeners.views.feedback_builder import (
    build_feedback_blocks,
    build_response_blocks,
)


def test_build_feedback_blocks():
    blocks = build_feedback_blocks()

    assert len(blocks) > 0
    block_dict = blocks[0].to_dict()
    action_ids = [e["action_id"] for e in block_dict["elements"]]
    assert "feedback" in action_ids


def test_build_response_blocks_has_followups():
    blocks = build_response_blocks()
    assert len(blocks) >= 2
    actions = blocks[0].to_dict()
    ids = [e["action_id"] for e in actions["elements"]]
    assert "access_shorter" in ids
    assert "access_friendlier" in ids
    assert "access_more_formal" in ids


def test_build_app_home_view_default():
    view = build_app_home_view()

    assert view["type"] == "home"
    header = next(b for b in view["blocks"] if b["type"] == "header")
    assert header["text"]["text"] == "Access Coach"

    section_texts = [
        b["text"]["text"] for b in view["blocks"] if b["type"] == "section"
    ]
    mcp_section = next(t for t in section_texts if "Slack MCP Server" in t)
    assert "disconnected" in mcp_section


def test_build_app_home_view_connect():
    view = build_app_home_view(install_url="https://example.com/slack/install")

    section_texts = [
        b["text"]["text"] for b in view["blocks"] if b["type"] == "section"
    ]
    mcp_section = next(t for t in section_texts if "Slack MCP Server" in t)
    assert "disconnected" in mcp_section
    assert "https://example.com/slack/install" in mcp_section


def test_build_app_home_view_connected():
    view = build_app_home_view(is_connected=True)

    section_texts = [
        b["text"]["text"] for b in view["blocks"] if b["type"] == "section"
    ]
    mcp_section = next(t for t in section_texts if "Slack MCP Server" in t)
    assert "connected" in mcp_section


def test_lint_text_flags_jargon():
    report = lint_text(
        "Let's leverage our bandwidth and circle back on KPIs EOD."
    ).lower()
    assert "jargon" in report or "bandwidth" in report or "kpi" in report

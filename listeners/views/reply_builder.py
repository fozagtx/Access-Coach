"""Shared Slack reply helper — real Block Kit only."""

from slack_sdk.models.blocks import MarkdownTextObject, SectionBlock

from listeners.views.feedback_builder import build_response_blocks


def build_agent_message_blocks(markdown_text: str) -> list:
    """Section with agent text + follow-up / feedback actions."""
    text = (markdown_text or "").strip() or "No response generated."
    if len(text) > 2900:
        text = text[:2900] + "…"
    return [
        SectionBlock(text=MarkdownTextObject(text=text)),
        *build_response_blocks(),
    ]

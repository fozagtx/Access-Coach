from slack_bolt.async_app import AsyncApp

from .access_shortcuts import (
    handle_alt_text_shortcut,
    handle_rewrite_shortcut,
    handle_summarize_shortcut,
)
from .feedback_buttons import handle_feedback_button
from .followups import handle_followup


def register(app: AsyncApp):
    app.action("feedback")(handle_feedback_button)
    app.action("access_shorter")(handle_followup)
    app.action("access_friendlier")(handle_followup)
    app.action("access_more_formal")(handle_followup)
    app.shortcut("access_rewrite")(handle_rewrite_shortcut)
    app.shortcut("access_summarize")(handle_summarize_shortcut)
    app.shortcut("access_alt_text")(handle_alt_text_shortcut)

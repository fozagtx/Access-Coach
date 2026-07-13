def build_app_home_view(
    install_url: str | None = None, is_connected: bool = False
) -> dict:
    """Build the Access Coach App Home Block Kit view."""
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Access Coach",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Make Slack clearer for everyone.*\n\n"
                    "I help teams communicate so neurodivergent, ESL, and "
                    "screen-reader users can fully participate.\n\n"
                    "• *Plain language* — rewrite jargon into clear messages\n"
                    "• *Thread digest* — decisions, owners, next steps\n"
                    "• *Alt text* — captions for shared images\n\n"
                    "DM me, *@mention* me, or use a *message shortcut* "
                    "(⋯ → More message shortcuts)."
                ),
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*Try asking:*\n"
                    "• `Rewrite this in plain language`\n"
                    "• `Summarize this thread`\n"
                    "• `Suggest alt text for this image`"
                ),
            },
        },
        {"type": "divider"},
    ]

    if is_connected:
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "\U0001f7e2 *Slack MCP Server is connected.*",
                },
            }
        )
        blocks.append(
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": (
                            "I can search workspace messages for older context "
                            "when rewriting or summarizing."
                        ),
                    }
                ],
            }
        )
    elif install_url:
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"\U0001f534 *Slack MCP Server is disconnected.* "
                        f"<{install_url}|Connect the Slack MCP Server.>"
                    ),
                },
            }
        )
        blocks.append(
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": (
                            "MCP unlocks workspace search for richer accessibility help."
                        ),
                    }
                ],
            }
        )
    else:
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        "\U0001f534 *Slack MCP Server is disconnected.* "
                        "<https://docs.slack.dev|"
                        "Enable Slack MCP in Agents & AI Apps settings.>"
                    ),
                },
            }
        )
        blocks.append(
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": (
                            "Core Access Coach tools work without MCP. "
                            "Connect MCP for workspace-wide search."
                        ),
                    }
                ],
            }
        )

    return {
        "type": "home",
        "blocks": blocks,
    }

from agents import function_tool
from agents.run_context import RunContextWrapper
from slack_sdk.errors import SlackApiError

from agent.deps import AgentDeps


@function_tool
async def fetch_message(
    wrapper: RunContextWrapper[AgentDeps],
    message_ts: str | None = None,
) -> str:
    """Fetch one Slack message by timestamp for plain-language rewrite.

    Args:
        message_ts: Slack message timestamp. Defaults to the current message.
    """
    deps = wrapper.context
    message_ts = message_ts or deps.message_ts
    try:
        result = await deps.client.conversations_replies(
            channel=deps.channel_id,
            ts=deps.thread_ts,
            latest=message_ts,
            inclusive=True,
            limit=200,
        )
        messages = [m for m in result.get("messages", []) if m.get("ts") == message_ts]
        if not messages:
            return f"Could not fetch message: message_not_found (ts={message_ts})"

        msg = messages[0]
        text = (msg.get("text") or "").strip()
        files = msg.get("files") or []
        file_bits = [
            f"- {f.get('name', 'file')} (type={f.get('mimetype', 'unknown')}, id={f.get('id', 'n/a')})"
            for f in files
        ]
        parts = [
            f"Message ts={msg.get('ts')}",
            f"User=<@{msg.get('user', 'unknown')}>",
            f"Text:\n{text}" if text else "Text: (empty)",
        ]
        if file_bits:
            parts.append("Files:\n" + "\n".join(file_bits))
        return "\n".join(parts)
    except SlackApiError as e:
        return f"Could not fetch message: {e.response['error']}"

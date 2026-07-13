from agents import function_tool
from agents.run_context import RunContextWrapper
from slack_sdk.errors import SlackApiError

from agent.deps import AgentDeps


@function_tool
async def fetch_thread(
    wrapper: RunContextWrapper[AgentDeps],
    limit: int = 50,
) -> str:
    """Fetch messages from the current Slack thread for summarize / digest requests.

    Args:
        limit: Max messages to fetch (default 50, max 100).
    """
    deps = wrapper.context
    limit = min(max(limit, 1), 100)
    try:
        result = await deps.client.conversations_replies(
            channel=deps.channel_id,
            ts=deps.thread_ts,
            limit=limit,
        )
        lines = []
        for msg in result.get("messages", []):
            user = msg.get("user", msg.get("bot_id", "unknown"))
            text = (msg.get("text") or "").strip()
            if not text and msg.get("files"):
                names = [f.get("name", "file") for f in msg["files"]]
                text = f"[shared file(s): {', '.join(names)}]"
            if text:
                lines.append(f"<@{user}>: {text}")
        if not lines:
            return "No readable messages found in this thread."
        return f"Thread ({len(lines)} messages):\n\n" + "\n".join(lines)
    except SlackApiError as e:
        return f"Could not fetch thread: {e.response['error']}"

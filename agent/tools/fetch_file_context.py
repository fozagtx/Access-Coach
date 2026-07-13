from agents import function_tool
from agents.run_context import RunContextWrapper
from slack_sdk.errors import SlackApiError

from agent.deps import AgentDeps


@function_tool
async def fetch_file_context(
    wrapper: RunContextWrapper[AgentDeps],
    file_id: str | None = None,
) -> str:
    """Inspect a Slack file (especially images) to write alt text.

    Args:
        file_id: Slack file ID. If omitted, uses files on the current message.
    """
    deps = wrapper.context
    try:
        if file_id:
            info = await deps.client.files_info(file=file_id)
            files = [info["file"]] if info.get("file") else []
        else:
            result = await deps.client.conversations_replies(
                channel=deps.channel_id,
                ts=deps.thread_ts,
                latest=deps.message_ts,
                inclusive=True,
                limit=200,
            )
            files = []
            for msg in result.get("messages", []):
                if msg.get("ts") == deps.message_ts:
                    files = msg.get("files") or []
                    break

        if not files:
            return (
                "No file on this message. Share an image in Slack, "
                "or pass a real Slack file_id."
            )

        blocks = []
        for f in files:
            preview = f.get("preview") or f.get("plain_text") or ""
            name = f.get("name", "unnamed")
            blocks.append(
                "\n".join(
                    [
                        f"File id={f.get('id')}",
                        f"Name={name}",
                        f"Title={f.get('title') or name}",
                        f"Type={f.get('filetype')} ({f.get('mimetype')})",
                        f"Size={f.get('size')}",
                        f"Existing alt_txt={f.get('alt_txt') or '(none)'}",
                        f"Preview/text excerpt={preview[:500] if preview else '(none)'}",
                        "Write concise alt text for screen readers "
                        "(what matters, not 'image of').",
                    ]
                )
            )
        return "\n\n---\n\n".join(blocks)
    except SlackApiError as e:
        return f"Could not fetch file context: {e.response['error']}"

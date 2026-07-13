from agents import function_tool
from agents.run_context import RunContextWrapper
from slack_sdk.errors import SlackApiError

from agent.deps import AgentDeps


@function_tool
async def add_emoji_reaction(
    wrapper: RunContextWrapper[AgentDeps],
    emoji_name: str,
) -> str:
    """Add an emoji reaction to the user's current message.

    Args:
        emoji_name: Slack emoji name without colons (e.g. 'eyes', 'memo', 'books').
    """
    deps = wrapper.context
    try:
        await deps.client.reactions_add(
            channel=deps.channel_id,
            timestamp=deps.message_ts,
            name=emoji_name,
        )
        return f"Reacted with :{emoji_name}:"
    except SlackApiError as e:
        return f"Could not add reaction: {e.response['error']}"

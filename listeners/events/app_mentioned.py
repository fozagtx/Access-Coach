import re
from logging import Logger

from slack_bolt.context.async_context import AsyncBoltContext
from slack_bolt.context.say.async_say import AsyncSay
from slack_bolt.context.say_stream.async_say_stream import AsyncSayStream
from slack_bolt.context.set_status.async_set_status import AsyncSetStatus
from slack_sdk.web.async_client import AsyncWebClient

from agent import AgentDeps, run_agent
from listeners.views.reply_builder import build_agent_message_blocks
from thread_context import conversation_store


async def handle_app_mentioned(
    client: AsyncWebClient,
    context: AsyncBoltContext,
    event: dict,
    logger: Logger,
    say: AsyncSay,
    say_stream: AsyncSayStream,
    set_status: AsyncSetStatus,
):
    """Handle @mentions in channels."""
    try:
        channel_id = context.channel_id
        text = event.get("text", "")
        thread_ts = event.get("thread_ts") or event["ts"]
        cleaned_text = re.sub(r"<@[A-Z0-9]+>", "", text).strip()

        if not cleaned_text:
            await say(
                text=(
                    "Hi — I'm *Access Coach*. Ask me to rewrite in plain language, "
                    "summarize this thread, or suggest alt text for an image."
                ),
                thread_ts=thread_ts,
            )
            return

        await set_status(
            status="Thinking...",
            loading_messages=[
                "Cutting the jargon…",
                "Writing for every teammate…",
                "Building a clearer digest…",
                "Checking accessibility…",
            ],
        )

        history = conversation_store.get_history(channel_id, thread_ts)
        deps = AgentDeps(
            client=client,
            user_id=context.user_id,
            channel_id=channel_id,
            thread_ts=thread_ts,
            message_ts=event["ts"],
            user_token=context.user_token,
        )
        response_text, new_history = await run_agent(
            cleaned_text, history=history, deps=deps
        )

        streamer = await say_stream()
        await streamer.append(markdown_text=response_text)
        await streamer.stop(blocks=build_agent_message_blocks(response_text)[1:])

        conversation_store.set_history(channel_id, thread_ts, new_history)

    except Exception as e:
        logger.exception(f"Failed to handle app mention: {e}")
        await say(
            text=f":warning: Access Coach error: {e}",
            thread_ts=event.get("thread_ts") or event["ts"],
        )

"""Follow-up action buttons for Access Coach responses."""

from logging import Logger

from slack_bolt.context.ack.async_ack import AsyncAck
from slack_bolt.context.async_context import AsyncBoltContext
from slack_bolt.context.say.async_say import AsyncSay
from slack_sdk.web.async_client import AsyncWebClient

from agent import AgentDeps, run_agent
from listeners.views.reply_builder import build_agent_message_blocks
from thread_context import conversation_store

FOLLOWUPS = {
    "access_shorter": (
        "Take your previous accessibility output and make it shorter and more scannable. "
        "Keep the useful rewrite/digest/alt text. Cut fluff."
    ),
    "access_friendlier": (
        "Take your previous accessibility output and make the tone warmer and more inclusive "
        "without losing clarity. Keep the same structure."
    ),
    "access_more_formal": (
        "Take your previous accessibility output and make the tone more professional/formal "
        "while staying plain language. Keep the same structure."
    ),
}


async def handle_followup(
    ack: AsyncAck,
    body: dict,
    client: AsyncWebClient,
    context: AsyncBoltContext,
    logger: Logger,
    say: AsyncSay,
):
    await ack()
    action = (body.get("actions") or [{}])[0]
    action_id = action.get("action_id", "")
    prompt = FOLLOWUPS.get(action_id)
    if not prompt:
        return

    channel_id = (body.get("channel") or {}).get("id") or context.channel_id
    message = body.get("message") or {}
    thread_ts = message.get("thread_ts") or message.get("ts")
    message_ts = message.get("ts")

    try:
        history = conversation_store.get_history(channel_id, thread_ts)
        deps = AgentDeps(
            client=client,
            user_id=context.user_id,
            channel_id=channel_id,
            thread_ts=thread_ts,
            message_ts=message_ts,
            user_token=getattr(context, "user_token", None),
        )
        response_text, new_history = await run_agent(
            prompt, history=history, deps=deps
        )
        await say(
            text=response_text or "No response generated.",
            channel=channel_id,
            thread_ts=thread_ts,
            blocks=build_agent_message_blocks(response_text),
        )
        conversation_store.set_history(channel_id, thread_ts, new_history)
    except Exception as e:
        logger.exception(f"Follow-up {action_id} failed: {e}")
        await say(
            text=f":warning: Access Coach error: {e}",
            channel=channel_id,
            thread_ts=thread_ts,
        )

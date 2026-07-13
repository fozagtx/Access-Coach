"""Message shortcut handlers for Access Coach."""

from logging import Logger

from slack_bolt.context.ack.async_ack import AsyncAck
from slack_bolt.context.async_context import AsyncBoltContext
from slack_bolt.context.say.async_say import AsyncSay
from slack_sdk.web.async_client import AsyncWebClient

from agent import AgentDeps, run_agent
from listeners.views.reply_builder import build_agent_message_blocks
from thread_context import conversation_store

PROMPTS = {
    "access_rewrite": (
        "Use fetch_message on the current message, run accessibility_check, then "
        "rewrite it in plain language. Format as:\n"
        "*Issues* (short bullets)\n"
        "*Plain rewrite* (ready to paste)\n"
        "Offer to refine tone (more formal / friendlier)."
    ),
    "access_summarize": (
        "Use fetch_thread on this conversation. Produce an accessible digest:\n"
        "*TL;DR* (1–2 sentences)\n"
        "*Decisions*\n"
        "*Owners / next steps*\n"
        "*Open questions*\n"
        "Keep it scannable for busy and neurodivergent readers."
    ),
    "access_alt_text": (
        "Use fetch_file_context for files on this message. Write accessible alt text:\n"
        "*Short* (≤125 characters)\n"
        "*Detailed* (for complex diagrams)\n"
        "Describe meaning, not just appearance. Never start with 'image of'."
    ),
}


async def _run_shortcut(
    *,
    callback_id: str,
    ack: AsyncAck,
    client: AsyncWebClient,
    context: AsyncBoltContext,
    body: dict,
    logger: Logger,
    say: AsyncSay,
):
    await ack()

    message = body.get("message") or {}
    channel_id = (body.get("channel") or {}).get("id") or context.channel_id
    message_ts = message.get("ts")
    thread_ts = message.get("thread_ts") or message_ts
    prompt = PROMPTS[callback_id]
    user_text = (message.get("text") or "").strip()
    composed = (
        f"{prompt}\n\n"
        f"Target message_ts={message_ts}\n"
        f"Message text (may be empty if file-only):\n{user_text or '(no text)'}"
    )

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
            composed, history=history, deps=deps
        )
        await say(
            text=response_text or "No response generated.",
            channel=channel_id,
            thread_ts=thread_ts,
            blocks=build_agent_message_blocks(response_text),
        )
        conversation_store.set_history(channel_id, thread_ts, new_history)
    except Exception as e:
        logger.exception(f"Shortcut {callback_id} failed: {e}")
        await say(
            text=f":warning: Access Coach error: {e}",
            channel=channel_id,
            thread_ts=thread_ts,
        )


async def handle_rewrite_shortcut(
    ack: AsyncAck,
    client: AsyncWebClient,
    context: AsyncBoltContext,
    body: dict,
    logger: Logger,
    say: AsyncSay,
):
    await _run_shortcut(
        callback_id="access_rewrite",
        ack=ack,
        client=client,
        context=context,
        body=body,
        logger=logger,
        say=say,
    )


async def handle_summarize_shortcut(
    ack: AsyncAck,
    client: AsyncWebClient,
    context: AsyncBoltContext,
    body: dict,
    logger: Logger,
    say: AsyncSay,
):
    await _run_shortcut(
        callback_id="access_summarize",
        ack=ack,
        client=client,
        context=context,
        body=body,
        logger=logger,
        say=say,
    )


async def handle_alt_text_shortcut(
    ack: AsyncAck,
    client: AsyncWebClient,
    context: AsyncBoltContext,
    body: dict,
    logger: Logger,
    say: AsyncSay,
):
    await _run_shortcut(
        callback_id="access_alt_text",
        ack=ack,
        client=client,
        context=context,
        body=body,
        logger=logger,
        say=say,
    )

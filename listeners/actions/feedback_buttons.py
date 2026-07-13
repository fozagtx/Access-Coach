from logging import Logger

from slack_bolt.context.ack.async_ack import AsyncAck
from slack_bolt.context.async_context import AsyncBoltContext
from slack_sdk.web.async_client import AsyncWebClient


async def handle_feedback_button(
    ack: AsyncAck,
    body: dict,
    client: AsyncWebClient,
    context: AsyncBoltContext,
    logger: Logger,
):
    """Handle thumbs up/down feedback on agent responses."""
    await ack()

    try:
        channel_id = context.channel_id
        user_id = context.user_id
        message_ts = body["message"]["ts"]
        thread_ts = body["message"].get("thread_ts") or message_ts
        feedback_value = body["actions"][0]["value"]

        if feedback_value == "good-feedback":
            text = "Glad that helped."
        else:
            text = "Thanks for the feedback — try again or tap Make shorter / Friendlier."

        await client.chat_postEphemeral(
            channel=channel_id,
            user=user_id,
            thread_ts=thread_ts,
            text=text,
        )
        logger.debug(
            f"Feedback received: value={feedback_value}, message_ts={message_ts}"
        )
    except Exception as e:
        logger.exception(f"Failed to handle feedback: {e}")

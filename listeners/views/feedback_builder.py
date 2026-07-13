from slack_sdk.models.blocks import (
    ActionsBlock,
    Block,
    ButtonElement,
    ContextActionsBlock,
    FeedbackButtonObject,
    FeedbackButtonsElement,
)


def build_feedback_blocks() -> list[Block]:
    """Thumbs up/down only (legacy helper)."""
    return [build_feedback_element_block()]


def build_feedback_element_block() -> Block:
    return ContextActionsBlock(
        elements=[
            FeedbackButtonsElement(
                action_id="feedback",
                positive_button=FeedbackButtonObject(
                    text="Good Response",
                    accessibility_label="Submit positive feedback on this response",
                    value="good-feedback",
                ),
                negative_button=FeedbackButtonObject(
                    text="Bad Response",
                    accessibility_label="Submit negative feedback on this response",
                    value="bad-feedback",
                ),
            )
        ]
    )


def build_response_blocks() -> list[Block]:
    """UX follow-ups + feedback — designed for the Design / Best UX rubric."""
    return [
        ActionsBlock(
            block_id="access_followups",
            elements=[
                ButtonElement(
                    text="Make shorter",
                    action_id="access_shorter",
                    value="shorter",
                ),
                ButtonElement(
                    text="Friendlier",
                    action_id="access_friendlier",
                    value="friendlier",
                ),
                ButtonElement(
                    text="More formal",
                    action_id="access_more_formal",
                    value="formal",
                ),
            ],
        ),
        build_feedback_element_block(),
    ]

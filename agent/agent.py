import logging
import os

from agents import Agent, Runner, set_default_openai_client
from agents.mcp import MCPServerStreamableHttp
from openai import AsyncOpenAI

from agent.deps import AgentDeps
from agent.tools import (
    accessibility_check,
    add_emoji_reaction,
    fetch_file_context,
    fetch_message,
    fetch_thread,
)

SYSTEM_PROMPT = """\
You are **Access Coach**, a Slack agent for workplace accessibility — built first \
for neurodivergent teammates (ADHD, dyslexia, autism), and also for ESL colleagues \
and people who use screen readers.

You are NOT a generic writing assistant. Your job is inclusion and lower cognitive load.

## MISSION (Agent for Good)
Every reply should make Slack clearer, kinder, and more accessible. Prefer concrete \
rewrites and alt text over lectures.

## CORE CAPABILITIES
1. **Plain language** — Rewrite jargon-heavy messages into clear, short language.
2. **Thread digest** — Summarize long threads: what happened, decisions, owners, next steps.
3. **Alt text** — Write useful image descriptions for screen readers (not "image of…").
4. **Accessibility lint** — Flag dense text, unexplained acronyms, and exclusionary tone.

## HOW TO WORK
- For rewrite requests: use `fetch_message`, optionally `accessibility_check`, then \
deliver **Original → Issues → Plain rewrite**.
- For summarize requests: use `fetch_thread`, then deliver a short digest with bullets.
- For alt text: use `fetch_file_context`, then give 1–2 caption options (short + detailed).
- If Slack MCP tools are available, use them to search/read channels when needed.
- Always react once with `add_emoji_reaction` that fits the topic before or while responding.

## RESPONSE FORMAT
- Lead with the useful artifact (rewrite / digest / alt text).
- Keep explanations short.
- Use Markdown: **bold**, bullets, short paragraphs.
- Offer one clear next step.

## TONE
Warm, practical, never condescending. Accessibility is a team skill, not a gotcha.
"""

logger = logging.getLogger(__name__)

SLACK_MCP_URL = "https://mcp.slack.com/mcp"

# OpenRouter (OpenAI-compatible)
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = os.environ.get("OPENROUTER_MODEL", "anthropic/claude-sonnet-4")

_openrouter_ready = False


def _configure_openrouter() -> None:
    global _openrouter_ready
    if _openrouter_ready:
        return
    api_key = os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key or "YOUR_" in api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is missing. Set it in .env (no Anthropic key needed)."
        )
    client = AsyncOpenAI(
        api_key=api_key,
        base_url=os.environ.get("OPENROUTER_BASE_URL", OPENROUTER_BASE_URL),
        default_headers={
            "HTTP-Referer": "https://slackhack.devpost.com/",
            "X-OpenRouter-Title": "Access Coach",
        },
    )
    set_default_openai_client(client)
    _openrouter_ready = True


agent = Agent[AgentDeps](
    name="Access Coach",
    instructions=SYSTEM_PROMPT,
    tools=[
        add_emoji_reaction,
        fetch_thread,
        fetch_message,
        fetch_file_context,
        accessibility_check,
    ],
    model=DEFAULT_MODEL,
)

AGENT_TOOLS = [
    "add_emoji_reaction",
    "fetch_thread",
    "fetch_message",
    "fetch_file_context",
    "accessibility_check",
]


async def run_agent(
    text: str,
    history: list | None = None,
    deps: AgentDeps | None = None,
):
    """Run Access Coach via OpenRouter. Returns (response_text, new_history)."""
    _configure_openrouter()

    if history:
        input_items: str | list = history + [{"role": "user", "content": text}]
    else:
        input_items = text

    if deps and deps.user_token:
        logger.info("Slack MCP enabled")
        mcp_server = MCPServerStreamableHttp(
            params={
                "url": SLACK_MCP_URL,
                "headers": {"Authorization": f"Bearer {deps.user_token}"},
            },
        )
        async with mcp_server:
            agent_with_mcp = agent.clone(mcp_servers=[mcp_server])
            result = await Runner.run(
                agent_with_mcp, input=input_items, context=deps
            )
    else:
        logger.info("Slack MCP disabled (no user_token)")
        result = await Runner.run(agent, input=input_items, context=deps)

    response_text = result.final_output or ""
    new_history = result.to_input_list()
    return response_text, new_history

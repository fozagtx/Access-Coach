# Access Coach

Slack agent for workplace accessibility (Agent for Good).

## Stack
- Bolt for Python (`AsyncApp`)
- Claude Agent SDK (`ClaudeSDKClient` + MCP tools)
- Optional Slack MCP (`https://mcp.slack.com/mcp`) when user OAuth token present

## Tools
`fetch_message`, `fetch_thread`, `fetch_file_context`, `accessibility_check`, `add_emoji_reaction`

## Surfaces
App Home, DM/agent prompts, @mention, message shortcuts, follow-up buttons

## Run (real workspace only)
```bash
cp .env.sample .env   # set ANTHROPIC_API_KEY
slack login
source .venv/bin/activate
slack run
```

Enable Slack MCP under App Settings → Agents & AI Apps.

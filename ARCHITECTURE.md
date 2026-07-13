# Access Coach — Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Slack Workspace                       │
│  DM / @mention / Message shortcuts / Agent panel / App Home │
└────────────────────────────┬────────────────────────────────┘
                             │ Socket Mode (or OAuth HTTP)
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              Access Coach (Bolt for Python)                  │
│  listeners/events  ·  shortcuts  ·  App Home  ·  feedback   │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│           Claude Agent SDK  (Slack AI agent runtime)         │
│  System prompt: accessibility coach                          │
│  Tools MCP server:                                           │
│    • fetch_message                                           │
│    • fetch_thread                                            │
│    • fetch_file_context                                      │
│    • accessibility_check                                     │
│    • add_emoji_reaction                                      │
│  Optional: Slack MCP (mcp.slack.com) via user OAuth token    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  Outputs in-thread: plain rewrite · digest · alt text        │
└─────────────────────────────────────────────────────────────┘
```

## Data flow

1. User triggers Access Coach (DM, mention, or message shortcut).
2. Bolt listener builds `AgentDeps` (channel, thread, message, tokens).
3. Claude Agent SDK runs with Access Coach tools (+ Slack MCP if connected).
4. Tools read Slack messages/files via Web API.
5. Agent streams a structured accessibility response back into the thread.

## Hackathon tech mapping

| Requirement | Where |
|---|---|
| Slack AI capabilities | Agent view, streaming replies, suggested prompts, Claude Agent SDK |
| MCP integration | Local tools MCP + Slack MCP Server (`is_mcp_enabled`) |
| Agent for Good | Accessibility / inclusion impact in everyday Slack work |

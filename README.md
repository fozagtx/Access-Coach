# Access Coach

Slack agent that makes messages clearer for everyone — plain language, thread digests, and alt text.

**Hackathon track:** Slack Agent for Good

## What it does

1. **Rewrite** — plain language from jargon  
2. **Summarize** — thread digest (decisions / owners / next steps)  
3. **Alt text** — captions for shared images  

Use message shortcuts, @mention, or DM.

## Run (real Slack only)

```bash
cd /Users/kaizen/Desktop/slack
cp .env.sample .env
# put OPENROUTER_API_KEY=sk-or-... in .env

source .venv/bin/activate
slack login          # in your Slack Developer sandbox workspace
python check_ready.py
slack run
```

Then in Slack App Settings → **Agents & AI Apps** → enable **Slack MCP**.

Invite judges to the sandbox: `slackhack@salesforce.com`, `testing@devpost.com`.

## Devpost

Paste `SUBMISSION.md`. Attach `ARCHITECTURE.md` diagram.

## Layout

```
agent/           Claude agent + tools (real Slack Web API)
listeners/       events, shortcuts, App Home, follow-ups
manifest.json    Access Coach app config
SUBMISSION.md    Devpost copy (simple English)
RUBRIC.md        judging map
```

# Access Coach

A Slack agent for **neurodivergent** teammates (and ESL / screen-reader users): plain language, low-cognitive-load thread digests, and image alt text — one click on a real message.

**Hackathon track:** Slack Agent for Good

## Why it’s not “just another rewrite bot”

| Generic AI rewrite | Access Coach |
|---|---|
| Sounds nicer | Built for **cognitive accessibility** |
| Outside Slack | Lives in the **message menu** |
| One-size copy | Digest structure for ADHD/busy brains + alt text for screen readers |

## What it does

1. **Plain language** — cut jargon that blocks neurodivergent / ESL readers  
2. **Thread digest** — TL;DR, decisions, owners, next steps (scannable)  
3. **Alt text** — captions so screen-reader users aren’t locked out  

## Run (real Slack only)

```bash
cd /Users/kaizen/Desktop/slack
cp .env.sample .env
# OPENROUTER_API_KEY=sk-or-...

source .venv/bin/activate
slack login
python check_ready.py
slack run
```

Enable **Slack MCP** under App Settings → Agents & AI Apps.

Invite judges: `slackhack@salesforce.com`, `testing@devpost.com`.

## Devpost

Paste `SUBMISSION.md`. Attach `ARCHITECTURE.md`.

Repo: https://github.com/fozagtx/-Access-Coach

# Access Coach

Slack agent for neurodivergent teammates (ADHD, dyslexia, autism) — also for ESL and screen-reader users.

Plain language · thread digests · alt text. One click on a Slack message.

**Track:** Slack Agent for Good

## Features

1. Plain language rewrite  
2. Thread digest (TL;DR / decisions / owners / next steps)  
3. Image alt text  

## Run

```bash
cp .env.sample .env   # OPENROUTER_API_KEY=sk-or-...
source .venv/bin/activate
slack login && slack run
```

Enable Slack MCP in App Settings → Agents & AI Apps.  
Invite: `slackhack@salesforce.com`, `testing@devpost.com`

## Docs

`SUBMISSION.md` · `ARCHITECTURE.md` · `RUBRIC.md`  
Repo: https://github.com/fozagtx/Access-Coach

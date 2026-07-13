# Access Coach — Devpost (simple words)

**Track:** Slack Agent for Good  
**Project name:** Access Coach  

**Tagline:**  
A Slack agent for neurodivergent teammates — cut jargon, shrink long threads, and caption images so everyone can keep up.

---

## Inspiration

Slack moves fast. For neurodivergent people (ADHD, dyslexia, autism) — and for ESL teammates and screen-reader users — that speed often means getting left behind:

- Jargon and walls of text raise cognitive load  
- Decisions hide inside long threads  
- Images go out with no alt text  

Most “accessibility” tools live on another website. Nobody opens them mid-chat.

**Access Coach** is different: an inclusion coach *inside* Slack, one click on a real message — built first for neurodivergent access, useful for the whole team.

## What it does

Not a generic rewrite bot. Three access tools designed for cognitive load and inclusion:

1. **Plain language** — rewrite corporate jargon so brains that need clarity can follow  
2. **Thread digest** — TL;DR → decisions → owners → next steps (scannable, not another wall of text)  
3. **Alt text** — captions for images so screen-reader users aren’t locked out  

How to use it:

- Message ⋯ → **Rewrite plain language** / **Summarize thread** / **Suggest alt text**  
- Or DM / @mention Access Coach  

Then tap **Make shorter**, **Friendlier**, or **More formal** to match the reader — not just “sound nicer.”

## How we built it

- **Slack Agent Kit** (Bolt + OpenAI Agents via OpenRouter)  
- **MCP tools** that read the real Slack message, thread, or file  
- **Slack MCP** for workspace search when connected  

No fake data. Real Slack. Real accessibility.

## Challenges we ran into

Standing up a real Slack agent (sandbox, scopes, Socket Mode) under a hard deadline — and keeping the product about *inclusion*, not another chatbot.

## Accomplishments that we're proud of

A working Slack agent judges can click, with a clear **Agent for Good** story: neurodivergence, ESL, and screen-reader access where work already happens.

## What we learned

Accessibility wins when it meets people in Slack — not when it asks them to leave the conversation.

## What's next for Access Coach

- More languages  
- “Add alt text before you post” nudges  
- Team writing norms tuned for cognitive accessibility  

## Built With

slack · bolt-python · openai-agents · openrouter · mcp

## Try it out

- Slack sandbox: `https://access-coach.slack.com` _(confirm in browser)_  
- Access for: `slackhack@salesforce.com`, `testing@devpost.com`  
- GitHub: https://github.com/fozagtx/-Access-Coach  

## Architecture

See `ARCHITECTURE.md` — attach that diagram on Devpost.

---

## 10-second pitch

“Access Coach is a Slack agent built for neurodivergent teammates. One click: plain-language rewrite, scannable thread digests, and image alt text — so people with ADHD, dyslexia, ESL needs, or screen readers aren’t left out of the chat.”

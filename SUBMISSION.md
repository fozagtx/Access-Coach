# Access Coach — Devpost

**Track:** Slack Agent for Good  
**Project name:** Access Coach  

**Tagline:**  
Slack agent for neurodivergent teammates — plain language, low-load thread digests, and image alt text.

---

## Inspiration

Slack is where teams decide things. For people with ADHD, dyslexia, or autism — and for ESL teammates and screen-reader users — dense jargon, long threads, and images without captions make it hard to keep up.

Access Coach brings accessibility into the message itself: one click in Slack.

## What it does

1. **Plain language** — rewrite jargon; explain acronyms; short sentences  
2. **Thread digest** — TL;DR, decisions, owners, next steps  
3. **Alt text** — captions for shared images  

Use message shortcuts, DM, or @mention. Follow-up buttons: Make shorter / Friendlier / More formal.

## How we built it

Slack Agent Kit (Bolt + OpenAI Agents via OpenRouter), MCP tools that read real Slack messages/threads/files, optional Slack MCP for workspace search.

## Challenges we ran into

Shipping a real Slack agent under the hackathon deadline: sandbox, scopes, Socket Mode, OpenRouter.

## Accomplishments that we're proud of

A working Access Coach in Slack with rewrite, digest, and alt text — aimed at neurodivergent access and Agent for Good.

## What we learned

Accessibility help is most useful when it sits inside Slack, on the message people are already reading.

## What's next for Access Coach

More languages, pre-post alt-text reminders, team writing norms for cognitive accessibility.

## Built With

slack · bolt-python · openai-agents · openrouter · mcp

## Try it out

- Sandbox: `https://access-coach.slack.com`  
- Judges: `slackhack@salesforce.com`, `testing@devpost.com`  
- GitHub: https://github.com/fozagtx/Access-Coach  

## Architecture

See `ARCHITECTURE.md`.

---

## Pitch

“Access Coach is a Slack agent for neurodivergent teammates. One click: plain language, thread digests, and alt text.”

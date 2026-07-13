# Access Coach — Devpost (simple words)

**Track:** Slack Agent for Good  
**Project name:** Access Coach  

**Tagline:**  
One click in Slack to make messages clearer for everyone.

---

## Inspiration

Slack is where teams talk. But a lot of messages are hard to understand.

- Too much work jargon  
- Super long threads  
- Pictures with no description  

That hurts people who learn English, people with ADHD or dyslexia, and people who use screen readers.

Most “accessibility” tools are on another website. Nobody opens them when they are busy chatting.

So we built help **inside Slack** — one click on a message.

## What it does

**Access Coach** is a Slack bot that helps your team write clearer.

Three things it can do:

1. **Rewrite** — Turn confusing messages into plain English  
2. **Summarize** — Shorten a long thread: what was decided, who owns what, what’s next  
3. **Alt text** — Write a short description for a picture so screen readers can read it  

How to use it:

- Right-click / more actions on a message → pick Rewrite, Summarize, or Alt text  
- Or message Access Coach in a DM  
- Or @mention it in a channel  

After it answers, you can tap buttons like **Make shorter**, **Friendlier**, or **More formal**.

## How we built it

- **Slack Agent Kit** — Slack’s way to build AI agents (Bolt + Claude)  
- **MCP tools** — Small tools that read the real Slack message, thread, or file  
- **Slack MCP** — Lets the agent search the workspace when connected  

No fake data. It works on real Slack messages.

## Challenges we ran into

Getting a real Slack app running fast: login, permissions, and connecting the AI agent without breaking the demo.

## Accomplishments that we're proud of

A working Slack agent people can actually click — rewrite, summarize, and alt text — built for social good (accessibility).

## What we learned

You do not need a fancy website to help people. Putting accessibility **where the team already works** (Slack) is more useful.

## What's next for Access Coach

- More languages  
- Remind people to add alt text before they post  
- Stronger search for team writing guides  

## Built With

slack · bolt-python · claude-agent-sdk · mcp

## Try it out

- Slack sandbox: _(paste URL after install)_  
- Give access to: `slackhack@salesforce.com` and `testing@devpost.com`  
- GitHub: _(paste when ready)_  

## Architecture

See `ARCHITECTURE.md` — attach that diagram on Devpost.

---

## 10-second pitch (say this out loud)

“Access Coach is a Slack agent that makes messages easier to understand. One click: rewrite jargon, summarize long threads, or add alt text for pictures — so more people on the team can follow along.”

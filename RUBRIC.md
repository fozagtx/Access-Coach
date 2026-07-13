# Rubric map — Slack Agent Builder Challenge

Primary prize: **Slack Agent for Good**  
Side prizes: Best UX · Best Technological Implementation

> Beginner tip: judges score the published rubric. Hit every box. Demo 2–3 working features.

## Judging criteria → Access Coach

### 1. Technological Implementation
**Question:** Quality software? Uses Slack AI, MCP, or RTS?

| Requirement | Evidence |
|---|---|
| Slack AI capabilities | Claude Agent SDK agent, streaming replies, agent view, suggested prompts, assistant status |
| MCP server integration | Custom tools MCP (`fetch_*`, `accessibility_check`) + Slack MCP (`is_mcp_enabled`) |
| Quality | Typed Bolt listeners, session store, tests, Socket Mode |

**Demo line:** “Built on Slack Agent Kit with MCP tools and Slack MCP search.”

### 2. Design
**Question:** UX thought out? Frontend + backend balance?

| Surface | What judges see |
|---|---|
| Message shortcuts | One-click Rewrite / Summarize / Alt text |
| Follow-up buttons | Make shorter · Friendlier · More formal |
| App Home | Mission, how-to, MCP status |
| Feedback | Good/Bad on every reply |

**Demo line:** “Zero setup for teammates — right-click a message, get an accessible rewrite.”

### 3. Potential Impact (For Good — critical)
**Question:** Impact on Slack community and beyond?

| Layer | Story |
|---|---|
| Slack community | Every workspace has jargon, long threads, images without alt text |
| Beyond | Neurodivergence, ESL, screen readers, cognitive load — WCAG-aligned habits inside chat |
| Why Slack | Accessibility tools usually leave the workplace chat; this meets people where work happens |

**Demo line:** “Inclusion is a one-click Slack habit, not a separate training site.”

### 4. Quality of the Idea
**Question:** Creative? Improves on what exists?

| Existing | Our twist |
|---|---|
| Generic writing assistants | Purpose-built for **workplace accessibility in Slack** |
| External a11y checkers | Native agent + shortcuts + MCP context |
| Summarization bots | Digest optimized for cognitive load (TL;DR → owners → next steps) |

**Demo line:** “Not another chatbot — an accessibility coach that lives in the message menu.”

## What we deliberately do NOT build
(Beginner tip: 2 polished features > 10 half-built)

- Marketplace / Organizations track
- RTS (optional stretch only)
- Custom web dashboard
- Multi-language UI beyond English plain language

## Submission checklist
- [ ] Track: Slack Agent for Good
- [ ] Impact paragraph on Devpost (required for this track)
- [ ] ~3 min video with working Project footage
- [ ] Architecture diagram (`ARCHITECTURE.md`)
- [ ] Sandbox URL + access for `slackhack@salesforce.com` and `testing@devpost.com`

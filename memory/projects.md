# Projects

Track active initiatives here.

## Active Projects

| Project | Status | Next Action | Risk | Updated |
| --- | --- | --- | --- | --- |
| Freewheelin / Mathflat AI tutor outsourced work | Active revenue work, approx. KRW 60M/month. Source inspection of `~/projects/ai-tutor-pm` confirms active agent-core, realtime tutoring, concept-teaching, correction, eval, and TutorFlat product-transition work. | Continue delivery; clarify contract duration, renewal likelihood, margin, strategic leverage, and whether TutorFlat can become a product wedge rather than only outsourced code. | Revenue is not guaranteed indefinitely; even if stable, long-term reliance may pull the company toward outsourced development rather than entrepreneurship. Also, much of the durable know-how is in internal PM/harness memory that must not leak into customer repos. | 2026-06-15 |
| Pagecall B2B SaaS | Legacy revenue, approx. KRW 40M/month | Track churn risk, maintenance burden, and whether any remaining assets can be reused. | No longer viewed as the winning path after 설탭 / 오누이 churn and increased customer-side internalization via coding agents. | 2026-06-15 |
| Alcanthia mobile game | Active side project and serious candidate for larger opportunity; DAU approx. 200, ROAS approx. 150%, D7 retention approx. 10-15%. Current strategic read: the game may be closer to a cozy automation / production-economy game than a simple cozy farming game. | Keep the 3-month validation push, but add creative segmentation: compare cozy farming ads against automation/production/economy/RPG-growth creatives, and measure early funnel quality plus D1/D7/payment quality. Also test moving the first automation / production-system aha moment into the first 10 minutes. See `memory/alcanthia.md`. | Above BEP but not yet profitable enough to justify shifting heavy company weight onto it. Current cozy ads may attract users expecting a simpler farming game, while system-oriented users may not be targeted clearly enough. If D7 remains 10-15% after serious product and positioning experiments, reduce to maintenance and test a smaller next-game hypothesis. | 2026-06-16 |
| US immigration and ecosystem access track | Newly opened long-term personal strategy track. Treat US access as an option to build over 12-36 months, not as an immediate abandonment of current Korea-based execution. The evidence base should come from successful company management. See `memory/us-immigration.md`. | Consult a US startup / AI immigration lawyer; map evidence for O-1A, EB-1A, EB-2 NIW, E-2; convert Pagecall / AI tutor achievements into English-facing proof; begin US founder, researcher, customer, and investor conversations while protecting current execution focus. | Could distract from current company execution if treated as an emotional escape plan. Immigration outcomes are uncertain and require professional legal review. US residence alone may not equal frontier access if nationality, trust, institutional affiliation, or security constraints become binding. | 2026-06-15 |

## Freewheelin / Mathflat AI Tutor Details

Source inspected: local `~/projects/ai-tutor-pm`, including `AGENTS.md`, `.agents/memory/`, `docs/`, and nested delivery repo `ai-tutor/`. Inspection date: 2026-06-15.

Durable facts:

- `ai-tutor-pm` is the internal private PM and agent-harness repository. It must not be shared with the customer.
- `ai-tutor/` is the customer-owned delivery repository under `mathFLAT-PageCall/ai-tutor.git`.
- The delivery code is a pnpm workspace with `agent/` and `web/`.
- `agent/` is a TypeScript/Hono/OpenAI/Deepgram/Supabase/Playwright service. Its current production-style architecture uses `Orchestrator2`, OpenAI Realtime paths, BrowserBody, Pagecall room/canvas control, study sessions, concept sessions, correction pipelines, drawing tools, handwriting rendering, and evaluation harnesses.
- `web/` is a Next.js 15 / React 19 app with start/stop, session, concept, OCR, debug, and home/testbed routes.
- The default agent server port is 3001 and web dev port is 3000.
- Supabase project referenced in delivery config is `qtlrdxbmxgmpzzdalxyh` in Seoul.
- Current API surface includes `/start`, `/start-concept`, `/concept-utterance`, `/select-problem`, `/stop`, `/backfill-orphans`, `/debug/realtime-trace/:sessionId`, `/health`, and OCR testbed routes.
- Study mode handles problem selection, Pagecall canvas loading, hints, solution display, auto-advance, answer judging, session summaries, and problem tags.
- Concept mode currently includes a code-authored lesson for quadratic formula derivation aimed at weak middle-school grade 9 students. Its structure uses hook-first opening beats, board obligations, Socratic checkpoints, hint ladders, required student evidence, and explicit forbidden claims.
- Realtime concept work reached live verification on 2026-06-12: bridge beats can write to the board and speak deterministic planned lines while staying internal continuations; ready-check remains the first student-response boundary.
- The current latest local `ai-tutor` commit observed on 2026-06-15 is `fc35193 fix: stabilize realtime concept board flow`.
- The current latest local `ai-tutor-pm` commit observed on 2026-06-15 is `94a58e5 docs: record font-derived glyph retrospective`.
- TutorFlat is the intended customer-visible product direction in `docs/prd-ai-tutor-home.md`: login, student dashboard, AI tutor room, and session summary around the agent core. TutorFlat repo is recorded as `https://github.com/mathFLAT-PageCall/TutorFlat`, customer-visible, with CTO account `js-seo` invited as admin.

Open questions:

- Contract duration, renewal probability, payment/margin structure, and IP reuse rights.
- Whether TutorFlat becomes a customer-funded product wedge, a custom deliverable, or a reusable asset for Pagecall's own next business.
- Which parts of the current `ai-tutor` agent core can legally and practically be reused outside the Freewheelin / Mathflat relationship.

## Parking Lot

Ideas or future initiatives that are not active yet.

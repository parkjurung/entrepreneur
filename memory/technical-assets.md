# Technical Assets

This file records durable facts distilled from the local source repositories that hold most of the company's technical assets.

Inspection date: 2026-06-15.

Primary local source repositories inspected:

- `~/projects/pagecall`
- `~/projects/media-infra`

Important caveat: both repositories were inspected from the local filesystem, including current dirty/untracked state. Facts below are operationally useful but should be rechecked before legal, security, sale, or production migration decisions.

## Executive Summary

The company's core technical asset is a mature real-time education interaction stack, not just a single B2B SaaS application.

The stack includes:

- Real-time web classroom / meeting product code.
- Canvas and whiteboard delta synchronization logic.
- Room, member, session, page, PDF, content, usage, webhook, invoice, and replay data models.
- WebSocket and REST serverless APIs for realtime room state, sessions, chat, and canvas changes.
- Multiple media backends, including Pagecall's own mediasoup-based media infrastructure.
- Recording, replay, and media-stat inspection tooling.
- Customer-facing and internal apps: live classroom app, admin console, tutor/academy surfaces, monitoring, release assistant, design system, and icon system.
- AWS infrastructure knowledge encoded as Serverless, Lambda@Edge, CloudFront, DynamoDB, S3, Kinesis, ECS/ECR, Athena/Glue, X-Ray, and Slack notification automation.

Strategic interpretation:

- The reusable asset is the ability to build complex synchronous interaction systems where video/audio, canvas state, documents, replay, and operational observability must stay coherent.
- This maps directly to AI tutor/canvas opportunities because the company already has canvas interaction, session control, replay, and education workflow primitives.
- The source also shows substantial operational debt: mixed Node runtimes, old dependency surfaces, dirty generated files, local handoff docs, and at least one hardcoded secret risk.

## Pagecall Repository

Local path: `~/projects/pagecall`.

Observed branch: `caihong-oh-espanol-inicial-realdaily-json`.

Observed dirty state:

- `package.json` modified.
- Large generated icon build artifacts deleted under `packages/icons/build/`.
- Untracked `.tmp/`, `packages/app/.tmp/`, and a PDF file under `packages/app/`.

### Repository Shape

Pagecall is a Yarn workspace / Lerna TypeScript monorepo.

High-signal packages:

| Package | Durable Fact |
| --- | --- |
| `packages/app` | Main React/CRA Pagecall classroom application with live, meet, replay, preview, thumbnail, and customer-template surfaces. |
| `packages/core` | Shared realtime classroom SDK/core: controllers, media providers, canvas providers, API providers, chat/session/file services, device brokers, replay controllers, and exported canvas delta types. |
| `packages/delta-canvas-resolver` | Standalone canvas delta and resolver library with Delta, DeltaMap, local resolver, reversible changes, tests, and benchmark scripts. |
| `packages/api` | Main Pagecall serverless API: REST routes, WebSocket routers, scheduled jobs, Mongo/Mongoose models via server-common, Redis-backed delta canvas room state, S3 archive/replay storage, Chime capture processing, usage/invoice logic, and custom Serverless plugins. |
| `packages/server-common` | Shared server models/utilities for Mongo/Mongoose entities such as Room, RoomTemplate, Application, Member, Session, Usage, Invoice, FirebaseUser, Content, WebhookEndpoint, and chat models. |
| `packages/common` | Shared types, constants, models, and utilities used across client/server packages. |
| `packages/ui` | Pagecall UI component package using React, Tailwind, Headless UI, Storybook, Chromatic, and Pagecall icons. |
| `packages/icons` | Pagecall icon package generated from SVG assets. |
| `packages/admin` | Next.js admin/console surface for Pagecall administration and reporting. |
| `packages/tutor` | Next.js 14 App Router tutor product surface using Supabase, Pagecall room creation, subscriptions/Stripe, realtime DB changes, and teacher/student room flows. |
| `packages/academy` | Next.js 14 academy/scheduling/workspace product surface using Supabase migrations, Kakao sign-in, schedules, homework, feedback, member requests, notifications, and Pagecall room integration. |
| `packages/api-router` | Lambda@Edge/API router for dynamically routing API traffic and workers through CloudFront/DynamoDB route records. Runtime observed as Node.js 22. |
| `packages/app-router` | Lambda@Edge app router that routes app requests to specific builds by room ID / stable-canary logic using DynamoDB. Runtime observed as Node.js 22. |
| `packages/content-router` | Lambda@Edge content/PDF router for S3/CloudFront origins. Runtime observed as Node.js 16. |
| `packages/log` | Kinesis-to-S3 log ingestion, gzip partitioning by time and room. Runtime observed as Node.js 16. |
| `packages/monitoring` | API monitoring / Slack notification stack for 500 errors, log details, X-Ray/CloudWatch shortcut generation. Runtime observed as Node.js 16. |
| `packages/assistant` | Internal release/build/status assistant with Slack, GitHub, PagerDuty, S3, Pagecall test room creation, and media-recording monitoring. Runtime observed as Node.js 16 plus a custom AWS Lambda runtime ARN. |

### Product And Domain Facts

- Pagecall is a web-based real-time video call and whiteboard meeting platform for education services.
- The main app includes reusable classroom templates and customer-specific templates such as `NewSeoltab`, `NextSeoltab`, `Skytab`, `Dshare`, `Knowre`, `Caihong`, `Qanda`, and others.
- The domain model centers on applications, users, members, rooms, sessions, pages, PDFs, contents, webhooks, usage, invoices, and replay media.
- The app supports live classroom, meeting, replay, preview, thumbnail, and layout rendering flows.
- README-listed production URLs include `api.pagecall.com`, `console.pagecall.com`, and `app.pagecall.com`.

### Realtime Canvas Asset

Facts from `packages/core`, `packages/api`, and `packages/delta-canvas-resolver`:

- Canvas state is represented through `Delta`, `DeltaMap`, `VersionedDeltaMap`, page IDs, participant IDs, and object/entity deltas.
- `@pagecall/delta-canvas-resolver` exports constants, delta operations, delta-map operations, helpers, interfaces, and resolver logic.
- The resolver package includes tests for attributes, op iteration, delta compose/diff/invert/transform, and operators.
- The API side has a `DeltaCanvasRoom` abstraction that can initialize, restore, activate, apply changes, clean invalid deltas, clean dangling participants, and notify connected clients.
- Active canvas room state uses Redis helpers and locking; archived/restored state uses S3 helpers.
- WebSocket routes include `deltaMap.changes` and `deltaMap.documentJoin`.
- Replay canvas reconstructs state from timestamped changes, supports subdocuments, fallback replay viewer creation, playback rate, navigation, and 20 FPS replay iteration.

Strategic relevance:

- This is directly reusable for AI tutor canvas work: the company already owns a custom state model for collaborative writing/drawing, replay, document/page structure, and multi-participant consistency.

### Realtime Media Asset

Facts from `packages/core`:

- Pagecall supports multiple media providers: Chime, LiveKit, Pagecall media-infra (`MiMediaProvider`), native/mobile variants, fake media, and replay media.
- `MiMediaProvider` uses `@pplink/mediasoup-client`, a `MiSignalingService`, media infra client logic, produce/consume handlers, screenshare/audio/video streams, and remote video grouping by session.
- `LivekitMediaProvider` exists and connects to LiveKit rooms, but the inspected implementation has multiple TODO placeholders for video/display handling.
- Chime media and Chime capture processing are present in API scheduled jobs and controllers.

Strategic relevance:

- The team has accumulated practical knowledge across managed media services and a self-operated SFU path.
- The own-media-infra path is strategically important when latency, control, recording, or cost constraints matter.

### AI Tutor And Academy Surfaces

Facts from `packages/tutor`:

- Tutor is a Next.js 14 App Router app using Supabase SSR/client utilities.
- Tutor creates Pagecall private rooms through the Pagecall API, stores room records in Supabase, and enforces one active teacher room at a time.
- Tutor includes teacher/student room flows, invitation, live-session lookup, subscription/Stripe checkout/customer portal, coupon/benefit/student-seat actions, and Supabase realtime refresh hooks.

Facts from `packages/academy`:

- Academy is a Next.js 14 app using Supabase, migrations, and local Supabase development.
- Academy includes scheduling, member requests, homework, feedback, files/bulletins, notifications, role guards, Kakao sign-in, Skyway-specific workflows, and Pagecall room utilities.
- Academy Supabase migrations from 2024-10 through 2025-01 show schema evolution around workspace sharing, tags, deactivation, layout, timeslots, homework, student notes, feedbacks, file policies, notifications, bulletins, score, auto-approval, and join-request templates.

Strategic relevance:

- These packages are evidence that Pagecall assets have already been extended beyond generic meeting SaaS into narrower education workflows.
- They are likely the most relevant front-end/product surfaces for Freewheelin / Mathflat AI tutor thinking, even if the exact current outsourced code lives elsewhere.

### Infrastructure And Operations Asset

Facts:

- Pagecall uses Serverless Framework, AWS Lambda, API Gateway REST/WebSocket, Lambda@Edge, CloudFront, S3, DynamoDB, MongoDB/Mongoose, Redis, Kinesis, SES, EventBridge, X-Ray, Firebase, Supabase, Vercel, Slack, and Sentry.
- Main API runtime observed as Node.js 22.
- App router and API router runtimes observed as Node.js 22.
- Content router, log, monitoring, and assistant runtimes observed as Node.js 16.
- The API package contains repo-owned custom Serverless plugins, including a warmup plugin and pagecall helper/log-metrics plugins.
- The monitoring package sends Slack notifications and produces AWS console shortcuts for X-Ray / CloudWatch investigation.
- The assistant package automates release/build/status/test workflows and can create Pagecall test rooms for release checks.

Strategic relevance:

- A large part of the asset is operating know-how around real-time serverless systems, not only client UX.
- Runtime inconsistency is a modernization risk if these assets need to be sold, reused, or scaled in a new product.

### Security And Maintenance Risks

Facts:

- `packages/api/src/utils/openaiApiInstance.ts` contains a hardcoded OpenAI API key. The key value is intentionally not copied into this memory file.
- Several packages are still on Node.js 16 runtimes.
- Dependency surfaces include older libraries such as legacy Axios/Sentry/Slack SDK versions in some packages.
- Pagecall has a large dirty worktree with generated icon build deletions and local/untracked files, so current local facts may differ from committed repository state.

Recommended next action:

- Rotate/revoke the hardcoded OpenAI key, move it to secret/environment management, and check git history exposure.
- Before any strategic reuse or buyer-facing diligence, run a focused modernization and security audit.

## Media Infra Repository

Local path: `~/projects/media-infra`.

Observed branch: `main`.

Observed dirty state:

- Untracked `docs/` handoff/review files.

### Repository Shape

`media-infra` is a Yarn 3 workspace TypeScript monorepo for Pagecall's own media infrastructure.

High-signal packages:

| Package | Durable Fact |
| --- | --- |
| `packages/media-api` | Serverless control plane/API for media routers, rooms, peers, producers, consumers, recordings, scale policies, containers, WebSocket signaling, scheduled scaling, and daily notifications. |
| `packages/media-router` | mediasoup-based media router process running in Docker/ECS-style containers; manages WebRTC transports, producers, consumers, worker processes, pipes, recording capture, stats, and Kinesis/S3 logging. |
| `packages/media-converter` | Recording converter service that invokes a compiled GStreamer C converter to turn captured packet files into media outputs. |
| `packages/media-utils` | Shared models, HTTP clients, mediasoup types, WebSocket request/response/notification classes, recording metadata, user-agent helpers, and validation helpers used by media-api/router/client sides. |
| `packages/media-console` | React operations console for rooms, users, state, media routers, peers, recordings, scale policy, utilization, monitor, manual launch, and worker detail views. |
| `packages/kinesis-handler` | Kinesis log handler package, still observed on Node.js 16 runtime. |
| `packages/tester` | Puppeteer/TypeScript scenarios for interhost and group media testing with local video fixtures. |

### Media Infra Architecture Facts

- `media-api` runtime observed as Node.js 22.
- `kinesis-handler` runtime observed as Node.js 16.
- `media-api` exposes HTTP routes for API, internal media-router calls, rooms, recordings, users, media routers, scale policies, peers, and environment variables.
- `media-api` exposes WebSocket handlers for connect, disconnect, ping/pong, and media signaling message handlers.
- Signaling message classes include router RTP capabilities, WebRTC transport creation/connection, producer creation/destruction/pause/resume, consumer listen/resume/pause, preferred layer selection, keep-alive, and recording start/stop.
- DynamoDB tables encode scale policies, environment variables, media routers, sessions, peers, producers, consumers, recordings, and websocket requests.
- Session and websocket request tables use TTL via `expiresAt`.
- S3 buckets include log storage, fluentd log storage, and recording storage with lifecycle policies.
- Recording storage lifecycle includes mp4/ts/m3u8 expiration at 180 days and pcap deep archive transition at 180 days, with special application-specific lifecycle rules.
- `media-api` has scheduled jobs for minutely scale application, container destruction, and daily notifications.
- The API uses AWS SDK v3 clients for DynamoDB, ECS, ECR, EC2, S3, Kinesis, Lambda, Athena, Glue, STS, API Gateway Management API, and presigning.
- Recent local handoff docs document a Node 20 -> 22 migration for `media-api`, including local warmup plugin internalization and AWS SDK packaging changes.

### Media Router / SFU Facts

- `media-router` uses `mediasoup@3.11.15`, Express, CORS, Morgan, Sentry, Kinesis, S3, and pidusage.
- Media codecs configured include Opus audio, VP8, VP9, and H.264 variants.
- The router creates one mediasoup worker per CPU core and samples worker utility over a buffer.
- Worker death handling removes pipes, cleans worker references, and creates replacement workers.
- WebRTC transport options enable SCTP.
- The router supports piping producers across workers through mediasoup pipe transports.
- `Pipe` tracks send/receive pipe transports, producers, consumers, stats, and RTC stats loggers.
- `media-router` reports utilization and media stats through logs and APIs.

Strategic relevance:

- This is an in-house SFU/control-plane implementation, not a thin wrapper around a SaaS video provider.
- The asset is valuable where the company needs control over recording, routing, multi-participant media behavior, or cost structure.

### Recording And Replay Media Facts

- Recording starts at the producer level.
- `MediaRecorderService` creates a captor, assigns RTP/RTCP ports, creates a `RecordItem`, and returns RTP info for the producer.
- On stop, if bytes were sent, it uploads a `.pcap` file to S3 using keys shaped like `group/roomId/recordingId.pcap`, records metadata/tags, notifies media-api, and deletes the local capture file.
- If no bytes were sent, it destroys the captor and deletes the local capture file.
- Uploads are queued with `@pplink/async-queue`.
- `media-converter` spawns `./gst-recorder/build/converter`, passes video/audio packet file path, payload type, dimensions, and destination path, and times out after 6 hours.
- The GStreamer converter is written in C and parses arguments, initializes GStreamer, links elements, and converts to output media.

Strategic relevance:

- The team has non-trivial knowledge in capture, packet-level recording, conversion, storage lifecycle, and replay pipelines.
- This is relevant to AI tutor quality review, post-class analysis, replay, supervision, and data flywheel opportunities.

### Operations Console Facts

- `media-console` is a React app for operating media infra.
- It includes dashboard, monitor, client panel, state views, media router detail pages, room detail pages, worker detail, recording tables, scale policy dialogs, manual launch dialogs, and user management.

Strategic relevance:

- The team built internal observability/control surfaces for realtime infrastructure, reducing dependency on raw cloud consoles.

### Known Maintenance Risks

Facts:

- `media-api` has recent Node 22 migration commits and handoff docs; migration status should be verified before production-critical changes.
- `kinesis-handler` remains on Node.js 16.
- Handoff docs record previous TypeScript check failures in `media-api` involving global Error type narrowing, unresolved `compact`, and older type dependencies; the latest committed state should be revalidated.
- `media-console` had an installation issue in prior handoff docs due to a missing `@pplink/logger@0.0.2` tarball dependency through `@pplink/media-infra-client@0.1.16`.

## AI Tutor PM And Delivery Repositories

Local source inspected: `~/projects/ai-tutor-pm` on 2026-06-15.

Important caveat: `ai-tutor-pm` is an internal private PM/harness repository, while `ai-tutor/` inside it is the customer-owned delivery repository. Do not copy internal PM memory, harness prompts, agent operating notes, or private retrospectives into customer-visible repositories.

### Repository Boundary

| Path | Durable Fact |
| --- | --- |
| `~/projects/ai-tutor-pm` | Internal private meta-repo for project management, handoffs, agent memory, eval findings, operating rules, and internal strategy. |
| `~/projects/ai-tutor-pm/ai-tutor` | Customer-owned delivery repo for the AI tutor application, remote observed as `https://github.com/mathFLAT-PageCall/ai-tutor.git`. |
| `~/projects/ai-tutor-pm/.agents/memory` | Dense incident and project memory covering voice, vision, correction, realtime, tests, prompt policy, and operational rules. |
| `~/projects/ai-tutor-pm/docs` | Handoffs, architecture docs, PRD, test plans, eval notes, and retrospectives. |

### Delivery Repo Shape

`ai-tutor` is a pnpm workspace with two main packages:

| Package | Durable Fact |
| --- | --- |
| `agent` | TypeScript/Hono service using OpenAI, Deepgram, Supabase, Playwright BrowserBody, Pagecall API/canvas, realtime voice orchestration, study/concept modes, correction, drawing, handwriting, OCR, and eval tooling. |
| `web` | Next.js 15 / React 19 app with student/testbed UI, start/stop API proxies, concept and OCR routes, debug sessions, and reusable UI components. |

Observed current local state on 2026-06-15:

- `ai-tutor` latest local commit: `fc35193 fix: stabilize realtime concept board flow`.
- `ai-tutor-pm` latest local commit: `94a58e5 docs: record font-derived glyph retrospective`.
- Agent server default port: 3001.
- Web dev port: 3000.
- Supabase project referenced in config: `qtlrdxbmxgmpzzdalxyh` in Seoul.
- Agent dependencies include OpenAI SDK, Deepgram SDK, Hono, Supabase JS, Playwright, Sharp, WebSocket, TypeScript, and Vitest.
- Web dependencies include Next.js 15.5, React 19.1, Supabase JS, lucide-react, Tailwind, and Vitest.

### Agent Architecture Facts

The delivery agent has evolved beyond a simple chat demo. Durable modules include:

- `realtime/`: OpenAI Realtime client, Orchestrator2, voice channel, response loop, barge-in controller, turn planner, tool runtime, audio bridge, STT input gate, transcription context, observe cache, and concept/study launchers.
- `session/`: session bootstrap for study-backed realtime sessions.
- `study/`: problem selection, study state, canvas runtime, session runtime, turn manager, answer checking, authored self-check, hints, solution and next-problem flow tools.
- `concept/`: concept lesson spec, teaching beats, board state, turn contract, lesson runtime, concept canvas runtime, checkpoint evaluation, and a quadratic formula derivation lesson.
- `correction/`: reader, validator, block segmenter, glyph locator, token aligner, LLM judge, verdict store, async fences, and annotation pipeline.
- `drawing/`: drawing toolkit, geometry, scene graph, table renderer/placement, stroke renderer/analyzer, SymPy bridge.
- `handwriting/`: captured Latin/digit/math glyphs, Korean glyph support, math layout, renderer, text fallback, and coverage tools.
- `eval/`: scenario runner, blind and omniscient judges, scorer, arena, rejudge, noise floor measurement, tuner, fine-tune data generation, and scenario suites.
- `ocr/`: stateless perception testbed server and OCR/perception tooling.
- `policy/`: prompt constitution, prompt fragments, reactor policy, and visual correction policy.

### Runtime Product Facts

- The agent server exposes study and concept session routes:
  - `/start` for study-backed sessions.
  - `/start-concept` for concept sessions.
  - `/concept-utterance` for operator-injected concept speech.
  - `/select-problem`, `/stop`, `/backfill-orphans`, `/debug/realtime-trace/:sessionId`, `/health`, and OCR testbed routes.
- Sessions have a 30 minute safety timeout.
- Cleanup marks Supabase sessions as `shutdown` before expensive teardown and reaps stale active/shutdown sessions on boot as `crashed`.
- There is an explicit guard against uncaught Deepgram inner WebSocket errors crashing the whole process.
- Study mode waits for Pagecall audio consumer before starting the realtime agent.
- Concept mode can skip audio input wait when `audioInputEnabled` is false, enabling text-injected live tests.

### Realtime Tutoring Asset

Facts:

- The stack has migrated significant tutoring behavior to OpenAI Realtime-style orchestration while retaining Pagecall canvas/body control.
- Realtime concept sessions can run internal bridge continuations after a student greeting.
- As of the 2026-06-12 live verification memory, bridge beats can deterministically emit planned speech while required board-writing tools execute, and ready-check remains the first student-response boundary.
- Realtime turn traces record user/agent turns, recent plans, recent finalized turns, raw events, interruptions, and observe-cache events.
- Barge-in, STT input gating, turn accumulation, tool-call policy, forced continuation, and response-loop behavior are isolated in dedicated modules and tests.

Strategic relevance:

- This is a concrete implementation of "AI agent as realtime teacher on a shared canvas," not a generic chatbot.
- The team has working know-how for turn-taking, internal continuations, speech while writing, barge-in, canvas observation, tool execution, and Pagecall room control.

### Concept Teaching Asset

Facts:

- The current concept lesson spec is `quadratic-formula-derivation`, targeting weak middle-school grade 9 students.
- The lesson uses hook-first opening beats, planned speech, planned board writes, a final ready-check, prerequisites, checkpoints, accepted forms, hint ladders, board obligations, and exit criteria.
- The concept turn contract includes phase, checkpoint, board preconditions, required actions, forbidden claims, beat progress, and response policy.
- Response policy structurally encodes Socratic constraints: max one question, no checkpoint advance without student evidence, and controlled speaking before board preconditions.
- Board obligations are treated as runtime invariants rather than prompt-only suggestions.

Strategic relevance:

- This is an early form of authored AI lesson runtime: pedagogy is represented as typed content plus runtime contracts.
- It could become a reusable content/agent architecture if the business moves toward AI-native tutoring products.

### Correction, OCR, Drawing, And Handwriting Assets

Facts:

- Correction work includes OCR/reader, block segmentation, glyph localization, token alignment, equation validation, LLM judging, annotation rendering, and async fences to avoid perception delays.
- Per-problem authored hints exist in memory and schema direction, including problem-specific context used by judge priors.
- Drawing tools include geometric and math rendering support, table placement/rendering, stroke analysis, and a Python SymPy bridge.
- Handwriting renderer uses captured glyph data for Latin/digits/math and Korean composition support.
- A 2026-06-15 font-derived glyph retrospective concluded that font outline/skeleton extraction should not be promoted to production; existing captured handwriting glyphs should remain production source. Future handwriting improvements should use curated semantic templates or small manually reviewed subsets.

Strategic relevance:

- The hard part is not only recognizing math; it is closing the loop: read student work, decide whether and how to intervene, draw or speak the correction, and keep the tutoring flow natural.
- The handwriting lesson is strategically useful: static visual quality is not enough for AI tutoring because live stroke order and writing intent matter.

### Evaluation And Operating Harness Asset

Facts:

- The project uses an internal eval harness with scenarios, blind judge, omniscient judge, scorer, arena comparisons, rejudge, noise floor measurement, and tuner/fine-tune data generation.
- Test and eval doctrine is heavily measurement-driven: do not infer regressions from single noisy scores; use scenario variance, N-run measurements, dimension breakdowns, and raw logs.
- The deploy-readiness guard catalog includes page leak, study-cycle e2e, correction noise-floor, voice relay, vision relay, stress signals, write cancel, mic-grant delay, handwriting coverage, and handwriting line-overlap.
- On 2026-06-12, the Vitest suite was intentionally reduced from 1073 to 763 cases while preserving branch/dispatch and incident-derived coverage.
- Voice relay and vision relay tools isolate STT/TTS and canvas perception variables.

Strategic relevance:

- This process asset is valuable because AI tutor quality is probabilistic and multi-modal. The team has built a measurement culture around variance, noise floor, and incident replay rather than only manual demos.

### Product Transition Asset: TutorFlat

Facts from `docs/prd-ai-tutor-home.md`:

- TutorFlat is the intended customer-visible product shell around the AI tutor agent.
- Strategic purpose: make Freewheelin / Mathflat believe the AI tutor business is worth continued investment and prove Pagecall is the uniquely capable team.
- First product areas: signup/login, student dashboard, AI tutor room, and session summary.
- Product positioning: premium AI math tutor available anytime, remembering recent learning state and preparing the next recommended learning action.
- Customer problem bank should remain central; AI is a tutoring layer over the customer's question bank, not merely a problem generator.
- Ownership boundary: CEO / agent core owner owns tutoring intelligence, recognition, reasoning, tool use, model routing, prompts, latency, voice/canvas behavior; CTO/product owner owns student product shell, UX, dashboard, room, session lifecycle, summaries, integration, loading/error/empty states.
- TutorFlat repository is customer-visible: `https://github.com/mathFLAT-PageCall/TutorFlat`; internal PM/harness knowledge and secrets must not be placed there.

Strategic relevance:

- TutorFlat is the bridge from outsourced agent-core work to a product-like customer proof. It may become a stronger wedge than the current testbed if it demonstrates customer-retainable product value.

### AI Tutor Risks And Open Questions

Risks:

- Revenue/IP risk: the code is customer-owned delivery work; reuse rights must be clarified before treating it as a directly reusable company asset.
- Boundary risk: internal PM/harness memory contains the most valuable process knowledge but is not customer-shareable.
- Product risk: demos can over-focus on agent core while the customer may evaluate whether a full student product could exist.
- Technical risk: realtime/model APIs, voice stack behavior, and LLM tool determinism are moving targets; baselines require periodic remeasurement.
- Operational risk: live sessions should not be interrupted by deploys; previous memory explicitly records no deploy during live sessions.

Open questions:

- Which parts of `ai-tutor` can be reused in Pagecall-owned future products under the Freewheelin / Mathflat contract?
- Whether TutorFlat becomes a custom customer deliverable, a reusable Pagecall product base, or only a sales/proof artifact.
- Whether the current concept lesson runtime should evolve into a content authoring system, DB-backed lesson model, or stay code-authored until contracts stabilize.
- Whether OpenAI Realtime remains strategically superior after measuring cost, Korean voice quality, strict tool behavior, and canvas image-injection latency.

## Strategic Asset Map

### Strong Technical Assets

- Collaborative canvas and whiteboard state model with delta transforms, resolver logic, undo/replay-capable change history, Redis active state, and S3 archive/restore.
- Mature Pagecall classroom UX and customer-specific education layouts.
- Room/session/member/page/document/replay abstractions that can support tutoring and AI-agent teaching flows.
- Real-time WebSocket APIs for sessions, chat, and canvas changes.
- Multiple media provider experience: Chime, LiveKit, and in-house mediasoup infrastructure.
- In-house SFU/control-plane with WebRTC signaling, mediasoup workers, producer/consumer routing, scaling, recording, and stats.
- Recording/replay pipeline from producer-level capture to S3 lifecycle and GStreamer conversion.
- Operational tooling: admin console, media console, monitoring, Slack notifications, release assistant, and test-room automation.
- Education workflow extensions through `tutor` and `academy`, including Supabase-backed scheduling, teacher/student rooms, homework, feedback, memberships, notifications, subscriptions, and realtime DB refresh.
- AI tutor realtime agent architecture: OpenAI Realtime orchestration, BrowserBody/Pagecall embodiment, speech while writing, turn-taking, barge-in, study and concept session lifecycle, and traceable realtime plans.
- AI tutor pedagogy runtime: typed concept lesson specs, board obligations, Socratic turn contracts, correction pipeline, handwriting renderer, drawing toolkit, and authored hint/judge-prior mechanisms.
- AI tutor eval discipline: scenario harness, blind/omniscient judges, arena, noise-floor measurement, voice/vision relays, correction gates, and deploy-readiness guard catalog.

### Weaker Or Riskier Technical Areas

- Mixed runtime modernization state: Node 22 for main Pagecall API/router and media-api, Node 16 still present in several auxiliary stacks.
- Legacy dependency surface across older packages.
- Security hygiene issue: hardcoded OpenAI API key in Pagecall API utility.
- Dirty local source states make it hard to distinguish committed product reality from work-in-progress without a cleanup pass.
- Some newer media-provider or AI-facing surfaces may be partial or experimental; LiveKit provider has TODOs, and AI tutor-specific logic is not fully represented by a single obvious package.
- AI tutor delivery code is customer-owned unless contract terms say otherwise; distinguish technical know-how from reusable IP.
- Realtime and LLM behavior baselines are unstable and must be remeasured after model/API changes.

## Implications For Future Strategy Discussions

Facts to keep in mind:

- The company should not describe its asset narrowly as "a video tutoring SaaS." A more accurate description is "real-time education interaction infrastructure with collaborative canvas, media, replay, and workflow products."
- The technical base is unusually relevant to AI-native tutoring because it combines synchronous interaction, handwriting/canvas context, teacher/student room flows, replay data, and operations tooling.
- `ai-tutor-pm` confirms that the company has already built the next layer on top of Pagecall: a realtime AI teacher that can observe, speak, write, correct, and run authored concept-teaching flows.
- Selling raw code or a generic SaaS may be hard in the agent era, but these assets can support narrower products where realtime interaction quality, data capture, and domain UX matter.
- If pursuing AI tutor or adjacent realtime learning products, the likely reusable pieces are `@pagecall/core`, `@pagecall/delta-canvas-resolver`, Pagecall API room/session/canvas endpoints, media-infra recording/replay, and tutor/academy workflow surfaces.
- If pursuing TutorFlat or a similar product, the reusable company capability is the combination of agent core plus premium student product shell, not either alone.
- If pursuing a sale, partnership, or diligence process, the next prerequisite is not feature work but repository hygiene: secret rotation, runtime/dependency modernization, build reproducibility, dirty-state cleanup, and architecture documentation.

## Open Questions

- Contractually, which parts of the Freewheelin / Mathflat AI tutor implementation and TutorFlat work can Pagecall reuse?
- Which Pagecall customers still actively use which templates and infrastructure paths?
- What is the current production media backend mix: Chime, LiveKit, media-infra, or hybrid by customer/application?
- Which parts of `media-infra` are still in active production after the recent Node 22 migration?
- What recordings/replay data can legally and contractually be used for product analytics or AI training?
- How much cost advantage does in-house media-infra currently provide versus Chime/LiveKit at real customer traffic?
- What would be the minimal AI tutor product slice that reuses the strongest existing assets without dragging all legacy Pagecall maintenance burden forward?

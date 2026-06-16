# Business

Track business-wide context here.

## Confirmed Facts

- Business started in November 2015 as "수파자", a B2C 1:1 live video tutoring platform.
- Around 2017, the company received investment from Primer, described by the user as Korea's top accelerator, and shifted toward B2B.
- Around 2018, "설탭" (company name: 오누이) became a customer.
- During the COVID period in 2019 and 2020, the business grew quickly and generated meaningful, though not large, revenue.
- As of 2026, 설탭 / 오누이, historically the largest customer, has churned.
- As of 2026, the company is doing outsourced AI tutor work for Freewheelin, a Korean edtech company behind the Mathflat math question bank service.
- The company is also building and operating a side project mobile game called "알칸시아" / "Alcanthia".
- As of 2026-06-15, the company is profitable on a monthly basis.
- Current monthly outsourced AI tutor revenue is approximately KRW 60M.
- Current monthly Pagecall B2B SaaS revenue is approximately KRW 40M.
- Current monthly costs, including payroll, server costs, and other expenses, are approximately KRW 50M.
- Current average monthly surplus is approximately KRW 50M.
- As of 2026-06-16, the user estimates that if AI tutor outsourced revenue stopped at the end of 2026 and Alcanthia contribution profit went to zero, the company could still operate for roughly three years with zero revenue and no payroll cuts before cash reached zero.
- Local source inspection of `~/projects/ai-tutor-pm` on 2026-06-15 confirms that the Freewheelin / Mathflat AI tutor work is not just a demo wrapper: it contains a real multimodal agent stack, realtime voice/canvas orchestration, correction/eval harnesses, and product-transition planning for a customer-visible TutorFlat experience.
- Standard financial statement certificates are stored in this repository under `data/source-documents/financial-statements/`.
- Original financial statement source found locally at `~/Documents/Pagecall/표준재무제표 증명원/`.
- Extracted financial statement JSON is stored at `data/extracted/financial-statements/financial_statements.json`.

## Timeline

| Period | Event |
| --- | --- |
| 2015-11 | Started as "수파자", a B2C 1:1 live video tutoring platform. |
| Around 2017 | Received investment from Primer and shifted toward B2B. |
| Around 2018 | 설탭 / 오누이 became a customer. |
| 2019-2020 | COVID-period growth; generated meaningful revenue. |
| 2026 | 설탭 / 오누이 churned as the largest customer. |
| 2026 | Company is surviving through outsourced AI tutor work for Freewheelin / Mathflat and operating Alcanthia as a side project. |

## Strategy

- Current strategic thesis: As of 2026, survival is the primary objective. The company is intentionally avoiding a high-inertia identity while reassessing what kind of business can survive in the agent era.
- Target market:
- Customer segments:
- Positioning:
- Business model: Current cash flow comes from outsourced AI tutor development work for Freewheelin / Mathflat. B2B SaaS is no longer treated as the winning path.
- Key constraints:
  - Largest historical customer churned in 2026.
  - B2B SaaS differentiation is weakening because coding agents make customer-side internalization easier.
  - In the agent era, selling software may require being world-class or category-leading because software creation itself is increasingly commoditized.
  - Outsourced development revenue is not guaranteed to continue indefinitely.
  - Even if outsourced revenue continues, relying on it long term is strategically unfavorable because the user identifies as an entrepreneur, not an outsourced developer.

## Strategic Beliefs

- B2B SaaS is no longer considered a promising path for the company after the 2026 churn of 설탭 / 오누이.
- Coding agents reduce the defensibility of software vendors because customers can internalize more software development than before.
- Selling software in the agent era may become a winner-take-most game where companies with the most token budget and strongest distribution compound faster.
- The company should avoid "we can build this software for you" as the main strategic claim. Durable software-mediated businesses need proprietary data, workflow ownership, measurable outcomes, trust, real-world control rights, difficult integration, or taste/worldbuilding/fun as the scarce asset.
- Working 2026-06-16 AI-era thesis: AI may pull value out of objectively measurable, correct-answer software categories and into foundation-model / infrastructure providers. Many customers building internal B2B SaaS with AI can be interpreted as software margin moving from application vendors toward OpenAI, Anthropic, and cloud/model providers.
- For a small challenger, the attractive arenas may be "subjective-answer" markets where quality is not fully reducible to objective metrics before the fact: fun, taste, worldbuilding, identity, trust, community, or emotional preference. Games are one candidate because retention and ROAS are measurable after launch, but the cause of fun remains creative and sensory.
- Products born from the company's own repeated operational pain are strategically preferred because Pagecall can be its own first customer before external packaging.
- Games may remain viable without being number one because, like music, demand is taste-driven and diverse.
- A game can be a sustainable business if it deeply satisfies a specific user persona rather than dominating the entire market.
- Deeptech remains a long-term aspiration, especially energy, but should be approached through capital, credibility, network access, and PhD-level cofounder pairing rather than immediate solo entry into capital-intensive hardware. See `memory/deeptech-strategy.md`.
- US immigration and ecosystem access is a long-term option track, but its strongest evidence base is successful company management. Current company execution, customer outcomes, revenue durability, product proof, and team credibility are prerequisite assets for that track.

## Current Strategic Posture

As of 2026-06-15:

- The closest current strategy is to use AI tutor outsourced revenue to survive while searching for a larger opportunity.
- Alcanthia is one candidate for that larger opportunity.
- The company is not yet ready to put heavy weight behind Alcanthia because its ROAS is around 150%, above BEP, but profitability is not very high after platform fees and VAT.
- Applying real-time AI canvas/whiteboard technology to other markets would be attractive if possible.
- However, selling technology or code itself is viewed as difficult in the agent era.
- The AI tutor work has two strategic meanings:
  - It is current cash-flow work for Freewheelin / Mathflat.
  - It is also evidence that the company can turn Pagecall's realtime canvas/media infrastructure into AI-native tutoring behavior, which may be a stronger strategic asset than legacy B2B SaaS alone.
- The customer-facing product direction recorded in `~/projects/ai-tutor-pm/docs/prd-ai-tutor-home.md` is "TutorFlat": a premium AI math tutor product that wraps the agent core in login, student dashboard, tutor room, and session summary experiences. Its strategic goal is to make the customer continue investing in AI tutor and to prove Pagecall is the uniquely capable team for this product.

As of 2026-06-16:

- The company is not capital-constrained in the normal startup sense. Runway is long and the company is currently generating surplus.
- The immediate bottleneck is not fundraising, generic burn, or hiring. It is the absence of a sufficiently clear investable thesis where more capital or more people would predictably increase speed.
- Alcanthia is not currently capital-constrained because existing monthly ad spend of roughly KRW 3M already produces enough inflow for meaningful retention learning, and D7 validation is gated by time rather than simply by spend.
- AI tutor cannot be treated as Pagecall's direct productization target under the current customer contract because the user reports exclusivity restrictions that block using the AI tutor business or selling it to other companies.
- CEO time relief is not automatically leverage unless there is a defined high-leverage target for the freed time.
- The current "aggressive" move is therefore not to increase burn for its own sake, but to increase the rate of strategic thesis production: reading, interviewing, writing claims, segmenting markets, identifying non-obvious user desires, and finding a game board where money can later accelerate a validated bottleneck.

## Strategic Assets

As of 2026-06-15, the user sees the company's real assets as:

- Detailed source-derived technical asset map: see `memory/technical-assets.md`.
- Real-time interaction technology: live video, whiteboard, real-time data consistency, and infrastructure optimization.
- Ability to extend legacy real-time canvas/whiteboard assets into new AI-native interfaces.
- AI tutor product know-how: applying an LLM agent to a canvas writing interface so the agent can read student handwriting and annotate on top of it like a real teacher.
- AI tutor evaluation and iteration know-how: the `ai-tutor-pm` workspace contains repeated noise-floor measurement, arena/eval infrastructure, voice/vision relay tools, correction-suite regression gates, and incident-driven prompt/runtime policies. This is a process asset, not only code.
- Real-time online game engineering: Alcanthia also uses the company's strengths in real-time synchronization and infrastructure optimization.
- Strong team execution: the CTO is especially fast and accurate, and productivity has increased further when combined with LLM agents.
- Education/tutoring/math/learning UX tacit knowledge: the company has accumulated intuition about customer needs and what makes learning experiences effective.
- Current cash flow: monthly surplus creates leverage to run experiments, though it is not guaranteed indefinitely.

Assets that are weaker or uncertain:

- Customer pool is not viewed as a strong asset.
- Brand/trust is uncertain as a strategic asset.
- The user's personal network is not currently viewed as a strong advantage.

## Metrics

- North-star metric:
- Input metrics:
  - Monthly outsourced AI tutor revenue: approx. KRW 60M as of 2026-06-15.
  - Monthly Pagecall B2B SaaS revenue: approx. KRW 40M as of 2026-06-15.
  - Monthly operating costs: approx. KRW 50M as of 2026-06-15.
  - Monthly surplus: approx. KRW 50M as of 2026-06-15.
  - Downside zero-revenue runway: user-estimated roughly 36 months as of 2026-06-16, assuming no payroll cuts after AI tutor revenue stops and Alcanthia contribution goes to zero.
- Review cadence:

## Team

As of 2026-06-15:

| Type | Role | Current Focus |
| --- | --- | --- |
| Full-time | CEO / user | Engineer as well as CEO; currently spending most man-month capacity on AI tutor outsourced work. |
| Full-time | CTO | Mainly game development; occasionally contributes to AI tutor work. |
| Full-time | Designer | Mainly game design assets and AI tutor UI/UX; also partially acts as marketer. |
| Part-time | Management support | Finance, accounting, tax, and administration; helps keep the user focused on development. |

Current team dynamic:

- The CEO's execution capacity is heavily tied to AI tutor outsourced delivery.
- Game development is mainly driven by the CTO and designer.
- Management support reduces administrative load and protects CEO development focus.

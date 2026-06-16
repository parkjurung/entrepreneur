# Alcanthia

Alcanthia / 알칸시아 is a mobile-first pixel-art simulation RPG and one candidate for the company's next larger opportunity.

## Source Pointers

- Local project: `~/projects/alcanthia`
- Product README: `~/projects/alcanthia/README.md`
- Game design: `~/projects/alcanthia/docs/GAME_DESIGN.md`
- App store positioning: `~/projects/alcanthia/APP_STORE.md`
- Technical differentiation: `~/projects/alcanthia/docs/ip/03_소프트웨어_기술_특징.md`
- Analytics scripts: `~/projects/alcanthia/scripts/analytics.ts`, `~/projects/alcanthia/scripts/dau_chart.ts`

## Product Definition

- Korean subtitle / positioning: "마녀의 텃밭 - 재배하고, 양조하고, 모험을 떠나세요".
- Genre: simulation RPG with farming, brewing/alchemy, adventure, crafting, automation, and player trading.
- Platform: mobile-first iOS/Android via Capacitor, plus web.
- Tech stack: Phaser 3, TypeScript, Capacitor, Supabase, RevenueCat, Stripe.
- Art direction: cozy pixel-art fantasy, witch garden, potion brewing, night forest / cauldron glow brand tone.

## Long-Term Product Thesis

As of 2026-06-16, the user's emerging philosophical thesis for Alcanthia is:

- In a future where AI and automation reduce human production time, many people may not simply want passive leisure. They may still feel a biological and psychological need to produce, improve, accumulate, and cooperate.
- Alcanthia can be framed as a "post-labor production play" game: a small fantasy economy where players satisfy productive instincts through farming, brewing, crafting, automation, adventure, and trade.
- The game is not only meant to fill idle time. Its stronger promise is to give players a safe, playful substitute for the feeling of acting on a world, improving a system, and participating in a productive economy.
- The four independent productive instincts to respect are accumulation, improvement/optimization, making/crafting, and exchange/cooperation.
- This thesis should not replace near-term retention discipline. It should help clarify why the automation aha moment matters: automation is the moment when the player's small world begins to feel alive and productive beyond direct tapping.

## Core Loop

The player:

1. Plants and grows magical crops in a garden.
2. Harvests crops and ingredients.
3. Brews or synthesizes items/potions through recipe discovery.
4. Sends adventurers on expeditions.
5. Uses adventure loot to craft or enhance items.
6. Expands farming productivity, automation, and economic capacity.
7. Trades with other players to pursue goals through different economic specializations.

The design docs describe the loop as: new crops -> higher farm income -> stronger equipment -> higher adventures -> new crops.

## Target Users

- Men and women in their 20s to 40s who like pixel art, RPGs, and automation.
- Adjacent store keywords and tags include witch, potion, brew, farm, pixel, idle, simulation, alchemy, plant, adventure, garden, craft, magic, RPG, cozy.

## Founder-Market Fit And Game Taste

As of the 2026-06-16 strategy interview, the user's game founder-market fit appears strongest in system-heavy games rather than action, romance simulation, or board-game-like design.

Games the user has spent significant time on and understands deeply:

- Factorio.
- Satisfactory.
- Civilization.
- Paradox grand strategy games: HOI4, Victoria, Stellaris.
- Minecraft.
- World of Warcraft.
- EVE Online.

Taste pattern:

- Automation / production systems: the pleasure of complex factories producing advanced goods automatically after the player struggled to make basic intermediates manually.
- Spatial system-building: the pleasure of seeing a large designed system physically exist in the world.
- Strategy compounding: the pleasure of role-playing a concept, making sharp early choices, and watching them compound into long-term strategic advantage.
- Sandbox ownership: exploration and constructing a personally meaningful space.
- Persistent-world economy and cooperation: becoming as strong as others, surpassing others, combining player strengths to clear difficult missions, and selling self-produced goods into a real market.

Working founder-market-fit claim:

> The team is most likely to build a strong game where player intent hardens into a system, the system acts on the player's behalf, and the output gains meaning through space, strategy, market, or cooperation.

## Retention Thesis

Users return because:

- They want to see the result of automated farming and offline progress.
- They pursue self-defined goals such as crafting highly enhanced tools or expanding the field to increase farming productivity.
- The game uses progressive disclosure, recipe discovery, automation desire, and short mobile sessions as retention mechanics.
- The design target is short sessions of roughly 10-15 minutes after early onboarding.

## Current Retention Bottleneck Hypothesis

As of 2026-06-15, the user's leading intuition is:

- D7 retention is held back because players take too long to taste automation.
- The core aha moment is too deep in the progression.
- Players currently need to endure too much before they understand why the game becomes compelling.
- Therefore, the most important product question is likely not "add more content" but "move the automation aha moment earlier without collapsing long-term progression."

As of 2026-06-16, the thesis sharpened:

- Alcanthia's first 10 minutes currently feel like planting crops and following a tutorial, not like watching a small production system come alive.
- The strongest activation hypothesis is that new players should quickly feel: manual action -> small automation -> accumulated output -> conversion into brewing, adventure, sale, or upgrade.
- If Alcanthia works, it may work less because of "cozy farming" and more because of a small Factorio/EVE-like production economy inside a cozy witch-fantasy wrapper.
- The game should not be reduced to a pure factory game. The current differentiated promise is closer to "cozy automation / witch factory / small production economy."

## Advertising And Positioning Hypotheses

As of 2026-06-16:

- Current ads are reported to lean toward cozy farming.
- This may create an acquisition-message mismatch: users expecting a simple cozy farming game may find the underlying production/economy system too complex.
- Conversely, players who would enjoy automation, production systems, and player economy may not be receiving a strong enough signal from the current ads.
- The issue may not only be product activation. It may be a combined product-positioning problem: Alcanthia's skin says cozy farming, while the durable core may be automation/economy.

Creative segmentation to test without materially increasing spend:

- Baseline cozy farming creative.
- Automation / production explosion creative.
- Market / trade / player economy creative.
- Adventure / RPG growth / equipment enhancement creative.

Early signals before D7:

- Tutorial completion.
- First brew reached.
- First automation or offline reward reached.
- D1 retention.
- First payment or ad watch.
- Qualitative signs of "too complex" or "I don't know what to do."

Important interpretation rule:

- A more system-oriented creative may have higher CPI or lower click-through than cozy farming creative. It can still be better if retained users have higher D1/D7, payer conversion, or payment quality.

## Current Metrics

As of 2026-06-15, based on user-provided figures:

- DAU: approximately 200.
- ROAS: approximately 150%.
- Daily ad spend: approximately KRW 160K.
- Daily average payment revenue: approximately KRW 220K.
- D7 retention: currently around 10-15%.
- User's expected threshold for stronger confidence: D7 retention around 20%.
- Current assessment: above BEP, but not profitable enough after platform fees and VAT to justify shifting heavy company weight onto it yet.

Note: daily payment revenue of KRW 220K divided by daily ad spend of KRW 160K implies gross ROAS around 137.5%. Treat the 150% figure as approximate unless reconciled against the actual dashboard.

## Success Probability And Revenue Estimate

As of 2026-06-15, a working estimate was made from the current metrics, team capacity, and public comparable game cases.

### Facts Used

- Current scale is small but real: DAU around 200 with daily payment revenue around KRW 220K.
- Current annualized gross payment revenue is approximately KRW 80.3M at KRW 220K/day.
- Current annualized ad spend is approximately KRW 58.4M at KRW 160K/day.
- Current ARPDAU is approximately KRW 1,100, which is not weak for the current DAU scale.
- Under a rough 30% platform fee and 10% VAT assumption, daily net revenue after store fee and VAT is approximately KRW 140K, below the KRW 160K daily ad spend.
- Under a rough 15% platform fee and 10% VAT assumption, daily net revenue after store fee and VAT is approximately KRW 170K, slightly above the KRW 160K daily ad spend.
- Therefore, current contribution after platform fee, VAT, and ad spend is roughly break-even before server, support, and team cost.

### Public Comparables Used

- GameAnalytics Q1 2024 benchmark summary: across all markets/projects, median D1 retention was reported around 22.91%, D7 around 4.2%, and D28 around 0.85%. Alcanthia's D7 10-15% is meaningfully above the broad mobile-game median, but genre/channel/cohort quality still matters.
- Sensor Tower 2019 analysis: game revenue is extremely concentrated; the top 1% of revenue-earning game publishers captured around 95% of App Store / Google Play game revenue in Q3 2019. This supports treating breakout upside as real but low-probability.
- Tiny Tower: a two-person pixel idle/simulation case that reportedly reached 825K DAU early, with estimated gross monthly revenue around USD 375K and post-Apple monthly revenue around USD 262K. This is a useful genre-adjacent upside example, but its DAU was thousands of times larger than Alcanthia's current scale.
- BitLife / Candywriter: Stillfront disclosed Candywriter's 2019 revenue at approximately USD 26M with approximately 59% EBIT margin, 1.2M DAU, 7.8M MAU, and a transaction structure capped at USD 195M. This is a mobile simulation breakout case, not a base case.
- Melvor Idle: a solo-developed idle RPG reached more than 600K downloads in Early Access across Steam, App Store, and Google Play before Jagex publishing support, and later more than 1M unique players. This supports the plausibility of niche idle/RPG success by a small team.
- Rusty's Retirement: a solo-developed idle farming game reportedly sold around 330K Steam copies within months, with roughly USD 5 revenue per unit before Steam's 30% cut and around USD 1,800/day four months post-launch. This suggests that a PC/Steam niche path may be worth considering if mobile UA is the bottleneck.

Reference URLs used in the 2026-06-15 estimate:

- GameAnalytics benchmark summary: `https://gamedevreports.substack.com/p/gameanalytics-benchmarks-in-mobile`
- Sensor Tower publisher concentration analysis: `https://sensortower.com/blog/top-one-percent-downloads`
- Tiny Tower early revenue analysis: `https://www.gamesbrief.com/2011/07/ios-tiny-tower-on-track-to-make-3-million-in-its-first-year/`
- Stillfront / Candywriter acquisition disclosure: `https://www.stillfront.com/en/stillfront-group-acquires-candywriter-llc-and-discloses-updated-pro-forma-figures-for-2019/`
- Jagex / Melvor Idle publishing announcement: `https://www.jagex.com/news/jagex-announces-partnership-to-publish-melvor-idle`
- Rusty's Retirement sales analysis: `https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed`

### Scenario Model

This is a strategic estimate, not a forecast:

| Scenario | Estimated probability | Annual gross payment revenue | Annual contribution after variable costs |
| --- | ---: | ---: | ---: |
| Maintenance / small live game | 55-65% | KRW 60-120M | KRW -20M to +20M |
| Niche sustainable game | 20-30% | KRW 200-600M | KRW 30-150M |
| Main-bet candidate for the company | 8-15% | KRW 1-3B | KRW 300M-1B |
| Breakout | 1-3% | KRW 5B+ | KRW 1.5B+ |

Probability-weighted revenue can look attractive because of the breakout tail, but the decision-useful median case is much lower. For planning purposes, treat Alcanthia as a KRW 100-300M annual gross revenue candidate until retention and paid acquisition scalability are proven.

### Strategic Interpretation

- Alcanthia's current signal is better than a random mobile game because it already has paying users, positive gross ROAS signal, and D7 retention above broad mobile-game median benchmarks.
- The current signal is not enough to justify making Alcanthia the company's dominant bet because net contribution is roughly break-even and scale is not proven.
- The key question is not whether users can pay at DAU 200; it is whether the same payment density and retention survive at 3-5x paid acquisition spend.
- If recent paid cohorts reach stable D7 retention around 18-22% and gross ROAS remains around 150-170% after scaling spend, the estimated probability of becoming a meaningful company bet can be raised from roughly 10% to roughly 20-30%.
- If serious 3-month experiments leave D7 near 10-15%, Alcanthia should be treated as a small live asset and learning source, not the next primary company bet.

## 3-Month Strategic Validation Gate

As of 2026-06-15, the working strategy is to treat Alcanthia as a serious candidate for the company's next main opportunity, but not yet as the company's dominant bet.

Primary validation target:

- Over the next roughly 3 months, attempt to raise D7 retention from 10-15% toward approximately 20%.
- The target should mean stable cohort performance, not a one-off spike: recent 2-3 week new-user cohorts should land around 18-22% D7 retention.
- D7 20% is a first gate for whether Alcanthia deserves more company weight, not a complete success definition.

Guardrails:

- D1 retention should improve or at least not materially degrade.
- Payer conversion, ARPPU, and ROAS should not be sacrificed to inflate retention.
- D14/D30 should be watched so early generosity does not destroy long-term progression.
- The team should measure whether players reach the first automation / offline-progress aha moment earlier.

Recommended 3-month operating sequence:

1. Month 1: clean up the funnel view from first farm, first brew, first adventure, first automation/offline reward, and first payment.
2. Month 1-2: segment creatives by promise, especially cozy farming versus automation/production/economy, to test whether retained users differ by acquisition expectation.
3. Month 2: run 2-3 product experiments that move the automation aha moment earlier without collapsing long-term progression.
4. Month 3: validate the best product/creative combination with paid acquisition cohorts and check whether retention and ROAS survive modest spend expansion.

Post-validation decision rules:

- If D7 reaches roughly 18-22% and ROAS/payment quality holds, consider increasing Alcanthia's company weight.
- If D7 reaches 15-18% and the improvement mechanism is clear, continue experiments for another 1-2 months.
- If D7 remains around 10-15% after serious experiments, remove Alcanthia from the company's primary-bet candidate list.
- If D7 improves only by over-rewarding users while payment quality or ROAS worsens, do not count that as validation.

If the 3-month effort fails:

- Do not automatically shut down the game immediately if it still has users and positive contribution margin.
- Reduce Alcanthia to maintenance / small-event mode rather than continuing heavy strategic investment.
- Preserve learning about which theme, loop, persona, or mechanic showed signal.
- Consider a smaller 6-8 week next-game validation project that inherits only the strongest Alcanthia hypothesis, rather than building a broad successor.

## Team Strengths Expressed Through Alcanthia

- Real-time state synchronization and consistency.
- Infrastructure optimization for real-time/online play.
- Handling complex software and exposing it through manageable UX/UI.
- Deterministic simulation, server action replay validation, hash-based lightweight sync, and session/CAS protection.
- Offline simulation and online validation allow a complex mobile game to work with both offline progress and anti-cheat constraints.

## Implemented Or Planned System Evidence From Local Project

- README describes Alcanthia as "실시간 식물 재배 & 포션 양조 게임" and "경영 시뮬레이션 + 생태계 시뮬레이션".
- Game design includes 5x5 garden, plant system, brewing system, adventurers, battle, equipment/enhancement, witch skill tree, progressive disclosure, server verification, and cash currency.
- App store metadata emphasizes real-time grow -> brew -> adventure loop, recipe-free discovery, gradual unlocks, and short mobile sessions.
- Codebase includes exchange/market systems, garden raid/PVP systems, offline simulation tests, login/retention/DAU analytics, and technical IP documentation.

## Strategic Interpretation

- Alcanthia is not just a game experiment; it reuses the company's real-time synchronization, infrastructure, and complex UX strengths.
- It may fit the user's belief that games can survive without being number one because tastes are diverse and persona-driven.
- It is not yet de-risked enough to become the company's dominant bet.
- The most important next validation is whether retention and net profitability improve enough to justify increased focus.

## Open Questions

- What is the net contribution margin after platform fees, VAT, ad spend, server costs, and support load?
- Which user persona is driving payment and retention: automation optimizer, cozy pixel RPG player, economy/trading player, or completionist?
- What specific product changes can move the automation aha moment earlier and raise D7 retention from 10-15% toward 20%?
- Are current cozy farming ads attracting users whose expectations conflict with Alcanthia's actual system complexity?
- Which creative promise attracts the highest-quality users: cozy farming, automation/production, player economy, or RPG adventure/growth?
- What scale ceiling is plausible at the current ROAS and creative/channel mix?
- How much CEO time should move from AI tutor work to Alcanthia if retention improves?

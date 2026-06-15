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

## Current Metrics

As of 2026-06-15, based on user-provided figures:

- DAU: approximately 200.
- ROAS: approximately 150%.
- Daily ad spend: approximately KRW 160K.
- Daily average payment revenue: approximately KRW 220K.
- D7 retention: currently around 10-15%.
- User's expected threshold for stronger confidence: D7 retention around 20%.
- Current assessment: above BEP, but not profitable enough after platform fees and VAT to justify shifting heavy company weight onto it yet.

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
2. Month 2: run 2-3 product experiments that move the automation aha moment earlier without collapsing long-term progression.
3. Month 3: validate the best variant with paid acquisition cohorts and check whether retention and ROAS survive modest spend expansion.

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
- What scale ceiling is plausible at the current ROAS and creative/channel mix?
- How much CEO time should move from AI tutor work to Alcanthia if retention improves?

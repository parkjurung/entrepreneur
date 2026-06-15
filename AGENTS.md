# Entrepreneur Workspace Agent Guide

This repository is the operating workspace for the user's business, CEO decision-making, career path as an entrepreneur, management strategy, and active project portfolio.

Both Codex and Claude use this file as the shared entry point. Keep long-lived memory, operating context, project records, data, and tools in ordinary project directories.

## Source Of Truth

- Shared agent instructions: `AGENTS.md`
- Durable memory and operating records: `memory/`
- Source and extracted data: `data/`
- Repeatable scripts and utilities: `tools/`
- Codex pointer only: `CODEX.md`
- Claude pointer only: `CLAUDE.md`

Do not duplicate durable context into `CODEX.md` or `CLAUDE.md`. Update `AGENTS.md` or files under `memory/` instead.

## Workspace Purpose

Support the user as a CEO and entrepreneur across:

- Business-wide strategy and execution
- Entrepreneurial career-path design
- Strategic decisions and tradeoff analysis
- Active project and initiative management
- Operating cadence, reviews, and follow-through
- Persistent memory across Codex and Claude sessions

## Operating Rules For Agents

- Read `AGENTS.md` first, then inspect the relevant files under `memory/`, `data/`, or `tools/`.
- Treat `memory/` as durable shared memory unless a file states otherwise.
- Preserve Korean business context and user intent when summarizing or reorganizing notes.
- Keep decision records concrete: date, context, options considered, decision, next actions.
- Separate facts, assumptions, and recommendations.
- Prefer concise executive summaries with actionable next steps.
- When adding memory, write it to the most specific `memory/` file instead of scattering duplicates.

## Project Structure

- `memory/profile.md`: User identity, CEO role, career direction, working preferences.
- `memory/business.md`: Business model, market, customers, positioning, strategy.
- `memory/deeptech-strategy.md`: Long-term deeptech entry thesis, energy interest, software defensibility beliefs, and realistic entry scenarios.
- `memory/us-immigration.md`: US immigration and ecosystem access strategy, evidence portfolio, and milestone plan.
- `memory/projects.md`: Active projects, status, owners, next actions, risks.
- `memory/decisions.md`: Decision log and rationale.
- `memory/harness.md`: Repeatable workflows, review cadences, agent operating routines.
- `memory/inbox.md`: Raw notes to triage before they become durable memory.
- `data/source-documents/`: Original source documents.
- `data/extracted/`: Machine-readable extracted data and audit text.
- `tools/`: Repeatable scripts.

## Maintenance

- Keep this guide thin and stable.
- Move detailed or frequently changing context into `memory/`.
- If Codex- or Claude-specific behavior is needed, add the minimum pointer in `CODEX.md` or `CLAUDE.md` and keep shared behavior here.

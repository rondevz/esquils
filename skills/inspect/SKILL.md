---
name: inspect
description: "Read-only code inspection before planning or implementing a feature, ticket, task, or issue. Verify its claims against actual code, map affected paths and reuse opportunities, and recommend whether to run grill-with-docs. Use when asked to inspect or confirm a ticket against the code."
---

# Inspect

Inspect the codebase before planning or implementation. A ticket describes the system as its author believes it works; check that belief against the actual implementation so subsequent design, grilling, and implementation start from verified facts.

This skill is strictly read-only: no edits, commits, ticket updates, or implementation. Its deliverable is a findings report in the conversation. Communicate in the user's preferred language.

## Input

Accept any of:

- A tracker ticket ID or URL: fetch its full description, comments, and relevant attachments using available tools. Use a ClickUp connector when the reference is a ClickUp task and that connector is available; do not assume it is installed.
- A path to a spec, PRD, or ticket file.
- A plain-language description of the work.
- No argument: infer a ticket reference from the current branch only when the project's naming convention supports that inference. Otherwise ask what to inspect.

If the ticket cannot be retrieved or the input is too vague to identify the affected behavior, ask for the missing input rather than inspecting blindly. State inaccessible comments or attachments as evidence gaps.

## 1. Extract the story

Read the input in full, including available comments and screenshots. Distill it into numbered claims: factual statements it makes or implies about the current system. Typical claims include:

- Current behavior: "X currently behaves like Y."
- Diagnosis: "The bug is caused by Z."
- Structure: "Field, endpoint, or table A exists and holds B."
- Scope: "Only component C needs to change."

Requirements such as "it should do W" are the ask, not facts about current behavior. Keep them separate for feasibility checks. An agreed design is intended behavior; its absence from code may be expected rather than a contradiction.

## 2. Locate the related files

Search by domain concept, not only the ticket's literal wording. Cover the relevant vertical slice without forcing unrelated layers into the inspection:

- UI routes, views, components, forms, navigation, and state ownership.
- Server routes, controllers, CLI entry points, consumers, or scheduled jobs.
- Models, business rules, validation, authorization, and persistence.
- Schemas and migrations when applicable.
- Async paths and side effects, including queues and indexing when applicable.
- Existing tests and comparable implementations.
- Recent history of key files, for example `git log --oneline -10 -- <file>`.

For broad independent searches, batch reads and searches. Use exploration subagents only when available and authorized, with the same read-only boundary. Lack of delegation must not prevent a direct inspection.

## 3. Verify the story against the code

Assign each claim a verdict:

- **CONFIRMED**: the inspected implementation supports the claim; cite `file:line`.
- **CONTRADICTED**: the implementation tells a different story; cite `file:line` and explain the difference.
- **UNVERIFIED**: code alone does not establish the claim; identify the required logs, runtime observation, production data, or reporter input.

Do not mistake static evidence for proof of runtime behavior or causality. A plausible cause is not confirmed without evidence that distinguishes it from alternatives. For unverified claims, cite relevant code when useful but never invent a citation for unavailable evidence.

Check every materially relevant path: a claim may hold in one caller and fail in another. Check the ask for hidden constraints, existing implementations, coupling that widens scope, and earlier attempts in git history. Trace changes from completed dependency tickets in the current checkout; their status alone does not prove their implementation is available here.

## 4. Build the full context

Capture what an implementer or designer needs to know:

- End-to-end data flow and responsibility ownership.
- Side effects and consumers of changed fields, contracts, events, and components.
- Established patterns and components to reuse rather than reinvent, including related views.
- Applicable shared design decisions and differences between the ticket's references and current code.
- Test coverage, gaps, and faithful verification locations.

Describe existing architecture without designing a replacement. Identify unresolved shared decisions for the feature-design workflow; leave local, reversible implementation details to implementation.

## 5. Report and stop

Use this structure, scaled to the work:

```markdown
## Inspection: <ticket ID or short title>

### Verdict
<Does the story hold up? Highlight the most consequential finding.>

### Story vs code
| # | Claim | Verdict | Evidence |
|---|-------|---------|----------|
| 1 | <claim> | CONFIRMED / CONTRADICTED / UNVERIFIED | <file:line and explanation, or missing evidence> |

### Related files
<Grouped file map with each file's role in the flow.>

### Full context
<Data flow, responsibilities, consumers, reuse opportunities, conventions, and test coverage.>

### Open questions
<Decisions, missing requirements, and unknowns code cannot resolve. Identify which block design or implementation.>

### Recommendation
Run /grill-with-docs: YES / NO — <reasons>.
<Any missing evidence to gather first or shared decision to revisit.>
```

Recommend `/grill-with-docs` when contradicted premises materially affect the plan, the ask has competing interpretations, scope expands beyond the description, viable approaches have consequential trade-offs, or new domain meanings need agreement.

Recommend skipping it when relevant claims are confirmed, the ask is clear, and existing decisions and patterns sufficiently determine the work. A minor factual correction with no effect on scope or design does not require a new interview. With material unverified claims, identify the missing evidence; interviewing cannot substitute for observing facts.

If unresolved architecture appears during ticket inspection, recommend returning to feature design rather than silently choosing architecture for that ticket. Do not invoke another skill, fix findings, or begin implementation. Report the recommendation and stop; the user chooses the next step.

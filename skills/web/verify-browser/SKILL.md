---
name: verify-browser
description: "Verify user stories and use cases in the real browser with Playwright after implementation and code review, or when asked for browser acceptance. Produce evidence for agreed outcomes and report failures or blocked flows."
---

# Verify browser

Prove that the delivered stories work through the real application's UI. Use the ticket or spec's agreed acceptance flows as the oracle; implementation details and passing code review do not establish user-visible success.

## Establish coverage

Read the requested stories, acceptance criteria, review outcome, and project verification instructions. Follow referenced code only to resolve a concrete execution question. For each required browser scenario, identify its actor, starting data, actions, and expected result. Include specified validation, permission, empty, and error cases alongside the happy path. Ask only about missing expectations that would change the verdict; keep independent scenarios moving.

Cover the ticket's affected journeys. When invoked for an integrated feature, cover the complete journey across its tickets and views. Reuse current, applicable evidence rather than repeating unrelated suites or exploring the entire product.

Record the tested revision and any uncommitted changes. After implementation, run this gate once code-review findings are resolved. Earlier browser checks may guide development, but the final verdict must cover the final code.

## Prepare execution

Load `browser-preflight` from the installed catalog, or resolve this skill's real directory through symlinks and read `../browser-preflight/SKILL.md`. Reuse its readiness record when it still applies. It owns environment diagnosis and its recovery budget; this skill owns the acceptance verdict.

Use Playwright CLI for the walkthrough. Read the installed `playwright-cli --help` and the preflight's executor reference for commands; reuse a configured Playwright MCP or project Playwright runner when appropriate. Follow mandatory harness browser routing first and disclose the actual executor. If no allowed executor works, mark the affected flows blocked with the missing prerequisite. Installing a runtime or configuring Manuvra is separate setup work.

Use an isolated application fixture and synthetic accounts with the required roles. Establish the actual data target before creating or resetting fixtures. Reuse project setup and authentication recipes, preserving user-owned services and data. Create a run-specific browser session and keep its handle across steps.

## Exercise the stories

For each scenario:

1. Reach the starting state through the real application and confirm the actor and fixture.
2. Inspect the current page, then interact through visible controls using current snapshot references or accessible roles and names. Refresh stale references rather than guessing selectors. Use supported waits or assertions for observable readiness.
3. Compare the observed result with the agreed expectation. Verify the resulting state, validation message, navigation, or permission boundary; a successful click or an HTTP 200 alone is insufficient. Reload or revisit persisted changes, including a subsequent read through another relevant view when the scenario requires it.
4. Save focused evidence for the verdict: screenshots and relevant snapshot, trace, console, or network excerpts. Investigate errors that affect the scenario; keep unrelated existing errors separate. Avoid dumping full page trees or logs into context.

Use UI actions for the behavior under test. Direct API or database access can prepare fixtures or corroborate persistence, but cannot substitute for the user's journey. Capture the states that prove an outcome or explain a failure; every action does not need its own screenshot. Follow the agreed viewport and design references when relevant to the story.

Classify each required scenario as **passed**, **failed**, or **blocked**. A product outcome that contradicts the agreed expectation fails. An unavailable environment, role, dependency, or executor blocks it. Keep unexecuted steps explicit; neither inference from code nor another passing scenario makes them pass.

## Handle failures and finish

Retain reproduction steps, expected versus actual results, and evidence before changing anything. In an implementation workflow, fix in-scope defects, rerun affected automated checks, obtain review of the fix, then rerun affected browser scenarios. Broaden the rerun only when the change can affect other covered stories. When invoked for verification alone, report defects; implement fixes only within the user's authorized scope.

Stop equivalent retries after two failures without new evidence. Distinguish a product defect from an environment boundary and retain the original error. Report a blocking prerequisite rather than starting open-ended tooling work.

Write a compact acceptance record in the project's existing delivery location, or a local Markdown artifact if none exists:

- Tested revision and working-tree state, URL, executor, actor/fixture, and viewport where relevant.
- One row per scenario: story/criterion, expected result, observed result, status, and evidence path.
- Failed reproductions, blocked prerequisites, and any remaining coverage gaps.

Keep credentials and session state out of the report and screenshots. Close only run-owned browser sessions and services; preserve the evidence and readiness record for the caller.

**Verified means every required browser scenario passed against the final tested code.** Failed or blocked scenarios leave acceptance incomplete. Report browser acceptance separately from code review, automated tests, and integration status. A walkthrough produces observed evidence; create a permanent Playwright Test suite only when requested or required by the project.

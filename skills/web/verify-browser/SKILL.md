---
name: verify-browser
description: "Verify user stories and use cases in the real browser with Playwright after implementation and code review, or when asked for browser acceptance. Produce evidence for agreed outcomes and report failures or blocked flows."
---

# Verify browser

Prove that the delivered stories work through the real application's UI. Use the ticket or spec's agreed acceptance flows as the oracle; implementation details and passing code review do not establish user-visible success.

## Establish coverage

Read the requested stories, acceptance criteria, review outcome, and project verification instructions. Record the ticket's short reference and title, with its link or local path when available; for a feature spanning tickets, retain each scenario's ticket reference. If no ticket exists, identify the supplied spec or scope explicitly rather than inventing one. Follow referenced code only to resolve a concrete execution question. Derive concrete browser scenarios proactively from the agreed behavior: actor, starting data, actions, and expected result. Include specified validation, permission, empty, and error cases alongside the happy path. Choose representative inputs yourself; ask only about missing expectations that would change the verdict, and keep independent scenarios moving.

Cover the ticket's affected journeys. When invoked for an integrated feature, cover the complete journey across its tickets and views. Reuse current, applicable evidence rather than repeating unrelated suites or exploring the entire product.

Record the tested revision and any uncommitted changes. After implementation, run this gate once code-review findings are resolved. Earlier browser checks may guide development, but the final verdict must cover the final code.

## Prepare execution

Load `browser-preflight` from the installed catalog, or resolve this skill's real directory through symlinks and read `../browser-preflight/SKILL.md`. Reuse its readiness record when it still applies. It owns environment diagnosis and its recovery budget; this skill owns the acceptance verdict.

Use Playwright CLI for the walkthrough. Read the installed `playwright-cli --help` and the preflight's executor reference for commands; reuse a configured Playwright MCP or project Playwright runner when appropriate. Follow mandatory harness browser routing first and disclose the actual executor. If no allowed executor works, mark the affected flows blocked with the missing prerequisite. Installing a runtime or configuring Manuvra is separate setup work.

Use an isolated application fixture and synthetic accounts with the required roles. Establish the actual data target before creating or resetting fixtures. Reuse project setup and authentication recipes, preserving user-owned services and data. Create a run-specific browser session and keep its handle across steps.

## Prepare scenario data

Build a minimal data plan from the scenarios: accounts and roles, related records, and the states each case needs. Reuse suitable synthetic fixtures; create missing data proactively within the verified isolated environment instead of asking the user to populate routine test records. Missing fixtures are preparation work to attempt, not an immediate blocked verdict. If preflight stops only because the fixture or test actor is missing, use its established data target to prepare them, then resume readiness without restarting environment discovery.

Prefer the project's existing factories, seeders, fixture commands, application services, or test-support APIs. Use framework tooling already available, such as Laravel Boost when it exposes suitable application operations; treat it as one adapter, not a required dependency. Otherwise use a small project-native script or the application's UI. Preserve domain invariants and required relationships; raw database writes are a last resort when the schema and invariants are understood. Keep fixture preparation separate from the UI behavior being verified: precreating a record cannot prove the story's create action.

Create only the data needed for the selected cases, with run-specific identifiers and a record of created entities, roles, and preparation commands or recipe. Reuse setup across compatible cases and isolate cases whose starting states conflict. Use the existing environment record rather than inspecting credentials or services again. Keep ordinary fixture preparation distinct from infrastructure recovery, and report time spent on it separately when material. If a prerequisite needs external credentials, shared-data changes, or substantial new tooling, report that specific gap and continue independent scenarios.

Clean up only run-owned data using the project's scoped cleanup recipe. If data must remain for reproduction, record how to locate and remove it. Preserve user-owned records and keep secrets out of fixture artifacts.

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
- Ticket reference and title (or spec/scope), scenario identifiers, and fixture preparation recipe with run-owned entity identifiers.
- One row per scenario: story/criterion, expected result, observed result, status, and evidence path.
- Failed reproductions, blocked prerequisites, and any remaining coverage gaps.

Keep credentials and session state out of the report and screenshots. Close only run-owned browser sessions and services; preserve the evidence and readiness record for the caller.

End with a user-facing summary, even when all flows passed or the run stopped early. Name the ticket briefly, give totals for passed, failed, and blocked scenarios, and list each case by a recognizable behavior with its status and a short observed outcome. Include required cases that could not run as blocked with their reason. Link the detailed acceptance record and relevant evidence so the user need not open artifacts to learn which cases were actually verified. Keep preparation success and automated-test results separate from browser outcomes. For example:

> Ticket #42 — Edit profile. Browser: 2 passed, 0 failed, 1 blocked.
> Passed: save a new name; the value remains after reload. Passed: reject an empty name; the validation message appears. Blocked: administrator-only edit; the test role could not be provisioned. Details: [acceptance record](<report-path>).

**Verified means every required browser scenario passed against the final tested code.** Failed or blocked scenarios leave acceptance incomplete. Report browser acceptance separately from code review, automated tests, and integration status. A walkthrough produces observed evidence; create a permanent Playwright Test suite only when requested or required by the project.

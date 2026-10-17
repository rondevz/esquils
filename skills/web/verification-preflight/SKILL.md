---
name: verification-preflight
description: "Prepare quick browser verification with a ready executor, preferring Playwright CLI for ordinary agent-driven journeys. Use before ad hoc acceptance flows or when browser access fails; bound environment recovery and preserve reusable readiness evidence."
---

# Verification Preflight

Find one working path from the selected browser to the real application and its isolated fixture. Return that path to the acceptance workflow; readiness alone does not verify the feature.

## Establish the boundary

Reuse the agreed journey, expected results, project launch instructions, and selected browser. Identify the URL resolver when the project provides one. Keep tool selection subordinate to the current harness and the user's choices.

For ordinary agent-driven journeys, prefer an already configured Playwright CLI. Use a working native browser when the harness requires it, or retain an existing project executor rather than migrating tools during verification. Read [browser-executor.md](references/browser-executor.md) when selecting or using the executor. A repeatable test suite is a separate deliverable; ordinary walkthroughs do not require a new test project.

For explicitly requested first-time setup, use the Spanish [system setup guide](references/setup.md). Keep installation separate from the readiness timebox.

Record the start time, existing services, and which processes, profiles, and datasets belong to this run. Assign one environment owner when work is delegated. A parent and child should share readiness evidence rather than provision competing stacks. An agent-scoped browser error may require moving verification to the active parent, not changing the application.

Use a short initial timebox: two minutes for an existing local setup unless the task or user supplies another budget. Use one preferred executor and at most one permitted fallback within that same budget. Each retry should test a changed condition or distinguish a hypothesis. After two equivalent failures at one boundary, follow the permitted fallback or report that boundary as blocked. A new URL spelling, executor, or browser profile does not reset the budget. First-time installation and setup need their own explicit scope rather than consuming the walkthrough.

## Prove readiness

Use existing project commands and focused, read-only probes. Report status codes, service identities, and relevant errors; keep credentials, cookies, and full environment dumps out of diagnostic output.

| Boundary | Evidence required | What failure means |
| --- | --- | --- |
| Dependencies → application | A dynamic application request can use its required services. | A healthy database process alone does not establish app connectivity. |
| Application → agent environment | The resolved endpoint returns the expected app or login response. | A port mapping or listening process alone does not establish reachability. |
| Browser → application | The selected browser loads that same app, not an error page or another service. | A successful shell request alone does not establish browser access. |
| Application → fixture | The running web process and fixture setup use the intended isolated database and storage. | A different port, container name, or env file alone does not establish data isolation. |
| Assets and authentication → journey | Required assets finish loading, the app renders, and a fixture user can reach the journey's starting state. | HTML 200, an empty root, or an authenticated dashboard alone does not establish journey readiness. |

Stop probing a boundary once its evidence is sufficient. If a dependency fails, diagnose it before retrying browser actions. If the app works but the browser cannot reach it, keep investigation on the browser/transport boundary.

For Docker DNS, network namespaces, browser ownership, and stale assets, read [environment-boundaries.md](references/environment-boundaries.md) only for the applicable branch.

## Recover within scope

Prefer the smallest reversible repair supported by the failed probe. Preserve the running user's stack and data. Verify the actual database connection before seeding or resetting anything, including when copying a working configuration into a new container.

A fallback must be permitted by the harness and preserve the real app, authentication, fixture isolation, and acceptance criteria. Reuse installed tools and established launch or forwarding recipes. Keep the original error and state which executor ultimately ran the journey.

If recovery would require installing dependencies, inventing a browser driver or proxy, or changing shared infrastructure, surface that as environment work with its scope and cost. Proceed only within existing authorization and a deliberate budget; feature implementation does not silently become open-ended tooling work. Keep independently runnable checks moving while a required external prerequisite is unresolved.

**Ready means:** the selected execution path reaches the required starting screen with a verified fixture and loaded assets. Continue the caller's authorized acceptance workflow immediately with that executor; this internal handoff does not require another user confirmation. Use the executor's supported commands to inspect, interact, check the expected result, and capture evidence. Leave later interaction and product failures to that workflow, using its expected outcomes to distinguish a product defect from an execution failure.

## Handoff and cleanup

Return a compact readiness record:

- **Ready or blocked:** exact boundary and a representative successful probe or raw error.
- **Execution path:** URL, service context, browser session/profile handle, fixture identity, and secret references where needed.
- **Recovery:** changes made, approaches already ruled out, and any remaining limitation.
- **Ownership:** processes and temporary resources to clean up, plus user-owned services to preserve.
- **Time:** environment preparation duration, separate from the later acceptance duration. Report tokens only when actual usage telemetry is available.

Carry this record across handoffs and resume it rather than restarting setup. After acceptance, stop only run-owned services and restore temporary configuration. Keep required flows pending until they have evidence from the real application; a fallback, prototype, or passing automated suite is not itself a passed browser journey.

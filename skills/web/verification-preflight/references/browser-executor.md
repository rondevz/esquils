# Browser executor for ordinary journeys

Use browser automation to perform the agreed journey directly: inspect the page, interact, observe the result, and capture evidence. Prefer the maintained Playwright CLI for this work when it is already available. Follow harness-specific browser requirements first; a working native browser needs no replacement. An existing Puppeteer, Playwright MCP, or project-selected executor can also be reused.

## Readiness

Check `command -v playwright-cli` and `playwright-cli --help`. Use the installed version's help or skill for exact commands and session options. Preserve the returned session and snapshot references across actions. If the executable, browser runtime, or app connection is missing, identify that prerequisite within the preflight budget. Treat installation as setup work instead of downloading packages opportunistically during a journey.

The CLI is an agent-facing executor. Playwright Test is for authored, repeatable tests; creating its configuration and suite is unnecessary for a one-off walkthrough. Consult the [official coding-agent guide](https://github.com/microsoft/playwright/blob/main/docs/src/getting-started-cli.md) when preparing the CLI as a separate setup task.

## Execute with the installed commands

The following illustrates a journey; take actual element references from the current snapshot and discover screenshot, viewport, and session flags from installed help.

```bash
playwright-cli open http://localhost:8000
playwright-cli snapshot
playwright-cli click e3
playwright-cli fill e5 "synthetic value"
playwright-cli press Tab
playwright-cli screenshot
playwright-cli close
```

Navigate using current element references, labels, or roles. Refresh a stale snapshot instead of repeatedly guessing selectors. Use supported click, fill, and key commands; reserve page JavaScript for focused inspection or a demonstrated gap in the executor. Reuse viewport presets or dimensions agreed in the acceptance flow.

Capture the states that prove an outcome or diagnose a failure. Keep the URL, fixture identity, visible result, and persistence check with that evidence. Stop when those agreed outcomes are established. An ordinary journey should produce evidence, not a custom browser driver, CDP implementation, proxy, or test framework.

Close only the run-owned session. Retain the app readiness record so the next journey can start without repeating setup.

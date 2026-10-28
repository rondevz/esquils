# Web

Skills for browser verification and web workflows.

For first-time installation, see the Spanish [system setup guide](./browser-preflight/references/setup.md).

## Model-invoked

Model- or user-reachable.

- **[browser-preflight](./browser-preflight/SKILL.md)**: Reuse the browser session and fixture, confirm the journey's starting state, and return immediately when ready. Diagnose missing readiness only, within a 60-second budget for configured environments. Prefers Playwright CLI.
- **[verify-browser](./verify-browser/SKILL.md)**: After implementation and review, verify stories and use cases through the real UI with Playwright. Reuse preflight readiness and report scenario outcomes with evidence; required failed or blocked scenarios leave acceptance incomplete.

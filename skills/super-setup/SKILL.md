---
name: super-setup
description: "Configure a project for the Esquils workflow by running Matt Pocock's setup-matt-pocock-skills. Use for initial project setup or an explicitly requested configuration update."
---

# Super Setup

The Esquils entry point for project setup. Delegate tracker and domain-document configuration to the Matt Pocock skill bundled in this repository, then offer optional technology guidance. Communicate with the user in their preferred language.

## Bundled skill

Use [setup-matt-pocock-skills](../engineering/setup-matt-pocock-skills/SKILL.md), imported from [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills).

Use this repository's copy and its supporting resources, not an unrelated globally installed version. Resolve dependencies on other Matt Pocock skills from the bundled catalog when needed. If a required bundled resource is missing, report the missing path and stop rather than fabricating its behavior or installing a replacement automatically.

## Run

1. Identify the target project from the user's request or current working directory. If unclear, ask which project to configure. The Esquils skill directory is not the target unless the user explicitly chooses it.
2. Load the bundled `setup-matt-pocock-skills` using the harness's skill mechanism when it can target this copy. Otherwise read the linked `SKILL.md` and follow it directly, resolving supporting resources relative to that skill's directory.
3. Let that skill inspect the project, resolve its configuration choices, and write its configuration. Preserve existing user authorization and decisions; do not ask the same questions again in this wrapper.
4. Handle the optional technology context below. Skip questions already answered by the user or project documentation.
5. Report the actual result and the configuration files created or updated. If setup is incomplete, state the missing dependency, input, or failed operation rather than reporting success.

Stop after setup. Do not start inspection, feature design, ticket creation, or implementation unless separately requested.

## Optional technology context

Inspect existing manifests, project instructions, and technology decisions. Distinguish the observed stack, user-selected constraints, suggestions, and deferred decisions. An existing stack does not require a replacement proposal.

If preferences or a request for guidance have not already been supplied, offer one optional choice in the user's language: "Would you like to provide technology preferences, get a recommendation for this problem, or leave this for later?" Deferring technology choices does not block tracker setup.

- **Provide preferences:** record only what the user selected. Do not infer a full stack from one library preference.
- **Request recommendations:** ground suggestions in the actual problem, existing project, deployment constraints, and team needs. Ask only for information that changes the recommendation. Compare a small number of viable options, including retaining the current stack when applicable. Use current primary documentation for compatibility and capability claims; if it cannot be checked, state the uncertainty. Explain trade-offs in plain language and let the user choose or defer. A recommendation is not an accepted decision.
- **Defer:** continue without selecting or installing technologies. Shared choices that later affect implementation must be resolved during feature design.

When preferences or useful context need to be preserved, update the project's existing source of technology decisions. If there is none, use `docs/agents/project-context.md` with observed technologies, user choices, optional recommendations, and pending decisions clearly separated. Add a pointer in the existing agent instructions following the bundled setup's file-selection rules. Preserve unrelated content and prior decisions. Do not create a context file merely to record that guidance was declined.

This extension documents context; it does not install packages, scaffold the application, or make shared architecture decisions. Keep the Matt setup responsible for its existing configuration.

## Selected verification tooling

When the project already uses a verification tool or the user selects one, preserve that choice and link its execution instructions from the existing agent guidance. [Manuvra](../manuvra/SKILL.md) is bundled as an available option, not a compulsory dependency.

For a selected Manuvra setup, record the application's launch/reset method, synthetic fixture data, evidence location, and persistence readback method when known. Refer to the executable's current schemas instead of copying a fixed job schema into project guidance. Check whether the executable and provider credentials are available without displaying credentials. Missing prerequisites leave verification setup pending; they do not block unrelated tracker configuration. Installing the executable or executing paid provider calls is separate work, not part of documenting the selection.

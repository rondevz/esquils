# Esquils

A skills repository for a workflow built on Matt Pocock's skills, with focused additions for shared design, reuse, and consistency across deliveries. The complete Matt catalog is bundled here rather than required from a separate installation.

## Global installation for local development

```bash
git clone https://github.com/rondevz/esquils.git ~/code/esquils
cd ~/code/esquils
python3 scripts/link-global-skills.py
```

If the repository is already cloned, run the script from that checkout. It links each skill directory directly into `~/.agents/skills` for Codex and OpenCode, and `~/.claude/skills` for Claude Code. It honors `CLAUDE_CONFIG_DIR` when set and preserves conflicting existing entries rather than overwriting them.

Edit skills in this checkout to iterate on the shared source. Rerun the script when adding a skill, and start a new agent session if discovery has not refreshed. Keep this checkout in place while using its links. Local installation does not make skills available on another machine or a cloud runner automatically, and does not install external tools such as Manuvra.

## Catalog

- [Engineering](skills/engineering/README.md): 20 Matt Pocock skills, including setup, specs, tickets, implementation, review, and prototypes.
- [Productivity](skills/productivity/README.md): 7 Matt Pocock skills, including grilling and handoff.
- [In progress](skills/in-progress/README.md): 7 experimental Matt Pocock skills.
- [Miscellaneous](skills/misc/README.md): 4 specialized Matt Pocock skills.
- [inspect](skills/inspect/SKILL.md): read-only inspection adapted from the work skill supplied by the user.
- [explorer](skills/explorer/SKILL.md): read-only implementation preparation, invoked inside implement.
- [super-setup](skills/super-setup/SKILL.md): our entry point, delegating to the Matt setup bundled in this repository.
- [manuvra](skills/manuvra/SKILL.md): the unchanged upstream skill for browser journeys and evidence validation.

The imported skills include their supporting resources. Source revision, copyright, license, and local adaptations are recorded in [UPSTREAM.md](UPSTREAM.md). There are 42 skills in total; the complete catalog is available, but not every skill is a required workflow step.

## Setup

Run [super-setup](skills/super-setup/SKILL.md) in the target project. It uses our local [setup-matt-pocock-skills](skills/engineering/setup-matt-pocock-skills/SKILL.md) copy, then optionally lets the user provide technology preferences, request grounded recommendations, or defer. Suggestions stay distinct from accepted choices. No technology selection is required to configure the tracker, and setup does not install packages.

> Read `~/code/esquils/skills/super-setup/SKILL.md` and configure [project path].

The repository contains the skills; the project being configured is the target. Bundling the catalog does not automatically register it in an agent harness. Skills can be used by supplying their paths, or installed using the harness's supported mechanism.

## Two connected workflows

**Define the feature:** inspect → grill as needed → resolve shared architecture and design, prototyping when useful → spec → tickets.

**Resolve each ticket:** implement → explorer prepares context internally → resolve blocking questions → TDD and agreed acceptance flows → review → record evidence → commit and push.

Inspect is available before ticket implementation when its story needs checking; it is not a compulsory duplicate of explorer. Explorer always runs inside implement. Pushing a branch is not integration; verify the integrated feature journey when the project's delivery process integrates the work.

These workflows organize the work; they are not two replacement skills. Shared architecture and design decisions should be settled before implementation. Local, reversible choices belong in ticket preparation. If inspection reveals a contradicted premise or required change to shared design or scope, revisit that decision and update affected tickets. This is an exception path, not an architecture stage repeated for every ticket.

## Inspect

[inspect](skills/inspect/SKILL.md) verifies claims against code, maps the affected flow and reuse opportunities, and recommends whether further grilling is needed. It is read-only and stops after its report.

Use it to ground feature design or check a ticket whose premises are uncertain. It recommends whether further grilling is necessary and stops for the user's next action. Explorer serves a different purpose: connecting accepted decisions and current code for the agent actually implementing the ticket.

> Read `~/code/esquils/skills/inspect/SKILL.md` and inspect [ticket path or description] in [project path]. Report findings without making changes.

The adaptation makes ClickUp tools and exploration agents optional, distinguishes intended behavior from claims about existing code, and separates static evidence from runtime proof.

## Current approach

Use the bundled Matt skills as the baseline. Our [implement](skills/engineering/implement/SKILL.md) invokes explorer before editing, uses agreed acceptance examples, retains Matt's TDD and code review, records delivery evidence, and delivers through commit and push. Delegated implementers must explore their own checkout using explicit pointers to the ticket, spec, design, and architecture. This does not require delegation and does not add automatic PR/MR creation.

The adapted [to-spec](skills/engineering/to-spec/SKILL.md) and [to-tickets](skills/engineering/to-tickets/SKILL.md) define completion flows before implementation: initial state, actions, expected results, and verification method. The user determines product success; agents inspect facts and execute verification. Required flows that fail or cannot run prevent a verified-completion claim.

Use the project's selected verification tools and respect the harness's browser-tool rules. An agent-driven UI walkthrough gives evidence of observed behavior; repeatable tests provide reusable regression protection. [Manuvra](skills/manuvra/SKILL.md) is bundled as an initial option without modifying its upstream instructions. Its executable and provider key have not been installed or configured, and it has not been run on a target project. The code-review adaptation includes changes that have not yet been committed.

When a project selects Manuvra, document its launch/reset commands, synthetic data, journey definitions, evidence location, and application-owned persistence checks in the project's verification instructions. Explorer discovers those instructions; implement follows the bundled Manuvra skill when the runtime and harness permit its use. A browser result alone is not the ticket's final product verdict. Keep credentials outside skill files and source control.

Prototype only when it resolves a concrete question; an existing view can already be sufficient.

[codebase-design](skills/engineering/codebase-design/SKILL.md) is available for design criteria but has not been trialed in our workflow. Taecontrol's architect remains a candidate for important shared decisions; it is not bundled here and is not a current dependency.

For a new project, shared product, technology, and design decisions must be made explicit before dependent implementation. Super-setup can preserve supplied or selected technology choices in existing project documentation, or `docs/agents/project-context.md` when needed. It does not choose architecture for the user. Shared design and architecture still belong to feature definition; explorer flags missing decisions rather than inventing them.

## Working conventions and first trial

Write skills and resources in English; user-facing communication follows the user's preferred language. Preserve provenance and explain local changes when adapting imported skills. Use project conventions, revalidate references, and define expected behavior before implementation.

Configure a target project with super-setup, inspect a real ticket, and try a small feature one ticket at a time. Check the integrated journey and consistency across views. For evaluating the main greenfield problem, follow with a small new project whose journeys share components and data.

The initial define-feature and implement-ticket drafts remain removed. The current skills have not yet been tested on a real feature. Change the workflow based on observed gaps rather than adding mandatory stages in advance.

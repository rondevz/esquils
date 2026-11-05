---
name: prototype-game
description: Build a small playable Godot experiment to answer a gameplay, control, or game-feel question. Use for uncertain mechanics before committing to a feature design.
---

# Prototype game

Turn one unresolved gameplay question into an experiment in the user's Godot project. The deliverable is a runnable experiment and what was learned. Communicate in the user's language.

## Frame the experiment

Read the request, existing prototype, design decisions and project instructions. State the question, the hypothesis and what would distinguish viable alternatives. Reuse decisions already made; ask only about missing intent that changes the experiment. A chosen behavior awaiting implementation belongs in `implement` rather than another experiment.

Choose a small scene or isolated project with a quick reset. Record which variables change, what stays fixed, the starting state and the task a player performs. Use placeholders unless an asset is necessary to answer the question. Keep any new code scoped to the experiment; a reusable framework or full feature backlog is not the goal.

## Build and run

Use `godot-preflight` to establish only the execution capabilities needed for this experiment. Resolve dependencies by name in the catalog first. For direct reads, resolve this directory through symlinks: sibling game skills are at `../<name>/SKILL.md` in the source checkout and in a flat installation. Report a missing dependency instead of substituting an HTML mockup or unverified execution.

Implement the smallest playable path in the engine. Make relevant state and parameters observable, with restart instructions. Use existing project controls and tooling. Keep saves and progression in an isolated fixture when they are part of the question; ordinary experiments can remain in memory.

Run a technical smoke check sufficient to make the experiment usable. A new test suite is unnecessary for throwaway tuning code; retain meaningful checks for complex rules or regressions that the experiment actually exercises. Record the actual executor and any limitations.

## Playtest and decide

Give the user a precise scene/build and short task, including which alternatives to compare. Exercise available technical checks yourself. When evaluating control, legibility, rhythm or enjoyment, gather play observations and the player's feedback; code inspection, internal input injection and screenshots alone do not establish that experience.

Record the build/revision, configuration, variables, observed behavior, technical issues and player observations separately. Conclude **keep**, **adjust**, **discard**, or **unresolved** for the hypothesis, with the evidence and next question. If no relevant playtest occurred, state **awaiting playtest** rather than inventing a design verdict. Partial capabilities do not block unrelated checks.

Use the project's existing experiment record location, or `.scratch/<experiment>/experiment.md` if none exists. Preserve the runnable experiment and reference it from any resulting design or ticket. Use existing version-control conventions within the user's authorization; a separate branch is optional and does not justify deleting work. Carry validated decisions into design/specs, keeping prototype code distinct from production commitments.

Finish with the question, how to run/reset the experiment, what was actually checked, the result or pending playtest, and a link to the record. Stop at that result unless further implementation was requested.

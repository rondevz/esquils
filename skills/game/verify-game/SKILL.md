---
name: verify-game
description: Verify agreed Godot gameplay or asset-integration behavior in a real scene or exported build, after implementation/review or on request. Report runtime acceptance and playtest observations separately with evidence.
---

# Verify game

Use the agreed behavior as the acceptance oracle and execute the relevant Godot runtime. Code review, successful import and a clean launch are supporting evidence, not substitutes for the behavior under test. Communicate in the user's language.

## Establish coverage and readiness

Read the ticket/spec or bounded request, applicable design references, review outcome and project execution instructions. Record the tested revision and relevant uncommitted changes. Derive cases with starting state, actions, expected observable outcomes and verification method. Reuse settled expectations; ask only about an ambiguity that changes the verdict.

Separate objective contracts from experience questions such as control comfort, legibility, tension or enjoyment. Give the latter a concrete player task and record observations; a technical passing case does not establish a favorable playtest result.

Use `godot-preflight` for the capabilities these cases need, reusing current readiness evidence. Locate it by catalog name first; for direct reads, resolve this directory through symlinks and read `../godot-preflight/SKILL.md` in either the source checkout or a flat installation. Report a missing dependency or capability precisely rather than claiming an unexecuted check passed.

## Prepare and execute scenarios

Prepare the smallest isolated fixture with project-native scenes, reset methods and synthetic state. Create routine test enemies, inventory or save fixtures proactively within the authorized project environment; preserve user saves, editor sessions and source assets. Keep fixture preparation separate from the action being verified.

For each case:

1. Confirm the starting scene/build, fixture and execution mode.
2. Perform the behavior through the applicable runtime interface. A harness may inject game commands when that is the agreed boundary. It must not bypass the behavior being tested, such as teleporting an enemy instead of exercising its response to noise. Desktop focus, device bindings and mouse capture need a desktop-input path.
3. Observe the required state or output through runtime evidence. Use agreed tolerances/time windows for physics, movement and timing. A fixed seed helps reproduce random choices but does not guarantee deterministic physics.
4. Retain focused logs/assertion reports and, where relevant, rendered captures, video, save readback or measurements tied to the tested case and revision. A screenshot supports appearance; motion, sound and input response need corresponding observation.
5. Classify the case as **passed**, **failed** or **blocked**. A contradicted contract fails; an unavailable execution capability blocks it. Keep unexecuted steps explicit and distinguish scenario preparation from acceptance.

For asset work, exercise the asset in its integration scene and reimport it when reimport behavior is part of the contract. Check only relevant scale, material, skeleton, animation, collision or gameplay requirements. An asset merely appearing in the editor does not verify those contracts.

## Playtest and close

Run available technical cases yourself. If the requested assessment depends on playing, supply a short reproducible task, scene/build and reset instructions. Capture the player's actions, confusions and feedback separately from objective failures. Without that observation, report **awaiting playtest**; do not infer enjoyment or comfort from code or images. A human playtest is required only when the agreed scope includes that experience question, not for every asset or rule change.

On failure, preserve reproduction and expected/actual outcomes. If fixes are within the implementation task's scope, correct them, rerun affected checks, resolve review findings and repeat acceptance on the final change. In a verification-only request, report defects unless fixing them is also authorized. Stop equivalent retries after two failures without new evidence; name the environment gap and continue independent cases.

Write a compact acceptance record in the project's existing delivery/evidence location, or `.scratch/<scope>/game-acceptance.md` when none exists. Include scope/ticket, tested revision, engine/platform/renderer as applicable, executor, starting/reset recipe, cases with expected and observed results, statuses, evidence paths and remaining gaps. Record playtest observations and their design conclusion separately. If implementation changed after evidence was captured, identify which cases were rerun and which evidence remains applicable.

Finish with the ticket/scope, each case's outcome, required failed or blocked coverage, playtest status when applicable and the report link. Runtime acceptance is complete only when all required runtime cases passed on the final tested change. Review, automated tests, runtime acceptance, human playtest and integration retain their own statuses. Close only run-owned processes and temporary fixtures; preserve evidence and existing user work.

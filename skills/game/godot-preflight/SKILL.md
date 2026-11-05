---
name: godot-preflight
description: Establish a working Godot execution path before a gameplay experiment or runtime acceptance. Check the requested headless, rendered, desktop-input, or export capabilities and diagnose missing readiness.
---

# Godot preflight

Prepare a usable executor and starting scene for the requested check. Readiness is capability-specific: headless logic, rendered output, desktop input, export and performance are different capabilities. Communicate in the user's language.

## Establish the target

Read the project's execution instructions, selected tools, acceptance scenario and recent readiness evidence. Identify the actual `project.godot`, executable and expected Godot version. Preserve the chosen engine version, renderer and platform; missing access is not a reason to migrate the project or select another engine.

Reuse current evidence when the executable, project, relevant configuration and executor have not changed. A new gameplay revision may reuse environment readiness but still needs its own behavior checks. For a new setup or a changed executor, read [runtime guidance](references/runtime.md) for command semantics and capability limits.

## Check the needed capabilities

1. Confirm the executable with `--version` and consult its `--help` before choosing commands. Locate required extensions, scripts and project-native launch/reset methods.
2. For headless checks, establish that imports complete and the intended scene or harness starts with observable output. Record its completion signal and timeout. Import success or a clean startup alone does not prove assertions passed.
3. For rendered checks, confirm the intended renderer works and the scene actually renders. For visual acceptance, establish a capture or live-observation method. An offline recording is not a real-time performance measurement.
4. For desktop-input checks, establish how focus, keyboard/mouse or controller input and capture/release will be exercised. Internal action injection proves only the path it reaches; record if physical input remains untested.
5. When export is required, check the selected preset, matching templates or custom binaries, destination and target platform. Running an existing build does not require re-exporting it. An exported file still needs an execution check.

A CLI, project harness or connected MCP may be the executor. Verify its actual tools and behavior before relying on it. Neither an MCP server nor any third-party testing framework is compulsory. Preserve a user-selected executor; if it fails, report the concrete failure and use an alternative only within the user's existing authorization.

## Diagnose and hand off

Confirm the starting scene and fixture or identify what scenario preparation remains. Missing synthetic enemies, inventory or a resettable save are preparation tasks for the caller; distinguish them from an unavailable engine or display.

For a configured environment, attempt bounded recovery of missing readiness, reusing the project's recipe. Stop equivalent retries after two failures without new evidence. Cold installation, substantial tooling repair or changing shared configuration is separate setup work; report what is needed and continue independent capability checks. Preserve open user editor sessions, unsaved scenes and user saves.

Return or update the project's readiness record, using `docs/agents/godot.md` when setup has selected it. Include the verified executable/version, project, platform, renderer when applicable, commands, scene/reset recipe, executor, evidence location and a **ready**, **failed** or **blocked** result for each requested capability. Distinguish observations from configured-but-unchecked settings. Record fixture preparation still needed.

Finish when the caller can execute its requested check or has a specific missing prerequisite. Preflight reports readiness; the caller owns behavior acceptance. Do not mark unrelated capabilities blocked merely because they were outside this run.

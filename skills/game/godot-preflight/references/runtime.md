# Godot execution reference

Use the project's exact Godot version and its `--help`. Official `stable` URLs move over time. The examples below illustrate execution modes; substitute the actual executable, project and harness rather than assuming those names exist.

## Execution modes and evidence

| Mode | Useful evidence | Limit |
| --- | --- | --- |
| Import / parse | Imports and scripts load, process diagnostics | Does not exercise gameplay assertions |
| Headless scene or script | Rule outcomes, physics/state observations from a harness | Does not establish final rendering, audible sound or physical input |
| Rendered runtime | Camera, materials, animation, visual feedback | A screenshot does not establish temporal behavior or control comfort |
| Desktop interaction | Focus, mouse capture, bindings, pause and input response | Internal injection does not exercise the OS/device boundary |
| Exported build | Target-platform startup and relevant gameplay | Export success alone is insufficient |
| Real-time measurement | Comparable runtime/frame measurements on recorded hardware | Offline captures and headless runs do not establish GPU frame budgets |

Godot's [CLI documentation](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html) describes `--path`, `--headless`, `--import`, scene/script execution and export options. For example:

```bash
/path/to/godot --version
/path/to/godot --help
/path/to/godot --headless --path /path/to/game --import
```

`--headless` uses a headless display and dummy audio. `--check-only --script` checks parsing rather than game behavior. `--quit-after` counts iterations, not a guaranteed number of physics ticks. Movie capture uses fixed-rate execution and must be treated separately from real-time benchmarking. Unknown CLI options may be ignored; verify the installed binary rather than treating a zero exit as proof of a capability.

## Repeatable scenarios

Record starting scene, spawn positions, inventory/enemy state, relevant settings, reset recipe, actions and expected observations. Include version, platform, physics backend and tick frequency when they affect a result. Use a fixed seed for random choices when useful, and let a harness count physics ticks when timing depends on them.

Godot physics is [not guaranteed deterministic](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html). Use agreed invariants, tolerances and time windows instead of promising identical trajectories or pixels. A missing assertion report or timeout is incomplete evidence, not a passing result.

Use the project's existing test framework or harness. [Godot's engine unit tests](https://docs.godotengine.org/en/stable/engine_details/architecture/unit_testing.html) are not a game-script testing suite provided by `--test`. GUT, GdUnit and MCP integrations are optional external tools whose version and setup must be checked before use.

## Assets and export

Keep source assets and runtime integration responsibilities explicit. [glTF/GLB import](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html) can avoid requiring Blender on an import-only machine; importing `.blend` uses Blender. Rebuilding the GLB from source still needs the source toolchain.

Use an inherited/wrapper scene or project-native import customization to preserve gameplay across reimports. Verify scale, orientation, materials, animation names, skeleton and collision requirements that matter to the task. Consult [import configuration](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html) rather than assuming editor modifications to generated data survive a new source export.

For [export](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html), check the editor binary, preset, matching export templates/custom binaries and output directory. Record which target was executed and which were only exported.

## Readiness record

Use existing project guidance as the source of configured commands. Record verified version and observation date alongside capability outcomes, commands actually used and evidence paths. Keep untested configuration and missing capabilities explicit. Persist only useful reusable readiness evidence; avoid creating a report for every trivial executable lookup.

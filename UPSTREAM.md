# Upstream provenance

The complete `skills/` catalog from [mattpocock/skills](https://github.com/mattpocock/skills) was imported at commit `49dd158d1076134a641b33efb035946536778336`.

The snapshot contains 38 skills and 108 files, including their supporting references, templates, scripts, and category documentation. Original files are unchanged at import. Experimental and miscellaneous skills remain in their upstream categories; inclusion does not make them mandatory workflow stages.

Matt Pocock's copyright and MIT license are preserved in [third_party/mattpocock/LICENSE](third_party/mattpocock/LICENSE). This notice applies to the imported material; it does not declare a license for separately authored Esquils skills.

[upstream.json](third_party/mattpocock/upstream.json) records the source revision and SHA-256 hashes of imported files. The hashes describe the original snapshot, not future local modifications. When adapting a skill, keep the original revision recorded and document the purpose of the local change. Compare future upstream updates before applying them over local adaptations.

`skills/inspect` is adapted from instructions supplied by the user. `skills/super-setup` wraps the bundled Matt setup and provides optional technology guidance. `skills/explorer` prepares implementation context for a ticket. None of these directories is part of the imported snapshot.

`skills/web/verification-preflight` is authored for Esquils: select a prepared browser executor, establish browser-verification readiness, bound environment recovery, and carry evidence across agents and resumed sessions. Ordinary journeys prefer an available Playwright CLI without requiring a new test suite. It is not part of an imported snapshot.

## Local adaptations

- `skills/engineering/implement/SKILL.md`: run explorer in the implementation checkout before edits, use agreed acceptance flows, verify real product behavior, and record delivery evidence according to project conventions. Review includes uncommitted changes. Delivery includes commit and push, preserving unrelated changes and reporting incomplete publication. The original TDD and code-review steps remain.
  Dependency lookup supports both the categorized source checkout and flat skills CLI installations.
  Browser acceptance uses verification-preflight to establish readiness before driving the journey.
- `skills/engineering/to-spec/SKILL.md`: capture agreed acceptance flows, representative data, expected results, design references, and verification methods before implementation. Consume the agreed architecture brief and preserve its shared decisions; unresolved shared design does not become ready work.
- `skills/engineering/to-tickets/SKILL.md`: carry applicable acceptance flows and design references into ticket verification criteria. Include governing architecture references and dependencies between shared contracts or patterns.
- `skills/engineering/code-review/SKILL.md`: add explicit working-tree review, including staged, unstaged, and in-scope untracked files, plus initial repositories without a commit. Default committed review remains.

## Manuvra

The complete `skills/manuvra/` directory from [taecontrol/manuvra](https://github.com/taecontrol/manuvra) was imported unchanged at commit `0bbd1cf1489320736d525260a98f1cd2b6356519`. At that revision, it contains one `SKILL.md` with inline procedures and no supporting skill files.

Luis Güette's copyright and MIT license are preserved in [third_party/manuvra/LICENSE](third_party/manuvra/LICENSE). [The Manuvra manifest](third_party/manuvra/upstream.json) records the revision and original file hash. Importing the skill does not install the executable, provision an API key, or run paid judgments.

## TaeControl Architect

The complete `skills/engineering/architect/` directory from [taecontrol/skills](https://github.com/taecontrol/skills) was imported at commit `ae55f0c619c5204e3d738851ebcb27f396091a1d` and mapped to `skills/architect/`.

The adaptation starts with contextual analysis and feature fit, includes shared reversible decisions when they affect multiple tickets, and leads an interactive recommendation process. Architecture and interaction design can iterate before the spec and tickets. Alternative comparison scales with uncertainty and impact rather than requiring independent agents for every decision. The implementation brief is a shared handoff; the skill stops before production work. Upstream deep-module design-quality criteria remain unchanged.

Copyright and MIT license are preserved in [third_party/taecontrol/LICENSE](third_party/taecontrol/LICENSE). [The manifest](third_party/taecontrol/upstream.json) retains original source hashes and the path mapping; local edits are intentional and those hashes remain the import baseline.

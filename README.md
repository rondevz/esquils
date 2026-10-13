# Esquils

An experimental collection of skills for AI coding agents. “Esquils” is a playful Spanish take on “skills.” It builds on Matt Pocock's skills and takes inspiration from the TaeControl methodology by [guetteman](https://github.com/guetteman).

The goal is a more consistent workflow connecting product decisions, design, implementation, and verification. **All skills, including imported ones, are subject to changes and modifications.**

## Install globally

```bash
git clone https://github.com/rondevz/esquils.git ~/code/esquils
cd ~/code/esquils
python3 scripts/link-global-skills.py
```

The script links this checkout's skills for Claude Code, Codex, and OpenCode, preserving existing entries. Edit them here to iterate; rerun it when adding skills. Open a new agent session if changes haven't appeared. External tools such as Manuvra require separate setup.

## Workflow

Start with [super-setup](skills/super-setup/SKILL.md) in your target project.

- **Define a feature:** inspect → clarify → design and architecture → spec → tickets.
- **Implement a ticket:** explorer → implementation → agreed acceptance flows → review → commit and push.

[inspect](skills/inspect/SKILL.md) checks assumptions against code. [implement](skills/engineering/implement/SKILL.md) runs [explorer](skills/explorer/SKILL.md) internally to gather context and reuse existing patterns. Prototype when it helps resolve a design question, and agree on acceptance flows before implementation.

Browse the [skills](skills/) for details. Source revisions, licenses, and local adaptations are recorded in [UPSTREAM.md](UPSTREAM.md).

## Inspiration and references

- [Matt Pocock's skills](https://github.com/mattpocock/skills)
- [TaeControl's skills](https://github.com/taecontrol/skills), by [guetteman](https://github.com/guetteman)
- [Manuvra](https://github.com/taecontrol/manuvra)

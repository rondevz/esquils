#!/usr/bin/env python3
"""Link this checkout's skills into user-level agent discovery directories."""

import os
from pathlib import Path


def main():
    repository = Path(__file__).resolve().parents[1]
    sources = sorted(path.parent.resolve() for path in (repository / "skills").rglob("SKILL.md"))
    names = [source.name for source in sources]
    if not sources or len(names) != len(set(names)):
        raise SystemExit("No skills found or duplicate directory names; no links created.")

    home = Path.home()
    claude_root = Path(os.environ.get("CLAUDE_CONFIG_DIR", str(home / ".claude"))).expanduser()
    targets = [home / ".agents" / "skills", claude_root / "skills"]
    conflicts = []
    for target in targets:
        target.mkdir(parents=True, exist_ok=True)
        created = existing = 0
        for source in sources:
            destination = target / source.name
            if destination.exists() or destination.is_symlink():
                if destination.is_symlink() and destination.resolve() == source:
                    existing += 1
                else:
                    conflicts.append(destination)
                continue
            destination.symlink_to(source, target_is_directory=True)
            created += 1
        print(f"{target}: {created} links created, {existing} already linked")

    if conflicts:
        print("Existing entries preserved; these skills were not linked:")
        for conflict in conflicts:
            print(f"  {conflict}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

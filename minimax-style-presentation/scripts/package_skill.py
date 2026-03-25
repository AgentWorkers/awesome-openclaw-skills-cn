#!/usr/bin/env python3
"""
MiniMax Style Presentation Skill Packager
Packages the skill for ClawHub publishing.
"""

import os
import sys
import zipfile
from pathlib import Path
from datetime import datetime


def get_version(skill_path: Path) -> str:
    """Get version from _meta.json."""
    import json
    meta_path = skill_path / "_meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        return meta.get("version", "1.0.0")
    return "1.0.0"


def create_package(skill_path: Path, output_dir: Path) -> Path:
    """Create a .zip package for publishing."""
    skill_name = skill_path.name
    version = get_version(skill_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Package filename
    package_name = f"{skill_name}_v{version}_{timestamp}.zip"
    output_path = output_dir / package_name

    # Files to include
    include_patterns = [
        "SKILL.md",
        "_meta.json",
        "scripts/",
    ]

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add SKILL.md
        skill_md = skill_path / "SKILL.md"
        if skill_md.exists():
            zf.write(skill_md, arcname="SKILL.md")

        # Add _meta.json
        meta_json = skill_path / "_meta.json"
        if meta_json.exists():
            zf.write(meta_json, arcname="_meta.json")

        # Add scripts/
        scripts_dir = skill_path / "scripts"
        if scripts_dir.exists():
            for script_file in scripts_dir.rglob("*"):
                if script_file.is_file():
                    arcname = f"scripts/{script_file.name}"
                    zf.write(script_file, arcname=arcname)

    return output_path


def main():
    """Package the skill."""
    skill_path = Path(__file__).parent.parent
    output_dir = skill_path.parent

    print(f"Packaging skill: {skill_path.name}")
    print("-" * 50)

    try:
        output_path = create_package(skill_path, output_dir)
        print(f"Package created: {output_path}")
        print(f"Size: {output_path.stat().st_size} bytes")
        print("-" * 50)
        print("Ready for ClawHub publishing!")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

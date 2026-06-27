#!/usr/bin/env python3
"""
MiniMax Style Presentation Skill Validator
Validates the skill structure for ClawHub publishing.
"""

import os
import re
import sys
from pathlib import Path


def validate_frontmatter(skill_path: Path) -> tuple[bool, str]:
    """Validate SKILL.md frontmatter format."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")

    # Check frontmatter format
    if not content.startswith("---"):
        return False, "SKILL.md must start with YAML frontmatter (---)"

    # Extract frontmatter (between first --- and second ---)
    parts = content.split("---")
    if len(parts) < 3:
        return False, "Frontmatter incomplete (missing closing ---)"
    frontmatter = parts[1]

    # Check required fields
    has_name = "name:" in frontmatter
    has_description = "description:" in frontmatter

    if not has_name:
        return False, "Frontmatter missing 'name' field"
    if not has_description:
        return False, "Frontmatter missing 'description' field"

    return True, "Valid frontmatter"


def validate_meta(skill_path: Path) -> tuple[bool, str]:
    """Validate _meta.json format."""
    meta_path = skill_path / "_meta.json"
    if not meta_path.exists():
        return False, "_meta.json not found"

    import json
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if "id" not in meta:
            return False, "_meta.json missing 'id' field"
        if "version" not in meta:
            return False, "_meta.json missing 'version' field"
        return True, "Valid meta"
    except json.JSONDecodeError as e:
        return False, f"_meta.json is invalid JSON: {e}"


def validate_scripts(skill_path: Path) -> tuple[bool, str]:
    """Validate scripts directory exists with executables."""
    scripts_dir = skill_path / "scripts"
    if not scripts_dir.exists():
        return False, "scripts/ directory not found"

    scripts = list(scripts_dir.glob("*"))
    if not scripts:
        return False, "scripts/ directory is empty"

    return True, f"Found {len(scripts)} script(s)"


def validate_naming(skill_path: Path) -> tuple[bool, str]:
    """Validate naming conventions."""
    folder_name = skill_path.name

    # Check folder name format (hyphen-case)
    if not re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', folder_name):
        return False, f"Folder name '{folder_name}' should be hyphen-case (e.g., 'minimax-style-presentation')"

    # Check SKILL.md frontmatter name matches
    skill_md = skill_path / "SKILL.md"
    if skill_md.exists():
        content = skill_md.read_text(encoding="utf-8")
        match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
        if match:
            frontmatter_name = match.group(1).strip()
            if frontmatter_name != folder_name:
                return False, f"SKILL.md name '{frontmatter_name}' doesn't match folder name '{folder_name}'"

    return True, "Valid naming"


def main():
    """Run all validations."""
    skill_path = Path(__file__).parent.parent

    validations = [
        ("Frontmatter", validate_frontmatter),
        ("Meta", validate_meta),
        ("Scripts", validate_scripts),
        ("Naming", validate_naming),
    ]

    all_passed = True
    print(f"Validating skill at: {skill_path}")
    print("-" * 50)

    for name, validator in validations:
        passed, message = validator(skill_path)
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {message}")
        if not passed:
            all_passed = False

    print("-" * 50)
    if all_passed:
        print("All validations passed!")
        return 0
    else:
        print("Some validations failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

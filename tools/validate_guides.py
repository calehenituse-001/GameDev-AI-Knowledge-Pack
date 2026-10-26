"""Static checks for this documentation-only repository (no extra dependencies)."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

root = Path(__file__).resolve().parents[1]
docs = sorted(root.rglob("*.md"))
problems = []

if len(docs) < 10:
    problems.append(f"Expected at least 10 Markdown guides, got {len(docs)}")

for doc in docs:
    content = doc.read_text(encoding="utf-8")
    if not content.strip():
        problems.append(f"{doc.relative_to(root)}: empty Markdown file")
    # Check ordinary local Markdown links. External and anchored-only links are ignored.
    for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
        link = link.strip().split(" ", 1)[0].strip("<>")
        if link.startswith(("#", "mailto:")) or "://" in link:
            continue
        path = unquote(urlsplit(link).path)
        if path and not (doc.parent / path).exists():
            problems.append(f"{doc.relative_to(root)}: missing link target {path}")

skills = list((root / "skills").rglob("SKILL.md"))
if not skills:
    problems.append("No SKILL.md found")
for skill in skills:
    content = skill.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        problems.append(f"{skill.relative_to(root)}: missing YAML frontmatter")
        continue
    sections = content.split("---", 2)
    if len(sections) < 3 or not all(k in sections[1] for k in ("name:", "description:")):
        problems.append(f"{skill.relative_to(root)}: frontmatter needs name and description")

if problems:
    for problem in problems:
        print("ERROR:", problem)
    sys.exit(1)

print(f"PASS: {len(docs)} Markdown files, {len(skills)} skills, local links resolved")

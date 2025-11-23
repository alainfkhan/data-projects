"""
Absolute paths of superproject: data-projects.
Do not include data folders generated from initialisation.
"""

from pathlib import Path


SUPROJECT_PATH = Path(__file__).parent.parent.resolve()
PROJECTS_PATH = SUPROJECT_PATH / "projects"

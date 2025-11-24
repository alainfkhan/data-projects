from pathlib import Path
from typing import Dict

from src.utils.paths import PROJECTS_PATH


data_folder_names: list[str] = ["raw", "interim", "processed", "external"]


def mkdir_project(project_name: str) -> None:
    Path(PROJECTS_PATH / project_name).mkdir(parents=True, exist_ok=True)
    return


def mkdir_data_folders(project_path: Path) -> Dict[str, Path]:
    data_folders_paths: Dict[str, Path] = {}

    # project/data
    data_path: Path = project_path / "data"

    for name in data_folder_names:
        data_folder: Path = data_path / name
        Path(data_folder).mkdir(parents=True, exist_ok=True)
        data_folders_paths[name] = data_folder

    return data_folders_paths


def csv_to_excel(csv_file: Path) -> None:
    pass

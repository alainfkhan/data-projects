import os
import re
import shutil
from pathlib import Path

import kaggle
import nbformat as nbf
import typer
from icecream import ic
from requests.exceptions import HTTPError
from rich import print
from urllib.parse import urlparse

from src.utils.paths import PROJECTS_DIR, PLAYGROUND_DIR, BASE_DIR
from src.utils.util import (
    random_string,
    mkdir_project,
    mkdir_data_folders,
    csv_to_excel,
)

lines = "-" * 40

app = typer.Typer()


class ProjectsManager:
    def init(self) -> None:
        pass

    pass


class KaggleProjectManager:
    valid_kaggle_url = "www.kaggle.com"

    def is_kaggle_url(self, url: str) -> bool:
        parsed_url = urlparse(url=url)
        return parsed_url.netloc == self.valid_kaggle_url

    def get_handle_from_url(self) -> str:
        """https://www.kaggle.com/datasets/johnsmith/somedataset/data -> johnsmith/somedataset"""

        handle: str = self.kaggle_url.removeprefix(
            f"https://{self.valid_kaggle_url}/datasets/"
        ).removesuffix("/data")
        return handle

    def __init__(self, kaggle_url: str, project_name: str) -> None:
        if not self.is_kaggle_url(kaggle_url):
            raise ValueError("Not a valid kaggle url.")

        self.kaggle_url = kaggle_url
        self.project_name = project_name

        handle = self.get_handle_from_url()
        self.handle = handle

    def init_kaggle(self) -> None:
        project_path: Path = PROJECTS_DIR / self.project_name

        # Make project folder
        mkdir_project(self.project_name)

        # Make data folders in the newly created project folder
        data_folders_paths = mkdir_data_folders(project_path)
        raw_path: Path = data_folders_paths["raw"]
        external_path: Path = data_folders_paths["external"]

        # Download dataset from kaggle
        kaggle.api.authenticate()

        try:
            kaggle.api.dataset_download_files(
                dataset=self.handle, path=raw_path, unzip=True
            )
        except HTTPError as e:
            print(e)
            print("Kaggle dataset not found. Please verify the kaggle URL is correct.")
        else:
            kaggle.api.dataset_metadata(dataset=self.handle, path=external_path)

        print("The dataset has been succefully downloaded")
        return

    def copy_all_files(self) -> None:
        pass


def _find_projects(home: Path = PROJECTS_DIR, randoms_only: bool = False) -> list[str]:
    unwanted_strs = ("__", ".")

    dirs = os.listdir(home)
    projects: list[str] = []
    randoms: list[str] = []

    for dir in dirs:
        if dir.startswith(unwanted_strs):
            continue

        if dir.startswith("_"):
            randoms.append(dir)

        projects.append(dir)

    if randoms_only:
        return randoms

    return projects


def _get_project_dir(name: str, playground: bool = False) -> Path:
    home_dir = PLAYGROUND_DIR if playground else PROJECTS_DIR
    return home_dir / name


@app.command(help="Initialise a project.")
def init(
    name: str = typer.Argument(
        "_" + random_string(), help="Create a name for the project."
    ),
    playground: bool = typer.Option(
        False,
        "-p",
        "--playground",
        help="Initialise the project in the playground directory.",
    ),
    force: bool = typer.Option(
        False,
        "--force-overwrite",
        help="Forcefully overwrite existing initialisation files.",
    ),
) -> None:
    new_project_dir = _get_project_dir(name, playground)
    home = new_project_dir.parent

    # Create project directory
    try:
        new_project_dir.mkdir()
        print(f"{home.name}/")
        print(f"New folder: '{new_project_dir.name}'")
    except FileExistsError:
        if force:
            print("Overwriting initialisation files.")
        else:
            print(f"File '{name}' in {home} already exists.")

    # Create data folders
    mkdir_data_folders(new_project_dir)

    # Create docs/ and reports/ folder
    (new_project_dir / "docs" / "assets").mkdir(parents=True, exist_ok=True)
    (new_project_dir / "reports").mkdir(parents=True, exist_ok=True)

    # Create default initialisation files
    project_files = os.listdir(new_project_dir)
    docs_files = os.listdir(new_project_dir / "docs")

    # Python notebook
    nb_name = f"{name}.ipynb"
    if nb_name not in project_files or force:
        # Create new notebook
        nb = nbf.v4.new_notebook()
        nb["cells"].append(nbf.v4.new_code_cell())
        with open(f"{new_project_dir}/{name}.ipynb", "w") as f:
            nbf.write(nb, f)

        print(f"New file: '{nb_name}'")

    # README.md
    readme = "README.md"
    if readme not in project_files or force:
        with open(f"{new_project_dir}/{readme}", "w"):
            pass

        print(f"New file: '{readme}'")

    # Sources
    sources = "sources.txt"
    if sources not in docs_files or force:
        with open(f"{new_project_dir}/docs/{sources}", "w"):
            pass

        print(f"New file: '{sources}'")


@app.command(help="List the projects.")
def ls(
    playground: bool = typer.Option(
        False,
        "-p",
        "--playgound",
        help="List the projects in the playground directory.",
    ),
    all: bool = typer.Option(
        False, "--all", help="List all project files in both directories."
    ),
) -> None:
    if all:
        projects: list[str] = _find_projects()
        playground_projects: list[str] = _find_projects(PLAYGROUND_DIR)

        total: int = len(projects) + len(playground_projects)

        print(f"[{total}] total projects found")
        print(lines)
        for name in sorted(playground_projects):
            print("playground/      ", end="")
            print(name)

        print("")
        for name in sorted(projects):
            print("projects/        ", end="")
            print(name)
        return

    home: Path = PLAYGROUND_DIR if playground else PROJECTS_DIR
    projects = _find_projects(home)

    print(f"[{len(projects)}] projects found in {home.name}/")
    print(lines)
    for name in sorted(projects):
        print(name)


@app.command(help="Delete a project.")
def rm(
    folders: list[str] | None = typer.Argument(
        None, help="The names of the projects you want to remove."
    ),
    playground: bool = typer.Option(
        False, "-p", "--playground", help="Remove projects in the playground directory."
    ),
    randoms: bool = typer.Option(
        False, "--randoms", help="Delete projects that were randomly generated."
    ),
    all_randoms: bool = typer.Option(
        False,
        "--all-randoms",
        help="Delete random projects in the projects/ and playground/ directories.",
    ),
) -> None:
    if folders is None:
        folders = []

    home = PLAYGROUND_DIR if playground else PROJECTS_DIR

    if randoms and all_randoms:
        raise ValueError("Must have either --randoms or --all-randoms but not both.")

    if randoms:
        random_projects = _find_projects(home, randoms_only=randoms)
        folders = folders + random_projects

    if all_randoms:
        random_projects = _find_projects(randoms_only=True)
        random_playground_projects = _find_projects(PLAYGROUND_DIR, randoms_only=True)
        all_random_projects = random_projects + random_playground_projects

        folders = folders + all_random_projects

    # TODO: fix parents

    for name in folders:
        folder_dir = _get_project_dir(name, playground)

        try:
            shutil.rmtree(folder_dir)
            # print(f"Removed: {folder_dir.parent.name}/{folder_dir.name}")
        except FileNotFoundError:
            print(
                f"Project: {folder_dir.name} does not exist inside {folder_dir.parent.name}/."
            )
            return


@app.command(help="Move a project from projects/ to playground/")
def demote() -> None:
    pass


@app.command(help="Move a project from playground/ to projects/")
def promote() -> None:
    pass


@app.command()
def copy_data_files(name: str = typer.Argument(help="")) -> None:
    print(name)

    pass


@app.command()
def create_db() -> None:
    pass


@app.command()
def download() -> None:
    pass


@app.command()
def init_kaggle() -> None:
    pass


@app.command(help="Begin working on the main file to start analysis.")
def begin() -> None:
    pass


def main() -> None:
    app()
    # # Developer entries:
    # init_kaggle_project: bool = False
    # kaggle_url: str = (
    #     "https://www.kaggle.com/datasets/sticktogethertm/business-analysis-junior"
    # )
    # project_name: str = "panteleev-baj"

    # print("running")
    # copy_csv_files: bool = True

    # if init_kaggle_project:
    #     kaggle_project_manager = KaggleProjectManager(kaggle_url, project_name)
    #     print(f"Initialising kaggle project {kaggle_project_manager.handle}")
    #     kaggle_project_manager.init_kaggle()
    #     print("Initialisation complete.")
    #     return


if __name__ == "__main__":
    main()

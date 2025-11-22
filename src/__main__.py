import os
from pathlib import Path

import kaggle
from icecream import ic
from rich import print
from urllib.parse import urlparse
from requests.exceptions import HTTPError

from utils.paths import PROJECTS_PATH
from utils.util import mkdir_project, mkdir_data_folders, csv_to_excel


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
        project_path: Path = PROJECTS_PATH / self.project_name

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


def main() -> None:
    # Developer entries:
    init_kaggle_project: bool = False
    kaggle_url: str = (
        "https://www.kaggle.com/datasets/sticktogethertm/business-analysis-junior"
    )
    project_name: str = "panteleev-baj"

    copy_csv_files: bool = True

    if init_kaggle_project:
        kaggle_project_manager = KaggleProjectManager(kaggle_url, project_name)
        print(f"Initialising kaggle project {kaggle_project_manager.handle}")
        kaggle_project_manager.init_kaggle()
        print("Initialisation complete.")
        return


if __name__ == "__main__":
    main()

import kaggle
import yaml
from pathlib import Path

NATRAYN_IMDB_DIR: Path = Path(__file__).parent.resolve()
CONFIG_DIR: Path = NATRAYN_IMDB_DIR / "config.yml"
RAW_DATA_DIR: Path = NATRAYN_IMDB_DIR / "data" / "raw"

with open(CONFIG_DIR, "r") as f:
    config = yaml.safe_load(f)

# url: str = config["url"]
handle: str = config["handle"]
# dataset_name: str = config["dataset_name"]


def download_files() -> None:
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(handle, path=RAW_DATA_DIR, unzip=True)
    kaggle.api.dataset_metadata(handle, path=RAW_DATA_DIR)


def create_copy_to_folder():
    pass


def main():
    pass


if __name__ == "__main__":
    main()

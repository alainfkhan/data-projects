import inspect
import kaggle
from pathlib import Path
from urllib.parse import urlparse


def is_kaggle_url(url: str) -> bool:
    parsed_url = urlparse(url=url)
    return parsed_url.netloc == "www.kaggle.com"


def get_handle_from_url(url: str) -> str:
    """
    https://www.kaggle.com/datasets/johnsmith/some-dataset/data -> "johnsmith/some-dataset"
    """
    # url implies https:// included
    # case where url could end in /data

    # Check if kaggle url
    if not is_kaggle_url(url):
        raise ValueError(
            "Invalid URL. The URL has to start with 'https://www.kaggle.com/datasets/...'"
        )

    handle: str = url.removeprefix("https://www.kaggle.com/datasets/").removesuffix(
        "/data"
    )
    return handle


def get_caller_path() -> Path:
    caller_path: Path = Path(inspect.stack()[3].filename).resolve()
    return caller_path


def main(url: str) -> None:
    # THIS_PATH: Path = Path(__file__).resolve()
    CALLER_PATH: Path = get_caller_path()

    PROJECT_PATH: Path = CALLER_PATH.parent.resolve()
    DATA_PATH: Path = PROJECT_PATH / "data"
    DATA_RAW_PATH: Path = DATA_PATH / "raw"
    DATA_EXTERNAL_PATH: Path = DATA_PATH / "external"

    handle: str = get_handle_from_url(url)

    # Make data directories
    data_dirs: list[str] = ["raw", "interim", "cleaned", "external"]
    for dir in data_dirs:
        Path(DATA_PATH / dir).mkdir(parents=True, exist_ok=True)

    # Download data to data/raw
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset=handle, path=DATA_RAW_PATH, unzip=True)
    kaggle.api.dataset_metadata(dataset=handle, path=DATA_EXTERNAL_PATH)

    # dataset_files: Dict[str, list[Dict[str, str]]] = kaggle.api.dataset_list_files(dataset=handle)
    # print(f"Downloaded files: {dataset_files}")

    pass

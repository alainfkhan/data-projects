"""main.py initialises the workspace
installs relevant data
creates relavant dbs
initialises notebooks
"""

import kaggle
import pandas as pd
import sqlite3
from pandas import DataFrame
from pathlib import Path


NATRAYN_IMDB_DIR: Path = Path(__file__).parent.resolve()
DATA_DIR: Path = NATRAYN_IMDB_DIR / "data"

handle: str = "bharatnatrayn/movies-dataset-for-feature-extracion-prediction"
filename_stem: str = "movies"
filename_extension: str = ".csv"
filename: str = f"{filename_stem}{filename_extension}"


def download_files() -> None:
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset=handle, path=DATA_DIR, unzip=True)
    kaggle.api.dataset_metadata(dataset=handle, path=DATA_DIR)


def copy_to_excel() -> None:
    filepath: Path = DATA_DIR / filename
    new_filename_stem: str = f"{filename_stem}-copy"
    new_filename: str = f"{new_filename_stem}.xlsx"

    df: DataFrame = pd.read_csv(filepath)
    df.to_excel(DATA_DIR / f"{new_filename}", sheet_name=new_filename_stem, index=False)
    print(f"{new_filename} created.")


def create_db() -> None:
    # Create database
    conn = sqlite3.connect("natrayn-imdbnatryan-imdb.db")
    conn.close()


def main() -> None:
    # download_files()
    # copy_to_excel()
    # create_db()

    pass


if __name__ == "__main__":
    main()

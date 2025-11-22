# import kaggle
import os
from pathlib import Path

from utils.init_kaggle import main as init_kaggle_main
from utils.util import csv_to_excel


PROJECT_DIR = Path(__file__).parent.resolve()

DATA_DIR = PROJECT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"

url: str = "https://www.kaggle.com/datasets/tylermorse/retail-business-sales-20172019"


def main() -> None:
    init_kaggle_main(url=url)

    # files: list[str] = os.listdir(RAW_DIR)
    # print(files)
    
    # file_paths: list[Path] = [RAW_DIR / f for f in files]
    
    # for file in file_paths:
    #     print("inside for loop")
    #     csv_to_excel(file)

    # print("outside for loop")

if __name__ == "__main__":
    main()

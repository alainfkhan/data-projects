# import kaggle
from utils.init_kaggle import main as init_kaggle_main


url: str = "https://www.kaggle.com/datasets/tylermorse/retail-business-sales-20172019"


def main() -> None:
    init_kaggle_main(url=url)
    pass


if __name__ == "__main__":
    main()

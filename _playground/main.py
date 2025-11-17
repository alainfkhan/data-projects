from utils.init_kaggle import main as init_kaggle_main


def main() -> None:
    print("inside playground")
    url: str = "https://www.kaggle.com/datasets/kainatjamil12/housing/data"
    init_kaggle_main(url=url)
    pass


if __name__ == "__main__":
    main()

from utils import load
from histogram import get_col_values


def main():
    df = load("dataset_train.csv")

    get_col_values(df)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
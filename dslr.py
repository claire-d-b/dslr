from utils import load
from histogram import get_bars
from scatter_plot import get_scatter_plot
from pair_plot import get_pair_plot


def main():
    df = load("dataset_train.csv")

    get_bars(df)
    get_scatter_plot(df)
    get_pair_plot(df)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")

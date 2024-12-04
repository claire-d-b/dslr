from utils import load
from histogram import get_col_values
from scatter_plot import get_scatter_plot
from pair_plot import get_scatter_plot_matrix

def main():
    df = load("dataset_train.csv")

    get_col_values(df)
    # get_scatter_plot(df)
    # get_scatter_plot_matrix(df)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
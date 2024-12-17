from pandas import DataFrame, concat
from seaborn import pairplot
from matplotlib.pyplot import savefig, tight_layout
from utils_figures import load


def get_pair_plot(df: DataFrame) -> any:
    """Display a scatter plot matrix with colors, showing how
    students' scores are spread for each course. Different
    colors are used to distinguish houses."""
    df_house = df.iloc[:, [0]]
    df_courses = df.iloc[:, 6:]

    df = concat([df_house, df_courses], axis=1)

    table = []

    for i in range(df.shape[0]):
        table.insert(i, [])

        for j in range(df.shape[1]):
            if j == 0:
                table[i].insert(j, df.iloc[[i], [j]].values[0][0])
            else:
                table[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    grouped = DataFrame(table)

    pairplot(grouped, hue=grouped.index[0], palette='Set1',
             markers=["o", "s", "D", "X"])

    tight_layout()
    savefig("pairplot")


if __name__ == "__main__":
    try:
        get_pair_plot(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

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

    grouped = concat([df_house, df_courses], axis=1)

    grouped = grouped.sort_values(by='Hogwarts House')

    # Group by house - does not work if no operation like "sum"
    # Bool "as index" to avoid autoindexing of first column
    ngrouped = grouped.groupby('Hogwarts House', as_index=False).sum()
    categories = ngrouped["Hogwarts House"]

    colors = {"Gryffindor": "lightblue", "Hufflepuff": "pink",
              "Ravenclaw": "lightgray", "Slytherin": "lightgreen"}

    # Below, hue is the name of variable in data:
    # variable in data to map plot aspects to different colors.

    pairplot(grouped, hue="Hogwarts House", palette=[colors[category] for category in categories],
             markers=["o", "s", "D", "X"])

    tight_layout()
    savefig("pairplot")


if __name__ == "__main__":
    try:
        get_pair_plot(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

from pandas import DataFrame, concat
from seaborn import pairplot
from stats import get_min, get_max
from matplotlib.pyplot import savefig, tight_layout
from utils_figures import load, normalize_column


def get_pair_plot(df: DataFrame) -> any:
    """Display a scatter plot matrix with colors, showing how
    students' scores are spread for each course. Different
    colors are used to distinguish houses."""
    df_house = df.iloc[:, [0]]
    df_courses = df.iloc[:, 5:]

    min_value = df_courses.get_min()
    max_value = df_courses.get_max()
    df_courses = normalize_column(df_courses, min_value, max_value)
    grouped = concat([df_house, df_courses], axis=1)
    grouped = grouped.sort_values(by='Hogwarts House')

    categories = sorted(set(grouped['Hogwarts House']))
    colors = {"Gryffindor": "lightblue", "Hufflepuff": "pink",
              "Ravenclaw": "lightgray", "Slytherin": "lightgreen"}

    pairplot(grouped, hue="Hogwarts House", palette=[colors[category]
                                                     for category
                                                     in categories],
             markers=["o", "s", "D", "X"])

    tight_layout()
    savefig("pairplot")


if __name__ == "__main__":
    try:
        get_pair_plot(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

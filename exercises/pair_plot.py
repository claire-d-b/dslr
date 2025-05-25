from pandas import DataFrame, concat
from seaborn import pairplot
from matplotlib.pyplot import savefig, tight_layout
from utils_figures import load, normalize_df
from sys import argv


def get_pair_plot(df: DataFrame) -> any:
    """Display a scatter plot matrix with colors, showing how
    students' scores are spread for each course. Different
    colors are used to distinguish houses."""
    df_house = df.iloc[:, [0]]
    df_courses = df.iloc[:, 5:]

    df_courses = normalize_df(df_courses)
    grouped = concat([df_house, df_courses], axis=1)
    grouped = grouped.sort_values(by='Hogwarts House')

    categories = sorted(set(grouped['Hogwarts House']))
    colors = {"Gryffindor": "red", "Hufflepuff": "yellow",
              "Ravenclaw": "blue", "Slytherin": "green"}

    pairplot(grouped, hue="Hogwarts House", palette=[colors[category]
                                                     for category
                                                     in categories],
             markers=["o", "s", "D", "X"])

    tight_layout()
    savefig("pairplot")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python pair_plot.py <path_to_csv_file>.csv")
    else:
        try:
            get_pair_plot((load(argv[1])))
        except AssertionError as error:
            print(f"{error}")

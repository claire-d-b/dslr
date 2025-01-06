# scores / standard deviation / range
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, legend
from numpy import arange
from matplotlib.patches import Rectangle
from utils_figures import load, normalize_column


def get_bars(df: DataFrame) -> any:
    """Create a bar chart plotting each house's scores per course"""
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Select the 2nd column (index 1)
    df_house = df.iloc[:, [0]]
    # Select columns starting from 7th (index 6) onward
    df_courses = df.iloc[:, 6:]
    min_value = df_courses.min()
    max_value = df_courses.max()
    df_courses = normalize_column(df_courses, min_value, max_value)
    df = concat([df_house, df_courses], axis=1)

    table = []

    for i in range(df.shape[0]):
        table.insert(i, [])

        for j in range(df.shape[1]):

            if j == 0:
                table[i].insert(j, df.iloc[[i], [j]].values[0][0])
            else:
                table[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    table = sorted(table)
    ntable = DataFrame(table)

    # Group by 'Hogwarts House' and sum up all columns so we get a table with
    # one row per house
    grouped = ntable.groupby(0)[ntable.columns[1:]].sum().reset_index()

    fig, ax = subplots(figsize=(8, 6))
    x = arange(len(houses))
    bar_width = 0.2
    colors = ["lightblue", "pink", "lightgray", "lightgreen"]
    size = [-1.5, -0.5, 0.5, 1.5]

    handles = [Rectangle((0, 0), 1, 1, color=color) for color in colors]

    for i, house in enumerate(houses):
        values = [float(x) for x in grouped.iloc[i][0:].values[1:]]

        x = [int(x) for x in grouped.iloc[i].index[1:]]

        for j, metric in enumerate(values):
            # X-axis positions for each group of bars
            ax.bar(x[j] + size[i] * bar_width, metric, width=bar_width,
                   label=house, color=colors[i])

    tight_layout()
    legend(handles=handles, labels=houses)
    # ylim(-1000, 1000)
    xlabel("Course n°")
    ylabel("Scores")
    title("Histogram of Data")
    savefig("histogram")


if __name__ == "__main__":
    try:
        get_bars(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, legend, bar
from matplotlib.patches import Rectangle
from utils_figures import load, normalize_column


def get_bars(df: DataFrame) -> any:
    """Create a bar chart plotting each house's scores per course"""
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Select the 2nd column (index 1)
    df_house = df.iloc[:, [0]]
    # Select columns starting from 7th (index 6) onward
    df_courses = df.iloc[:, 5:]

    min_value = df_courses.min()
    max_value = df_courses.max()
    df_courses = normalize_column(df_courses, min_value, max_value)
    df = concat([df_house, df_courses], axis=1)

    fig, ax = subplots(figsize=(8, 6))

    bar_width = 0.2
    colors = ["lightblue", "pink", "lightgray", "lightgreen"]
    size = [-1.5, -0.5, 0.5, 1.5]

    handles = [Rectangle((0, 0), 1, 1, color=color) for color in colors]

    counts = load("describe.csv")

    table = []
    ndf = df.groupby('Hogwarts House').sum()
    for i, (unit, house) in enumerate(zip(counts.iloc[[0], :].values,
                                          ndf.values)):
        table.insert(i, [])

        for j, course in enumerate(house):
            course /= unit
            table[i].insert(j, course)

    table = DataFrame(table)

    for i, col in enumerate(table.columns):
        course = table[col][0]

        for j, metric in enumerate(course):
            # X-axis positions for each group of bars
            bar(i + size[j] * bar_width, metric, width=bar_width,
                label=houses[j], color=colors[j])

    tight_layout()
    legend(handles=handles, labels=houses)
    # ylim(-1000, 1000)
    xlabel("Course n°")
    ylabel("Scores")
    title("Scores per course per house")
    savefig("histogram")


if __name__ == "__main__":
    try:
        get_bars(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

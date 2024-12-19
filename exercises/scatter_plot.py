# scores / standard deviation / ranges
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, scatter, legend
from matplotlib.patches import Patch
from utils_figures import load


def get_scatter_plot(df: DataFrame) -> any:
    """Disay a scatter plot with colored points, student
    number as x-axis vs student score as y-axis. Each
    color representing the house of the student."""
    df_house = df.iloc[:, [0]]
    df_courses = df.iloc[:, 6:]

    grouped = concat([df_house, df_courses], axis=1)

    xaxis = grouped.iloc[:, 0:].index.tolist()  # Height (x-axis)
    yaxis = grouped.iloc[:, 1:].values.tolist()  # Weight (y-axis)

    yaxis = [sum(row) for row in yaxis]

    categories = grouped.iloc[:, 0].values.tolist()  # Category (color)

    colors = {"Gryffindor": "lightblue", "Hufflepuff": "pink",
              "Ravenclaw": "lightgray", "Slytherin": "lightgreen"}
    # Color map for categories
    fig, ax = subplots(figsize=(8, 6))

    scatter(xaxis, yaxis, c=[colors[category] for category in categories])

    tight_layout()

    blue_patch = Patch(color='lightblue', label='Gryffindor')
    pink_patch = Patch(color='pink', label='HufflePuff')
    gray_patch = Patch(color='lightgray', label='Ravenclaw')
    green_patch = Patch(color='lightgreen', label='Slytherin')

    legend(title='Categories', handles=[blue_patch, pink_patch,
                                        gray_patch, green_patch])

    # Add the legend to the plot with custom colors and labels
    xlabel("Student n°")
    ylabel("Scores")
    title("Histogram of Data")
    savefig("scatterplot")


if __name__ == "__main__":
    try:
        get_scatter_plot(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

# scores / standard deviation / ranges
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, legend
from matplotlib.patches import Patch
from utils_figures import load, normalize_column
from numpy import repeat


def get_scatter_plot(df: DataFrame) -> any:
    """Disay a scatter plot with colored points, student
    number as x-axis vs student score as y-axis. Each
    color representing the house of the student."""
    df_house = df.iloc[:, [0]]

    df_courses = df.iloc[:, 5:]

    min_value = df_courses.min()
    max_value = df_courses.max()
    df_courses = normalize_column(df_courses, min_value, max_value)
    grouped = concat([df_house, df_courses], axis=1)

    houses = grouped['Hogwarts House']

    courses = repeat(df_courses.columns, 1600)
    courses_values = [x for sublist in df_courses.values.T for x in sublist]

    colors = {"Gryffindor": "lightblue", "Hufflepuff": "pink",
              "Ravenclaw": "lightgray", "Slytherin": "lightgreen"}
    fig, ax = subplots(figsize=(20, 8))

    ax.scatter(courses, courses_values, c=[colors[category] for
                                           category in repeat(houses, 13)])

    blue_patch = Patch(color='lightblue', label='Gryffindor')
    pink_patch = Patch(color='pink', label='HufflePuff')
    gray_patch = Patch(color='lightgray', label='Ravenclaw')
    green_patch = Patch(color='lightgreen', label='Slytherin')

    legend(loc="lower right", title='Categories', handles=[
                                                           blue_patch,
                                                           pink_patch,
                                                           gray_patch,
                                                           green_patch],
           framealpha=0.25)

    # Add the legend to the plot with custom colors and labels
    xlabel("course")
    ylabel("scores")
    title("scores vs course")
    tight_layout()
    savefig("scatterplot")


if __name__ == "__main__":
    try:
        get_scatter_plot(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

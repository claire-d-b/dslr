# scores / standard deviation / ranges
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, scatter, legend
from matplotlib.patches import Patch


def get_scatter_plot(df: DataFrame) -> any:

    df_house = df.iloc[:, [0]]  # Select the 2nd column (index 1)
    df_courses = df.iloc[:, 6:]   # Select columns starting from 7th (index 6)
    # onward
    grouped = concat([df_house, df_courses], axis=1)

    xaxis = grouped.iloc[:, 0:].index.tolist()  # Height (x-axis)

    yaxis = grouped.iloc[:, 1:].values.tolist()  # Weight (y-axis)

    yaxis = [sum(row) for row in yaxis]

    categories = df.iloc[:, 0].values.tolist()  # Category (color)

    colors = {"Ravenclaw": "blue", "Slytherin": "green",
              "Gryffindor": "red", "Hufflepuff": "gray"}
    # Color map for categories
    fig, ax = subplots(figsize=(8, 6))

    scatter(xaxis, yaxis, c=[colors[category] for category in categories])

    tight_layout()
    # Define RGB value for purple
    gray_rgb = (0.5, 0.5, 0.5)

    red_patch = Patch(color='b', label='Ravenclaw')
    blue_patch = Patch(color='g', label='Slytherin')
    green_patch = Patch(color='r', label='Gryffindor')
    # Create a Patch with the gray color
    gray_patch = Patch(color=gray_rgb, label='HufflePuff')

    legend(title='Categories', handles=[red_patch, blue_patch,
                                        green_patch, gray_patch])

    # Add the legend to the plot with custom colors and labels
    xlabel("Student n°")
    ylabel("Scores")
    title("Histogram of Data")
    savefig("scatterplot")

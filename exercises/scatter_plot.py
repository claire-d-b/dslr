# scores / standard deviation / ranges
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, scatter, legend
from matplotlib.patches import Patch
from utils_figures import load, normalize_column


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

    # grouped = grouped.sort_values(by='Hogwarts House')
    # print("GR", grouped)
    # print("grouped", grouped.iloc[:, 1:])
    categories = [x for sublist in DataFrame(sorted(set(grouped["Hogwarts House"]))).values for x in sublist]
    # xaxis = grouped.iloc[:, 0:].index.tolist()  # Height (x-axis)

    # yaxis = [sum(row) for row in yaxis]
    # xaxis = grouped.iloc[:, 1:].values
    # xaxis = xaxis.mean(axis=0)
    yaxis = grouped.groupby("Hogwarts House").mean()
    # categories = DataFrame(grouped.groupby("Hogwarts House").mean().iloc[:, 0])
    # categories = grouped.iloc[:, 0].values
    scores = grouped.iloc[:, 1:].mean(axis=1)
    # print("yaxis", yaxis)
    houses = [x for sublist in sorted(df_house.values) for x in sublist]
    # houses = DataFrame([x for sublist in grouped.groupby("Hogwarts House").mean().values for x in sublist])
    # categories = grouped.iloc[:, 0].mean(axis=0) # Category (color)
    print("scores", scores.shape)
    print("houses", houses)
    print("cats", DataFrame(categories))
    colors = {"Gryffindor": "lightblue", "Hufflepuff": "pink",
              "Ravenclaw": "lightgray", "Slytherin": "lightgreen"}
    # Color map for categories
    subplots(figsize=(8, 6))
    scatter(houses, scores, c=[colors[category] for category in houses])
    # scatter(xaxis, yaxis.T, c=[colors[category] for category in categories])
    # course, score, house

    blue_patch = Patch(color='lightblue', label='Gryffindor')
    pink_patch = Patch(color='pink', label='HufflePuff')
    gray_patch = Patch(color='lightgray', label='Ravenclaw')
    green_patch = Patch(color='lightgreen', label='Slytherin')

    legend(loc="lower right", title='Categories', handles=[blue_patch, pink_patch,
                                        gray_patch, green_patch], framealpha=0.25)

    # Add the legend to the plot with custom colors and labels
    xlabel("House")
    ylabel("Scores")
    title("Spread of scores per house")
    tight_layout()
    savefig("scatterplot")


if __name__ == "__main__":
    try:
        get_scatter_plot(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

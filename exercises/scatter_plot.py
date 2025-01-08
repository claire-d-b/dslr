# scores / standard deviation / ranges
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, legend, scatter
from matplotlib.patches import Patch
from utils_figures import load, normalize_column
from numpy import repeat


def get_scatter_plot(df: DataFrame) -> any:
    """Disay a scatter plot with colored points, student
    number as x-axis vs student score as y-axis. Each
    color representing the house of the student."""

    ndf = df.sort_values(by='Hogwarts House')

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    colors = ["lightblue", "pink", "lightgray", "lightgreen"]

    fig, ax = subplots(figsize=(20, 8))

    for i, (house, color) in enumerate(zip(houses, colors)):
        df = ndf[ndf['Hogwarts House'] == houses[i]]

        df_house = df.iloc[:, [0]]
        df_courses = df.iloc[:, 5:]
        
        min_value = df_courses.min()
        max_value = df_courses.max()
        df_courses = normalize_column(df_courses, min_value, max_value)
        grouped = concat([df_house, df_courses], axis=1)
        nhouses = grouped['Hogwarts House']
        nhouses = repeat(nhouses, 13).values

        courses = repeat(df_courses.columns, grouped.shape[0])
        courses_values = [x for sublist in df_courses.values.T for x in sublist]

        scatter(courses, courses_values, label=house, c=color)

        legend(loc="lower right", title='Categories', framealpha=0.25)

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

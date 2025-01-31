# scores / standard deviation / ranges
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, legend, \
                              scatter
from utils_figures import load, normalize_column
from numpy import repeat


def get_scatter_plot(df: DataFrame) -> any:
    """Disay a scatter plot with colored points, student
    number as x-axis vs student score as y-axis. Each
    color representing the house of the student."""

    df = df.sort_values(by='Hogwarts House')

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    colors = {"Gryffindor": "lightblue", "Hufflepuff": "pink",
              "Ravenclaw": "lightgray", "Slytherin": "lightgreen"}
 
    df_house = df.iloc[:, [0]]
    df_courses = df.iloc[:, 5:]

    min_value = df_courses.min()
    max_value = df_courses.max()
    df_courses = normalize_column(df_courses, min_value, max_value)

    df_courses = concat([df_courses['Astronomy'], df_courses['Defense Against the Dark Arts']], axis=1)
    grouped = concat([df_house, df_courses], axis=1)

    fig, ax = subplots(figsize=(10, 8))
    # Create lists to store custom handles and labels for the legend
    handles = []
    labels = []

    # Loop through each house and plot the corresponding data points
    for house in houses:
        house_data = grouped[grouped['Hogwarts House'] == house]
        x_unit = house_data['Astronomy']
        y_unit = house_data['Defense Against the Dark Arts']
        
        # Scatter plot for each house
        scatter_plot = ax.scatter(x_unit, y_unit, c=colors[house], label=house)

        # Collect the handle and label for the legend
        handles.append(scatter_plot)  # scatter_plot object is the handle
        labels.append(house)  # House name as the label for the legend

    # Create custom legend by passing handles and labels explicitly
    ax.legend(handles=handles, labels=labels, loc="lower right", title="Hogwarts Houses")

    # Add labels and title
    xlabel("Astronomy")
    ylabel("Defense Against the Dark Arts")
    title("Features")

    # Adjust layout and save the figure
    tight_layout()
    savefig("scatterplot")


if __name__ == "__main__":
    try:
        get_scatter_plot(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

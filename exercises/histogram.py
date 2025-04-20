from pandas import DataFrame, concat
from stats import get_mins, get_maxs
from matplotlib.pyplot import savefig, tight_layout, subplots
from utils_figures import load, normalize


def get_bars(df: DataFrame) -> any:
    """Create a bar chart plotting each house's scores per course"""
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    colors = ["lightblue", "pink", "lightgray", "lightgreen"]

    # Select the 2nd column (index 1)
    df_house = df.iloc[:, [0]]
    # Select columns starting from 7th (index 6) onward
    df_courses = df.iloc[:, 5:]

    # min_value = get_mins(df_courses)
    # max_value = get_maxs(df_courses)

    # print(min_value)
    # print(max_value)
    ndf_courses = normalize_df(df_courses)
    ndf = concat([df_house, df_courses], axis=1)

    # Create a figure with 4 rows and 4 columns of subplots
    fig, axs = subplots(4, 4, figsize=(15, 5))
    # Flatten the 2D array of axes (axs) into a 1D array for easier iteration
    axs = axs.flatten()

    for i, course_unit in enumerate(ndf.iloc[:, 1:]):

        for j, house_unit in enumerate(houses):
            house_data = df[df['Hogwarts House'] == house_unit][course_unit]

            axs[i].hist(house_data, bins=20, alpha=0.5, color=colors[j],
                        label=course_unit)
            axs[i].set_title(course_unit)

    tight_layout()
    savefig("histogram")


if __name__ == "__main__":
    try:
        get_bars(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

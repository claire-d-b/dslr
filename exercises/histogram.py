# scores / standard deviation / range
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, legend, bar
from numpy import arange
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
    print("DF=", df)
    # table = []

    # for i in range(df.shape[0]):
    #     table.insert(i, [])

    #     for j in range(df.shape[1]):

    #         if j == 0:
    #             table[i].insert(j, df.iloc[[i], [j]].values[0][0])
    #         else:
    #             table[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    # table = sorted(table)
    # ntable = DataFrame(table)

    # # Group by 'Hogwarts House' and sum up all columns so we get a table with
    # # one row per house
    # grouped = ntable.groupby(0)[ntable.columns[1:]].sum().reset_index()

    fig, ax = subplots(figsize=(8, 6))
    x = arange(len(houses))
    bar_width = 0.2
    colors = ["lightblue", "pink", "lightgray", "lightgreen"]
    size = [-1.5, -0.5, 0.5, 1.5]

    handles = [Rectangle((0, 0), 1, 1, color=color) for color in colors]

    counts = load("describe.csv")

    print("counts", counts.iloc[[0], :])
    # for i, unit in enumerate(counts.iloc[[0], :].values):
    #     print("unit", unit)
    table = []
    ndf = df.groupby('Hogwarts House').sum()
    for i, (unit, house) in enumerate(zip(counts.iloc[[0], :].values, ndf.values)):
        table.insert(i, [])
        for j, course in enumerate(house):
            print("unit", unit)
            print("houze", course)
            print("j", j)
            course /= unit
            table[i].insert(j, course)

    table = DataFrame(table)
    # table.columns = ndf.columns
    print("table", table)

    # scores_per_house_per_course = table
    # values = ndf.iloc[:, 0:].values
    # print("valz", values)
    # print("cvalz", df_courses.values)
    print("result", len(table.columns))
    # result = table
    for i, col in enumerate(table.columns):
        print('i:', i)
        
        course = table[col][0]
        print("course", course)

        for j, metric in enumerate(course):
            print("metric", metric)
            print("j:", j)
            # X-axis positions for each group of bars
            bar(i + size[j] * bar_width, metric, width=bar_width,
                   label=houses[j], color=colors[j])

    tight_layout()
    legend(handles=handles, labels=houses)
    # ylim(-1000, 1000)
    # xlabel("Course n°")
    # ylabel("Scores")
    title("Histogram of Data")
    savefig("histogram")


if __name__ == "__main__":
    try:
        get_bars(load("../dataset_train.csv"))
    except AssertionError as error:
        print(f"{error}")

# scores / standard deviation / range
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              show, hist, xlabel, ylabel, title, bar, ylim, legend
from collections import Counter
from numpy import arange
from matplotlib.patches import Rectangle


def get_bars(df: DataFrame) -> any:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    dist_to_mean = []
    ranges = []
    std_deviation = []
    df_house = df.iloc[:, [0]]  # Select the 2nd column (index 1)
    df_courses = df.iloc[:, 6:]   # Select columns starting from 7th (index 6) onward
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
    
    # Group by 'Category' and sum the 'Value' column
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
            ax.bar(x[j] + size[i] * bar_width, metric, width=bar_width, label=house, color=colors[i])

    tight_layout()
    legend(handles=handles, labels=houses)
    # ylim(-1000, 1000)
    xlabel("Course n°")
    ylabel("Scores")
    title("Histogram of Data")
    savefig("histogram")


# def get_distance_to_mean(largs: list) -> any:
#     try:
#         len(largs)
#         for arg in largs:
#             ret += arg
#         ret = ret / len(largs)

#     except Exception:
#         print("ERROR")
#     else:
#         return ret

# def get_range(largs: list) -> any:
#     try:
#         largs.sort()
#         for i, lst_unit in enumerate(largs):
#             range.insert(i, lst_unit - largs[len(largs) - 1])
#     except Exception:
#         print("ERROR")
#     else:
#         return range

# def get_standard_deviation(largs: list) -> float:
#     try:
#         len(largs)
#         # Calculate the Mean:
#         mean = 0
#         for arg in largs:
#             mean += arg
#         mean = mean / len(largs)
#         # Calculate Each Deviation from the Mean and
#         # Square it:
#         deviation_lst = []
#         for arg in largs:
#             deviation_lst.append((arg - mean) ** 2)
#         # Calculate the Mean of These Squared Deviations:
#         sd_mean = 0

#         for item in deviation_lst:
#             sd_mean += item
#         sd_mean = sd_mean / len(deviation_lst)
#     except Exception as e:
#         print(f"ERROR: {e}")
#     else:
#         return sd_mean

from pandas import DataFrame, concat
from seaborn import pairplot
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              show, hist, xlabel, ylabel, title, bar, ylim, scatter
from collections import Counter
from numpy import arange
from pandas import DataFrame, read_csv, set_option


def get_pair_plot(df: DataFrame) -> any:
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

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

    grouped = DataFrame(table)

    print("grp", grouped)

    # X-axis positions for each group of bars
    x = arange(len(houses))
    bar_width = 0.2

    # categories = df.iloc[:, 0].values.tolist()  # Category (color)
    print("maison", grouped.index[0])
    pairplot(grouped, hue=grouped.index[0], palette='Set1', markers=["o", "s", "D", "X"])

    tight_layout()
    savefig("pairplot")

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

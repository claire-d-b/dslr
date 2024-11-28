# scores / standard deviation / range
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              show, hist, xlabel, ylabel, title, bar
from collections import Counter


def get_col_values(df: DataFrame) -> any:
    houses = ["Slytherin", "Ravenclaw", "Gryffindor", "Hufflepuff"]

    dist_to_mean = []
    ranges = []
    std_deviation = []
    df_house = df.iloc[:, [0]]  # Select the 2nd column (index 1)
    df_courses = df.iloc[:, 6:]   # Select columns starting from 7th (index 6) onward
    df = concat([df_house, df_courses], axis=1)
    # print(df.shape[1])
    table = []
    #print(df.shape[0])

    for i in range(df.shape[0]):
        table.insert(i, [])

        for j in range(df.shape[1]):

            # print(f"{df.iloc[[i], [j]].values[0][0]}")
            if j == 0:
                table[i].insert(j, df.iloc[[i], [j]].values[0][0])
            else:
                table[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    table = sorted(table)
    ntable = DataFrame(table)

    fig, ax = subplots()
    # for i in range(ntable.shape[1]):
    #     for j in range(ntable.shape[0]):
    #     # ax.plot(col_unit)
    #         print(ntable[i][j])
    
    # Group by 'Category' and sum the 'Value' column
    grouped = ntable.groupby(0)[ntable.columns[1:]].sum().reset_index()
    print("GROUEPD", grouped)

    std_deviation = float("inf")
    min_deviation_index = 0
    for i, category in enumerate(houses):
        # print("un", grouped.iloc[i][1:])
        # print("deux", grouped.iloc[i][1:].index)
        ax.bar(grouped.iloc[i][1:].index, grouped.iloc[i][1:])
        # print("HAHA", grouped.iloc[i][0:].values[1:])
        # # Convert to floats using list comprehension
        # float_list = [float(x) for x in grouped.iloc[i][0:].values[1:]]
        # print("FLOATLST", float_list)
        # print("STD DEVIATION", std_deviation)
        # print("MIN DEVIATION INDEX", min_deviation_index)

        # if (get_standard_deviation(float_list) < std_deviation):
        #     std_deviation = get_standard_deviation(float_list)
        #     min_deviation_index = i
    # if sum(grouped.iloc[i][1:]) < minimum:


    # Add labels and title
    xlabel("Course n°")
    ylabel("Scores")
    title("Histogram of Data")

    #print(ntable)

    # print(ntable.shape[0])
    # print(ntable.iloc[1:ntable.shape[0]])

    # print(ntable.loc[houses[0]])
    # print(ntable.loc[houses[1]])
    # print(ntable.loc[houses[2]])
    # print(ntable.loc[houses[3]])
    # print(ntable)
    # print(ntable.iloc[0])

    # ax.scatter(lhs, rhs)

    tight_layout()
    savefig("output_histogram")
    show()


def get_distance_to_mean(largs: list) -> any:
    try:
        len(largs)
        for arg in largs:
            ret += arg
        ret = ret / len(largs)

    except Exception:
        print("ERROR")
    else:
        return ret

def get_range(largs: list) -> any:
    try:
        largs.sort()
        for i, lst_unit in enumerate(largs):
            range.insert(i, lst_unit - largs[len(largs) - 1])
    except Exception:
        print("ERROR")
    else:
        return range

def get_standard_deviation(largs: list) -> float:
    try:
        len(largs)
        # Calculate the Mean:
        mean = 0
        for arg in largs:
            mean += arg
        mean = mean / len(largs)
        # Calculate Each Deviation from the Mean and
        # Square it:
        deviation_lst = []
        for arg in largs:
            deviation_lst.append((arg - mean) ** 2)
        # Calculate the Mean of These Squared Deviations:
        sd_mean = 0

        for item in deviation_lst:
            sd_mean += item
        sd_mean = sd_mean / len(deviation_lst)
    except Exception as e:
        print(f"ERROR: {e}")
    else:
        return sd_mean

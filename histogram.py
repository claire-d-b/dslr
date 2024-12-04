# scores / standard deviation / range
from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              show, hist, xlabel, ylabel, title, bar, ylim
from collections import Counter
from numpy import arange


def get_col_values(df: DataFrame) -> any:
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

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

    # for i in range(ntable.shape[1]):
    #     for j in range(ntable.shape[0]):
    #     # ax.plot(col_unit)
    #         print(ntable[i][j])
    
    # Group by 'Category' and sum the 'Value' column
    grouped = ntable.groupby(0)[ntable.columns[1:]].sum().reset_index()
    print("GROUEPD", grouped)
    i = 0

    std_deviation = float("inf")
    min_deviation_index = 0
    value_2 = [float(x) for x in grouped.iloc[i][0:].values[1:]]
    # X-axis positions for each group of bars
    fig, ax = subplots(figsize=(8, 6))
    x = arange(len(houses))
    bar_width = 0.2
    colors = ["lightblue", "pink", "lightgray", "lightgreen"]
    for i, house in enumerate(houses):

        value_1 = [int(x) for x in grouped.iloc[i].index[1:]]
        value_2 = [float(x) for x in grouped.iloc[i][0:].values[1:]]
        value_3 = houses
        print("val1", value_1)
        print("val2", value_2)
        print("val3", value_3)
        print("VALUUUUE", value_2[i])

        wi = [-1.5, -0.5, 0.5, 1.5]
        for j, metric in enumerate(value_2):
            # hist(value_2[j], bins=sorted(value_2))
            ax.bar(value_1[j] + wi[i] * bar_width, metric, width=bar_width, label=house, color=colors[i])
        # print("un", grouped.iloc[i][1:])
        # print("deux", grouped.iloc[i][1:].index)
            print("valJ", value_2[j])
            print("i", i)
        tight_layout()
        # ylim(-1000, 1000)
        xlabel("Course n°")
        ylabel("Scores")
        title("Histogram of Data")
        savefig("hist")

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

    #print(ntable)

    # print(ntable.shape[0])
    # print(ntable.iloc[1:ntable.shape[0]])

    # print(ntable.loc[houses[0]])
    # print(ntable.loc[houses[1]])
    # print(ntable.loc[houses[2]])
    # print(ntable.loc[houses[3]])
    # print(ntable)
    # print(ntable.iloc[0])



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

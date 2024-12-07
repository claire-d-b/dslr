from pandas import DataFrame, concat
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel, title, legend
from numpy import arange
from matplotlib.patches import Rectangle
from stats import get_mean, get_median, get_variance, get_standard_deviation, get_quartile


def print_dataframe(df: DataFrame) -> any:
    df_house = df.iloc[:, [0]]  # Select the 2nd column (index 1)
    df_courses = df.iloc[:, 6:]   # Select columns starting from 7th (index 6)
    # onward
    df = concat([df_house, df_courses], axis=1)
    print("df", df)
    print("fd")

    table = []

    for i in range(df.shape[0]):
        table.insert(i, [])

        for j in range(df.shape[1]):

            if j == 0:
                table[i].insert(j, df.iloc[[i], [j]].values[0][0])
            else:
                table[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    ntable = DataFrame(sorted(table))
    # Group by 'Category' and sum the 'Value' column
    grouped = ntable.groupby(0)[ntable.columns[1:]].sum().reset_index()
    print("grouped", grouped)
    ngrouped = grouped.iloc[:, 1:]
    print("ngrouped", ngrouped)

    for i in range(ngrouped.shape[0]):
        print("i", i)
        lst = ngrouped[i:i+1].values.tolist()
        # Flatten using list comprehension
        flattened_lst = [item for sublist in lst for item in sublist]
        print(flattened_lst)
        print("mean:", get_mean(flattened_lst))
        print("median:", get_median(flattened_lst))
        print("variance:", get_variance(flattened_lst))
        print("std deviation:", get_standard_deviation(flattened_lst))
        print("quartile:", get_quartile(flattened_lst))

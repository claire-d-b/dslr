from pandas import DataFrame, concat
from stats import (get_median, get_standard_deviation, get_quartile, get_min,
    get_max, _len, get_mean)
from utils_figures import load
from math import isnan
# from numpy import percentile, std


def print_dataframe(df: DataFrame) -> any:
    """Print statistics per category (house) from a dataframe's values"""
    # Select houses
    df_house = df.iloc[:, [0]]
    # Select courses and scores
    df_courses = df.iloc[:, 5:]

    df = concat([df_house, df_courses], axis=1)

    # # How many scores per course
    # stud_per_course_count = df.shape[0]

    ncolumns = list(df_courses.columns)
    df = df.iloc[:, 1:]

    # df.fillna(df.mean())
    df.dropna()

    values = []
    # nvalues = []

    data = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    ndf = DataFrame(data)

    # nndf = DataFrame(data)

    for i in range(df.shape[1]):
        row_values = df.iloc[:, i].dropna().values
        # Get scores for all 12 courses in a specific house
        nrow_values = df.iloc[:, i].fillna(get_mean(row_values)).values
        # print("row values", nrow_values.tolist())

        # print("i:", i)
        values.insert(i, [])
        # nvalues.insert(i, [])
        # print("row values shape", DataFrame(row_values).shape)
        values[i].append(_len(nrow_values))
        # nvalues[i].append(_len(nrow_values))

        # print("courses_count i", stud_per_course_count)
        values[i].append(get_mean(nrow_values))
        # nvalues[i].append(nrow_values.mean())

        values[i].append(get_standard_deviation(nrow_values))
        # nvalues[i].append(std(nrow_values))

        values[i].append(get_min(nrow_values))
        # nvalues[i].append(nrow_values.min())

        values[i].append(get_quartile(nrow_values)[0])
        # nvalues[i].append(percentile(nrow_values, 25))

        values[i].append(get_median(nrow_values))
        # nvalues[i].append(percentile(nrow_values, 50))

        values[i].append(get_quartile(nrow_values)[1])
        # nvalues[i].append(percentile(nrow_values, 75))

        values[i].append(get_max(nrow_values))
        # nvalues[i].append(nrow_values.max())

        # Remove NaN values before calculating
        row_values = [x for x in nrow_values if not isnan(x)]
        ndf = concat([ndf, DataFrame(values[i])], axis=1)
        # nndf = concat([nndf, DataFrame(nvalues[i])], axis=1)

    # Get the current columns
    columns = ndf.columns.tolist()
    # nncolumns = nndf.columns.tolist()
    # print("ncolumns")
    # # Rename columns to new names
    columns[1:14] = ncolumns
    # nncolumns[1:14] = ncolumns
    # # Assign the new column names back to the DataFrame
    ndf.columns = columns
    # nndf.columns = nncolumns

    # Write the entire DataFrame to a CSV file
    ndf.to_csv("describe.csv", index=False)
    # nndf.to_csv("describe_truth.csv", index=False)

    # A downward-sloping diagonal (from top-left to bottom-right) indicates
    # a negative correlation, where as one variable increases, the other
    # decreases.
    # For example, if you're plotting time spent studying vs. time spent on
    # social media, and they are perfectly inversely related
    # (one goes up, the other goes down), the scatter plot might show
    # a downward diagonal.

    return ndf


if __name__ == "__main__":
    try:
        print(print_dataframe(load("../dataset_train.csv")))
    except AssertionError as error:
        print(f"{error}")
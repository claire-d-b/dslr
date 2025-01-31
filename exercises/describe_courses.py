from pandas import DataFrame, concat
from stats import get_median, get_standard_deviation, get_quartile
from utils_figures import load
from math import isnan


def print_dataframe(df: DataFrame) -> any:
    """Print statistics per category (house) from a dataframe's values"""
    # Select houses
    df_house = df.iloc[:, [0]]
    # Select courses and scores
    df_courses = df.iloc[:, 5:]

    df = concat([df_house, df_courses], axis=1)

    # How many scores per course
    stud_per_course_count = df.shape[0]
    print("stud count", stud_per_course_count)

    ncolumns = list(df_courses.columns)
    print("ncols", ncolumns)
    df = df.iloc[:, 1:]
    print("df", df)

    # print("df shape", df.shape)

    values = []
    data = ["Count", "Std", "Min", "25%", "50%", "75%", "Max"]
    ndf = DataFrame(data)
    print("df ICI", df)

    for i in range(df.shape[1]):
        # Get scores for all 12 courses in a specific house
        nrow_values = df.iloc[:, i]
        # print("row values", nrow_values)
        print("course", DataFrame(nrow_values).columns)

        # print("i:", i)
        values.insert(i, [])
        # print("row values shape", DataFrame(row_values).shape)
        values[i].append(stud_per_course_count)
        # print("courses_count i", stud_per_course_count)
        values[i].append(get_standard_deviation(nrow_values))
        values[i].append(min(nrow_values))
        values[i].append(get_quartile(nrow_values)[0])
        values[i].append(get_median(nrow_values))
        values[i].append(get_quartile(nrow_values)[1])
        values[i].append(max(nrow_values))
        # Remove NaN values before calculating
        row_values = [x for x in nrow_values if not isnan(x)]
        nvalues = DataFrame(values[i]).fillna(get_median(row_values))

        ndf = concat([ndf, nvalues], axis=1)

    # Get the current columns
    print("nnddff", ndf)
    # Get the current columns
    columns = ndf.columns.tolist()
    # print("ncolumns")
    # # Rename columns to new names
    columns[1:14] = ncolumns
    # # Assign the new column names back to the DataFrame
    ndf.columns = columns
    print("cols", ndf.columns)

    # Write the entire DataFrame to a CSV file
    ndf.to_csv("describe_courses.csv", index=False)

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

from pandas import DataFrame, concat
from stats import get_median, get_standard_deviation, get_quartile
from utils_figures import load


def print_dataframe(df: DataFrame) -> any:
    """Print statistics per category (house) from a dataframe's values"""
    # Select houses
    df_house = df.iloc[:, [0]]

    # Select courses and scores
    df_courses = df.iloc[:, 6:]

    df = concat([df_house, df_courses], axis=1)
    # Group by house
    df = df.groupby('Hogwarts House')
    # How many students per house
    houses_count = df.size()
    # sum up courses scores per house
    df = df.sum()

    indexes = list(df.index)

    values = []
    data = ["Count:", "Std:", "Min:", "25%:", "50%:", "75%:", "Max:"]
    ndf = DataFrame(data)

    for i in range(df.shape[0]):
        values.insert(i, [])
        # Get scores for all 12 courses in a specific house
        row_values = [value for value in df.iloc[i]]

        values[i].append(houses_count.iloc[i])
        # print("variance:", get_variance(row_values))
        values[i].append(get_standard_deviation(row_values))
        values[i].append(min(row_values))
        values[i].append(get_quartile(row_values)[0])
        values[i].append(get_median(row_values))
        values[i].append(get_quartile(row_values)[1])
        values[i].append(max(row_values))
        ndf = concat([ndf, DataFrame(values[i])], axis=1)

    ndf = DataFrame(ndf)

    # Get the current columns
    columns = ndf.columns.tolist()
    # Rename columns to new names
    columns[1:5] = indexes
    # Assign the new column names back to the DataFrame
    ndf.columns = columns

    print(ndf)
    return ndf


if __name__ == "__main__":
    try:
        print_dataframe(load("../dataset_train.csv"))
        print_dataframe(load("../dataset_test_completed.csv"))
    except AssertionError as error:
        print(f"{error}")

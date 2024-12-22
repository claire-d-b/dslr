from utils import load, switch_case
from logistic_regression import train_model
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              xlabel, ylabel
from pandas import concat, DataFrame
from seaborn import pairplot
from math import e


def train():
    """Plot the scores per course and classify"""
    df = load("dataset_train.csv")
    # Replace NaN with 0
    df = df.fillna(0)
    df_house = df.iloc[:, [1]]
    df_courses = df.iloc[:, 6:]

    grouped = concat([df_house, df_courses], axis=1)

    grouped = grouped.sort_values(by='Hogwarts House')

    # Group by house - does not work if no operation like "sum"
    # Bool "as index" to avoid autoindexing of first column
    ngrouped = grouped.groupby('Hogwarts House', as_index=False).sum()
    categories = ngrouped["Hogwarts House"]

    xaxis = grouped.iloc[:, 1:].values.tolist()
    yaxis = [value for sublist in df_house.values for value in sublist]

    colors = {0: "lightblue", 1: "pink"}

    # fig, ax = subplots(figsize=(8, 6))
    # print("grouped1", grouped)
    pairplot(grouped, hue="Hogwarts House", palette=[colors
                                                     [switch_case(category)]
                                                     for category in
                                                     categories],
             markers=["o", "s", "D", "X"])
    tight_layout()
    savefig("output_class_I")

    weights, bias = train_model(xaxis, yaxis, 0.01)

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_courses = ndf.iloc[:, 6:]
    cols = ndf.columns[6:].values

    nxaxis = ndf.iloc[:, 6:].values.tolist()

    predictions = []
    for i, scores in enumerate(nxaxis):
        predictions.insert(i, float(1 / (1 + (e ** -((sum(scores) / len(scores)) * weights + bias)))))
    
    grouped = concat([ndf[col] for col in cols], axis=1)

    grouped.insert(0, 'Hogwarts House', [round(p) for p in predictions])
    ngrouped = grouped.groupby('Hogwarts House', as_index=False).sum()
    categories = ngrouped["Hogwarts House"]

    # fig, ax = subplots(figsize=(8, 6))

    grouped = grouped.sort_values(by='Hogwarts House')

    # Write the entire DataFrame to a CSV file
    grouped.to_csv("dataset_test_completed.csv", index=True)
    # print("grouped2", grouped)
    pairplot(grouped, hue="Hogwarts House", palette=[colors
                                                     [category]
                                                     for category in
                                                     categories],
             markers=["o", "s"])

    tight_layout()
    savefig("output_class_II")


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

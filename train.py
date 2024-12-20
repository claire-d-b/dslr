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
    xaxis = [sum(row) for row in xaxis]
    yaxis = [value for sublist in df_house.values for value in sublist]

    grouped = grouped.sort_values(by='Hogwarts House')

    colors = {0: "lightblue", 1: "lightgray"}

    fig, ax = subplots(figsize=(8, 6))

    pairplot(grouped, hue="Hogwarts House", palette=[colors
                                                     [switch_case(category)]
                                                     for category in
                                                     categories],
             markers=["o", "s", "D", "X"])
    tight_layout()

    xlabel("Student n°")
    ylabel("Scores")
    savefig("output_class_I")

    weights, bias = train_model(xaxis, yaxis, 0.01)

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_courses = ndf.iloc[:, 6:]
    ndf = ndf_courses

    nxaxis = ndf_courses.values
    nxaxis = [sum(row) for row in nxaxis]

    predictions = []
    for i, score_unit in enumerate(nxaxis):
        predictions.insert(i, 1 / (1 + (e ** -(score_unit * weights + bias))))

    grouped = concat([DataFrame(predictions), ndf_courses], axis=1)

    fig, ax = subplots(figsize=(8, 6))

    ngrouped = [round(x) for x in grouped.iloc[:, 0].values]

    categories = [round(x) for x in grouped.iloc[:, 0]]
    grouped = concat([DataFrame(categories), ndf_courses], axis=1)

    pairplot(grouped, hue=grouped.columns[0], palette={0: 'lightblue',
                                                       1: 'lightgray'},
             markers=["o", "s"])

    tight_layout()

    xlabel("Student n°")
    ylabel("Scores")
    savefig("output_class_II")


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

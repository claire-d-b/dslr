from utils import load, switch_case
from logistic_regression import train_model
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              scatter, legend, xlabel, ylabel, title
from matplotlib.patches import Patch
from pandas import concat, DataFrame
from numpy import array
from math import e


def train():

    df = load("dataset_train.csv")
    # Replace NaN with 0
    df = df.fillna(0)
    df_house = df.iloc[:, [1]]
    df_courses = df.iloc[:, 6:]

    grouped = concat([df_house, df_courses], axis=1)

    indexes = grouped.iloc[:, 0:].index.tolist()
    xaxis = grouped.iloc[:, 1:].values.tolist()
    xaxis = [sum(row) for row in xaxis]
    yaxis = [value for sublist in df_house.values for value in sublist]

    print("axis - x", xaxis)
    print("axis - y", yaxis)

    categories = grouped.iloc[:, 0].values.tolist()

    colors = {0: "lightblue", 1: "lightgray"}

    fig, ax = subplots(figsize=(8, 6))

    scatter(indexes, xaxis, c=[colors[switch_case(y_axis_unit)] for y_axis_unit in yaxis])

    tight_layout()

    blue_patch = Patch(color='lightblue', label=0)
    gray_patch = Patch(color='lightgray', label=1)

    legend(title='Categories', handles=[blue_patch, gray_patch])

    xlabel("Student n°")
    ylabel("Scores")
    title("Histogram of Data")
    savefig("output_class_I")

    weights, bias = train_model(xaxis, yaxis, 0.01)

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    nindexes = ndf.iloc[:, 0:].index.tolist()
    nxaxis = ndf.iloc[:, 6:].values
    nxaxis = [sum(row) for row in nxaxis]

    predictions = []
    for i, score_unit in enumerate(nxaxis):
        predictions.insert(i, 1 / (1 + (e ** -(score_unit * weights + bias))))

    fig, ax = subplots(figsize=(8, 6))

    scatter(nindexes, nxaxis, c=[colors[round(prediction_unit)] for prediction_unit in predictions])

    tight_layout()

    legend(title='Categories', handles=[blue_patch, gray_patch])

    xlabel("Student n°")
    ylabel("Scores")
    title("Histogram of Data")
    savefig("output_class_II")


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

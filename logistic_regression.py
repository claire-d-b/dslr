from utils import load, switch_case
from linear_regression import train_model
from matplotlib.pyplot import savefig, clf, close
from pandas import concat, DataFrame
from seaborn import pairplot
from math import e
from numpy import round


def stable_sigmoid(z):
    """Compute the sigmoid function in a numerically stable way."""
    if z >= 0:
        exp_neg_z = e ** -z
        return 1 / (1 + exp_neg_z)
    else:
        exp_pos_z = e ** z
        return exp_pos_z / (1 + exp_pos_z)


def train():
    """Plot the scores per course and classify"""
    df = load("dataset_train.csv")

    df_house = df['Hogwarts House']
    df_course = df.iloc[:, 5:]

    df = concat([df_house, df_course], axis=1)

    weight_lst = []
    bias = 0
    houses = df.iloc[:, 0]
    scores = df.iloc[:, 1:]

    for i, score_idx in enumerate(scores.columns):

        weight, bias = train_model(scores[score_idx], houses, 0.01)
        weight_lst.append(weight)
        bias += bias / len(scores[score_idx])

    # print("weight", weight_lst)
    # print("bais", bias)

    categories = sorted(set(houses))

    df = df.sort_values(by='Hogwarts House')

    colors = {0: "lightblue", 1: "pink"}
    # colors_test = {0: "lightblue", 1: "pink"}

    pairplot(df, hue="Hogwarts House", palette=[colors
                                                [switch_case(category)]
                                                for category in
                                                categories],
             markers=["o", "s", "D", "X"])

    savefig("output_class_VII")
    clf()  # Clear the figure content
    close()

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_house = ndf['Hogwarts House']
    ndf_course = ndf.iloc[:, 5:]

    ndf_course = DataFrame(ndf_course)
    ndf = concat([ndf_house, ndf_course], axis=1)

    predictions = []
    for i, row in enumerate(ndf.iloc[:, 1:].values):
        predictions.insert(i, [])

        for j, unit in enumerate(row):
            predictions[i].insert(j, stable_sigmoid(-(weight_lst[j] *
                                  unit + bias)))

    # Display all rows and columns
    # set_option('display.max_rows', None)
    # set_option('display.max_columns', None)

    ndf["Hogwarts House"] = [round(sum(sublist) / len(sublist)) for
                             sublist in predictions]

    ndf = ndf.sort_values(by='Hogwarts House')
    categories = [0, 1]

    pairplot(ndf, hue="Hogwarts House", palette=[colors
                                                 [category]
                                                 for category in
                                                 categories],
             markers=["o", "s"])

    savefig("output_class_VIII")
    clf()  # Clear the figure content
    close()


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

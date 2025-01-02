from utils import load, switch_case
from linear_regression import train_model
from matplotlib.pyplot import savefig, clf, close
from pandas import concat, DataFrame, set_option
from seaborn import pairplot
from math import e
from numpy import round


def train():
    """Plot the scores per course and classify"""
    df = load("dataset_train.csv")

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    df = df[df['Hogwarts House'] == houses[2]]
    print("filter0", df)

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
        bias += bias
    bias /= len(scores.columns)

    # print("weight", weight_lst)
    # print("bais", bias)

    categories = sorted(set(houses))

    df = df.sort_values(by='Hogwarts House')

    colors = {0: "lightblue", 1: "pink"}

    pairplot(df, hue="Hogwarts House", palette=[colors
                                                [switch_case(category)]
                                                for category in
                                                categories],
             markers=["o", "s", "D", "X"])

    savefig("output_class_III")
    clf()  # Clear the figure content
    close()

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_house = ndf['Hogwarts House']
    ndf_course = ndf.iloc[:, 5:]

    ndf_course = DataFrame(ndf_course)
    ndf = concat([ndf_house, ndf_course], axis=1)

    predictions = []
    print("ndf", ndf)
    print("vals", ndf.iloc[:, 1:].values)
    values = ndf.iloc[:, 1:].values
    for i, row in enumerate(values):
        predictions.insert(i, [])

        for j, unit in enumerate(row):
            print("unit", unit)
            z = weight_lst[j] * unit + bias
            predictions[i].insert(j, 1 / (1 + e ** -z))

    # Display all rows and columns
    set_option('display.max_rows', None)
    set_option('display.max_columns', None)
    print("preds", predictions)
    ndf["Hogwarts House"] = [round(sum(sublist) / len(sublist)) for
                             sublist in predictions]

    ndf = ndf.sort_values(by='Hogwarts House')
    categories = sorted(set(ndf["Hogwarts House"]))

    pairplot(ndf, hue="Hogwarts House", palette=[colors
                                                 [category]
                                                 for category in
                                                 categories],
             markers=["o", "s"])

    savefig("output_class_IV")
    clf()  # Clear the figure content
    close()


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

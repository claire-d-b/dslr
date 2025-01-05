from utils import load, get_housename, get_housenumber, normalize_column
from linear_regression import train_model, minimize_cost
from matplotlib.pyplot import savefig, clf, close
from pandas import concat, DataFrame, set_option
from seaborn import pairplot
from math import e
from numpy import round, dot
import random


def train():
    """Plot the scores per course and classify"""
    origin_df = load("dataset_train.csv")

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    df_house = origin_df.iloc[:, [0]]
    df_course = origin_df.iloc[:, 5:]

    # Normalization
    min_values = df_course.min()
    max_values = df_course.max()
    # -> résultats entre -1 et 1
    df_course = df_course.apply(lambda col: normalize_column(col, min_values[col.name], max_values[col.name]))

    df = concat([df_house, df_course], axis=1)
    df = df.sort_values(by='Hogwarts House')

    summed_df = df.groupby("Hogwarts House", as_index=False).sum()

    w = []
    b = []
    # Generate a random floating-point number between -0.01 and 0.01
    theta_0 = random.uniform(-0.01, 0.01)
    theta_1 = random.uniform(-0.01, 0.01)
    for i in range(len(houses)):
        w.insert(i, [])
        b.insert(i, [])
        # Scores of all students in the 13 courses for each house
        overall_scores = [item for sublist in summed_df[summed_df['Hogwarts House'] == houses[i]].iloc[:, 1:].values for item in sublist]

        for j, item in enumerate(overall_scores):
            weight, bias, mse = minimize_cost(len(origin_df), theta_0, theta_1, item, houses[i], 0.01)
            w[i].insert(j, weight)
            b[i].insert(j, bias)

    total_sum = sum(sum(sublist) for sublist in b)
    total_length = sum(len(sublist) for sublist in b)
    bias = total_sum / total_length

    colors = {0: "lightblue", 1: "pink", 2: "lightgray", 3: "lightgreen"}
    # index of category (0 to 3)
    categories = [i for i, x in enumerate(houses)]

    pairplot(df, hue="Hogwarts House", palette=[colors
                                                [category]
                                                for category in
                                                categories],
             markers=["o", "s", "D", "X"])

    savefig("output_class_I")
    clf() # Clear the figure content
    close()

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_house = ndf['Hogwarts House']
    ndf_course = ndf.iloc[:, 5:]

    min_values = ndf_course.min()
    max_values = ndf_course.max()  # Valeurs maximales par colonne
    # Normalization of data (between -1 and 1)
    ndf_course = ndf_course.apply(lambda col: normalize_column(col, min_values[col.name], max_values[col.name]))

    ndf = concat([ndf_house, ndf_course], axis=1)

    predictions = []
    for i, col in enumerate(ndf.iloc[:, 1:].values):
        predictions.insert(i, [])

        for j in range(len(houses)):
            z = dot(col, w[j]) + bias
            predictions[i].insert(j, 1 / (1 + (e ** -z)))

    ndf['Hogwarts House'] = [get_housename(p.index(max(p))) for p in predictions]

    ndf = ndf.sort_values(by='Hogwarts House')

    pairplot(ndf, hue="Hogwarts House", palette=[colors
                                                 [category]
                                                 for category in
                                                 categories],
             markers=["o", "s", "D", "X"])

    savefig("output_class_II")
    clf()
    close()


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

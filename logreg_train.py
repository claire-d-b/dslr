from utils import load, get_housename, normalize_column
from linear_regression import minimize_cost
from matplotlib.pyplot import savefig, clf, close
from pandas import concat
from seaborn import pairplot
from math import e
from numpy import dot
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
    df_course = df_course.apply(lambda col: normalize_column(col,
                                min_values[col.name], max_values[col.name]))

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
        overall_scores = [item for sublist in summed_df[summed_df
                          ['Hogwarts House'] == houses[i]].iloc[:, 1:].values
                          for item in sublist]

        for j, item in enumerate(overall_scores):
            weight, bias, mse = minimize_cost(len(origin_df), theta_0, theta_1,
                                              item, houses[i], 0.01)
            w[i].insert(j, weight)
            b[i].insert(j, bias)

    total_sum = sum(sum(sublist) for sublist in b)
    total_length = sum(len(sublist) for sublist in b)
    bias = total_sum / total_length

    f = open("thetas.csv", "w")
    f.write(f"theta_0: {bias}\ntheta_1: {[[float(x) for x in row] for row in w]}")
    f.close()

    colors = {0: "lightblue", 1: "pink", 2: "lightgray", 3: "lightgreen"}
    # index of category (0 to 3)
    categories = [i for i, x in enumerate(houses)]

    pairplot(df, hue="Hogwarts House", palette=[colors
                                                [category]
                                                for category in
                                                categories],
             markers=["o", "s", "D", "X"])

    savefig("output_class_I")
    # Clear the figure content
    clf()
    close()


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

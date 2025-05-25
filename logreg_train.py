from utils import load, normalize_df
from linear_regression import minimize_cost
from matplotlib.pyplot import savefig, clf, close
from pandas import concat
from seaborn import pairplot
import random
from exercises.stats import _len


def train():
    """Plot the scores per course and classify"""
    origin_df = load("dataset_train.csv")
    origin_df = origin_df.fillna(0)

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    df_house = origin_df.iloc[:, [0]]
    df_course = origin_df.iloc[:, 5:]

    # # Normalization
    # min_values = df_course.get_min()
    # max_values = df_course.get_max()
    # # -> résultats entre -1 et 1
    # df_course = df_course.apply(lambda col: normalize_column(col,
    #                             min_values[col.name], max_values[col.name]))
    df_course = normalize_df(df_course)

    df = concat([df_house, df_course], axis=1)

    df = df.sort_values(by='Hogwarts House')

    summed_df = df.groupby("Hogwarts House", as_index=False).sum()

    w = []
    b = []
    # Generate a random floating-point number between -0.01 and 0.01
    theta_0 = random.uniform(-0.01, 0.01)
    theta_1 = random.uniform(-0.01, 0.01)
    for i in range(_len(houses)):
        w.insert(i, [])
        b.insert(i, [])
        # Scores of all students in the 13 courses for each house :
        # 4 lists of 13 values
        overall_scores = [item for sublist in summed_df[summed_df
                          ['Hogwarts House'] == houses[i]].iloc[:, 1:].values
                          for item in sublist]
        # print("overall scores", overall_scores)
        # print("overall scores shape", DataFrame(overall_scores).shape)

        for j, item in enumerate(overall_scores):
            # print("i:", i)
            weight, bias, mse = minimize_cost(_len(overall_scores),
                                              theta_0, theta_1,
                                              item, 1, 0.01)
            w[i].insert(j, weight)
            b[i].insert(j, bias)

    # Here we take the average value of ou bias
    # print("bias", b)
    bias = [sum(b_row) / _len(b_row) for b_row in b]
    # print("bias", bias)

    # Write reusable thetas to a file
    f = open("thetas.csv", "w")
    thetas_1 = [[float(x) for x in row] for row in w]
    f.write(f"theta_0: {bias}\ntheta_1: {thetas_1}")
    f.close()

    colors = {0: "red", 1: "yellow", 2: "blue", 3: "green"}
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

from utils import load, switch_case, switch_case_rev, normalize_column
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
    print("courses scores 0", df_course)

    # Appliquer la normalisation pour chaque colonne (matière)
    min_values = df_course.min()  # Valeurs minimales par colonne
    print("minval", min_values)
    max_values = df_course.max()  # Valeurs maximales par colonne
    print("maxvals", max_values)
    df_course = df_course.apply(lambda col: normalize_column(col, min_values[col.name], max_values[col.name]))

    df = concat([df_house, df_course], axis=1)
    # print("DF", df)
    df = df.groupby("Hogwarts House", as_index=False).sum()

    # print("DF", df)
    w = []
    b = []
    # Generate a random floating-point number between -0.01 and 0.01
    theta_0 = random.uniform(-0.01, 0.01)
    theta_1 = random.uniform(-0.01, 0.01)
    # print("eq", [item for sublist in df[df['Hogwarts House'] == houses[0]].iloc[:, 1:].values for item in sublist])
    for i in range(len(houses)):
        w.insert(i, [])
        b.insert(i, [])
        flat_values = [item for sublist in df[df['Hogwarts House'] == houses[i]].iloc[:, 1:].values for item in sublist]
        for j, item in enumerate(flat_values):
            # print("item", len(origin_df))
            # print("itemmmm", item)
            weight, bias, mse = minimize_cost(len(origin_df), theta_0, theta_1, item, switch_case(houses[i]), 0.01)
            # print("wei", weight)
            w[i].insert(j, weight)
            b[i].insert(j, bias)

    # Calculate the sum of all elements
    total_sum = sum(sum(sublist) for sublist in b)
    # Calculate the total number of elements
    total_length = sum(len(sublist) for sublist in b)
    # Calculate the average of all elements
    bias = total_sum / total_length

    categories = [switch_case(x) for x in houses]
    colors = {0: "lightblue", 1: "pink", 2: "lightgray", 3: "lightgreen"}
    onevsall_categories = [0, 1, 2, 3]
    
    # print("w", w)

    # print("bias", bias)
    # print("df1", df)
    pairplot(df, hue="Hogwarts House", palette=[colors
                                                [category]
                                                for category in
                                                categories],
             markers=["o", "s", "D", "X"])

    savefig("output_class_I")
    clf()  # Clear the figure content
    close()

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_house = ndf['Hogwarts House']
    ndf_course = ndf.iloc[:, 5:]
    print("courses scores 1", ndf_course)

    min_values = ndf_course.min()  # Valeurs minimales par colonne
    max_values = ndf_course.max()  # Valeurs maximales par colonne
    ndf_course = ndf_course.apply(lambda col: normalize_column(col, min_values[col.name], max_values[col.name]))
    # print("df2", ndf)
    # Configurer Pandas pour afficher toutes les lignes et colonnes
    set_option('display.max_rows', None)  # Afficher toutes les lignes
    set_option('display.max_columns', None)  # Afficher toutes les colonnes
    set_option('display.width', None)  # Désactiver la limitation de la largeur d'affichage
    set_option('display.max_colwidth', None)  # Afficher toute la largeur des colonnes
    # ndf_course = ndf_course.iloc[:, :]

    # ndf_course = DataFrame(ndf_course)
    ndf = concat([ndf_house, ndf_course], axis=1)

    predictions = []
    # flat = [w[row][col] for col in range(len(w[0])) for row in range(len(w))]
    # print("flatlist", len(flat))
    # print("ha", ndf.iloc[:, 1:].values)
    which_house = []
    for i, col in enumerate(ndf.iloc[:, 1:].values):
        predictions.insert(i, [])
        print("col2", col)
        for j in range(len(houses)):
        #     # print("j", j)
        #     # print("weight2", w[j])
        #     z = dot(col, w[j]) + bias
        #     print("value", z)
        #     predictions[i].insert(j, 1 / (1 + (e ** -z)))
        #     # print("vALUE", 1 / (1 + (e ** -z)))
            print("house", houses[j])
            z = dot(col, w[j]) + bias
            print("z", z)
            # which
            predictions[i].insert(j, 1 / (1 + (e ** -z)))
            print("sigmoid result", round(1 / (1 + (e ** -z))))

    # print("equals", e)
    print("perd", predictions)
    # print("preds", len(predictions))
    ndf['Hogwarts House'] = [switch_case_rev(p.index(max(p))) for p in predictions]

    print("ndf", ndf)
    pairplot(ndf, hue="Hogwarts House", palette=[colors
                                                 [category]
                                                 for category in
                                                 onevsall_categories],
             markers=["o", "s", "D", "X"])

    savefig("output_class_II")
    clf()  # Clear the figure content
    close()


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

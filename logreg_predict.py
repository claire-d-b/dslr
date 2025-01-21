from utils import load, get_housename, normalize_column, open_thetas_file
from matplotlib.pyplot import savefig, clf, close
from pandas import concat, DataFrame
from seaborn import pairplot
from math import e
from numpy import dot
import ast


def predict():
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    ndf = load("dataset_test.csv")

    ndf_house = ndf['Hogwarts House']
    ndf_course = ndf.iloc[:, 5:]

    min_values = ndf_course.min()
    max_values = ndf_course.max()  # Valeurs maximales par colonne
    # Normalization of data (between -1 and 1)
    ndf_course = ndf_course.apply(lambda col: normalize_column(col,
                                  min_values[col.name], max_values[col.name]))

    ndf = concat([ndf_house, ndf_course], axis=1)

    bias, w = open_thetas_file("thetas.csv")
    bias = ast.literal_eval(bias)
    # Step 1: Use ast.literal_eval to safely parse the string as a 2D list
    parsed_data = ast.literal_eval(w)
    # Step 2: Convert each element to a float
    parsed_data = [[float(value) for value in row] for row in parsed_data]
    w = parsed_data

    # Make predictions based on computed thetas
    predictions = []
    # print("ndf.iloc[:, 1:]", ndf.iloc[:, 1:])
    # We iterate on 400 rows (students) and 13 columns (courses)
    # We make 4 predictions <=> probability that the student will
    # belong to each house.
    # We take the highest probability.
    for i, col in enumerate(ndf.iloc[:, 1:].values):
        predictions.insert(i, [])

        for j in range(len(houses)):
            z = dot(col, w[j]) + bias
            predictions[i].insert(j, 1 / (1 + (e ** -z)))
    # predictions shape is (400, 4) with values between 0 and 1.
    # Values upper than 0.5 indicates a probability that the student
    # will be in target class (houses[j]), whereas a < 0.5 value
    # tends to indicate the student belongs to another class.
    # when z is pos, the sigmoid function approches 1, whereas when
    # z is negative, the sigmoid function approaches 0.
    # From predictions get the highest value and corresponding house:
    # print("predictions", predictions)
    # print("predictions shape", DataFrame(predictions).shape)
    ndf['Hogwarts House'] = [get_housename(p.index(max(p))) for p
                             in predictions]

    # Write the entire DataFrame to a CSV file
    ndf.iloc[:, 0].to_csv("houses.csv")

    ndf = ndf.sort_values(by='Hogwarts House')

    for i in range(len(houses)):
        filtered_df = ndf[ndf['Hogwarts House'] == houses[i]]
        percent = len(filtered_df) * 100 / len(ndf)
        print(f"There are {percent}% students from test data \
who would probably belong to {houses[i]}")

    colors = {0: "lightblue", 1: "pink", 2: "lightgray", 3: "lightgreen"}
    # index of category (0 to 3)
    categories = [i for i, x in enumerate(houses)]

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
        predict()
    except AssertionError as error:
        print(f"{error}")

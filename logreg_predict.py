from utils import load, get_housename, normalize_df, open_thetas_file, get_max
from utils import get_dot
from matplotlib.pyplot import savefig, clf, close, figure, axhline, scatter
from matplotlib.pyplot import legend, gca
from pandas import concat, DataFrame
from seaborn import pairplot
from math import e
import ast
from exercises.stats import _len


def predict():
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    colors = {0: "red", 1: "yellow", 2: "blue", 3: "green"}

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_house = ndf['Hogwarts House']
    ndf_course = ndf.iloc[:, 5:]

    ndf_course = normalize_df(ndf_course)

    ndf = concat([ndf_house, ndf_course], axis=1)

    ndf = ndf.reset_index()

    bias, w = open_thetas_file("thetas.csv")
    bias = ast.literal_eval(bias)
    # Step 1: Use ast.literal_eval to safely parse the string as a 2D list
    parsed_data = ast.literal_eval(w)
    # Step 2: Convert each element to a float
    parsed_data = [[float(value) for value in row] for row in parsed_data]
    w = parsed_data

    # print("w:", w)
    # print("bias", bias)

    # Make predictions based on computed thetas
    predictions = []
    # print("ndf.iloc[:, 1:]", ndf.iloc[:, 1:])
    # We iterate on 400 rows (students) and 13 columns (courses)
    # We make 4 predictions <=> probability that the student will
    # belong to each house.
    # We take the highest probability.
    figure(figsize=(8, 5))
    for i, col in enumerate(ndf.iloc[:, 2:].values):
        predictions.insert(i, [])
        # print("col", col)

        for j in range(_len(houses)):
            z = get_dot(col, w[j]) + bias[j]
            # print("z", z)
            # Le résultat z représente souvent un score ou une valeur avant
            # l'application d'une fonction d'activation.
            predictions[i].insert(j, 1 / (1 + (e ** -z)))
            scatter(z, 1 / (1 + (e ** -z)), color=colors[j], marker='o',
                    label=houses[j])

    # récupère tous les labels.
    handles, labels = gca().get_legend_handles_labels()
    # garde seulement un exemplaire de chaque label.
    by_label = dict(zip(labels, handles))
    # remplace la légende avec des labels uniques.
    legend(by_label.values(), by_label.keys())

    axhline(y=0.5, color='purple', linestyle='--',
            label="Seuil de décision (0.5)")
    savefig("output_scurve")
    clf()
    close()

    # predictions shape is (400, 4) with values between 0 and 1.
    # Values upper than 0.5 indicates a probability that the student
    # will be in target class (houses[j]), whereas a < 0.5 value
    # tends to indicate the student belongs to another class.
    # when z is pos, the sigmoid function approches 1, whereas when
    # z is negative, the sigmoid function approaches 0.
    # From predictions get the highest value and corresponding house:
    # print("predictions", predictions)
    # print("predictions shape", DataFrame(predictions).shape)
    ndf['Hogwarts House'] = [get_housename(p.index(get_max(p))) for p
                             in predictions]

    # Write the entire DataFrame to a CSV file
    DataFrame(ndf.iloc[:, :2]).to_csv("houses.csv", header=True, index=False)

    ndf = ndf.sort_values(by='Hogwarts House')

    for i in range(_len(houses)):
        filtered_df = ndf[ndf['Hogwarts House'] == houses[i]]
        percent = _len(filtered_df) * 100 / _len(ndf)
        print(f"There are {percent}% students from test data \
who would probably belong to {houses[i]}")

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

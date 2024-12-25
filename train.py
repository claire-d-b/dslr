from utils import load, switch_case
from logistic_regression import train_model
from matplotlib.pyplot import savefig, tight_layout
from pandas import concat, DataFrame, set_option
from seaborn import pairplot
from math import e


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

    print("grouped", grouped)

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    filtered_df_0 = grouped[grouped['Hogwarts House'] == houses[0]]
    print("filter0", filtered_df_0)

    filtered_df_1 = grouped[grouped['Hogwarts House'] == houses[1]]
    print("filter1", filtered_df_1)

    filtered_df_2 = grouped[grouped['Hogwarts House'] == houses[2]]
    print("filter2", filtered_df_2)

    filtered_df_3 = grouped[grouped['Hogwarts House'] == houses[3]]
    print("filter3", filtered_df_3)

    colors = {0: "lightblue", 1: "pink", 2: "lightgray", 3: "lightgreen"}

    pairplot(grouped, hue="Hogwarts House", palette=[colors
                                                     [switch_case(category)]
                                                     for category in
                                                     categories],
             markers=["o", "s", "D", "X"])
    tight_layout()
    savefig("output_class_III")

    xaxis = df.iloc[:, 6:].values.tolist()
    yaxis = df.iloc[:, [1]].values.tolist()
    yaxis = [item for sublist in yaxis for item in sublist]
    print("xaxis", xaxis)
    print("yaxis", yaxis)
    weights, bias = train_model(xaxis, yaxis, 0.01)

    # group by columns
    w = [sum(column) / len(weights) for column in zip(*weights)]
    print("weights", w)
    print("lenweights", len(w))
    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    cols = ndf.columns[6:].values

    nxaxis = ndf.iloc[:, 6:].values

    predictions = []
    for i, scores_row in enumerate(nxaxis):
        predictions.insert(i, [])

        for j, score in enumerate(scores_row):
            weight = w[j]
            predictions[i].insert(j, stable_sigmoid(-(score * weight + bias)))

    ndf = DataFrame(predictions)
    print("dfcourses", df_courses.iloc[[0], :].columns)
    ndf.columns = df_courses.iloc[[0], :].columns

    # ndf = concat([ndf_house, ndf_courses], axis=1)
    print("gr", ndf)

    # print("gr", grouped)
    # ngrouped = grouped.groupby('Hogwarts House', as_index=False).sum()
    categories = [0, 1]
    print("groupedfinal", list(ndf))
    ndf.insert(0, 'Hogwarts House', [round(sum(pred) / len(pred)) for pred in predictions])

    # Display all rows and columns
    set_option('display.max_rows', None)
    set_option('display.max_columns', None)
    print("ndf final", DataFrame(ndf))

    # Write the entire DataFrame to a CSV file
    DataFrame(ndf).to_csv("dataset_test_completed.csv", index=True)

    pairplot(ndf, hue="Hogwarts House", palette=[colors
                                                     [category]
                                                     for category in
                                                     categories],
             markers=["o", "s"])

    tight_layout()
    savefig("output_class_IV")


if __name__ == "__main__":
    try:
        train()
    except AssertionError as error:
        print(f"{error}")

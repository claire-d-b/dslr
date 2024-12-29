from utils import load, switch_case
from linear_regression import train_model
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
    
    # filtered_df_0 = grouped[grouped['Hogwarts House'] == houses[0]]
    # print("filter0", filtered_df_0)

    # filtered_df_0 = grouped[grouped['Hogwarts House'] == houses[1]]
    # print("filter1", filtered_df_0)

    # filtered_df_0 = grouped[grouped['Hogwarts House'] == houses[2]]
    # print("filter2", filtered_df_0)

    # filtered_df_0 = grouped[grouped['Hogwarts House'] == houses[3]]
    # print("filter3", filtered_df_0)
    color = {0: "lightblue", 1: "pink"}
    colors = {0: "lightblue", 1: "pink", 2: "lightgray", 3: "lightgreen"}

    # grouped = filtered_df_0
    print("groupd", grouped)
    pairplot(grouped, hue="Hogwarts House", palette=[colors[switch_case(category)] for category in categories],
             markers=["o", "s", "D", "X"])
    tight_layout()
    savefig("output_class_III")

    xaxis = df.iloc[:, 6:].values.tolist()
    yaxis = df.iloc[:, [1]].values.tolist()
    yaxis = [item for sublist in yaxis for item in sublist]
    print("xaxis", xaxis)
    print("yaxis", yaxis)

    cols = grouped.columns[1:].tolist()
    w = []
    for col in cols:
        print("grcols", grouped[col])
        weights, bias = train_model(grouped[col], yaxis, 0.01)
        w.append(weights)
    bias /= len(cols)
    print("weightlist", w)

    print("lenweights", len(w))
    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_house = ndf.iloc[:, [1]]
    ndf_courses = ndf.iloc[:, 6:]

    print("ndhouse", ndf_house)
    print("ndcourse", ndf_courses)
    ndf = concat([ndf_house, ndf_courses], axis=1)

    nxaxis = ndf.iloc[:, 1:].values
    print("xaxis", nxaxis)
    predictions = []
    for i, scores_row in enumerate(nxaxis):
        predictions.insert(i, [])
        print("scoresrow", scores_row)

        for j, score in enumerate(scores_row):
            weight = w[j]
            print("weight_loop", weight)
            print("score!", score)
            predictions[i].insert(j, stable_sigmoid(-(score * weight + bias)))

    preds = DataFrame(predictions)

    table = []
    for i, col in enumerate(preds.columns):
        print("COL", list(preds[col]))
        table.insert(i, [sum(preds[col]) / len(preds[col])])

    print("TABLE", table)

    print("dfcourses", df_courses.iloc[[0], :].columns)
    # ndf.columns = df_courses.iloc[[0], :].columns

    # ndf = concat([ndf_house, ndf_courses], axis=1)
    print("preds", preds)

    # print("gr", grouped)
    # ngrouped = grouped.groupby('Hogwarts House', as_index=False).sum()``
    house = []
    for i, scores_row in enumerate(nxaxis):
        house.insert(i, [])
        print("scoresrow", scores_row)

        for j, score in enumerate(scores_row):
            weight = float(table[j][0])
            print("w8", weight)
            print("weight_loop", weight)
            print("score!", score)
            house[i].insert(j, stable_sigmoid(-score * weight + bias))

    ndf['Hogwarts House'] = [round(sum(sublist) / len(sublist)) for sublist in house]
    print("house cols", house)
    ndf = ndf.sort_values(by='Hogwarts House')

    print("groupedfinal", ndf)

    nndf = ndf.groupby('Hogwarts House', as_index=False).sum()
    categories = nndf["Hogwarts House"]

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
from utils import load
from histogram import get_bars
from scatter_plot import get_scatter_plot
from pair_plot import get_pair_plot
from describe import print_dataframe
from pandas import DataFrame, concat
from logistic_regression import train_model, predict, predict_real, sigmoid
from matplotlib.pyplot import savefig, tight_layout, subplots, figure, title, show, xticks, scatter, plot
from numpy import meshgrid, zeros_like, mean, arange, array, clip
from math import e


def switch_case(case_value) -> int | None:
    match case_value:
        case 'Gryffindor':
            return 0
        case 'Ravenclaw':
            return 0
        case 'Hufflepuff':
            return 0
        case 'Slytherin':
            return 1
        case _:
            return None


def main():
    df = load("dataset_train.csv")
    # Replace NaN with 0
    df = df.fillna(0)

    print_dataframe(df)

    df_house = df.iloc[:, [0]]  # Select the 2nd column (index 1)
    df_courses = df.iloc[:, 6:]   # Select columns starting from 7th (index 6)
    # onward
    df = concat([df_house, df_courses], axis=1)

    table = []

    houses = []
    scores = []

    for i in range(df.shape[0]):
        table.insert(i, [])
        scores.insert(i, [])
        for j in range(df.shape[1]):

            if j == 0:
                print("case:", df.iloc[[i], [j]].values[0][0])
                table[i].insert(j, switch_case(df.iloc[[i], [j]].values[0][0]))
                houses.append(switch_case(df.iloc[[i], [j]].values[0][0]))
                
            else:
                table[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))
                scores[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    table = sorted(table)
    ntable = DataFrame(table)
    indexes = [x for x in ntable.index]

    rhs = array(indexes)
    lhs = array(scores)

    # Run logistic regression
    learning_rate = 0.1
    epochs = 1000
    weights, bias = train_model(lhs, houses)
    print("wlen", len(weights))

    # Final parameters
    print("\nFinal weights:", weights)
    print("Final bias:", bias)

    predictions = predict(lhs, weights, bias)

    print("Predictions:", predictions)

    lhs = [sum(sublist) / len(sublist) for sublist in lhs]

    # Map categories to colors
    
    color_map = {0: 'red', 1: 'blue'}
    colors = [color_map[label] for label in houses]
    scatter(lhs, predictions, c=colors, alpha=0.8, edgecolor='k')

    # The decision boundary corresponds to the line where the model's prediction
    # probability is 0.5 (threshold for binary classification).
    # In the case of logistic regression, z (the input to the sigmoid function),
    # is the output of a linear regression model.

    savefig("output_train")

    ndf = load("dataset_test.csv")
    ndf = ndf.fillna(0)

    ndf_courses = ndf.iloc[:, 6:]
    ndf_house = ndf.iloc[:, [0]]

    nhouses = []
    nscores = []
    ndf = concat([ndf_house, ndf_courses], axis=1)

    for i in range(ndf.shape[0]):
        table.insert(i, [])
        nscores.insert(i, [])
        for j in range(ndf.shape[1]):

            if j == 0:
                print("case:", ndf.iloc[[i], [j]].values[0][0])
                table[i].insert(j, switch_case(ndf.iloc[[i], [j]].values[0][0]))
                nhouses.append(switch_case(ndf.iloc[[i], [j]].values[0][0]))
                
            else:
                table[i].insert(j, float(ndf.iloc[[i], [j]].values[0][0]))
                nscores[i].insert(j, float(ndf.iloc[[i], [j]].values[0][0]))

    npredictions = predict(array(nscores), weights, bias)

    fig, ax = subplots()
    nnscores = [sum(sublist) for sublist in nscores]
    nnindexes = [index for index, item in enumerate(nnscores)]

    # Map categories to colors
    ncolor_map = {0: 'red', 1: 'blue'}
    ncolors = [ncolor_map[label] for label in npredictions]
    scatter(nnscores, npredictions, c=ncolors, alpha=0.8, edgecolor='k')

    savefig("output_test")



if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")

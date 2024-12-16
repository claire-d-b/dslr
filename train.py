from utils import get_lists_from_dataframe, load, switch_case
# from linear_regression_test import train_model
from logistic_regression import train_model
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              show, scatter, plot
from pandas import DataFrame, concat
from numpy import array
from math import e


def main():
    df = load("dataset_train.csv")
    # Replace NaN with 0
    df = df.fillna(0)

    df_house = df.iloc[:, [1]] # Select the 2nd column - house
    df_courses = df.iloc[:, 6:] # Select courses columns
    df = concat([df_house, df_courses], axis=1)

    table = []
    houses = []
    scores = []

    for i in range(df.shape[0]):
        scores.insert(i, [])
        for j in range(df.shape[1]):
            
            if j == 0:
                # switch_case returns 0 or 1 depending on the house
                # print(df.iloc[[i], [j]].values[0][0])
                houses.append(switch_case(df.iloc[[i], [j]].values[0][0]))
                
            else:
                scores[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    rhs = array(houses)
    lhs = array(scores)
    indexes = [i for i in range(len(scores))]

    # Run logistic regression
    learning_rate = 0.01
    pred = []

    weights, bias = train_model(lhs, houses, learning_rate)
    lhs = [sum(x) for x in lhs]

    for i, unit in enumerate(lhs):
        pred.insert(i, 1 / (1 + (e ** -(unit * weights + bias))))

    fig, ax = subplots()

    color_map = {0: 'red', 1: 'blue', 2: 'gray', 3: 'green'}
    colors = [color_map[label] for label in houses]

    scatter(indexes, lhs, c=colors, alpha=0.8, edgecolor='k')
    plot(pred)
    tight_layout()
    savefig("output_classification_I")
    # Use computed thetas for predictions

    ndf = load("dataset_test.csv")
    # Replace NaN with 0
    ndf = df.fillna(0)

    # ndf_house = df.iloc[:, [1]]  # Select the 2nd column - house
    ndf = df.iloc[:, 6:]   # Select courses columns
    # ndf = concat([ndf_house, ndf_courses], axis=1)

    ntable = []
    nhouses = []
    nscores = []

    for i in range(ndf.shape[0]):
        nscores.insert(i, [])
        for j in range(ndf.shape[1]):

            # if j == 0:
            #     # switch_case returns 0 or 1 depending on the house
            #     nhouses.append(switch_case(ndf.iloc[[i], [j]].values[0][0]))
                
            # else:
            nscores[i].insert(j, float(ndf.iloc[[i], [j]].values[0][0]))

    # nrhs = array(nhouses)
    nlhs = array(nscores)
    nindexes = [i for i in range(len(nscores))]


    # Run logistic regression
    learning_rate = 0.01
    npred = []

    nlhs = [sum(x) for x in nlhs]

    for i, unit in enumerate(nlhs):
        npred.insert(i, 1 / (1 + (e ** -(unit * weights + bias))))

    fig, ax = subplots()

    scatter(nindexes, nlhs, c=colors, alpha=0.8, edgecolor='k')
    plot(npred)
    tight_layout()
    savefig("output_classification_II")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
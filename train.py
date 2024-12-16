from utils import get_lists_from_dataframe, load
# from linear_regression_test import train_model
from logistic_regression import train_model
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              show, scatter, plot
from pandas import DataFrame, concat
from numpy import array
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

    df_house = df.iloc[:, [1]]  # Select the 2nd column - house
    df_courses = df.iloc[:, 6:]   # Select courses columns
    df = concat([df_house, df_courses], axis=1)

    table = []
    houses = []
    scores = []

    for i in range(df.shape[0]):
        scores.insert(i, [])
        for j in range(df.shape[1]):

            if j == 0:
                # switch_case returns 0 or 1 depending on the house
                houses.append(switch_case(df.iloc[[i], [j]].values[0][0]))
                
            else:
                scores[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    rhs = array(houses)
    lhs = array(scores)

    # Run logistic regression
    learning_rate = 0.01
    pred = []

    weights, bias = train_model(lhs, houses, learning_rate)
    lhs = [sum(x) for x in lhs]

    for i, unit in enumerate(lhs):
        pred.insert(i, 1 / (1 + (e ** -(unit * weights + bias))))

    fig, ax = subplots()

    color_map = {0: 'red', 1: 'blue'}
    colors = [color_map[label] for label in houses]

    scatter(lhs, pred, c=colors, alpha=0.8, edgecolor='k')

    tight_layout()
    savefig("output_classification")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
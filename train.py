from utils import get_lists_from_dataframe, load
# from linear_regression_test import train_model
from linear_regression import train_model
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

    df_house = df.iloc[:, [1]]  # Select the 2nd column (index 1)
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

    rhs = array(houses)
    lhs = array(scores)

    print("rhs", rhs)
    print("lhs", lhs)

    # Run logistic regression
    learning_rate = 0.01
    pred = []

    weights, bias = train_model(lhs, houses, learning_rate)
    lhs = [sum(x) for x in lhs]

    for i, unit in enumerate(lhs):
        pred.insert(i, 1 / (1 + (e ** -(unit * weights + bias))))

    fig, ax = subplots()

    print("lhhs", lhs)
    print("rhhs", rhs)

    color_map = {0: 'red', 1: 'blue'}
    colors = [color_map[label] for label in houses]
    scatter(lhs, pred, c=colors, alpha=0.8, edgecolor='k')

    # ax.scatter(lhs, rhs)

    tight_layout()
    savefig("output_training_v2")

# def main():
#     """Program that trains the model with 1000 iterations and a
#     learning rate of 0.01"""
#     lhs, rhs = get_lists_from_dataframe("data.csv", "km", "price")

#     theta_0 = 0
#     theta_1 = 0

#     learning_rate = 0.01

#     pred = []

#     theta_1, theta_0 = train_model(lhs, rhs, learning_rate)

#     f = open("thetas.csv", "w")
#     f.write(f"{theta_0}, {theta_1}")
#     f.close()

#     # print("theta_0 (y-interceipt) is: ", theta_0)
#     # print("theta_1 (slope) is: ", theta_1)

#     for i, unit in enumerate(lhs):
#         pred.insert(i, unit * theta_1 + theta_0)

#     fig, ax = subplots()

#     ax.plot(lhs, pred)
#     ax.scatter(lhs, rhs)

#     tight_layout()
#     savefig("output_training")
#     show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
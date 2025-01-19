import numpy as np
import matplotlib.pyplot as plt
from utils import load, normalize_column, open_thetas_file, get_housenumber, get_housename
from pandas import concat, DataFrame
import ast
from numpy import meshgrid, zeros_like, mean, zeros, dot, array, tile
from mpl_toolkits.mplot3d import Axes3D
from math import e, log
from matplotlib.pyplot import savefig, show, \
                              title, figure


def get_cost() -> any:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    ndf = load("dataset_train.csv")

    lhs = ndf['Hogwarts House']
    rhs = ndf.iloc[:, 5:]

    min_values = rhs.min()
    max_values = rhs.max()
    # Normalization of data (between -1 and 1)
    rhs = rhs.apply(lambda col: normalize_column(col,
                                  min_values[col.name], max_values[col.name]))

    ndf = concat([lhs, rhs], axis=1)

    bias, w = open_thetas_file("thetas.csv")
    bias = ast.literal_eval(bias)
    # Step 1: Use ast.literal_eval to safely parse the string as a 2D list
    parsed_data = ast.literal_eval(w)
    # Step 2: Convert each element to a float
    parsed_data = [[float(value) for value in row] for row in parsed_data]
    w = parsed_data

    theta_0 = bias
    theta_1 = w

    predictions = []
    # values ndf.iloc[:, 1:].values refers to normalized values (btw -1 and 1)
    # for each student in each course -> shape is (1600, 13)
    # print("values:", ndf.iloc[:, 1:].values)
    # print("values shape:", ndf.iloc[:, 1:].shape)

    # print("weights", DataFrame(w).shape)
    for i, col in enumerate(ndf.iloc[:, 1:].values):
        predictions.insert(i, [])
        # print("col", col)

        for j in range(len(houses)):
            # as weights (w) is of shape (4, 13), we can use dot product between col (13 elements)
            # and w[index] where index goes from 0 to 3 (there are four houses)
            # we do that 4 times: one hogwarts House at a time
            z = dot(col, w[j]) + bias
            predictions[i].insert(j, 1 / (1 + (e ** -z)))

    # Show all houses TBD -> predictions = [p.index(max(p)) for p in predictions]
    # Choose here 0, 1, 2 or 3 depending on the house you want to analyze below
    predictions = [1 if p.index(max(p)) == 0 else 0 for p in predictions]
    # print("predictions", predictions)

    # meshgrid is a function from the numpy library used to create coordinate grids,
    # typically for 3D plotting or evaluating functions over a 2D domain
    # numpy.meshgrid(*xi, indexing='xy')
    # *xi: The input vectors. These are 1D arrays representing the range of values for each axis.
    # indexing: A string that can be either 'xy' or 'ij'. It determines how the coordinate matrices are ordered.
    # By default, it uses 'xy', which is the most common for plotting and graphical tasks.

    # rhs.mean() gives us the average of all students' scores per course (shape 13, 1)
    # predictions is the preficted house: 0 if under 0.5 and 1 if upper than 0.5
    A, B = meshgrid(rhs.mean(), predictions)
    # print(DataFrame(rhs.mean()).shape)
    # print(DataFrame(predictions).shape)
    # print("A shape", A.shape) # 1600, 13
    # print("B shape", A.shape) # 1600, 13

    loss = zeros_like(A)
    y_hat = zeros_like(A)

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            # Mean along axis 0 (columns): this calculates the mean for each column (across the rows).
            # The result will be a 1D array with the shape (13,):
            # print("shape theta_1:", mean(theta_1, axis=0).shape)
            t_1 = mean(theta_1, axis=0)[j]
            z = A[i, j] * t_1 + theta_0
            y_hat[i, j] = 1 / (1 + e ** -z)
            loss[i, j] = -B[i, j] * log(y_hat[i, j]) - (1 - B[i, j]) * log(1 - y_hat[i, j])

    fig = figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surface = ax.plot_surface(A, B, loss, cmap='cool',
                              edgecolor='none')
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)
    title("Cost function in logistic regression")
    ax.set_xlabel("scores")
    ax.set_ylabel("house")
    ax.set_zlabel("cost")
    savefig("cost")
    show()


if __name__ == "__main__":
    try:
        get_cost()
    except AssertionError as error:
        print(f"{error}")

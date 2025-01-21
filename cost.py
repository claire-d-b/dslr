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

    # Choose here 0, 1, 2 or 3 depending on the house you want to analyze below
    real_houses = [1 if houses.index(h) == 0 else 0 for h in lhs]

    # meshgrid is a function from the numpy library used to create coordinate grids,
    # typically for 3D plotting or evaluating functions over a 2D domain
    # numpy.meshgrid(*xi, indexing='xy')
    # *xi: The input vectors. These are 1D arrays representing the range of values for each axis.
    # indexing: A string that can be either 'xy' or 'ij'. It determines how the coordinate matrices are ordered.
    # By default, it uses 'xy', which is the most common for plotting and graphical tasks.

    # rhs.mean() gives us the average of all students' scores per course (shape 13, 1)
    A, B = meshgrid(rhs.mean(), real_houses)
    # print(DataFrame(rhs.mean()).shape)
    # print(DataFrame(real_houses).shape)
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

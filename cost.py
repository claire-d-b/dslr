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


# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Logistic regression cost function
def compute_cost(theta_0, theta, X, y):
    m = len(y)
    print("tita", theta)
    theta.insert(0, theta_0)
    predictions = sigmoid(X.dot(theta))  # Compute the model predictions
    cost = -1/m * np.sum(y * np.log(predictions) + (1 - y) * np.log(1 - predictions))
    return cost


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
    # Step 2: Convert each element to a float (if needed, as ast.literal_eval already gives us floats)
    parsed_data = [[float(value) for value in row] for row in parsed_data]
    # Print the result
    w = parsed_data

    theta_0 = bias
    theta_1 = w

    predictions = []
    for i, col in enumerate(ndf.iloc[:, 1:].values):
        predictions.insert(i, [])

        for j in range(len(houses)):
            z = dot(col, w[j]) + bias
            predictions[i].insert(j, 1 / (1 + (e ** -z)))

    # predictions = [p.index(max(p)) for p in predictions]
    # Choose here 0, 1, 2 or 3 depending on the house you want to analyze
    predictions = [1 if p.index(max(p)) == 0 else 0 for p in predictions]

    A, B = meshgrid(rhs.mean(), predictions)

    loss = zeros_like(A)
    y_hat = zeros_like(A)

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            z = A[i, j] * mean(theta_1) + theta_0
            y_hat[i, j] = 1 / (1 + e ** -z)
            loss[i, j] = -B[i, j] * log(y_hat[i, j]) - (1 - B[i, j]) * log(1 - y_hat[i, j])

    fig = figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surface = ax.plot_surface(A, B, loss, cmap='viridis',
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
        print(f"{error}")# Generate a random dataset with 1600 samples and 13 features
    # np.random.seed(0)
    # X = np.random.rand(1600, 13)  # 1600 examples with 13 features
    # y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Binary labels (0 or 1)

    # # Create a grid of theta_0 and theta_1 values
    # theta_0_vals = np.linspace(-5, 5, 50)  # Varying intercept
    # theta_1_vals = np.linspace(-5, 5, 50)  # Varying feature coefficient

    # Create a meshgrid for 
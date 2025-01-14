from utils import open_thetas_file, load, get_housenumber, normalize_column
from numpy import meshgrid, zeros_like, mean
from matplotlib.pyplot import savefig, show, \
                              title, figure
from math import e, log
import ast


def main():
    """Program that builds a 3D shape figure to show the cost function"""
    # lhs, rhs = get_lists_from_dataframe("data.csv", "km", "price")
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    df = load("dataset_train.csv")

    theta_0 = 0
    theta_1 = 0

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
    
    lhs = df.iloc[:, 5:]
    min_values = lhs.min()
    max_values = lhs.max()  # Valeurs maximales par colonne
    # Normalization of data (between -1 and 1)
    lhs = lhs.apply(lambda col: normalize_column(col,
                                  min_values[col.name], max_values[col.name]))
    lhs = lhs.mean()
    rhs = df.iloc[:, 0]

    i = 1
    rhs = [0 if x == houses[3] else 1 for x in rhs]
    # Create a grid of a and b values
    A, B = meshgrid(lhs, rhs)

    # Calculate the squared error for each combination of a and b
    loss = zeros_like(A)

    for i in range(A.shape[0]):

        for j in range(A.shape[1]):

            z = A[i, j] * mean(theta_1) + theta_0  # Predicted function
            predicted_y = 1 / (1 + e ** -z)
            loss[i, j] = B[i, j] * log(predicted_y) + (1 - B[i, j]) * log(predicted_y)

    # 111: These are subplot grid parameters encoded as a single integer.
    # For example, "111" means "1x1 grid, first subplot" and "234" means
    # "2x3 grid, 4th subplot".
    # Alternative form for add_subplot(111) is add_subplot(1, 1, 1).
    fig = figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    surface = ax.plot_surface(A, B, loss, cmap='viridis',
                              edgecolor='none')
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)
    # Color bar to show the scale of error
    title("Cost function")
    ax.set_xlabel("scores")
    ax.set_ylabel("house")
    ax.set_zlabel("cost")
    savefig("Cost")
    show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
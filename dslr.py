from utils import load
from histogram import get_bars
from scatter_plot import get_scatter_plot
from pair_plot import get_pair_plot
from describe import print_dataframe
from pandas import DataFrame, concat
from logistic_regression import train_model, predict
from matplotlib.pyplot import savefig, tight_layout, subplots, figure, title, show, xticks, scatter, plot
from numpy import meshgrid, zeros_like, mean, arange, array
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


    # get_bars(df)
    # get_scatter_plot(df)
    # get_pair_plot(df)
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
    print("tableNEW", houses)
    print("NTABLE0", ntable.columns) # houses
    print("NTABLE1", scores) # scores
    # for i, unit in enumerate(ntable[0].values):
        # remplacer le nom des maisons par 0, 1, 2, 3

    rhs = array(houses)
    lhs = array(scores)

    print("hs:", rhs)
    print("ss:", lhs)

    pred = []

    print("lhs", lhs)

    # Example dataset
    # X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])  # Features
    # y = np.array([0, 0, 1, 1])  # Labels (binary: 0 or 1)

    # Run logistic regression
    learning_rate = 0.1
    epochs = 1000
    weights, bias = train_model(lhs, rhs)

    # Final parameters
    print("\nFinal weights:", weights)
    print("Final bias:", bias)

    predictions = predict(lhs, weights, bias)
    print("Predictions:", predictions)

    lhs = [sum(sublist) / len(sublist) for sublist in lhs]
    scatter(lhs, predictions)
    # plot(lhs, predictions)
    # Create a grid of a and b values
    # A, B = meshgrid(lhs, rhs)


    # # Calculate the squared error for each combination of a and b
    # squared_error = zeros_like(A) # a function provided by the NumPy library. It creates a new array of zeros that has the same shape and type as the input array provided to it.
    # pred = []

    # for i in range(A.shape[0]):
    #     for j in range(A.shape[1]):
    #         squared_error[i, j] = mean(predictions[i] - B[i, j]) ** 2
    #         # Mean squared error

    #  # 111: These are subplot grid parameters encoded as a single integer.
    # # For example, "111" means "1x1 grid, first subplot" and "234" means
    # # "2x3 grid, 4th subplot".
    # # Alternative form for add_subplot(111) is add_subplot(1, 1, 1).
    # fig = figure(figsize=(10, 8))
    # ax = fig.add_subplot(111, projection='3d')

    # surface = ax.plot_surface(A, B, squared_error, cmap='viridis',
    #                           edgecolor='none')
    # fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

    # # houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    # # # Create bar chart with numeric indices
    # # x_indices = arange(len(houses))  # Numeric indices: 0, 1, 2, 3
    # # nx_indices = [float(x / 10) for x in x_indices]
    # # xticks(nx_indices, houses)

    # # Color bar to show the scale of error
    # title("3D surface plot for Squared Error")
    # ax.set_xlabel("house")
    # ax.set_ylabel("score")
    # ax.set_zlabel("cost")
    savefig("cost_logistic_reg")
    show()

    # print(theta_1)
    # print(theta_0)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")

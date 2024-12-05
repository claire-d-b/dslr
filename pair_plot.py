from pandas import DataFrame, concat
from seaborn import pairplot
from matplotlib.pyplot import savefig, tight_layout


def get_pair_plot(df: DataFrame) -> any:

    df_house = df.iloc[:, [0]]  # Select the 2nd column (index 1)
    df_courses = df.iloc[:, 6:]   # Select columns starting from 7th (index 6)
    # onward
    df = concat([df_house, df_courses], axis=1)

    table = []

    for i in range(df.shape[0]):
        table.insert(i, [])

        for j in range(df.shape[1]):
            if j == 0:
                table[i].insert(j, df.iloc[[i], [j]].values[0][0])
            else:
                table[i].insert(j, float(df.iloc[[i], [j]].values[0][0]))

    grouped = DataFrame(table)

    print("maison", grouped.index[0])
    pairplot(grouped, hue=grouped.index[0], palette='Set1',
             markers=["o", "s", "D", "X"])

    tight_layout()
    savefig("pairplot")

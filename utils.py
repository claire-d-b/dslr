from pandas import DataFrame, read_csv
from math import e


def stable_sigmoid(z) -> float:
    """Compute the sigmoid function in a numerically stable way."""
    if z >= 0:
        exp_neg_z = e ** -z
        return 1 / (1 + exp_neg_z)
    else:
        exp_pos_z = e ** z
        return exp_pos_z / (1 + exp_pos_z)


def switch_case(case_value) -> int | None:
    """Defines 'true house' vs 'wrong houses'"""
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


def load(path: str) -> DataFrame:
    """Function that opens a file and display inner data in the shape
    of a datatable"""
    try:
        # Ici open est un gestionnaire de contexte qui retourne un
        # object-fichier
        file = read_csv(path, index_col=False)

    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return file

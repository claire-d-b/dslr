from pandas import DataFrame, read_csv
from math import e


def switch_case(case_value) -> int | None:
    """Defines 'true house' vs 'wrong houses'"""
    match case_value:
        case 'Gryffindor':
            return 0
        case 'Hufflepuff':
            return 0
        case 'Ravenclaw':
            return 0
        case 'Slytherin':
            return 0
        case _:
            return None

def switch_case_rev(case_value) -> str | None:
    """Defines 'true house' vs 'wrong houses'"""
    match case_value:
        case 0:
            return 'Gryffindor'
        case 1:
            return 'Hufflepuff'
        case 2:
            return 'Ravenclaw'
        case 3:
            return 'Slytherin'
        case _:
            return None


def load(path: str) -> DataFrame:
    """Function that opens a file and display inner data in the shape
    of a datatable"""
    try:
        # Ici open est un gestionnaire de contexte qui retourne un
        # object-fichier
        file = read_csv(path, index_col=0)

    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return file

# Normalisation manuelle entre -1 et 1
def normalize_column(col, min_val, max_val):
    return 2 * (col - min_val) / (max_val - min_val) - 1

from pandas import DataFrame, read_csv


def switch_case(case_value) -> int | None:
    """Defines 'true house' vs 'wrong houses'"""
    match case_value:
        case 'Gryffindor':
            return 0
        case 'Ravenclaw':
            return 0
        case 'Hufflepuff':
            return 1
        case 'Slytherin':
            return 0
        case _:
            return None


def load(path: str) -> DataFrame:
    """Function that opens a file and display inner data in the shape
    of a datatable"""
    try:
        # Ici open est un gestionnaire de contexte qui retourne un
        # object-fichier
        file = read_csv(path)

    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return file

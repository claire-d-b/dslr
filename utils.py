from pandas import DataFrame, read_csv


def open_thetas_file(name: str) -> tuple:
    theta_0 = 0
    theta_1 = []
    try:
        f = open(name, "r")
        file_content = f.read()

        index = file_content.find("theta_0:")
        i = index + len("theta_0:")
        theta_0 = file_content[i:file_content.find("\n")]

        index = file_content.find("theta_1:")
        i = index + len('\ntheta_1:')
        theta_1 = file_content[i:]

        return theta_0, theta_1
    except Exception as e:
        raise AssertionError(f"Error: {e}")


def get_housename(case_value) -> str | None:
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
        # file = file.fillna(0)

    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return file


# Normalisation manuelle entre -1 et 1
def normalize_column(col, min_val, max_val):
    return 2 * (col - min_val) / (max_val - min_val) - 1

from pandas import DataFrame, read_csv, set_option
from stats import get_min, get_max


def load(path: str) -> DataFrame:
    """Function that opens a file and display inner data in the shape
    of a datatable"""
    try:
        # Ici open est un gestionnaire de contexte qui retourne un
        # object-fichier
        df = read_csv(path, index_col=0)
        # df = df.fillna(0)
        # Solution: When reading the CSV, specify:
        # index_col=0 if the first column is an index.
        # header=None if there’s no header row in the file,
        # then rename columns manually.

        # Change pandas display options
        set_option('display.max_rows', None)  # Show all rows
        set_option('display.max_columns', None)  # Show all
        # columns
        set_option('display.width', None)  # Adjust the display
        # width for wrapping
        set_option('display.colheader_justify', 'lseft')  # Align headers
        # to the left

    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return df


def normalize_df(df):
    # Créer une copie du DataFrame pour ne pas modifier l'original
    normalized_df = df.copy()

    # Sélectionner uniquement les colonnes numériques
    numeric_columns = df.select_dtypes(include=float).columns

    for col in numeric_columns:
        # Calculer min et max de la colonne
        col_min = get_min(df[col])
        col_max = get_max(df[col])

        # Vérifier que min et max sont différents pour éviter division par zéro
        if col_max > col_min:
            # Formule de normalisation entre -1 et 1:
            # 2 * (x - min) / (max - min) - 1
            normalized_df[col] = 2*(df[col] - col_min)/(col_max - col_min)-1
        else:
            # Si toutes les valeurs sont identiques, on les met à 0
            normalized_df[col] = 0

    return normalized_df

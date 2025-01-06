from pandas import DataFrame, read_csv, set_option


def load(path: str) -> DataFrame:
    """Function that opens a file and display inner data in the shape
    of a datatable"""
    try:
        # Ici open est un gestionnaire de contexte qui retourne un
        # object-fichier
        df = read_csv(path, index_col=0)
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

# Normalisation manuelle entre -1 et 1
def normalize_column(col, min_val, max_val):
    return 2 * (col - min_val) / (max_val - min_val) - 1

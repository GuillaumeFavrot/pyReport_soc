from numpy import ndarray
from main_logic.tools.get_subset import get_subset_per_value

def concat_in_subset(value, df: ndarray, key: str, concat_column: str) -> str:
    """Concatene l'ensemble des string d'une colonne d'un subset"""

    subset = get_subset_per_value(value=value, df=df, key=key)

    str = subset[concat_column].str.cat(others=None, sep=",")

    return str
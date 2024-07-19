from numpy import ndarray
from main_logic.tools.get_subset import get_subset_per_value

def concat_in_subset_condition(value, df: ndarray, key: str) -> str:
    """Concatene l'ensemble des garanties des sinistres d'un sociétaire"""

    subset = get_subset_per_value(value=value, df=df, key=key)

    filtered_subset = subset[subset["charge_sinistre"] != ""].copy()

    filtered_subset["garantiec"] = filtered_subset["garantiec"].str.strip()
    filtered_subset["garantiel"] = filtered_subset["garantiel"].str.strip()

    filtered_subset["garantie"] = filtered_subset["garantiec"] + " " + filtered_subset["garantiel"]

    str = filtered_subset["garantie"].str.cat(others=None, sep=",")

    return str
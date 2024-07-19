from numpy import ndarray
from main_logic.tools.get_subset import get_subset_per_value

def count_iterations(value, df: ndarray, key: str):

    subset = get_subset_per_value(value, df, key)

    return subset.shape[0]
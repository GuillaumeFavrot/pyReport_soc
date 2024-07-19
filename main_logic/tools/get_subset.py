from numpy import ndarray

def get_subset_per_value(value, df: ndarray, key: str) -> ndarray:
    """Génère un subset de données en fonction d'une valeur et d'une clé"""
    return df[df[key] == value].copy()
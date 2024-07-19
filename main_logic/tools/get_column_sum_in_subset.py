from numpy import ndarray
from main_logic.tools.get_subset import get_subset_per_value

def get_column_sum_in_subset(value, df: ndarray, key: str, sum_column: str, data_type: str, filter: tuple = ()):
    """Additionne les valeurs d'une colonne d'un subset"""
    
    # Génération d'un subset
    subset = get_subset_per_value(value, df, key)
    
    # Application du filtre
    if len(filter) > 0:
        subset = subset[~subset[filter[1]].isin(filter[0])]

    # On remplace les valeurs vides '' par des '0'
    subset[subset[sum_column] == ''] = '0'

    # On remplace les ',' par des '.' afin de permettre la conversion et on converti
    subset[sum_column] = subset[sum_column].str.replace(',', '.').astype(data_type)
    
    # On retourne la somme des nombres de la série
    return subset[sum_column].sum()
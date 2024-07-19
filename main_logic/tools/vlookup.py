from numpy import ndarray
import pandas as pd

def vlookup(report, source_df, key_report, key_source, value) -> list:
    """Génère une liste à partir des données d'un dataframe source pour des valeurs 'clés' fournies"""

    source_df[key_source] = source_df[key_source].astype('str')
    report[key_report] = report[key_report].astype('str')

    merged = pd.merge(report, source_df, how='left', left_on=key_report, right_on=key_source)

    return merged[value].tolist()
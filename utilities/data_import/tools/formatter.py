from numpy import ndarray
import re

def column_name_formatter(df: ndarray) -> ndarray:
    """formatte les noms de colonne extraits des fichiers sources afin d'être plus facilement utilisables dans python"""

    replacements = [
        ("n°", "numero"),
        ("é", "e"),
        ("è", "e"),
        ("à", "a")
    ]

    for column in df.columns:
        old_name = str(column)
        
        #All lowercase
        new_name = old_name.lower()

        #Removes leading and trailing spaces
        new_name = new_name.strip()
        
        #special replacements
        for r in replacements:
            new_name = new_name.replace(r[0], r[1])

        #Remove special characters
        new_name = re.sub("[^ a-zA-Z0-9]+", '', new_name)

        #Replace space with underscores
        new_name = new_name.replace(" ", "_")

        #Rename the column in the dataframe
        df.rename(columns={old_name : new_name}, inplace=True)
    
    return df

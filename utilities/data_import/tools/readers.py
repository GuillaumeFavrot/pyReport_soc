from numpy import ndarray
import pandas as pd
from utilities.data_import.tools.data_entry_counter import data_entry_counter
from utilities.data_import.tools.formatter import column_name_formatter

class Readers: 
    def csv(file_path: str, formatting: bool) -> ndarray:
        """Convertis un fichier CSV en dataframe"""
            
        # Ouvre le fichier CSV et extrait ses données sous la forme d'une liste de chaine de string
        with open(file_path) as f:
            lines = list(f)

        # Convertis les données brutes extraites en un tableau (liste de liste) avec entêtes
        table:list[list] = []
        for line in lines:
            line = line.replace("|", ";").replace("\n", "")
            line = line.split(";")
            if data_entry_counter(line) > 1:
                table.append(line)

        # Récupère et formatte les entêtes
        raw_headers = table[0]
        headers_length = data_entry_counter(raw_headers)
        headers = raw_headers[0:headers_length:]

        # Rcupère et formatte les données
        raw_data = table[1::]
        data = []
        for entry in raw_data:
            data.append(entry[0:headers_length:])

        # Génère le dataframe
        df = pd.DataFrame(data, columns=headers)

        # Applique le formatting aux entêtes si stipulé
        if formatting:
            df = column_name_formatter(df)

        return df

    def xlsx(file_path: str, formatting: bool) -> ndarray:
        """Convertis un fichier xlsx en dataframe"""
        df = pd.read_excel(file_path)

        # Column name formatting
        if formatting:
            df = column_name_formatter(df)

        return df


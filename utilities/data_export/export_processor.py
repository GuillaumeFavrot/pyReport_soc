from numpy import ndarray
import re
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook
from utilities.data_export.tools.column_to_number import column_to_number
from utilities.timer.timer import Timer

def export_data(timer:Timer, df: ndarray, output_file_name: str, column_name: str, sheet_name: str, cell: str) -> None:
    """Exporte l'une des colonnes spécifée d'un dataframe dans l'une feuille d'un fichier excel donné à une position précise (au format A1,B2, etc...)"""

    status1 = f"{timer.get_time()} - Copie en cours des données {column_name} dans la feuille {sheet_name} du fichier {output_file_name}"
    print(status1)

    #Création des variables necessaires à l'exportation
    file_path = f"./output/{output_file_name}"
    row = int(re.sub("[^ 0-9]+", '', cell))
    column = column_to_number(re.sub("[^ a-zA-Z]+", '', cell))
    list = df.get(column_name).tolist()

    #Ouverture du fichier destination
    wb = load_workbook(file_path)
    
    #Sélection de la feuille
    ws = wb[sheet_name]

    #Copiage des données
    for i, value in enumerate(list, start=row):
        cell = ws.cell(row=i, column=column).value=value

    #Sauvegarde du fichier
    status2=f"{timer.get_time()} - Saving file"
    print(status2)
    wb.save(file_path)
    status3=f"{timer.get_time()} - File saved!"
    print(status3)


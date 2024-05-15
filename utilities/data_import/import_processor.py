from numpy import ndarray
from utilities.timer.timer import Timer
from utilities.data_import.tools.readers import Readers
from utilities.data_import.tools.input_checker import input_checker

def import_file(timer:Timer, file: str, column_name_formatting: bool = True) -> ndarray:
    """Recois le nom d'un fichier xlsx ou CSV et retourne un dataframe. L'importeur dispose d'une fonctionnalité de conversion des noms de colonnes (Default = True)"""
    
    print(f'{timer.get_time()} - Importation des données depuis le fichier "{file}"')

    # Vérification du type de la variable "file"
    if type(file) != str:
        raise TypeError("File name must be a string")
    
    # Création du chemin d'accès du fichier
    file_path = f"./base_data/{file}"
    
    # Contrôle du type de fichier transmis
    if not input_checker(file_path):
        raise Exception("File type not supported: suported types are .csv and .xlsx")

    # Conversion depuis CSV
    if file_path.endswith(".csv"):
        file = Readers.csv(file_path, column_name_formatting)
        print(f'{timer.get_time()} - Importation CSV terminée')
        return file
    
    #Converson depuis xlsx
    if file_path.endswith(".xlsx"):
        file = Readers.xlsx(file_path, column_name_formatting)
        print(f'{timer.get_time()} - Importation XLSX terminée')
        return file
    
        
from numpy import ndarray
from utilities.data_import.tools.readers import Readers
from utilities.data_import.tools.input_checker import input_checker

def import_file(file: str, column_name_formatting: bool = True) -> ndarray:
    """Receives an xlsx or csv file name as an input and returns a pandas dataframe. The importer can optionally format column names to facilitate their use in pandas (Default = True)"""
    
    if type(file) != str:
        raise TypeError("File name must be a string")
    
    file_path = f"./base_data/{file}"
    
    if not input_checker(file_path):
        raise Exception("File type not supported: suported types are .csv and .xlsx")

    if file_path.endswith(".csv"):
        return Readers.csv(file_path, column_name_formatting)
    
    if file_path.endswith(".xlsx"):
        return Readers.xlsx(file_path, column_name_formatting)
    
        
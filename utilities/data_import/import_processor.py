from numpy import ndarray
from utilities.data_import.tools.readers import Readers
from utilities.data_import.tools.input_checker import input_checker

def import_file(file: str) -> ndarray:
    """Receives an xlsx or csv file name as an input and returns a pandas dataframe"""
    
    if type(file) != str:
        raise TypeError("File name must be a string")
    
    file_path = f"./excel_raw_data/{file}"
    
    if not input_checker(file_path):
        raise Exception("File type not supported: suported types are .csv and .xlsx")

    if file_path.endswith(".csv"):
        return Readers.csv(file_path)
    
    if file_path.endswith(".xlsx"):
        return Readers.xlsx(file_path)
    
        
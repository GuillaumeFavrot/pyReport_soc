from numpy import ndarray
from utilities.data_import.tools.readers import Readers
from utilities.data_import.tools.input_checker import input_checker

def import_file(file_path: str) -> ndarray:
    """Receives an xlsx or csv file path as an input and returns a pandas dataframe"""
    
    if type(file_path) != str:
        raise TypeError("File path must be a string")
    
    if not input_checker(file_path):
        raise Exception("File type not supported: suported types are .csv and .xlsx")

    if file_path.endswith(".csv"):
        return Readers.csv(file_path)
    
    if file_path.endswith(".xlsx"):
        return Readers.xlsx(file_path)
    
        
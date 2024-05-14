from numpy import ndarray
import pandas as pd
from utilities.data_import.tools.data_entry_counter import data_entry_counter

class Readers: 
    def csv(file_path: str) -> ndarray:
        """Converts a csv file into a pandas dataframe"""
            
        # Opens the csv file and create a list of strings containing all data 
        with open(file_path) as f:
            lines = list(f)

        # Converts csv strings into lists and store those into the table variable if the list contains headers of actual data
        table:list[list] = []
        for line in lines:
            line = line.replace("|", ";").replace("\n", "")
            line = line.split(";")
            if data_entry_counter(line) > 1:
                table.append(line)

        # Extract and format headers
        raw_headers = table[0]
        headers_length = data_entry_counter(raw_headers)
        headers = raw_headers[0:headers_length:]

        # Extract and format data
        raw_data = table[1::]
        data = []
        for entry in raw_data:
            data.append(entry[0:headers_length:])

        # Dataframe creation
        df = pd.DataFrame(data, columns=headers)

        return df

    def xlsx(file_path: str) -> ndarray:
        """Converts an excel file into a pandas dataframe"""
        df = pd.read_excel(file_path)
        return df


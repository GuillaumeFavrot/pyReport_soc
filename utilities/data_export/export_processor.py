from numpy import ndarray
import re
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook
from utilities.data_export.tools.column_to_number import column_to_number

def export_data(df: ndarray, output_file_name: str, column_name: str, sheet_name: str, cell: str) -> None:
    """Export a specific dataframe column into a specified file and sheet at a defined position"""

    print(f"Copying {column_name} data into the {sheet_name} sheet of the {output_file_name} file")

    file_path = f"./output/{output_file_name}"

    row = int(re.sub("[^ 0-9]+", '', cell))

    column = column_to_number(re.sub("[^ a-zA-Z]+", '', cell))

    list = df.get(column_name).tolist()

    wb = load_workbook(file_path)
 
    ws = wb[sheet_name]

    for i, value in enumerate(list, start=row):
        cell = ws.cell(row=i, column=column).value=value

    print("Saving file")
    wb.save(file_path)
    print("File saved!")


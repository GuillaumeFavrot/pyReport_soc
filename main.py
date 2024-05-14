from numpy import ndarray
import pandas as pd
from utilities.data_import.import_processor import import_file

def main() -> None:

    polices = import_file("polices.csv")

    print(polices.head())





#     """Main loop function"""

#     #Read a CSV or Excel file from a directory and turn it into a dataframe
#     df.columns = df.columns.str.replace("-", "_", regex=True)
#     print("Dataframe created")

#     #Ask the user for a client code
#     code = input("Enter a client code: ")

#     #Query the database for the client code
#     def get_subset_per_value_criteria(df: ndarray, column: str, value: str | int | float | bool) -> ndarray:
#         """Return a subset of a dataframe based on a criteria(combiantion of a column and a value)"""

#         column_type = type(df[column][0].item())
#         value_type = type(value)

#         if value_type != column_type:
#             raise TypeError(f"Given value is of type {value_type}, required type for this column is {column_type}")

#         return df[df[column] == value]

#     result = get_subset_per_value_criteria(df, 'code_societ', int(code))
    
#     #Print the result
#     print(result)

# #Script launcher
    # data_import("./excel_raw_data/societaires.xlsx")


if __name__ == "__main__":
    main()      
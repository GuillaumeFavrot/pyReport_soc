def input_checker(file_path: str) -> bool:
    """Controls the extenssion of an input file type and checks whether it's in the list of supported file types. Return a boolean"""
    
    file_extenssion = file_path.split(".")[-1]
    supported_file_types = ["csv", "xlsx"]

    return file_extenssion in supported_file_types
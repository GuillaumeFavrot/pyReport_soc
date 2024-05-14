def data_entry_counter(list: list) -> int:
    """Counts the number of non-empty values in a data entry"""
    counter = 0
    for entry in list:
        if entry != "":
            counter += 1
    return counter
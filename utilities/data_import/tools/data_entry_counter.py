def data_entry_counter(list: list) -> int:
    """Compte le nombre de valeur non vide dans une entrée de tableau"""
    counter = 0
    for entry in list:
        if entry != "":
            counter += 1
    return counter
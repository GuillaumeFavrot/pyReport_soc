def column_to_number(col):
    """Recois un index de colonne excel (lettre) et le convertis en indice numérique"""
    num = 0
    for c in col:
        num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num
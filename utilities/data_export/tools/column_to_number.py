def column_to_number(col):
    """Receives an excel column letter and outputs the corresponding column number"""
    num = 0
    for c in col:
        num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num
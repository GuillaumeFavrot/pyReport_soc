def input_checker(file_path: str) -> bool:
    """Contrôle l'extenssion du fichier transmis et vérifie que le type de fichier est supporté. retourne un bouléen"""
    
    file_extenssion = file_path.split(".")[-1]
    supported_file_types = ["csv", "xlsx"]

    return file_extenssion in supported_file_types
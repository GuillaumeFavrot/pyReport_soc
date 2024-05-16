import shutil
from utilities.logger.logger import Logger
from utilities.timer.timer import Timer

def create_report(timer:Timer, logger:Logger, template_name: str, report_name: str) -> None:
    """Crée un nouveau fichier "rapport" à partir d'un fichier template"""

    # Création des liens vers les fichiers sources et destination
    logger.info(f'{timer.get_time()} - Création du rapport {report_name} à partir du modèle {template_name}')
    template_file_path = f"./templates/{template_name}"
    report_file_path = f"./output/{report_name}"

    # Ouverture du fichier source
    source_file =  open(template_file_path, 'rb')

    # Ouverture du fichier desistantion
    destination_file = open(report_file_path, 'wb')

    # use the shutil.copyobj() method to copy the contents of source_file to destination_file
    shutil.copyfileobj(source_file, destination_file)
    logger.info(f'{timer.get_time()} - Création du rapport {report_name} terminée')
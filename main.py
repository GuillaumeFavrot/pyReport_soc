from utilities.timer.timer import Timer
from utilities.logger.logger import Logger
from utilities.data_import.import_processor import import_file
from utilities.report_creation.report_creation_processor import create_report
from utilities.data_export.export_processor import export_data

def main() -> None:
    """Fonction principale du script"""

    #Définition du nom du rapport
    report_name = "Surveillance des sociétaires"

    #Création d'un nouveau log et timer d'execution
    logger = Logger(report_name)
    timer = Timer()
    
    #Lancement du log et du timer d'exectution
    timer.start()
    logger.info(f'{timer.get_time()} - Lancement du script "{report_name}"')

    #Extraction des données depuis le ou les fichiers sources
    polices = import_file(timer, logger, "polices.csv")

    #Génération du rapport à partir des données sources
    #####WORK IN PROGRESS

    #Création du fichier rapport
    create_report(timer, logger, template_name="file.xlsx", report_name="file.xlsx")
    
    #Création de la configuration d'exportation ("nom_de_la_clonne_a_exporter", "feuille_dan_le_fichier_destination", "cellule")
    config = [
        ("societ_code", "Fichier de surveillance", "C10")
    ]

    #Insertion des données dans le fichier rapport
    export_data(timer=timer, logger=logger,  df=polices, output_file_name="file.xlsx", config=config)

    #Fin du timer et de l'execution
    logger.info(f'{timer.get_time()} - Fin d\'éxecution')
    timer.stop()

if __name__ == "__main__":
    main()     
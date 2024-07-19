from utilities.timer.timer import Timer
from utilities.logger.logger import Logger
from utilities.data_import.import_processor import import_file
from utilities.report_creation.report_creation_processor import create_report_output_file
from utilities.data_export.export_processor import export_data
from main_logic.report_processor import generate_report

def main() -> None:
    """Fonction principale du script"""

    #Définition du nom du rapport
    report_name = "Surveillance des sociétaires"

    #Création d'un nouveau log et timer d'execution
    logger = Logger(report_name)
    timer = Timer(logger)
    
    #Lancement du log et du timer d'exectution
    timer.start()

    #Extraction des données depuis le ou les fichiers sources
    polices = import_file(timer, logger, "polices.csv")
    distributeurs = import_file(timer, logger, "distributeurs.xlsx")
    rapport_sp = import_file(timer, logger, "rapport_sp.csv")
    societaires = import_file(timer, logger, "societaires.xlsx")

    #Génération du rapport à partir des données sources
    rapport = generate_report(timer, logger, polices, distributeurs, rapport_sp, societaires)

    #Création du fichier rapport
    create_report_output_file(timer, logger, template_name="file.xlsx", report_name="file.xlsx")
    
    #Création de la configuration d'exportation ("nom_de_la_clonne_a_exporter", "feuille_dan_le_fichier_destination", "cellule")
    config = [
        ("societ_code", "Fichier de surveillance", "C10"),
        ("nom_societ", "Fichier de surveillance", "B10"),
        ("date_integr", "Fichier de surveillance", "E10"),
        ("volume_contrats", "Fichier de surveillance", "H10"),
        ("valeur_portefeuille", "Fichier de surveillance", "I10"),
        ("volumetrie_sinistre", "Fichier de surveillance", "K10"),
        ("couts_sinistre", "Fichier de surveillance", "M10"),
        ("sp", "Fichier de surveillance", "O10"),
        ("code_distrib", "Fichier de surveillance", "R10"),
        ("nom_distrib", "Fichier de surveillance", "Q10")
    ]

    #Insertion des données dans le fichier rapport
    export_data(timer=timer, logger=logger,  df=rapport, output_file_name="file.xlsx", config=config)

    #Fin du timer et de l'execution
    timer.stop()

if __name__ == "__main__":
    main()     
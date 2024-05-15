from utilities.timer.timer import Timer
from utilities.data_import.import_processor import import_file
from utilities.report_creation.report_creation import create_report
from utilities.data_export.export_processor import export_data

def main() -> None:
    """Fonction principlae du script"""

    #Création d'un nouveau timer
    timer = Timer()
    
    #Lancement du timer d'exectution
    timer.start()

    #Extraction des données depuis le ou les fichiers sources
    polices = import_file(timer, "polices.csv")

    #Génération du rapport à partir des données sources
    #####WORK IN PROGRESS

    #Création du fichier rapport
    create_report(template_name="file.xlsx", report_name="file.xlsx")
    
    #Insertion des données dans le fichier rapport
    export_data(timer=timer, df=polices, output_file_name="file.xlsx", column_name="societ_code", sheet_name="Fichier de surveillance", cell="C10")

    #Fin du timer et de l'execution
    timer.stop()

if __name__ == "__main__":
    main()     
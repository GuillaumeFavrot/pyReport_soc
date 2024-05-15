from utilities.data_import.import_processor import import_file
from utilities.report_creation.report_creation import create_report
from utilities.data_export.export_processor import export_data

def main() -> None:
    """Fonction principlae du script"""

    #Extraction des données depuis le ou les fichiers sources
    polices = import_file("polices.csv")

    #Génération du rapport à partir des données sources
    #####WORK IN PROGRESS

    #Création du fichier rapport
    create_report(template_name="file.xlsx", report_name="file.xlsx")
    
    #Insertion des données dans le fichier rapport
    export_data(df=polices, output_file_name="file.xlsx", column_name="societ_code", sheet_name="Fichier de surveillance", cell="C10")

if __name__ == "__main__":
    main()     
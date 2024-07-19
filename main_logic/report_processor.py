from numpy import ndarray
import pandas as pd
from utilities.timer.timer import Timer
from utilities.logger.logger import Logger
from main_logic.tools.vlookup import vlookup
from main_logic.tools.count_iterations import count_iterations
from main_logic.tools.get_column_sum_in_subset import get_column_sum_in_subset

def generate_report(timer: Timer, logger: Logger, polices: ndarray, distributeurs: ndarray, rapport_sp: ndarray, societaires: ndarray) -> ndarray :
    """Reçoit des dataframe source en entrée et génère un rapport au format dataframe en sortie"""

    # Lancement du processus
    logger.info(f"{timer.get_time()} - Lancement du processus de génération des données du rapport")

    # Création d'un dataframe vide qui contiendra l'ensemble des éléments du rapport
    logger.info(f"{timer.get_time()} - Création du rapport")
    report = pd.DataFrame()

    ## Création de la liste des sociétaires (nom + code)
    logger.info(f"{timer.get_time()} - Création de la liste des sociétaires (nom + code)")
    report["societ_code"] = polices["societ_code"].drop_duplicates().astype('str')
    report["nom_societ"] = vlookup(report, societaires, "societ_code", "codesociet", "nomsociet")


    ## Récupération de la date de création des fiches sociétaire
    logger.info(f"{timer.get_time()} - Récupération de la date de création des fiches sociétaire")
    report["date_integr"] = vlookup(report, societaires, "societ_code", "codesociet", "dateintegr")


    ## Génération de l'état portefeuille (nombre de contrat + valeur portefeuille)
    logger.info(f"{timer.get_time()} - Génération de l'état portefeuille (nombre de contrat + valeur portefeuille)")
    report["volume_contrats"] = report["societ_code"].apply(count_iterations, args=(polices, "societ_code"))
    report["valeur_portefeuille"] = report["societ_code"].apply(get_column_sum_in_subset, args=(polices, "societ_code", "mt_ann_ttc_cp_inclus", 'float'))


    ## Calcul de la volumétrie sinistre
    logger.info(f"{timer.get_time()} - Calcul de la volumétrie sinistre")
    report["volumetrie_sinistre"] = report["societ_code"].apply(get_column_sum_in_subset, args=(rapport_sp, "code_societ", "nb_sinistres", 'int', (["SANTE", "SANTE GROUPE", "SANTE DES FRONTALIERS"], "garantiec")))

    ## Calcul du coût des sinistres
    logger.info(f"{timer.get_time()} - Calcul du coût des sinistres")
    report["couts_sinistre"] = report["societ_code"].apply(get_column_sum_in_subset, args=(rapport_sp, "code_societ", "charge_sinistre", 'float'))

    ## Calcul du rapport s/p
    logger.info(f"{timer.get_time()} - Calcul du rapport S/P")
    report["sp"] = report["couts_sinistre"]/report["societ_code"].apply(get_column_sum_in_subset, args=(rapport_sp, "code_societ", "mt_prime", 'float'))

    ## Récupération du distributeur (nom + code)
    logger.info(f"{timer.get_time()} - Récupération du distributeur (nom + code)")
    report["code_distrib"] = vlookup(report, societaires, "societ_code", "codesociet", "codedistrib")
    report["nom_distrib"] = vlookup(report, distributeurs, "code_distrib", "codedistrib", "nomdistrib")


    ## Récupération de la typologie des contrats du sociétaire
    logger.info(f"{timer.get_time()} - Récupération de la typologie des contrats du sociétaire")


    ## Récupération de la nature des sinistres
    logger.info(f"{timer.get_time()} - Récupération de la nature des sinistres")


    # Fin du processus de génération du rapport
    logger.info(f"{timer.get_time()} - Génération des données du rapport terminée")
    print(report)

    return report
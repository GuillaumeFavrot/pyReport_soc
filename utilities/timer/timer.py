import time
from utilities.logger.logger import Logger

class TimerError(Exception):
    """Erreur custom pour signifier la mauvaise utilisation du timer"""

class Timer:
    def __init__(self, logger):
        self._start_time = None
        self.logger = logger

    def start(self):
        """Lance le timer"""
        if self._start_time is not None:
            self.logger.error("Le timer est déjà lancé")
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        
        self._start_time = time.perf_counter()
        self.logger.info(f'{self.get_time()} - Lancement du script "{self.logger.report_name}"')

    def get_time(self):
        """Récupère le temps d'éxecution"""
        if self._start_time is None:
            self.logger.error('Le timer n\'a pas encore été lancé')
            raise TimerError(f"Timer is not running. Use .start() to start it")
        
        elapsed_time = time.perf_counter() - self._start_time

        return f"{elapsed_time:0.4f}"
    
    def stop(self):
        """Stop le timer, et affiche le temps d'execution final"""
        if self._start_time is None:
            self.logger.error('Le timer n\'a pas encore été lancé')
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        logger.info(f'{self.get_time()} - Fin d\'éxecution - Temps d\'éxecution total: {elapsed_time}')
        self._start_time = None
        
        
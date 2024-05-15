import time

class TimerError(Exception):
    """Erreur custom pour signifier la mauvaise utilisation du timer"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Lance le timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def get_time(self):
        """Récupère le temps d'éxecution"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        
        elapsed_time = time.perf_counter() - self._start_time

        return f"{elapsed_time:0.4f}"
    
    def stop(self):
        """Stop le timer, et affiche le temps d'execution final"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
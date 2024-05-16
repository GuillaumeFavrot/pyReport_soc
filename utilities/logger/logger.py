import logging
import datetime

timestamp = f"{datetime.date.today()}--{datetime.datetime.now().hour}-{datetime.datetime.now().minute}" 

class Logger():

    def __init__(self, report):
        self.logger = logging.getLogger(report)
        logging.basicConfig(filename=f"./logs/{timestamp}.log", encoding='utf-8', level=logging.DEBUG)

    def info(self, message):
        self.logger.info(message)
        print(message)

    def info(self, warning):
        self.logger.info(warning)
        print(warning)

    def info(self, error):
        self.logger.info(error)
        print(error)
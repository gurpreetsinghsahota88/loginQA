
#log file
import logging

class LogGen:
    @staticmethod
    def loggen():
     fname ="C:\\Users\\GURPREET\\PycharmProjects\\hybridproject\\logs\\automation.log"
     logging.basicConfig(filename= fname, format='%(asctime)s: %(levelname)s %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
     logger = logging.getLogger()
     logger.setLevel(logging.INFO)
     return logger


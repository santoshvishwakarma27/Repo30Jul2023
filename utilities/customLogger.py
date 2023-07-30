import logging
import os,sys

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=os.path.join(sys.path[0]+"\\logs"+"\\automation.log"),
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

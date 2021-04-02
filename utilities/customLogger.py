import logging
from datetime import datetime

class LogGenenration:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
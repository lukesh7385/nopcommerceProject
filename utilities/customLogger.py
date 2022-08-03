import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\Logs\\automation.log',
                            format='%(asctime)s: %(levelname)s: %(massage)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.INFO)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

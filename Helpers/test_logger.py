import logging


def logger(msg="", error=False):
    logging.basicConfig(filename='testrun.log',
                        filemode='a+',
                        format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO
                        )
    if error:
        logging.error(msg)
    else:
        logging.info(msg)

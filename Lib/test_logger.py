import logging


def logger(msg="", error=False):
    logging.basicConfig(
            filename='test_run.txt', filemode='a+',
            format='%(created)f - %(levelname)s - %(message)s',
            level=logging.INFO, force=True)
    if error:
        logging.error(msg)
    else:
        logging.info(msg)

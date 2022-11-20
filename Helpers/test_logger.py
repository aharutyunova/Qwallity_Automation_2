import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : %(levelname)s : %(message)s',
    handlers=[logging.FileHandler("Runner.log"),
              logging.StreamHandler()],
    datefmt='%H:%M:%S',
    force=True,
    )

def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)

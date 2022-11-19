import logging


logging.basicConfig(filename='test_run.txt',
                    filemode='a+', format='%(created)f - %(levelname)s -\
                     %(message)s',
                    level=logging.INFO, force=True
                    )


def logger(msg="", error=False):
    '''Here is represented a method for logging both when there is an error
     and when there is no error'''
    if error:
        logging.error(msg)
    else:
        logging.info(msg)

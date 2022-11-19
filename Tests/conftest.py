import logging
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture
def get_driver():
    '''Here is represented a method to get driver'''
    return webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture
def logger(msg="", error=False):
    '''Here is represented a method for logging both when there is an error
     and when there is no error'''
    if error:
        logging.error(msg)
    else:
        logging.info(msg)

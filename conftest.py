import pytest
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_driver():
    '''Here is represented a method to get driver'''
    return webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture
def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)

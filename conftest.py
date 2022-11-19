"""Neccessary packages"""
import logging
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Fixture for driver"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def logger(msg="", error=False):
    """Fixture for logger"""
    if error:
        logging.error(msg)
    else:
        logging.info(msg)

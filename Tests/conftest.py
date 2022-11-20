import logging
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # driver = webdriver.Chrome(executable_path='/Users/goharmelkonyan/Downloads/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://www.list.am/')
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
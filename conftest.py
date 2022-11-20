import pytest
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def log():
    logging.info("\n\nStarting the test case...\n" +
                 os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0] + "\n")
    yield logging
    logging.info("\nFinished\n")

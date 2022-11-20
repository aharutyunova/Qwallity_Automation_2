from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import random

from Helpers.test_logger import logger
from Helpers.environment import global_timeout

class FunctionLib:
    def __init__(self, driver):
        self.driver = driver

    #added funtion
    def get_random_elem(self, loc, timeout = global_timeout):
        logger(f"Getting a random item locator from '{loc[1]}'")
        elem_list = self.find_all(loc, timeout)
        return random.choice(elem_list)

    #added function
    def visibility_of(self, loc, timeout = global_timeout):
        logger(f"Checking visibility of element '{loc[1]}'")
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(loc),
                message=f"Element '{loc}' not found!")
        except Exception as e:
            logger(e)
            return False
        return True

    #fixed
    def find(self, loc, timeout = global_timeout, should_exist=True, get_text="", get_attribute=""):                         
        logger(f"Search element '{loc[1]}'")
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(loc),
                message=f"Element '{loc}' not found!")
        except Exception as e:
            logger(e)
            if should_exist:
                return False
                #### raise Exception(e)
            # Seemed to be wrong logic, so I changed. But this part is not used
            #### return False
            return True
        if get_text:
            logger(f"Element text: {elem.text}")
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem

    def go_to_page(self, url):
        logger(f"Navigate to {url}")
        self.driver.get(url)
        self.driver.maximize_window()

    def find_and_click(self, loc, timeout = global_timeout):
        elem = self.find(loc, timeout)
        logger(f"Click on {loc[1]}")
        elem.click()

    def find_and_send_keys(self, loc, inp_text, timeout = global_timeout):
        elem = self.find(loc, timeout)
        logger(f"Send '{inp_text}' to {loc[1]}")
        elem.send_keys(inp_text)    
    
    def find_all(self, loc, timeout = global_timeout):
        logger(f"Search elements '{loc[1]}'")
        try:
            elements = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(loc), message=f"Elements '{loc}' not found!")
        except Exception as e:
            logger(e)
            return False
        logger(f"Found: {len(elements)}")
        return elements

    def wait_for_page(self, page="", not_page="", timeout = global_timeout):
        if page:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.url_contains(page))
        elif not_page:
            WebDriverWait(self.driver, timeout).until_not(
                expected_conditions.url_contains(not_page))

    def retrn_url(self):
        return str(self.driver.current_url)

    def hover_elem(self, elem):
        a = ActionChains(self.driver)
        a.move_to_element(elem).perform()

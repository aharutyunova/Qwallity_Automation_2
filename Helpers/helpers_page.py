from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Helpers.test_logger import logger


class GeneralHelpers:
    '''Here are represented helpers which are used in different pages'''

    def __init__(self, driver):
        '''Here is the default constructor of the class'''
        self.driver = driver

    def find_and_click(self, loc, timeout=10):
        '''Here is represented a method to find an element and click on it'''
        elem = self.find(loc, timeout)
        logger(f"Click on {loc[1]}")
        elem.click()

    def find_and_send_keys(self, loc, inp_text, timeout=10):
        '''Here is represented a method to find an element and send the given
        keys on it'''
        elem = self.find(loc, timeout)
        logger(f"Send '{inp_text}' to {loc[1]}")
        elem.send_keys(inp_text)

    def find(self, loc, timeout=10, should_exist=True, get_text="",
             get_attribute=""):
        '''Here is represented a method to find an element'''
        logger(f"Search element '{loc[1]}'")
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(loc),
                message=f"Element '{loc}' not found!")
        except Exception as error:
            logger(error)
            if should_exist:
                raise Exception(error)
            return False
        if get_text:
            logger(f"Element text: {elem.text}")
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem

    def find_all(self, loc, timeout=10):
        '''Here is represented a method to find all matches to critera
        elements'''
        logger(f"Search elements '{loc[1]}'")
        try:
            elements = WebDriverWait(self.driver, timeout)\
                .until(EC.visibility_of_all_elements_located(loc), message=f"\
                Elements '{loc}' not found!")
        except Exception as error:
            logger(error)
            return False
        logger(f"Found: {len(elements)}")
        return elements

    def wait_for_page(self, page="", not_page="", timeout=10):
        '''Here is represented a method which helps to wait for the redirected
         page'''
        if page:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(page))
        elif not_page:
            WebDriverWait(self.driver, timeout).until_not(
                EC.url_contains(not_page))

    def hover_elem(self, elem):
        '''Here is represented a method which hover over an element'''
        action = ActionChains(self.driver)
        action.move_to_element(elem).perform()

    def go_to_page(self, url):
        '''Here is represented a method which helps to navigate to the given \
        page'''
        logger(f"Navigate to {url}")
        self.driver.get(url)
        self.driver.maximize_window()

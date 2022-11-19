"""selenium package"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Helpers.helpers import GeneralHelpers

#locators
lbl_account = (By.XPATH, "//*[@id='ma']")
icon_lang = (By.XPATH, "//div[text()='English']")
inp_search = (By.ID, "idSearchBox")

class HeaderPage(GeneralHelpers):
    """Class for search page"""
    def change_english(self):
        """Method to change app lamguage to english"""
        self.find_and_click(icon_lang)

    def search_data(self, search_data):
        """Method to search 'house' word"""
        self.find_and_send_keys(inp_search, search_data)
        self.find(inp_search).send_keys(Keys.ENTER)

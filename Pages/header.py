from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.webdriver.common.keys import Keys
from TestData.testdata import input_data

inp_search = (By.XPATH, "//input[@id='idSearchBox']")
icon_lang = (By.XPATH, "//div[text()='English']")
menu_tab = (By.XPATH, f"//*[@id='menu']//a[text()='{input_data['menu_tab']}']")


class HeaderPage(GeneralHelpers):

    def search_data(self, test_data):
        self.find_and_send_keys(inp_search, test_data)
        self.find(inp_search).send_keys(Keys.ENTER)

    def change_english(self):
        self.find_and_click(icon_lang)

    def click_menu_tab(self):
        self.find_and_click(menu_tab)

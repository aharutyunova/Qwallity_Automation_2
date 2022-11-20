from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.webdriver.common.keys import Keys
from TestData import testdata
import  time


Search_field = (By.XPATH, "//input[@id='idSearchBox']")
icon_lang = (By.XPATH, "//div[text()='English']")
menu_tab = (By.XPATH, f"//*[@id='menu']//a[text()='{testdata.menu_tab}']")


# you don't have menu_tab in testdata, so you get error in line 10
class HeaderPage(GeneralHelpers):

    def saerch_data(self, test_data):
        self.find_and_send_keys(Search_field, test_data)
        self.find(Search_field).send_keys(Keys.ENTER)

    def change_language(self):
        self.find_and_click(icon_lang)

    def click_menu_tab(self):
        self.find_and_click(menu_tab)



from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Helpers.helpers_page import GeneralHelpers
from TestData.testdata import search_criteria


search_field = (By.XPATH, "//input[@id='idSearchBox']")
english_flag = (By.XPATH, "//div[text()='English']")
menu_tab = (By.XPATH, f"//*[@id='menu']//a[text()=\
           '{search_criteria['menu_tab']}']")


class HeaderPage(GeneralHelpers):
    '''Here are represented all methods connected to header section'''

    def search_item(self, test_data):
        '''Here is represented adding of an input into the search field'''
        self.find_and_send_keys(search_field, test_data)
        self.find(search_field).send_keys(Keys.ENTER)

    def select_language(self):
        '''Here is represented selecting of English as language for the
        website'''
        self.find_and_click(english_flag)

    def click_menu_tab(self):
        '''Here is represented clicking on a menu tab'''
        self.find_and_click(menu_tab)

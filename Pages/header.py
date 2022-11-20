from selenium.webdriver.common.by import By
from Lib.helpers import GeneralHelpers
from selenium.webdriver.common.keys import Keys
from TestData import testdata

inp_search = (By.ID, "idSearchBox")
icon_lang = (By.XPATH, "//div[text()='English']")
menu_tab = (By.XPATH, f"//*[@id='menu']//a[text()='{testdata.menu_tab}']")

# Anna - You don't have menu_tab in testdata file , so this locator return error
class HeaderPage(GeneralHelpers):

    def search_data(self, test_data):
        self.find_and_send_keys(inp_search, test_data)
        self.find(inp_search).send_keys(Keys.ENTER)

    def change_english(self):
        self.find_and_click(icon_lang)

    def click_menu_tab(self):
        self.find_and_click(menu_tab)

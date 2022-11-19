from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.webdriver.common.keys import Keys
from TestData.testdata import search_data
import  time

lbl_account = (By.XPATH, "//*[@id='ma']")
inp_search = (By.ID, "idSearchBox")
icon_lang = (By.XPATH, "//div[text()='English']")
#menu_tab = (By.XPATH, f"//*[@id='menu']//a[text()='{testdata.menu_tab}']")
#logo = (By.XPATH, '//*[@id="l"]')


class HeaderPage(GeneralHelpers):

    def change_english(self):
        self.find_and_click(icon_lang)

    def saerch_data(self, test_data):
        self.find_and_send_keys(inp_search, search_data)(Keys.ENTER)
        #self.find(inp_search).send_keys(Keys.ENTER)


    # def click_menu_tab(self):
    #     self.find_and_click(menu_tab)

    # def click_on_logo(self):
    #     print('logo')
    #     self.find_and_click(logo)


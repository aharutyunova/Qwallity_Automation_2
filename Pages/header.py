from selenium.webdriver.common.by import By
from Helpers.helpers import FunctionLib
from selenium.webdriver.common.keys import Keys
from TestData import testdata

class HeaderPage(FunctionLib):

    lbl_account = (By.XPATH, "//*[@id='ma']")
    inp_search = (By.ID, "idSearchBox")
    icon_lang_eng = (By.XPATH, "//div[text()='English']")
    menu_tab = (By.XPATH, f"//*[@id='menu']//a[text()='{testdata.MENU}']")
    logo = (By.XPATH, '//*[@id="l"]')


    def search_data(self, test_data):
        self.find_and_send_keys(self.inp_search, test_data)
        self.find(self.inp_search).send_keys(Keys.ENTER)

    def change_english(self):
        self.find_and_click(self.icon_lang_eng)

    def click_menu_tab(self):
        self.find_and_click(self.menu_tab)

    def click_on_logo(self):
        self.find_and_click(self.logo)


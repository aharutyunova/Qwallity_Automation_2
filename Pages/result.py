"""selenium package"""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers

#locators
result_container = (By.XPATH, "/html/body/div[3]/div[3]/div[2]")
from_price = (By.ID, "idprice1")
favorite_items = (By.XPATH, "//div[@id='contentr']//a")
to_price = (By.ID, "idprice2")
price_blue_button = (By.ID, "gobtn")
result_item = (By.XPATH, "//*[@id='hcontent']/div/div/div[3]/div/a[1]/img")
result_price = (By.XPATH, "//div[@id='contentr']//a//div[@class='p']")
contentr_items = (By.XPATH, "//div[@id='contentr']//a")
add_to_favorite = (By.XPATH, "//div[@id='sstar']//div")
login_require_popup = (By.XPATH, "//a[text()='Login to List.am']")
ddl_currency = (By.XPATH, "//*[text()='Currency']//following::div[@class='me']")
usd_price = (By.XPATH, "//div[text()='$ (USD)']")

class ResultPage(GeneralHelpers):
    """Result page class"""

    def select_usd_currency(self):
        """method to change currency to dollar"""
        self.find_and_click(ddl_currency)
        self.find_and_click(usd_price)

    def set_price(self, price_min, price_max):
        """Filer by price"""
        self.find_and_send_keys(from_price, price_min)
        self.find_and_send_keys(to_price, price_max)
        self.find_and_click(price_blue_button)

    def check_result(self):
        """Method to check the filter results"""
        elements = self.find_all(result_price)
        price_list = [el.text for el in elements]
        price_list_number = [int(el.split('$')[1].split(' ')[0]) for el in price_list]
        return price_list_number

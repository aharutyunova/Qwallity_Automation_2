from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
import random

result_container = (By.XPATH, "//div[@id='contentr']")
all_currency = (By.XPATH,
                "//*[text()='Currency']//following::div[@class='me']")
usd_price = (By.XPATH, "//div[text()='$ (USD)']")
from_price = (By.XPATH, "//input[@id='idprice1']")
favorite_items = (By.XPATH, "//div[@id='contentr']//a")
to_price = (By.XPATH, "//input[@id='idprice2']")
price_blue_button = (By.XPATH, "//img[@id='gobtn']")
result_item = (By.XPATH, "//*[@id='contentr']//div//a//img")
result_price = (By.XPATH, "//div[@id='contentr']//a//div[@class='p']")
add_to_favorite = (By.XPATH, "//div[@id='sstar']//div")
login_require_popup = (By.XPATH, "//a[text()='Login to List.am']")


class ResultPage(GeneralHelpers):

    def select_usd_currency(self):
        self.find_and_click(all_currency)
        self.find_and_click(usd_price)

    def set_price(self, price_min, price_max):
        self.find_and_send_keys(from_price, price_min)
        self.find_and_send_keys(to_price, price_max)
        self.find_and_click(price_blue_button)

    def check_result(self):
        elements = self.find_all(result_price)
        price_list = [el.text for el in elements]
        price_list_number = \
            [int(el.split('$')[1].split(' ')[0]) for el in price_list]
        return price_list_number

    def add_to_favorites(self):
        i = random.randint(0, 5)
        item = self.find(result_item)
        item.click()
        self.wait_for_page('item')

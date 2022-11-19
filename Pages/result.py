from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helpers.helpers_page import GeneralHelpers


from_price = (By.XPATH, "//input[@id='idprice1']")
to_price = (By.XPATH, "//input[@id='idprice2']")
all_currencies = (By.XPATH, "//*[text()='Currency']\
                 //following::div[@class='me']")
usd_currency = (By.XPATH, "//div[text()='$ (USD)']")
price_blue_button = (By.XPATH, "//img[@id = 'gobtn']")
result_container = (By.XPATH, "//div[@id='contentr'']")
result_item = (By.XPATH, "//div[@class='dl']//a")
result_price = (By.XPATH, "//div[@id='contentr']//a//div[@class='p']")
add_to_favorite = (By.XPATH, "//div[@original-title='Add to Favorites']")
favorite_items = (By.XPATH, "//div[@id='contentr']//a")
login_require_popup = (By.XPATH, "//a[text()='Login to List.am']")


class ResultPage(GeneralHelpers):
    '''Here are represented a filtered by price result and set to favorite
    items'''

    def select_usd_currency(self):
        '''Here are represented a filtered by price result and set to favorite
        items'''
        self.find_and_click(all_currencies)
        WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_element_located((usd_currency)))
        self.find_and_click(usd_currency)

    def set_price(self, price_min, price_max):
        '''Here are represented from/to fields filling in'''
        self.find_and_send_keys(from_price, price_min)
        self.find_and_send_keys(to_price, price_max)
        WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_element_located((price_blue_button)))
        self.find_and_click(price_blue_button)

    def return_price_list(self):
        '''Here are represented filtered result by price'''
        elements = self.find_all(result_price)
        price_list = [el.text for el in elements]
        price_list_number = [int(el.split('$')[1].split(' ')[0])
                             for el in price_list]
        return price_list_number

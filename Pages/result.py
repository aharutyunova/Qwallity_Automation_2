from selenium.webdriver.common.by import By
from Helpers.helpers import FunctionLib


class ResultPage(FunctionLib):
    class Locator:
        add_to_favorite = (By.XPATH, "//div[@id='sstar']//div")
        result_container = (By.XPATH, "/html/body/div[3]/div[3]/div[2]")
        ddl_currency = (By.XPATH, "//*[text()='Currency']//following::div[@class='me']")
        usd_price = (By.XPATH, "//div[text()='$ (USD)']")
        amd_price = (By.XPATH, "//div[text()='֏ (AMD)']")
        from_price = (By.ID, "idprice1")
        favorite_items = (By.XPATH, "//div[@id='contentr']//a")
        to_price = (By.ID, "idprice2")
        price_blue_button = (By.ID, "gobtn")
        result_block = (By.XPATH, "//div[3]/div/a[*]/img")
        result_price = (By.XPATH, "//div[@id='contentr']//a//div[@class='p']")
        contentr_items = (By.XPATH, "//div[@id='contentr']//a")
    
    #added function
    def select_currency(self, currency):
        self.find_and_click(self.Locator.ddl_currency)
        if str(currency).lower() in ["usd","$","USD"]:
            self.find_and_click(self.Locator.usd_price) 
        if str(currency).lower() in ["amd","֏","dram"]:
            self.find_and_click(self.Locator.amd_price) 
        
    def set_price(self, price_min, price_max):
        self.find_and_send_keys(self.Locator.from_price, price_min)
        self.find_and_send_keys(self.Locator.to_price, price_max)
        self.find_and_click(self.Locator.price_blue_button)
    
    #fixed function
    def get_price_list(self):
        elements = self.find_all(self.Locator.result_price)
        price_list = [el.text for el in elements]
        price_list_number = []
        for elem in price_list:
            if '$' in elem:
                price_list_number.append(int(elem.split('$')[1].split(' ')[0]))
            else:
                price_list_number.append(int(''.join(elem.split(' ')[0].split(','))))
        return price_list_number      

    #changed function to recieve web element
    def add_to_favorites(self, element):
        element.click()
        self.find_and_click(self.Locator.add_to_favorite)
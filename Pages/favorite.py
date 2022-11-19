"""Selenium package"""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers

class Favorite(GeneralHelpers):
    """Class for Favorite page"""
    #locators
    favorite_items = (By.XPATH, "//div[@id='contentr']//a")
    favorite_items_remove = (By.XPATH, '//div[@original-title="Remove from favorites"]')
    result_item = (By.XPATH, "//*[@id='hcontent']/div/div/div[3]/div/a[1]/img")
    add_to_favorite = (By.XPATH, "//div[@id='sstar']//div")
    login_require_popup = (By.XPATH, "//a[text()='Login to List.am']")
    favorite_ads = (By.XPATH, "//div[text()='Favorite Ads']")
    my_account_icon = (By.XPATH, '//*[@id="ma"]')

    def add_to_favorites(self):
        """Method to add items to favorites"""
        item = self.find(self.result_item)
        item.click()
        self.wait_for_page('item')
        self.find_and_click(self.add_to_favorite)

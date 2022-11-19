"""Import neccessary modules"""
import time
from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
from TestData.testdata import test_data

def test_search(driver):
    """
    Test case for searching 'house',
    filtering by price and getting search results
    """
    helper = GeneralHelpers(driver)
    helper.go_to_page("https://www.list.am/")
    time.sleep(2)
    search_page = HeaderPage(driver)
    search_page.change_english()
    search_page.search_data(test_data["search_data"])
    resultpage = ResultPage(driver)
    resultpage.select_usd_currency()
    resultpage.set_price(test_data["price_min"], test_data["price_max"])
    price_list = resultpage.check_result()
    for price in price_list:
        assert 0 <= price <= 50, helper.logger("Result is incorrect", error=True)
        helper.logger("Result is correct!")
    
from Pages.config import base_url
from Pages.header import HeaderPage
from Pages.result import ResultPage
from TestData.testdata import search_criteria
from Helpers.helpers_page import GeneralHelpers
from Helpers.test_logger import logger


def test_filtered_result(get_driver):
    '''Here is represented a method which helps to check if the filtered 
    result matches to the given criterias'''
    result_page = ResultPage(get_driver)
    header_page = HeaderPage(get_driver)
    helpers = GeneralHelpers(get_driver)
    helpers.go_to_page(base_url)
    header_page.select_language()
    header_page.search_item(search_criteria["search_data"])
    result_page.select_usd_currency()
    result_page.set_price(search_criteria["price_min"], search_criteria["price_max"])
    price_list = result_page.return_price_list()
    for price in price_list:
        assert 0 <= price <= 50, logger("Result is incorrect", error=True)
        logger("Result is correct!")
    get_driver.quit()

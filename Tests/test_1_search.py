from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Helpers.test_logger import logger
from TestData import testdata

price_list = None


def test_case1_search(driver):
    helper = GeneralHelpers(driver)
    resultpage = ResultPage(driver)
    headerpage = HeaderPage(driver)
    headerpage.change_english()
    headerpage.search_data(testdata.input_data["search_data"])
    resultpage.select_usd_currency()
    resultpage.set_price(testdata.input_data["price_min"],
                         testdata.input_data["price_max"])
    price_list = resultpage.check_result()
    for price in price_list:
        assert 0 <= price <= 50, logger("Result is incorrect", error=True)
    logger("Result is correct!")

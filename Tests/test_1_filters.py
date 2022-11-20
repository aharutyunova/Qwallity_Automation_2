from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

from Helpers import environment
from Helpers.helpers import FunctionLib
from Pages.header import HeaderPage
from Pages.login import LoginPage
from Pages.result import ResultPage
from  TestData.testdata import PRICE_FILTER
from  TestData.testdata import SEARCH_LINE


"""
1. Navigate to lits.am
2. Search by "house" word
3. Filter by 2 different Currencies and corresponding ranges
4. Click on blue icon to apply the filter
5. Check that result's prices are in filtered range
"""


# I would rather not put the parameters in testdata for better readability here
@pytest.mark.parametrize(
    "currency, price_range", PRICE_FILTER
)
class Test_FilterGroup:
    
    def test_1_price(self, driver, log, currency, price_range):
        resultpage = ResultPage(driver)
        header = HeaderPage(driver)
        loginpage = LoginPage(driver)
        helper = FunctionLib(driver)

        helper.go_to_page(environment.config_data["url"])
        header.change_english()
        header.search_data(SEARCH_LINE)
        resultpage.select_currency(currency)
        resultpage.set_price(price_range[0], price_range[1])
        price_list = resultpage.get_price_list()
        for price in price_list:
            assert price_range[0] <= price <= price_range[1], log.error("Result is incorrect")
        log.info("Result is correct!")
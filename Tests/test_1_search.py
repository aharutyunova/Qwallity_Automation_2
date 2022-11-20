from Lib.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Lib.test_logger import logger
from TestData.testdata import config_data
from TestData.testdata import search_data
from TestData.testdata import filter_data

# Anna - in line 12 you use 'URL' as key but real key is 'url', so you get key error
# Also you get key error in line 17 because key name not house but search_data per your testdata


def test_search(driver):
    my_helper = GeneralHelpers(driver)
    my_helper.go_to_page(config_data['URL'])

    search = HeaderPage(driver)
    search.change_english()
    search.search_data(search_data['house'])
    search.click_menu_tab()
    search.wait_for_page()
    filter_search_result = ResultPage(driver)
    filter_search_result.select_usd_currency()
    filter_search_result.set_price(
        filter_data['price_min'], filter_data['price_max']
        )

    filter_search_result.check_result()

    price_list = filter_search_result.check_result()
    for price in price_list:
        assert 0 <= price <= 50, logger("Result is incorrect", error=True)
        logger("Result is correct!")

    my_helper.close_browser()

# Anna - you already use driver.quite() in your conftest file for driver fixture,
# so no need to close it here
from Lib.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
# from Lib import environment
from Lib.test_logger import logger
from TestData.testdata import config_data


def test_favorite(driver):
    helper = GeneralHelpers(driver)
    helper.go_to_page(config_data['url'])

    resultpage = ResultPage(driver)

    search = HeaderPage(driver)
    search.change_english()

    resultpage.add_to_favorites()

    assert resultpage.popup, logger("Error", error=True)
    logger("Result is correct!")

    helper.close_browser()

# Anna - you already use driver.quite() in your conftest file for driver fixture,
# so no need to close it here
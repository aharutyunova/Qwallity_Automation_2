from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Pages.result import login_require_popup
from Pages.result import add_to_favorite
from Helpers.test_logger import logger


def test_favorite(driver):
    helper = GeneralHelpers(driver)
    headerpage = HeaderPage(driver)
    resultpage = ResultPage(driver)

    headerpage.change_english()
    headerpage.click_menu_tab()
    resultpage.add_to_favorites()
    resultpage.find_and_click(add_to_favorite)
    assert resultpage.find(login_require_popup), logger("Error", error=True)
    logger("Result is correct!")

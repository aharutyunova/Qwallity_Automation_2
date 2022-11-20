from Helpers.helpers import FunctionLib
from Pages.header import HeaderPage
from Pages.login import login_require_popup
from Helpers.environment import config_data as TestEnvironment
from Pages.result import ResultPage

"""

1. Navigate to list.am
2. Try add random item as favorite
3. System show popup for required login

"""

def test_favorite(driver, log):
    helper = FunctionLib(driver)
    header = HeaderPage(driver)
    resultpage = ResultPage(driver)

    helper.go_to_page(TestEnvironment["url"])
    header.change_english()
    random_item = helper.get_random_elem(resultpage.Locator.result_block)
    resultpage.add_to_favorites(random_item)

    assert helper.visibility_of(login_require_popup) == True, log.error("Required login popup is missing")
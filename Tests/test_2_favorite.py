"""Import neccessary modules"""
import time
from Helpers.helpers import GeneralHelpers
from Pages.favorite import Favorite
from Pages import header

def test_favorite(driver):
    """
1. Navigate to list.am
2. Try add random item as favorite
3. System show popup for required login

"""
    helper = GeneralHelpers(driver)
    favoritepage = Favorite(driver)
    helper.go_to_page("https://www.list.am/")
    time.sleep(2)
    helper.find_and_click(header.icon_lang)
    favoritepage.add_to_favorites()
    assert helper.find(favoritepage.login_require_popup), helper.logger(
        "Popup is not visible", error=True)
    helper.logger("Popup is visible!")
    
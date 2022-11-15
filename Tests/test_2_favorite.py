import time

from Helpers.helpers import GeneralHelpers
from Pages import header
from Pages.header import HeaderPage
from Pages.login import LoginPage
from Helpers import environment
from Pages.result import ResultPage
from Pages.favorite import Favorite
from Tests.some_helpers import TESTHelpers

"""

1. Login to the system
2. Go to Electronics page
3. Add random number of products as a favorite
4. Go to My Account-> Favorite Ads
5. Check that Favorite page contains correct(selected) products

"""

def test_favorite(driver):
    helper = GeneralHelpers(driver)
    headerpage = HeaderPage(driver)
    resultpage = ResultPage(driver)
    test_helper = TESTHelpers(driver)
    loginpage = LoginPage(driver)
    favoritepage = Favorite(driver)

    helper.go_to_page("https://www.list.am/")
    helper.find_and_click(header.icon_lang)
    favorite_item = resultpage.add_to_favorites()





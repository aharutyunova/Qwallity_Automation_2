# import time
from Helpers.helpers import GeneralHelpers
from Pages import header
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Pages.result import login_require_popup
from Pages.result import add_to_favorite
from Helpers.some_helpers import TESTHelpers



def test_favorite(get_driver):
    result_page = ResultPage(get_driver)
    header_page = HeaderPage(get_driver)
    helper = GeneralHelpers(get_driver)
    helper.go_to_page("https://www.list.am/")
    header_page.change_language
    header_page.click_menu_tab
    favorite_item = result_page.add_to_favorites()
    favorite_item.click()
    result_page.wait_for_page('favorit_item')
    result_page.find_and_click(add_to_favorite)
    assert helper.find(login_require_popup)
    get_driver.quit()
    
    
       





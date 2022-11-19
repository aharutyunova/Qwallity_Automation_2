from Pages.config import base_url
from Pages.result import add_to_favorite
from Pages.result import login_require_popup
from Pages.result import result_item
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Helpers.helpers_page import GeneralHelpers


def test_req_login(get_driver):
    '''Here is represented a method which helps to check if the filtered 
        result matches to the given criterias'''
    result_page = ResultPage(get_driver)
    header_page = HeaderPage(get_driver)
    helpers = GeneralHelpers(get_driver)
    helpers.go_to_page(base_url)
    header_page.select_language()
    header_page.click_menu_tab()
    item = result_page.find(result_item)
    item.click()
    result_page.wait_for_page('item')
    result_page.find_and_click(add_to_favorite)
    assert helpers.find(login_require_popup), "Items is not added to the \
                                           favorites list"                                  
    get_driver.quit()

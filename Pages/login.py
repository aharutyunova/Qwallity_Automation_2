from selenium.webdriver.common.by import By
from Helpers.test_logger import logger
from Helpers.helpers import FunctionLib
from Helpers.environment import config_data

login_require_popup = (By.XPATH, "//a[text()='Login to List.am']")

class LoginPage(FunctionLib):
    class Locator:
        email_field = (By.ID, "_idyour_email")
        pass_field = (By.ID, "_idpassword")
        btn_login = (By.ID, "action__form_action0")
        lbl_account = (By.XPATH, "//*[@id='ma']")

    def login(self):
        self.find_and_send_keys(self.Locator.email_field, config_data["email"])
        self.find_and_send_keys(self.Locator.pass_field, config_data["password"])
        self.find_and_click(self.Locator.btn_login)
        self.wait_for_page('my')
        logger(f"User successfully is logged to the system.")

    def click_myaccount(self):
        self.find_and_click(lbl_account)
        self.wait_for_page('login')
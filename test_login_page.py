
import pytest
import time
from .Pages.login_page import LoginPage, LoginPageLocators
from .Pages.user_profile_page import UserProfilePage, UserProfilePageLocators
from .Modules.email_generator import generate_emails

url = "https://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.critical_path
@pytest.mark.usefixtures("browser")
class TestRegisterLoginLogoffDeleteUser():

    __tmpEmail = generate_emails()[0]
    __tmpPwd = "q12345q12345"

    def test_register_new_user(self, browser):
        page = LoginPage(browser, url)
        page.open()
        page.register_new_user(self.__tmpEmail, self.__tmpPwd)
        time.sleep(1)
        page.should_be_authorized_user()


    def test_log_off(self, browser):
        page = LoginPage(browser, url)
        page.open()
        try:
            assert page.should_be_authorized_user()
        except AssertionError:
            page.log_in(self.__tmpEmail, self.__tmpPwd)
        page.log_off()
        page.should_not_be_authorized_user()

    def test_log_in_from_login_page(self, browser):
        page = LoginPage(browser, url)
        page.open()
        page.log_off()
        page.log_in(self.__tmpEmail, self.__tmpPwd)
        page.should_be_authorized_user()

    def test_delete_user_profile_from_login_page(self, browser):
        page = LoginPage(browser, url)
        page.open()
        try:
            assert page.should_be_authorized_user()
        except AssertionError:
            page.log_in(self.__tmpEmail, self.__tmpPwd)
        page.go_to_user_profile_page()
        page = UserProfilePage(browser)
        page.delete_user_profile()
        page = LoginPage(browser)
        page.log_in(self.__tmpEmail, self.__tmpPwd)
        page.should_not_be_authorized_user()


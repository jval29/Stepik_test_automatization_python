
from .base_page import BasePage
from .locators import LoginPageLocators
from ..Modules.email_generator import generate_emails


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def log_in(self, email=None, pwd=None):
        __pwd, pwd = pwd, None
        try:
            assert self.should_be_login_page(), "\nNo redirection to login page"
        except AssertionError:
            self.go_to_login_page()
        try:
            email, __stored_pwd = self.auth_get_data_json(email)
            if not __pwd:
                __pwd = __stored_pwd
        except KeyError:
            print("\nData not found")
        inputEmail = self.wait_element(*LoginPageLocators.INPUT_LOGIN_EMAIL)
        self.move_n_click(inputEmail)
        self.typing(email)
        inputPwd = self.wait_element(*LoginPageLocators.INPUT_LOGIN_PWD)
        inputPwd.send_keys(__pwd)
        submitButton = self.wait_element(*LoginPageLocators.BUTTON_SUBMIT_LOGIN)
        submitButton.click()
        try:
            assert self.should_be_authorized_user(), "\nUser is still unauthorized"
            return True
        except AssertionError:
            return False

    def register_new_user(self, email=generate_emails()[0], pwd=None):
        __pwd, pwd = pwd, None
        try:
            assert self.should_be_login_page(), "\nNo redirection to login page"
        except AssertionError:
            self.go_to_login_page()
        inputEmail = self.wait_element(*LoginPageLocators.INPUT_REGISTER_EMAIL)
        self.move_n_click(inputEmail)
        self.typing(email)
        inputPwd = self.wait_element(*LoginPageLocators.INPUT_REGISTER_PWD)
        inputPwd.send_keys(__pwd)
        inputPwdConfirm = self.wait_element(*LoginPageLocators.INPUT_REGISTER_PWD_CONFIRM)
        inputPwdConfirm.send_keys(__pwd)
        submitButton = self.wait_element(*LoginPageLocators.BUTTON_SUBMIT_REGISTRATION)
        submitButton.click()
        try:
            self.should_be_authorized_user()
            print("\nCalling auth data update")
            self.auth_update_data_json(email, __pwd)
            return True
        except AssertionError:
            return False

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        return True

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        currentURL = self.browser.current_url
        assert "login" in currentURL, r"There is no /login in current URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "\nLogin form is not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "\nRegister form is nor found"



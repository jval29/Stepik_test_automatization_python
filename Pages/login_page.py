from .base_page import BasePage
from .locators import LoginPageLocators
from ..Modules.email_generator import f_genemail as generate_email


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def register_new_user(self, email=generate_email()[0], password=""):
        try:
            assert self.should_be_login_page(), "No redirection to login page"
        except AssertionError:
            self.go_to_login_page()
        inputEmail = self.wait_element(*LoginPageLocators.INPUT_REGISTER_EMAIL)
        self.move_n_click(inputEmail)
        self.typing(email)
        inputPwd = self.wait_element(*LoginPageLocators.INPUT_REGISTER_PWD)
        inputPwd.send_keys(password)
        inputPwdConfirm = self.wait_element(*LoginPageLocators.INPUT_REGISTER_PWD_CONFIRM)
        inputPwdConfirm.send_keys(password)
        submitButton = self.wait_element(*LoginPageLocators.BUTTON_SUBMIT_REGISTRATION)
        self.move_n_click(submitButton)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        currentURL = self.browser.current_url
        assert "login" in currentURL, r"There is no /login in current URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is nor found"



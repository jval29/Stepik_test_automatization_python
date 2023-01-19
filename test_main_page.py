from selenium.webdriver.common.by import By
import time
import pytest
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestSuit:

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_should_be_login_page(self, browser):
        link = browser.current_url
        page = LoginPage(browser, link)
        page.should_be_login_page()

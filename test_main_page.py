from selenium.webdriver.common.by import By
import time
import pytest
from .Pages.main_page import MainPage, MainPageLocators
from .Pages.login_page import LoginPage, LoginPageLocators
from .Pages.basket_page import BasketPage, BasketPageLocators


@pytest.mark.usefixtures("browser")
class TestLoginSection:

    def test_guest_should_see_login_link(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)
        page.open()
        page.go_to_login_page()

    def test_should_be_login_page(self, browser):
        url = browser.current_url
        page = LoginPage(browser, url)
        page.should_be_login_page()


@pytest.mark.usefixtures("browser")
class TestBasketSection:

    @pytest.mark.new
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser, browser.current_url)
        page.should_be_basket_url()
        page.basket_should_be_empty()
        page.should_be_empty_basket_message()






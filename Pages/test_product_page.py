import pytest
from .product_page import ProductPage, ProductPageLocators
from .login_page import LoginPage, LoginPageLocators
import time
import re

urls = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail(reason="No promo code available")),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"
]


@pytest.mark.usefixtures("browser")
class TestSuit():

    # @pytest.mark.skip()
    @pytest.mark.parametrize("url", urls)
    def test_guest_can_add_product_to_basket(self, browser, url):
        page = ProductPage(browser, url)
        page.open()

        sumInCart = page.wait_element(*ProductPageLocators.AMOUNT_IN_CART_HEADER)
        sumInCart = re.search(r"\d+[.,]\d\d", sumInCart.text)[0]
        prodPrice = page.wait_element(*ProductPageLocators.PRODUCT_PRICE)
        productPrice = re.search(r"\d+[.,]\d\d", prodPrice.text)[0]
        prodName = page.wait_element(*ProductPageLocators.PRODUCT_NAME)
        productName = prodName.text.strip().lower()

        page.add_to_cart()
        time.sleep(0.1)
        page.solve_quiz_and_get_code()
        time.sleep(0.1)
        page.should_be_success_message(productName)
        page.should_be_equal_amount_in_cart(productPrice, sumInCart)
        browser.delete_all_cookies()
        time.sleep(1)

    @pytest.mark.xfail(reason="Should not be passed")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, 1), "Success message is present"
        browser.delete_all_cookies()
        time.sleep(1)

    def test_guest_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, url)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, 1), "Success message is present"
        browser.delete_all_cookies()
        time.sleep(1)

    @pytest.mark.xfail(reason="Should not be passed")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart()
        assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, 4), "Success message is present"
        browser.delete_all_cookies()
        time.sleep(1)

    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()
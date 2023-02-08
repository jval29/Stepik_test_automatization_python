import pytest
from .Pages.product_page import ProductPage, ProductPageLocators
from .Pages.login_page import LoginPage, LoginPageLocators
from .Pages.basket_page import BasketPage, BasketPageLocators
from .Modules.email_generator import f_genemail as generate_email
import time
import re

urls = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail(reason="No promo code available")),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"
]


def get_product_price_and_cart_amount(page):
    sumInCart = page.wait_element(*ProductPageLocators.AMOUNT_IN_CART_HEADER)
    sumInCart = re.search(r"\d+[.,]\d\d", sumInCart.text)[0]
    prodPrice = page.wait_element(*ProductPageLocators.PRODUCT_PRICE)
    productPrice = re.search(r"\d+[.,]\d\d", prodPrice.text)[0]
    return productPrice, sumInCart


@pytest.mark.usefixtures("browser")
class TestBasket():

    @pytest.mark.need_review
    @pytest.mark.parametrize("url", urls)
    def test_guest_can_add_product_to_basket(self, browser, url):
        page = ProductPage(browser, url)
        page.open()

        productPrice, sumInCart = get_product_price_and_cart_amount(page)
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
        page.base_check(page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, 1),
                        "Success message is still present")
        browser.delete_all_cookies()
        time.sleep(1)

    def test_guest_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, url)
        page.open()
        page.base_check(page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, 1),
                        "Success message is still present")
        browser.delete_all_cookies()
        time.sleep(1)

    @pytest.mark.new
    @pytest.mark.xfail(reason="Should not be passed")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart()
        page.base_check(page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, 4),
                        "Success message is not disappeared")
        browser.delete_all_cookies()
        time.sleep(1)


@pytest.mark.usefixtures("browser")
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, url)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser)
        page.should_be_login_page()


@pytest.mark.usefixtures("browser")
class TestBasketFromProductPage():

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser)
        page.should_be_basket_url()
        page.basket_should_be_empty()
        page.should_be_empty_basket_message()


@pytest.mark.usefixtures("browser")
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser)
        email, pwd = generate_email()[0], "q1234q1234"
        page.register_new_user(email, pwd)
        page.should_be_authorized_user()
        time.sleep(1)

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, url)
        page.open()
        page.base_check(page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, 1),
                        "Success message is present")
        browser.delete_all_cookies()
        time.sleep(1)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, url)
        page.open()

        productPrice, sumInCart = get_product_price_and_cart_amount(page)
        prodName = page.wait_element(*ProductPageLocators.PRODUCT_NAME)
        productName = prodName.text.strip().lower()

        page.add_to_cart()
        time.sleep(0.1)
        page.should_be_success_message(productName)
        page.should_be_equal_amount_in_cart(productPrice, sumInCart)
        browser.delete_all_cookies()
        time.sleep(1)

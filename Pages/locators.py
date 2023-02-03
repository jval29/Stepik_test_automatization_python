from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators():
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div#content_inner div.col-sm-6.product_main h1+p")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div#content_inner div.col-sm-6.product_main h1")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input#id_quantity+button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert-success:first-child>div.alertinner")
    AMOUNT_IN_CART_HEADER = (By.CSS_SELECTOR, "div.row div.basket-mini")
    AMOUNT_IN_CART = (By.CSS_SELECTOR, "div#messages div.alert-info>div.alertinner>p>strong")

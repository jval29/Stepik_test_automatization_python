from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOG_OUT_LINK = (By.CSS_SELECTOR, "div.container-fluid a#logout_link")
    CART_LINK = (By.CSS_SELECTOR, ".basket-mini span.btn-group>a.btn[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")


class BasketPageLocators():
    BASKET_CONTENT_FORM = (By.CSS_SELECTOR, "form#basket_formset")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    INPUT_LOGIN_EMAIL = (By.CSS_SELECTOR, "form#login_form input#id_login-username")
    INPUT_LOGIN_PWD = (By.CSS_SELECTOR, "form#login_form input#id_login-password")
    BUTTON_SUBMIT_LOGIN =(By.CSS_SELECTOR, "form#login_form button[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    INPUT_REGISTER_EMAIL = (By.CSS_SELECTOR, "form#register_form input#id_registration-email")
    INPUT_REGISTER_PWD = (By.CSS_SELECTOR, "form#register_form input#id_registration-password1")
    INPUT_REGISTER_PWD_CONFIRM = (By.CSS_SELECTOR, "form#register_form input#id_registration-password2")
    BUTTON_SUBMIT_REGISTRATION = (By.CSS_SELECTOR, "form#register_form button[name='registration_submit']")


class ProductPageLocators():
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div#content_inner div.col-sm-6.product_main h1+p")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div#content_inner div.col-sm-6.product_main h1")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input#id_quantity+button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert-success:first-child>div.alertinner")
    AMOUNT_IN_CART_HEADER = (By.CSS_SELECTOR, "div.row div.basket-mini")
    AMOUNT_IN_CART = (By.CSS_SELECTOR, "div#messages div.alert-info>div.alertinner>p>strong")


class UserProfilePageLocators():
    BUTTON_DELETE_PROFILE = (By.CSS_SELECTOR, "a#delete_profile")
    INPUT_DELETE_PWD_CONFIRM = (By.CSS_SELECTOR, "form#delete_profile_form input#id_password")
    BUTTON_DELETE_PWD_SUBMIT = (By.CSS_SELECTOR, "form#delete_profile_form button.btn-danger[type='submit']")
    CURRENT_EMAIL = (By.CSS_SELECTOR, "table>tbody>tr:nth-child(2)>th+td")

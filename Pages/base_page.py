import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expCond
from selenium.webdriver import ActionChains
from .locators import BasePageLocators
import math


class BasePage():

    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.actChain = ActionChains(browser)

    def go_to_login_page(self, wait=1):
        loginLink = self.wait_element(*BasePageLocators.LOGIN_LINK, wait)
        self.move_n_click(loginLink)

    def go_to_basket_page(self, wait=1):
        cartLink = self.wait_element(*BasePageLocators.CART_LINK, wait)
        self.move_n_click(cartLink)

    def is_element_present(self, by, locator, message="Element is not present", wait=1):
        try:
            self.wait_element(by, locator, wait)
            return True
        except (TimeoutException, NoSuchElementException):
            print(message)
            return False

    def is_not_element_present(self, by, locator, message="Element is still present", wait=1):
        try:
            self.wait_element(by, locator, wait)
            return False
        except (TimeoutException, NoSuchElementException):
            print(message)
            return True

    def is_disappeared(self, by, locator, message="Element is not disappeared", wait=1):
        try:
            WebDriverWait(self.browser, wait, 0.5, TimeoutException).until_not(
                expCond.presence_of_element_located((by, locator)))
            return True
        except TimeoutException:
            print(message)
            return False

    def open(self):
        self.browser.get(self.url)

    def move_n_click(self, element):
        self.actChain.reset_actions()
        self.actChain.move_to_element_with_offset(element, 1, 1).pause(0.05).click()
        self.actChain.perform()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("\nNo second alert presented")

    def typing(self, text_string):
        for symbol in text_string:
            self.actChain.reset_actions()
            self.actChain.key_down(symbol).pause(0.02).key_up(symbol)
            self.actChain.perform()

    def wait_element(self, by, locator, wait=1):
        element = WebDriverWait(self.browser, wait).until(expCond.presence_of_element_located((by, locator)))
        return element



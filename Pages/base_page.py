import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expCond
from selenium.webdriver import ActionChains
from .locators import BasePageLocators
import os
import json
import math

authDataPath = fr"{os.path.dirname(__file__)}\log_in_data.json"


class BasePage():

    def __init__(self, browser, url=None, timeout=None):
        self.browser = browser
        if url:
            self.url = url
        else:
            self.url = browser.current_url
        if timeout:
            self.browser.implicitly_wait(timeout)
        self.actChain = ActionChains(browser)

    def auth_get_data_json(self, email=None, path=authDataPath):
        with open(path, "r") as fileObject:
            logInData = json.load(fileObject)
            if not email:
                email = list(logInData.keys())[-1]
            __pwd = logInData[email]
        return email, __pwd

    def auth_update_data_json(self, email, pwd, path=authDataPath):
        __pwd, pwd = pwd, None
        try:
            with open(path, 'r') as fileObject:
                data = json.load(fileObject)
            data[email] = __pwd
            with open(path, 'w') as fileObject:
                json.dump(data, fileObject, indent=4, sort_keys=False)
                print("\nAuth data was updated")
        except FileNotFoundError:
            data = {email: __pwd}
            with open(path, 'w') as fileObject:
                json.dump(data, fileObject, indent=4, sort_keys=False)
                print("\nJson file log_in_data successfully created")

    def auth_remove_single_data_from_json(self, email=None, path=authDataPath):
        try:
            with open(path, 'r') as fileObject:
                data = json.load(fileObject)
            if email is None:
                email = list(data.keys())[-1]
            data.pop(email)
            with open(path, 'w') as fileObject:
                json.dump(data, fileObject, indent=4, sort_keys=False)
        except FileNotFoundError:
            print("\nFile not found.")
        except IndexError:
            print("\nNo keys in the auth_data.")

    def base_check(self, requiredCondition, message="\nThere is no required condition"):
        assert requiredCondition, message

    def check_document_state(self, timeLimit=10):
        for _ in range(timeLimit*2):
            state = self.browser.execute_script("return document.readyState")
            if state == "complete":
                return True
            time.sleep(0.5)
            print(f"Browser inactivity counter - {_ // 2} sec")

    def go_to_login_page(self, timeout=1):
        loginLink = self.wait_element(*BasePageLocators.LOGIN_LINK, timeout)
        loginLink.click()

    def go_to_basket_page(self, timeout=1):
        cartLink = self.wait_element(*BasePageLocators.CART_LINK, timeout)
        cartLink.click()

    def go_to_user_profile_page(self, timeout=1):
        userProfileLink = self.wait_element(*BasePageLocators.USER_ICON, timeout)
        userProfileLink.click()

    def is_element_present(self, by, locator, timeout=1):
        self.check_document_state()
        try:
            self.wait_element(by, locator, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_not_element_present(self, by, locator, timeout=1):
        self.check_document_state()
        try:
            self.wait_element(by, locator, timeout)
            return False
        except (TimeoutException, NoSuchElementException):
            return True

    def is_disappeared(self, by, locator, timeout=1):
        self.check_document_state()
        try:
            WebDriverWait(self.browser, timeout, 0.5, [TimeoutException]).until_not(
                expCond.presence_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

    def log_off(self):
        try:
            self.should_be_authorized_user()
            logOutLink = self.wait_element(*BasePageLocators.LOG_OUT_LINK)
            logOutLink.click()
            assert self.is_not_element_present(*BasePageLocators.USER_ICON), "\nLog off failed"
        except AssertionError:
            print("\nTrying to log off from unauthorized session")

    def move_n_click(self, element):
        self.actChain.reset_actions()
        self.actChain.move_to_element_with_offset(element, 1, 1).pause(0.05).click()
        self.actChain.perform()

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON, 8), "\nUser icon is not presented," \
                                                                     " probably unauthorised user"
        return True

    def should_not_be_authorized_user(self):
        assert self.is_not_element_present(*BasePageLocators.USER_ICON, 8), "\nUser icon is presented," \
                                                                     " probably authorised user"
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "\nLogin link is not presented"
        return True

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

    def wait_element(self, by, locator, timeout=3):
        self.check_document_state()
        element = WebDriverWait(self.browser, timeout).until(expCond.presence_of_element_located((by, locator)))
        return element

    def wait_elements(self, by, locator, timeout=3):
        self.check_document_state()
        elements = WebDriverWait(self.browser, timeout).until(expCond.presence_of_all_elements_located((by, locator)))
        return elements



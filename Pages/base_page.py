from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expCond
from selenium.webdriver import ActionChains
import math


class BasePage():

    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.actChain = ActionChains(browser)

    def open(self):
        self.browser.get(self.url)

    def move_n_click(self, element):
        self.actChain.move_to_element(element).pause(0.05).click()
        self.actChain.perform()

    def wait_element(self, by, locator, wait=3):
        element = WebDriverWait(self.browser, wait).until(expCond.presence_of_element_located((by, locator)))
        return element

    def is_element_present(self, by, locator):
        try:
            self.wait_element(by, locator)
        except (TimeoutException, NoSuchElementException):
            return False
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


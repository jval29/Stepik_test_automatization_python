from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expCond


class BasePage():

    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, locator):
        try:
            WebDriverWait(self.browser, 3).until(expCond.presence_of_element_located((by, locator)))
        except (TimeoutException, NoSuchElementException):
            return False
        return True


from selenium.webdriver.common.by import By
import time
import pytest

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


@pytest.mark.usefixtures("browser")
class TestSuit:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link) 
        go_to_login_page(browser)
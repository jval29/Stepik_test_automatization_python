from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
import time
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="choose browser name")
    parser.addoption("--language", action="store", default="en", help="choose the language: en / ru / de ....etc")
    parser.addoption("--headless", action="store", default="off", help="turn on / off browser UI")


@pytest.fixture(scope="class")
def browser(request):  # collecting initial options for selenium driver(browser)
    browserName = request.config.getoption("browser_name").lower().strip()
    userLanguage = request.config.getoption("language").lower().strip()
    headlessOption = request.config.getoption("headless").lower().strip()

    if browserName == "chrome" or browserName != "firefox":
        options = chromeOptions()
        options.add_experimental_option("prefs", {"intl.accept_languages": userLanguage})
        options.add_argument("--start-maximized")
        if headlessOption == "on":
            options.add_argument("--headless")
        webDriver = webdriver.Chrome(options=options)
    elif browserName == "firefox":
        options = firefoxOptions()
        options.set_preference("intl.accept_languages", userLanguage)
        webDriver = webdriver.Firefox(options=options)

    webDriver.maximize_window()
    yield webDriver

    time.sleep(1)
    print("\nTests ending")
    webDriver.quit()


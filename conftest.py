import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("/tests_drivers/chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()
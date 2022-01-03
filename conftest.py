import pytest
from selenium import webdriver

# Фикстура финализатор
# После завершения теста, который вызывал фикстуру,
# выполнение фикстуры продолжится со строки, следующей за строкой со словом yield
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("/tests_drivers/chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()


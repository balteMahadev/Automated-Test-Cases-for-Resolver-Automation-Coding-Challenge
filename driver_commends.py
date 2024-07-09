import pytest
from selenium import webdriver


class WebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()


@pytest.fixture
def browser():
    driver = WebDriver()
    yield driver.get_driver()
    driver.quit_driver()

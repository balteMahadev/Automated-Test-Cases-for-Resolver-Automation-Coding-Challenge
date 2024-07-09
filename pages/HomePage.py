import os
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = f"{os.getcwd() + os.path.sep}QE-index.html"

    email_input_loc = (By.ID, "inputEmail")
    password_input_loc = (By.ID, "inputPassword")
    signin_button_loc = (By.XPATH, "//button[text()='Sign in']")
    home_page_loc = (By.XPATH, "//a[text()='Home ']")
    test2_list_items_values_loc = (By.XPATH, "//h1[text()='Test 2']/following-sibling::ul/li/span")
    test2_list_items_loc = (By.XPATH, "//h1[text()='Test 2']/following-sibling::ul/li")
    test3_option_dropdown_loc = (By.XPATH, "//button[@id='dropdownMenuButton']")
    test3_option_dropdown_elements_loc = (By.XPATH, "//div[@aria-labelledby='dropdownMenuButton']/a")
    test4_button_loc = (By.XPATH, "//button[text()='Button']")
    test5_button_loc = (By.ID, "test5-button")
    test5_alert_message_loc = (By.ID, "test5-alert")

    # path
    test6_grid_coordinates = (By.XPATH, "//table/tbody/tr[{}]/td[{}]")

    @property
    def home_page(self):
        return self.driver.find_element(*self.home_page_loc)

    @property
    def test5_alert_message(self):
        return self.driver.find_element(*self.test5_alert_message_loc)

    @property
    def test5_button(self):
        return self.driver.find_element(*self.test5_button_loc)

    @property
    def test4_first_button(self):
        return self.driver.find_elements(*self.test4_button_loc)[0]

    @property
    def test4_second_button(self):
        return self.driver.find_elements(*self.test4_button_loc)[1]

    @property
    def test3_third_option(self):
        return self.driver.find_elements(*self.test3_option_dropdown_elements_loc)[2]

    @property
    def test3_option_dropdown(self):
        return self.driver.find_element(*self.test3_option_dropdown_loc)

    @property
    def test2_list_items_values(self):
        return self.driver.find_elements(*self.test2_list_items_values_loc)

    @property
    def test2_second_list_item_bridge_value(self):
        return self.driver.find_elements(*self.test2_list_items_values_loc)[1]

    @property
    def test2_second_list_item(self):
        return self.driver.find_elements(*self.test2_list_items_loc)[1]

    @property
    def email_input(self):
        return self.driver.find_element(*self.email_input_loc)

    @property
    def password_input(self):
        return self.driver.find_element(*self.password_input_loc)

    @property
    def signin_button(self):
        return self.driver.find_element(*self.signin_button_loc)

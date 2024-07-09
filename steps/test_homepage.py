from pytest_bdd import scenarios, when, then, parsers, given
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage

scenarios('../features/HomePage.feature')

@given('the Home page is loaded')
def user_on_home_page(browser):
    assert browser.title == 'Home'

@when(parsers.parse(
    "the user gets the value from the cell at coordinates {row:d}, {col:d} on Home page for element {loc:w}"),
      target_fixture="cell_value")
def find_cell_value(browser, row, col, loc):
    page = HomePage(browser)
    xpath = getattr(page, loc)[1].format(row + 1, col + 1)
    cell_value = browser.find_element(By.XPATH, xpath).text
    return cell_value

@then(parsers.parse("the value should be {value:w}"))
def validate_cell_value(cell_value, value):
    assert cell_value == value

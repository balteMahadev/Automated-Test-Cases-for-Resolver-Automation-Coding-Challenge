from driver_commends import browser
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import when, then, parsers, given
from selenium.webdriver.support.wait import WebDriverWait
from pages.HomePage import HomePage

PAGES = {
    "Home": HomePage,
}


@given(parsers.parse('the user loads {page_name:w} page'))
def user_on_home_page(browser, page_name):
    page_class = PAGES[page_name]
    page = page_class(browser)
    page_url = getattr(page, "url")
    browser.get(page_url)


@when(parsers.parse('the {element:w} is displayed on {page_name:w} page'))
def check_element_is_displayed(browser, element, page_name):
    page_class = PAGES[page_name]
    page = page_class(browser)
    ele = getattr(page, element)
    assert ele.is_displayed()


@when(parsers.parse('the {page_name:w} page contains {count:d} {element_name:w} elements'))
def check_count_of_elements(browser, page_name, count, element_name):
    page_class = PAGES[page_name]
    page = page_class(browser)
    element_count = getattr(page, element_name)
    assert len(element_count) == count


@when(parsers.parse('the user scrolls until {element:w} element is visible on the {page_name:w} page'))
def user_scroll_to_the_element(browser, element, page_name):
    page_class = PAGES[page_name]
    page = page_class(browser)
    ele = getattr(page, element)
    browser.execute_script("arguments[0].scrollIntoView(true)", ele)


@when(parsers.parse('the user waits until {locator:w} element is clickable on the {page_name:w} page'))
def user_waits_until_element_is_clickable(browser, locator, page_name):
    page_class = PAGES[page_name]
    page = page_class(browser)
    loc = getattr(page, f"{locator}_loc")
    wait = WebDriverWait(browser, 20)
    element = wait.until(EC.element_to_be_clickable(loc))
    element.click()


@when(parsers.parse('the {element_name:w} text on the {page_name:w} page matches: {text}'))
@then(parsers.parse('the {element_name:w} text on the {page_name:w} page matches: {text}'))
def element_matches_text(browser, element_name, page_name, text):
    page_class = PAGES[page_name]
    page = page_class(browser)
    element = getattr(page, element_name)
    assert str(text) in element.text


@when(parsers.parse('the user clicks on {element_name:w} on {page_name:w} page'))
@then(parsers.parse('the user clicks on {element_name:w} on {page_name:w} page'))
def click_element(browser, element_name, page_name):
    page_class = PAGES[page_name]
    page = page_class(browser)
    element = getattr(page, element_name)
    element.click()


@then(parsers.parse('the user fills {element:w} field on {page_name:w} page with {value}'))
def enter_valid_credentials(browser, element, page_name, value):
    page_class = PAGES[page_name]
    page = page_class(browser)
    ele = getattr(page, element)
    ele.send_keys(value)


@then(
    parsers.parse('the user verifies that the {element:w} element on the {page_name:w} page is: {enable_or_disable:w}'))
def check_element_is_enable_or_disable(browser, element, page_name, enable_or_disable):
    page_class = PAGES[page_name]
    page = page_class(browser)
    ele = getattr(page, element)
    assert ele.is_enabled() if enable_or_disable == 'enable' else not ele.is_enabled()

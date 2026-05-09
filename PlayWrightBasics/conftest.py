import pytest
from playwright.sync_api import Playwright
from pygments.lexer import default


@pytest.fixture(scope='session')
def user_credentials(request):
    return request.param


# access local variable


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default="chrome", help="browser selection"
    )
@pytest.fixture
def browser_instance(playwright: Playwright, request):
    browser_option = request.config.getoption("browser_name")
    if browser_option == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    elif browser_option == 'firefox':
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

# access global variable

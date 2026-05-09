import time

from playwright.sync_api import Page, Playwright, expect
from pytest_playwright.pytest_playwright import page

from APIUtils import APIUtils

fakePlayloadRespons = {"data":[],"message":"No Orders"}

def intercept_and_send_fake_data(route):
    route.fulfill(
        json=fakePlayloadRespons
    )
def intercept_order_url(route):
    route.continue_(
        url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69fdc8e6e83610b531d20f7f"
    )
def test_network_intercept_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_and_send_fake_data)
    page.locator("#userEmail").fill("")
    page.locator("#userPassword").fill("")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    error_message = page.locator(".mt-4").text_content()
    print(error_message)

def test_network_intercept_2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_order_url)
    page.locator("#userEmail").fill("")
    page.locator("#userPassword").fill("")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role('button', name = 'View').first.click()
    time.sleep(5)
    print(page.locator('.blink_me').text_content())

def test_session_storage(playwright:Playwright):
    api_util = APIUtils()
    token = api_util.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("69fdcd76e83610b531d21bf3")).to_be_visible()

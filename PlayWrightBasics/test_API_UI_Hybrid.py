from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from APIUtils import APIUtils


def test_wb_api_e2e(playwright:Playwright):
    # create order
    api_Util = APIUtils()
    orderId = api_Util.create_order(playwright)
    print("Oder Id : "+ orderId)
    # login to web
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("")
    page.locator("#userPassword").fill("")
    page.locator("#login").click()
    # Go to order history page and verify the order
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text(orderId)).to_be_visible()
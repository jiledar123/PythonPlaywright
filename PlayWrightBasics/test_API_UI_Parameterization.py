import json

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from APIUtils import APIUtils
from page_objects.LoginPage import LoginPage

with open("data/credentials.json") as f:
    user_data = json.load(f)
    print(user_data)
    user_credential_list = user_data["user_credentials"]
@pytest.mark.parametrize("user_credentials",user_credential_list)
def test_wb_api_e2e(playwright:Playwright,user_credentials,browser_instance):
    # create order
    api_Util = APIUtils()
    orderId = api_Util.create_order(playwright,user_credentials)
    print("Oder Id : "+ orderId)
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    dashboard_page = login_page.login(user_credentials)
    order_history_page = dashboard_page.navigation_link()
    order_history_page.verify_order_id(orderId)
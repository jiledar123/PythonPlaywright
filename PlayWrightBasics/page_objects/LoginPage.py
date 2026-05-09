from page_objects.DashboardPage import DashboardPage


class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")
    def login(self,user_credentials):
        self.page.locator("#userEmail").fill(user_credentials["userEmail"])
        self.page.locator("#userPassword").fill(user_credentials["userPassword"])
        self.page.locator("#login").click()
        return DashboardPage(self.page)
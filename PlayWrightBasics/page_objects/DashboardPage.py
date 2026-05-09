from page_objects.OrderHistoryPage import OrderHistoryPage


class DashboardPage:
    def __init__(self,page):
        self.page = page
    def navigation_link(self):
        self.page.get_by_role("button", name="ORDERS").click()
        return OrderHistoryPage(self.page)
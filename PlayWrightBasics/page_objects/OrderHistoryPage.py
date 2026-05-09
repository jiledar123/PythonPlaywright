from playwright.sync_api import expect


class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def verify_order_id(self, orderId):
        expect(self.page.get_by_text(orderId)).to_be_visible()

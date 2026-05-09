from playwright.sync_api import Playwright
payload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}
class APIUtils:
    def get_token(self,playwright:Playwright,user_credentials):
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response_object = request_context.post(url="/api/ecom/auth/login",
                                               headers={"content-type":"application/json"},
                                               data={"userEmail": user_credentials["userEmail"], "userPassword": user_credentials["userPassword"]})
        assert  response_object.ok
        print(response_object.json())
        return response_object.json()["token"]
    def create_order(self,playwright:Playwright,user_credentials):
        token = self.get_token(playwright,user_credentials)
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response_object = request_context.post(url="/api/ecom/order/create-order",
                             headers={"content-type":"application/json","authorization":token},
                             data=payload)
        print(response_object.json())
        order_ids = response_object.json()['orders']
        return order_ids[0]
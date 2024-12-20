from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart = page.locator('#shopping_cart_container')
        self.first_item_button = page.locator(".inventory_item").nth(0).locator(".btn_inventory")
        self.second_item_button = page.locator(".inventory_item").nth(1).locator(".btn_inventory")


    def get_first_item_name(self):
        return self.page.locator(".inventory_item_name").nth(0).inner_text()


    def get_first_item_price(self):
        price_text = self.page.locator(".inventory_item_price").nth(0).inner_text()
        return float(price_text[1:])


    def get_second_item_name(self):
        return self.page.locator(".inventory_item_name").nth(1).inner_text()


    def get_second_item_price(self):
        price_text = self.page.locator(".inventory_item_price").nth(1).inner_text()
        return float(price_text[1:])


    def add_first_item_to_shopping_cart(self):
        self.first_item_button.click()


    def add_second_item_to_shopping_cart(self):
        self.second_item_button.click()


    def load_shopping_cart(self):
        self.shopping_cart.click()
        self.page.wait_for_load_state("networkidle")
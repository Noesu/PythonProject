from playwright.sync_api import Page


class ShoppingCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.continue_shopping_button = page.locator('#continue-shopping')
        self.checkout_button = page.locator('#checkout')


    def get_items_count(self):
        first_item_count = int(self.page.locator('.cart_list .cart_quantity').nth(0).inner_text())
        second_item_count = int(self.page.locator('.cart_list .cart_quantity').nth(1).inner_text())
        return first_item_count + second_item_count


    def get_items_names(self):
        return [
            self.page.locator('.inventory_item_name').nth(0).inner_text(),
            self.page.locator('.inventory_item_name').nth(1).inner_text()
        ]


    def get_items_prices(self):
        return [
            float(self.page.locator('.inventory_item_price').nth(0).inner_text()[1:]),
            float(self.page.locator('.inventory_item_price').nth(1).inner_text()[1:])
        ]


    def return_to_inventory(self):
        self.continue_shopping_button.click()


    def proceed_to_checkout(self):
        self.checkout_button.click()

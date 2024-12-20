from playwright.sync_api import Page


class CheckoutPage2:
    def __init__(self, page: Page):
        self.page = page

        self.first_item = page.locator('.inventory_item_name').nth(0)
        self.first_item_price = page.locator('.inventory_item_price').nth(0)
        self.second_item = page.locator('.inventory_item_name').nth(1)
        self.second_item_price = page.locator('.inventory_item_price').nth(1)

        self.summary_subtotal = page.locator('.summary_subtotal_label')
        self.summary_tax = page.locator('.summary_tax_label')
        self.summary_total = page.locator('.summary_total_label')

        self.cancel_checkout_button = page.locator('#cancel')
        self.finish_button = page.locator('#finish')


    def get_items_names(self):
        return [
            self.first_item.inner_text(),
            self.second_item.inner_text()
        ]


    def get_items_prices(self):
        return [
            float(self.first_item_price.inner_text()[1:]),
            float(self.second_item_price.inner_text()[1:])
        ]


    def get_subtotal_price(self):
        return float(self.summary_subtotal.inner_text().split(sep='$')[1])


    def get_summary_tax(self):
        return float(self.summary_tax.inner_text().split(sep='$')[1])


    def get_total_price(self):
        return float(self.summary_total.inner_text().split(sep='$')[1])


    def cancel_checkout(self):
        self.cancel_checkout_button.click()


    def proceed_to_finish(self):
        self.finish_button.click()
from playwright.sync_api import Page


class CheckoutPage1:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator('#first-name')
        self.last_name_input = page.locator('#last-name')
        self.zip_input = page.locator('#postal-code')
        self.back_to_cart_button = page.locator('#cancel')
        self.continue_button = page.locator('#continue')
        self.error_message = page.locator('.error-message-container.error')


    def get_error_message(self):
        return self.error_message.inner_text()


    def enter_first_name(self, first_name):
        self.first_name_input.fill(first_name)


    def enter_last_name(self, last_name):
        self.last_name_input.fill(last_name)


    def enter_postal_code(self, postal_code):
        self.zip_input.fill(postal_code)


    def proceed_to_continue(self):
        self.continue_button.click()


    def back_to_cart(self):
        self.back_to_cart_button.click()
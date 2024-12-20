from playwright.sync_api import Page


class FinishPage:
    def __init__(self, page: Page):
        self.page = page
        self.complete_text = page.locator('.complete-text')
        self.burger_button = page.locator('#react-burger-menu-btn')
        self.logout = page.locator('#logout_sidebar_link')


    def open_sidebar(self):
        self.burger_button.click()
        self.page.wait_for_selector('#logout_sidebar_link', state='visible')


    def proceed_to_logout(self):
        self.logout.click()

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login-button')
        self.error_message = page.locator('.error-message-container.error')


    def load_page(self, link):
        self.page.goto(link)


    def login(self, username, password):
        if username:
            self.username_input.fill(username)
        if password:
            self.password_input.fill(password)
        self.login_button.click()


    def get_error_message(self):
        return self.error_message.inner_text()
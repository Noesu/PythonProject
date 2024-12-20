from config import Config

class BasePage:
    def __init__(self, page):
        self.page = page

    #  Request for loading page and check for correct load
    def navigate_and_verify(self, expected_suffix):
        self.page.goto(Config.WEBSITE_LINK + expected_suffix)
        assert self.page.url.endswith(expected_suffix), f"The page URL does not contain '{expected_suffix}'."

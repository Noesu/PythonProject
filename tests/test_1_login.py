import pytest

from config import Config
from pages.login_page import LoginPage


@pytest.mark.auth
@pytest.mark.parametrize("username, password, login_successful", [
    (Config.USER_NAME, Config.PASSWORD, True),
    (Config.INVALID_USERNAME, Config.PASSWORD, False),
    (Config.USER_NAME, Config.INVALID_PASSWORD, False),
    (Config.USER_NAME, None, False),
    (None, Config.PASSWORD, False),
])
def test_login(fresh_context_args, page, username, password, login_successful):
    login_page = LoginPage(page)
    login_page.load_page(Config.WEBSITE_LINK)
    login_page.login(username, password)
    if not login_successful:
        assert 'Epic sadface' in login_page.get_error_message(), 'Error message not displayed'
    else:
        assert page.url.endswith(Config.INVENTORY_LINK), f"The page URL does not contain '{Config.INVENTORY_LINK}'."


@pytest.mark.auth
@pytest.mark.parametrize("page_link", [
    Config.INVENTORY_LINK,
    Config.CART_LINK,
    Config.CHECKOUT_LINK1,
    Config.CHECKOUT_LINK2,
    Config.FINISH_LINK,
])
def test_unauthorized_access(fresh_context_args, page, page_link):
    login_page = LoginPage(page)
    login_page.load_page(Config.WEBSITE_LINK + page_link)
    assert login_page.get_error_message() == f"Epic sadface: You can only access '/{page_link}' when you are logged in."

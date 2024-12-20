import pytest

from config import Config
from pages.inventory_page import InventoryPage


@pytest.fixture(scope="function")
def fresh_context_args(browser_context_args):
    return browser_context_args


@pytest.fixture(scope="session")
def saved_cart_data():
    return {
        "cart_item_names": [],
        "cart_item_prices": [],
    }

@pytest.fixture(scope="function")
def prepare_cart_with_items(page):
    page.goto(Config.WEBSITE_LINK + Config.INVENTORY_LINK)
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_shopping_cart()
    inventory_page.add_second_item_to_shopping_cart()
    page.context.storage_state(path="auth.json")


@pytest.fixture(scope="function")
def authenticated_context(page):
    page.goto(Config.WEBSITE_LINK)
    page.fill("#user-name", Config.USER_NAME)
    page.fill("#password", Config.PASSWORD)
    page.click("#login-button")
    return page.context
from base_page import BasePage
from config import Config
from pages.shopping_cart_page import ShoppingCartPage


def test_correct_items_count_in_shopping_cart(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CART_LINK)

    cart_page = ShoppingCartPage(page)
    assert cart_page.get_items_count() == 2, "Wrong items count in shopping cart"


def test_correct_items_names_in_shopping_cart(authenticated_context, prepare_cart_with_items, saved_cart_data, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CART_LINK)

    cart_page = ShoppingCartPage(page)
    assert cart_page.get_items_names() == saved_cart_data["cart_item_names"], "Cart item names do not match saved data."


def test_correct_items_prices_in_shopping_cart(authenticated_context, prepare_cart_with_items, saved_cart_data, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CART_LINK)

    cart_page = ShoppingCartPage(page)
    assert cart_page.get_items_prices() == saved_cart_data["cart_item_prices"], "Cart items price do not match saved data."


def test_return_to_inventory(authenticated_context, prepare_cart_with_items, saved_cart_data, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CART_LINK)

    cart_page = ShoppingCartPage(page)
    cart_page.return_to_inventory()
    assert page.url.endswith(Config.INVENTORY_LINK), f"The page URL does not contain '{Config.INVENTORY_LINK}'."


def test_checkout(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CART_LINK)

    cart_page = ShoppingCartPage(page)
    cart_page.proceed_to_checkout()
    assert page.url.endswith(Config.CHECKOUT_LINK1), f"The page URL does not contain '{Config.CHECKOUT_LINK1}'."

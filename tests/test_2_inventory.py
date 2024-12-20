from base_page import BasePage
from config import Config
from pages.inventory_page import InventoryPage



def test_add_items_to_shopping_cart(authenticated_context, saved_cart_data, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.INVENTORY_LINK)

    inventory_page = InventoryPage(page)

    #  Load names and prices for first two items and store it to fixture
    first_item_name = inventory_page.get_first_item_name()
    first_item_price = inventory_page.get_first_item_price()
    second_item_name = inventory_page.get_second_item_name()
    second_item_price = inventory_page.get_second_item_price()
    saved_cart_data["cart_item_names"] = [first_item_name, second_item_name]
    saved_cart_data["cart_item_prices"] = [first_item_price, second_item_price]

    inventory_page.add_first_item_to_shopping_cart()
    inventory_page.add_second_item_to_shopping_cart()

    inventory_page.load_shopping_cart()
    assert page.url.endswith(Config.CART_LINK), f"The page URL does not contain '{Config.CART_LINK}'."

from base_page import BasePage
from config import Config
from pages.checkout_page2 import CheckoutPage2
from pages.finish_page import FinishPage


def test_correct_items_names_on_checkout_page(authenticated_context, prepare_cart_with_items, saved_cart_data, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK2)

    checkout_page = CheckoutPage2(page)
    assert checkout_page.get_items_names() == saved_cart_data["cart_item_names"], "Checkout item names do not match saved data."


def test_correct_items_prices_on_checkout_page(authenticated_context, prepare_cart_with_items, saved_cart_data, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK2)

    checkout_page = CheckoutPage2(page)
    assert checkout_page.get_items_prices() == saved_cart_data["cart_item_prices"], "Checkout item prices do not match saved data."


def test_correct_subtotal_price(authenticated_context, prepare_cart_with_items, saved_cart_data, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK2)

    checkout_page = CheckoutPage2(page)
    assert checkout_page.get_subtotal_price() == sum(saved_cart_data["cart_item_prices"])


def test_correct_tax_calculation(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK2)

    checkout_page = CheckoutPage2(page)
    assert checkout_page.get_subtotal_price() * Config.TAX <= checkout_page.get_summary_tax()


def test_correct_total_calculation(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK2)

    checkout_page = CheckoutPage2(page)
    assert checkout_page.get_total_price() == checkout_page.get_subtotal_price() + checkout_page.get_summary_tax()


def test_cancel_checkout(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK2)

    checkout_page = CheckoutPage2(page)
    checkout_page.cancel_checkout()
    assert page.url.endswith(Config.INVENTORY_LINK), f"The page URL does not contain '{Config.INVENTORY_LINK}'."


def test_finish(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK2)

    checkout_page = CheckoutPage2(page)
    checkout_page.proceed_to_finish()
    assert page.url.endswith(Config.FINISH_LINK), f"The page URL does not contain '{Config.FINISH_LINK}'."

    finish_page = FinishPage(page)
    assert finish_page.complete_text.inner_text() == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'


def test_logout(authenticated_context, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.FINISH_LINK)

    finish_page = FinishPage(page)
    finish_page.open_sidebar()
    finish_page.proceed_to_logout()
    assert page.url == Config.WEBSITE_LINK

    page.goto(Config.WEBSITE_LINK + Config.FINISH_LINK)
    assert page.url == Config.WEBSITE_LINK

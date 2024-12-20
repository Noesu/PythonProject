from base_page import BasePage
from config import Config
from pages.checkout_page1 import CheckoutPage1


def test_continue_without_user_data(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK1)

    checkout_page = CheckoutPage1(page)
    checkout_page.proceed_to_continue()
    assert checkout_page.get_error_message() == 'Error: First Name is required'


def test_continue_with_only_first_name(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK1)

    checkout_page = CheckoutPage1(page)
    checkout_page.enter_first_name(Config.FIRST_NAME)
    checkout_page.proceed_to_continue()
    assert checkout_page.get_error_message() == 'Error: Last Name is required'


def test_continue_with_only_first_name_and_last_name(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK1)

    checkout_page = CheckoutPage1(page)
    checkout_page.enter_first_name(Config.FIRST_NAME)
    checkout_page.enter_last_name(Config.LAST_NAME)
    checkout_page.proceed_to_continue()
    assert checkout_page.get_error_message() == 'Error: Postal Code is required'


def test_continue_with_all_required_user_data(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK1)

    checkout_page = CheckoutPage1(page)
    checkout_page.enter_first_name(Config.FIRST_NAME)
    checkout_page.enter_last_name(Config.LAST_NAME)
    checkout_page.enter_postal_code(Config.ZIP_CODE)
    checkout_page.proceed_to_continue()
    assert page.url.endswith(Config.CHECKOUT_LINK2  ), f"The page URL does not contain '{Config.CHECKOUT_LINK2}'."


def test_cancel_button(authenticated_context, prepare_cart_with_items, page):
    base_page = BasePage(page)
    base_page.navigate_and_verify(Config.CHECKOUT_LINK1)

    checkout_page = CheckoutPage1(page)
    checkout_page.back_to_cart()
    assert page.url.endswith(Config.CART_LINK), f"The page URL does not contain '{Config.CART_LINK}'."

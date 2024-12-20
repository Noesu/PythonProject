import os

class Config:
    USER_NAME = os.environ.get("USER_NAME")
    INVALID_USERNAME = os.environ.get("INVALID_USERNAME")
    PASSWORD = os.environ.get("PASSWORD")
    INVALID_PASSWORD = os.environ.get("INVALID_PASSWORD")

    WEBSITE_LINK = os.environ.get("WEBSITE_LINK")
    INVENTORY_LINK = os.environ.get("INVENTORY_LINK")
    CART_LINK = os.environ.get("CART_LINK")
    CHECKOUT_LINK1 = os.environ.get("CHECKOUT_LINK1")
    CHECKOUT_LINK2 = os.environ.get("CHECKOUT_LINK2")
    FINISH_LINK = os.environ.get("FINISH_LINK")

    FIRST_NAME = os.environ.get("FIRST_NAME")
    LAST_NAME = os.environ.get("LAST_NAME")
    ZIP_CODE = os.environ.get("ZIP_CODE")
    TAX = float(os.environ.get("TAX"))
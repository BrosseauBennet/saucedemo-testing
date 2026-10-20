import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def inventory_page(page: Page, login_page: LoginPage) -> InventoryPage:
    login_page.login("standard_user")
    return InventoryPage(page)


@pytest.fixture
def checkout_page(page: Page, inventory_page: InventoryPage) -> CheckoutPage:
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    CartPage(page).start_checkout()
    return CheckoutPage(page)
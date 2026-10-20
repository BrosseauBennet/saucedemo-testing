from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_add_item_updates_cart_badge(inventory_page: InventoryPage):
    inventory_page.add_to_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


def test_remove_item_clears_cart_badge(inventory_page: InventoryPage):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.remove_from_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_count(0)


def test_cart_page_lists_added_item(page: Page, inventory_page: InventoryPage):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    expect(CartPage(page).item_names).to_have_text("Sauce Labs Backpack")
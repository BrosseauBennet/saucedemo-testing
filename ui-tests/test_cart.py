from playwright.sync_api import Page, expect


def test_add_item_updates_cart_badge(logged_in_page: Page):
    page = logged_in_page
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")


def test_remove_item_clears_cart_badge(logged_in_page: Page):
    page = logged_in_page
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("[data-test='remove-sauce-labs-backpack']")
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_count(0)


def test_cart_page_lists_added_item(logged_in_page: Page):
    page = logged_in_page
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("[data-test='shopping-cart-link']")
    expect(page.locator(".cart_list .inventory_item_name")).to_have_text(
        "Sauce Labs Backpack")
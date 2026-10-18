from playwright.sync_api import Page, expect


def start_checkout(page: Page):
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("[data-test='shopping-cart-link']")
    page.click("[data-test='checkout']")


def test_complete_checkout(logged_in_page: Page):
    page = logged_in_page
    start_checkout(page)
    page.fill("[data-test='firstName']", "Test")
    page.fill("[data-test='lastName']", "User")
    page.fill("[data-test='postalCode']", "12345")
    page.click("[data-test='continue']")
    page.click("[data-test='finish']")
    expect(page.locator("[data-test='complete-header']")).to_have_text(
        "Thank you for your order!"
    )


def test_checkout_requires_first_name(logged_in_page: Page):
    page = logged_in_page
    start_checkout(page)
    page.fill("[data-test='lastName']", "User")
    page.fill("[data-test='postalCode']", "12345")
    page.click("[data-test='continue']")
    expect(page.locator("[data-test='error']")).to_contain_text(
        "First Name is required"
    )
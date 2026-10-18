from playwright.sync_api import expect

from pages.checkout_page import CheckoutPage


def test_complete_checkout(checkout_page: CheckoutPage):
    checkout_page.fill_info("Test", "User", "12345")
    checkout_page.continue_to_overview()
    checkout_page.finish()
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")


def test_checkout_requires_first_name(checkout_page: CheckoutPage):
    checkout_page.fill_info("", "User", "12345")
    checkout_page.continue_to_overview()
    expect(checkout_page.error).to_contain_text("First Name is required")
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"


def test_standard_user_can_log_in(page: Page):
    page.goto(BASE_URL)
    page.fill("[data-test='username']", "standard_user")
    page.fill("[data-test='password']", "secret_sauce")
    page.click("[data-test='login-button']")
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_locked_out_user_sees_error(page: Page):
    page.goto(BASE_URL)
    page.fill("[data-test='username']", "locked_out_user")
    page.fill("[data-test='password']", "secret_sauce")
    page.click("[data-test='login-button']")
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")
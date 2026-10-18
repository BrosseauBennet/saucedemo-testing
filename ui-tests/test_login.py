from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import BASE_URL, LoginPage


def test_standard_user_can_log_in(page: Page, login_page: LoginPage):
    login_page.login("standard_user")
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(InventoryPage(page).title).to_have_text("Products")


def test_locked_out_user_sees_error(login_page: LoginPage):
    login_page.login("locked_out_user")
    expect(login_page.error).to_contain_text("locked out")
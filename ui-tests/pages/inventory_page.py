from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_to_cart(self, item: str):
        self.page.click(f"[data-test='add-to-cart-{item}']")

    def remove_from_cart(self, item: str):
        self.page.click(f"[data-test='remove-{item}']")

    def open_cart(self):
        self.cart_link.click()
from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str = "secret_sauce"):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
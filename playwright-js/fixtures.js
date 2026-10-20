const base = require('@playwright/test');
const { LoginPage } = require('./pages/LoginPage');
const { InventoryPage } = require('./pages/InventoryPage');
const { CartPage } = require('./pages/CartPage');
const { CheckoutPage } = require('./pages/CheckoutPage');

const test = base.test.extend({
  loginPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await loginPage.open();
    await use(loginPage);
  },

  inventoryPage: async ({ page, loginPage }, use) => {
    await loginPage.login('standard_user');
    await use(new InventoryPage(page));
  },

  checkoutPage: async ({ page, inventoryPage }, use) => {
    await inventoryPage.addToCart('sauce-labs-backpack');
    await inventoryPage.openCart();
    await new CartPage(page).startCheckout();
    await use(new CheckoutPage(page));
  },
});

module.exports = { test, expect: base.expect };
const { test, expect } = require('../fixtures');
const { CartPage } = require('../pages/CartPage');

test('adding an item updates the cart badge', async ({ inventoryPage }) => {
  await inventoryPage.addToCart('sauce-labs-backpack');
  await expect(inventoryPage.cartBadge).toHaveText('1');
});

test('removing an item clears the cart badge', async ({ inventoryPage }) => {
  await inventoryPage.addToCart('sauce-labs-backpack');
  await inventoryPage.removeFromCart('sauce-labs-backpack');
  await expect(inventoryPage.cartBadge).toHaveCount(0);
});

test('cart page lists the added item', async ({ page, inventoryPage }) => {
  await inventoryPage.addToCart('sauce-labs-backpack');
  await inventoryPage.openCart();
  await expect(new CartPage(page).itemNames).toHaveText('Sauce Labs Backpack');
});
const { test, expect } = require('../fixtures');
const { InventoryPage } = require('../pages/InventoryPage');

test('standard user can log in', async ({ page, loginPage }) => {
  await loginPage.login('standard_user');
  await expect(page).toHaveURL(/inventory\.html/);
  await expect(new InventoryPage(page).title).toHaveText('Products');
});

test('locked out user sees an error', async ({ loginPage }) => {
  await loginPage.login('locked_out_user');
  await expect(loginPage.error).toContainText('locked out');
});
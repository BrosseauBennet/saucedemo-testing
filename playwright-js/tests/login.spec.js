const { test, expect } = require('@playwright/test');

test('standard user can log in', async ({ page }) => {
  await page.goto('https://www.saucedemo.com');
  await page.fill('[data-test="username"]', 'standard_user');
  await page.fill('[data-test="password"]', 'secret_sauce');
  await page.click('[data-test="login-button"]');
  await expect(page).toHaveURL(/inventory\.html/);
  await expect(page.locator('.title')).toHaveText('Products');
});

test('locked out user sees an error', async ({ page }) => {
  await page.goto('https://www.saucedemo.com');
  await page.fill('[data-test="username"]', 'locked_out_user');
  await page.fill('[data-test="password"]', 'secret_sauce');
  await page.click('[data-test="login-button"]');
  await expect(page.locator('[data-test="error"]')).toContainText('locked out');
});
const { test, expect } = require('../fixtures');

test('user can complete checkout', async ({ checkoutPage }) => {
  await checkoutPage.fillInfo('Test', 'User', '12345');
  await checkoutPage.continueToOverview();
  await checkoutPage.finish();
  await expect(checkoutPage.completeHeader).toHaveText('Thank you for your order!');
});

test('checkout requires a first name', async ({ checkoutPage }) => {
  await checkoutPage.fillInfo('', 'User', '12345');
  await checkoutPage.continueToOverview();
  await expect(checkoutPage.error).toContainText('First Name is required');
});
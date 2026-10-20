class CartPage {
  constructor(page) {
    this.page = page;
    this.itemNames = page.locator('.cart_list .inventory_item_name');
    this.checkoutButton = page.locator('[data-test="checkout"]');
  }

  async startCheckout() {
    await this.checkoutButton.click();
  }
}

module.exports = { CartPage };
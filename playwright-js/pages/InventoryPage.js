class InventoryPage {
  constructor(page) {
    this.page = page;
    this.title = page.locator('.title');
    this.cartBadge = page.locator('[data-test="shopping-cart-badge"]');
    this.cartLink = page.locator('[data-test="shopping-cart-link"]');
  }

  async addToCart(item) {
    await this.page.click(`[data-test="add-to-cart-${item}"]`);
  }

  async removeFromCart(item) {
    await this.page.click(`[data-test="remove-${item}"]`);
  }

  async openCart() {
    await this.cartLink.click();
  }
}

module.exports = { InventoryPage };
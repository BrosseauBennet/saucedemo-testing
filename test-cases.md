# SauceDemo Manual Test Cases

Target site: saucedemo.com
Login credentials for testing are published on the site's own login page (standard_user, locked_out_user, problem_user, etc., all with password: secret_sauce).

| Test ID | Title | Steps | Expected Result |
|---|---|---|---|
| TC-01 | Valid login | 1. Go to saucedemo.com 2. Enter `standard_user` / `secret_sauce` 3. Click Login | User is redirected to the Products (inventory) page |
| TC-02 | Invalid login - wrong password | 1. Go to saucedemo.com 2. Enter `standard_user` / wrong password 3. Click Login | Error message is displayed; user remains on login page |
| TC-03 | Locked out user | 1. Go to saucedemo.com 2. Enter `locked_out_user` / `secret_sauce` 3. Click Login | Error message indicates the user has been locked out |
| TC-04 | Empty credentials | 1. Go to saucedemo.com 2. Leave username and password blank 3. Click Login | Error message indicates username is required |
| TC-05 | Add single item to cart | 1. Log in as standard_user 2. Click "Add to cart" on any product | Cart icon updates to show 1 item; button changes to "Remove" |
| TC-06 | Add multiple items to cart | 1. Log in as standard_user 2. Add 3 different products to cart | Cart icon shows count of 3 |
| TC-07 | Remove item from cart | 1. Log in and add an item to cart 2. Click "Remove" on that product, or open cart and remove it | Cart count decreases by 1; item no longer listed in cart |
| TC-08 | Product sort - price low to high | 1. Log in 2. On Products page, use sort dropdown 3. Select "Price (low to high)" | Products reorder from lowest to highest price |
| TC-09 | Checkout flow - happy path | 1. Log in 2. Add an item to cart 3. Go to cart 4. Click Checkout 5. Fill in first name, last name, zip 6. Click Continue 7. Click Finish | Order confirmation page displays "Thank you for your order!" |
| TC-10 | Checkout - missing required field | 1. Log in 2. Add item to cart 3. Go to checkout 4. Leave zip code blank 5. Click Continue | Error message indicates zip/postal code is required |
| TC-11 | Checkout with empty cart | 1. Log in as standard_user 2. Do not add any items 3. Navigate directly to cart 4. Click Checkout | Checkout proceeds to info page, or cart shows no items to check out (verify actual behavior — this is a good edge case to explore) |
| TC-12 | Checkout - invalid zip format | 1. Log in and add an item 2. Go to checkout 3. Enter letters/symbols in the zip field instead of numbers 4. Click Continue | App either accepts it (SauceDemo doesn't validate zip format) or shows a validation error — document actual behavior |
| TC-13 | Checkout - cancel and return to cart | 1. Log in and add an item 2. Go to checkout 3. Fill in info 4. Click Cancel instead of Continue | User is returned to the cart page with the item still present |
## Notes
- These are manual test cases as a starting point. Once Playwright automation is added to this repo, each of these can map to an automated test.
- `problem_user` and `performance_glitch_user` are also available on the site for testing broken/slow behavior scenarios if you want to expand coverage later.

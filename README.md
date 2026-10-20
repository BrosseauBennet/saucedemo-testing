# SauceDemo Testing

![UI Tests](https://github.com/BrosseauBennet/saucedemo-testing/actions/workflows/tests.yml/badge.svg)

Manual test cases and automated UI tests for [SauceDemo](https://www.saucedemo.com), a demo e-commerce site built for test automation practice. The same test suite is implemented twice, in **Python (pytest)** and **JavaScript (Playwright Test)**, both using Playwright and the Page Object pattern.

For API testing, see the companion repo: [restful-booker-api-tests](https://github.com/BrosseauBennet/restful-booker-api-tests).

## What's tested

| Area | Cases covered |
|---|---|
| Login | Standard user logs in successfully; locked-out user sees an error |
| Cart | Adding an item updates the cart badge; removing an item clears it; cart page lists the added item |
| Checkout | Full purchase completes with a confirmation message; checkout is blocked when first name is missing |

Each suite has 7 tests. The original manual test cases are in `manual-test-cases/`.

## Project structure

```
manual-test-cases/        # Manual test cases
ui-tests/                 # Python suite (pytest + Playwright)
├── pages/                # Page Objects: login, inventory, cart, checkout
├── conftest.py           # Fixtures that set up logged-in and checkout states
└── test_*.py             # Login, cart, and checkout tests
playwright-js/            # JavaScript suite (Playwright Test)
├── pages/                # Page Objects (same four pages)
├── fixtures.js           # Fixtures that set up logged-in and checkout states
└── tests/                # Login, cart, and checkout specs
.github/workflows/        # GitHub Actions workflow that runs both suites
```

## Design

- **Page Object pattern:** each page of the app is a class that holds its locators and actions, so tests read as user steps and a UI change means editing one file.
- **Fixtures:** shared setup (logging in, reaching checkout) lives in fixtures, not in each test.
- **Assertions stay in the tests,** not in the page objects.
- **Scoped locators:** for example, cart items are located inside the cart list so they can't match product names on other pages.

## Running the Python tests

Requires Python 3.11 or newer.

```bash
git clone https://github.com/BrosseauBennet/saucedemo-testing.git
cd saucedemo-testing
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest ui-tests -v
```

Add `--headed` to watch the browser.

## Running the JavaScript tests

Requires Node.js 20 or newer.

```bash
cd playwright-js
npm ci
npx playwright install chromium
npx playwright test --project=chromium
```

Add `--headed` to watch the browser.

## Continuous integration

A GitHub Actions workflow runs both suites on every pull request and on pushes to `main`. The JavaScript job also uploads the Playwright HTML report as a build artifact.

## Python vs. JavaScript

| | Python | JavaScript |
|---|---|---|
| Test runner | pytest | Playwright Test |
| Shared setup | `conftest.py` fixtures | `test.extend` fixtures in `fixtures.js` |
| Browser actions | Synchronous calls | `async` / `await` |

## Known limitations

- CI runs Chromium only.
- Tests use the `standard_user` account and the `locked_out_user` account; the site's other test users aren't covered yet.
- SauceDemo is a public demo site, so changes on their end can break locators.

## Planned next steps

- Cover other SauceDemo users (for example `problem_user` and `performance_glitch_user`)
- Product sorting and logout tests
- Run CI across Firefox and WebKit
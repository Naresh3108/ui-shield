# UI Shield 🛡️

UI Test Automation Framework built with Playwright, pytest, and Page Object Model.

## Tech Stack
- Python 3.14
- Playwright
- pytest
- Page Object Model (POM)
- Allure Reports

## Test Coverage
- 15 automated tests
- Smoke, Functional (Login + Products)
- Cross-browser ready (Chrome, Firefox, WebKit)

## How to Run

### Install dependencies
pip install -r requirements.txt
playwright install

### Run all tests
pytest -v

### Run by category
pytest -m smoke -v
pytest -m functional -v

### Generate Allure Report
pytest -v --alluredir=reports/allure-results
allure serve reports/allure-results
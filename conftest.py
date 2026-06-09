# conftest.py
# this file sets up the browser before each test runs
# playwright needs a browser to open and a page to test on
# we set that up here so every test can use it

import pytest
from playwright.sync_api import sync_playwright

# the website we are going to test
BASE_URL = "https://automationexercise.com"

@pytest.fixture
def page():
    # start playwright
    playwright = sync_playwright().start()

    # open Chrome browser - headless=False means we can see it
    browser = playwright.chromium.launch(headless=False)

    # open a new tab
    page = browser.new_page()

    # go to the website
    page.goto(BASE_URL)

    # print so we know the browser opened
    print(f"\nBrowser opened: {BASE_URL}")

    # give the page to the test
    yield page

    # after the test finishes - close everything
    print("\nBrowser closed")
    browser.close()
    playwright.stop()


@pytest.fixture
def firefox_page():
    # same as above but using Firefox browser
    playwright = sync_playwright().start()
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)
    print(f"\nFirefox opened: {BASE_URL}")
    yield page
    print("\nFirefox closed")
    browser.close()
    playwright.stop()
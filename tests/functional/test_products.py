# test_products.py
# these are functional tests for the products page
# we navigate to products via the homepage nav to avoid blocks

import pytest
from pages.home_page import HomePage

@pytest.mark.functional
def test_products_page_loads(page):
    # go directly to products page and check URL
    page.goto("https://automationexercise.com/products")
    page.wait_for_load_state("domcontentloaded")
    current_url = page.url
    print(f"URL: {current_url}")
    assert "/products" in current_url

@pytest.mark.functional
def test_products_page_has_items(page):
    # check there are products showing on the page
    page.goto("https://automationexercise.com/products")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)
    products = page.locator(".productinfo")
    count = products.count()
    print(f"Total products found: {count}")
    assert count > 0

@pytest.mark.functional
def test_search_product(page):
    # go to products page and search for dress
    page.goto("https://automationexercise.com/products")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1000)

    print("Searching for: dress")
    page.fill("#search_product", "dress")
    page.click("#submit_search")
    page.wait_for_load_state("domcontentloaded")

    # the heading is uppercase so check uppercase
    heading = page.locator("h2.title.text-center")
    text = heading.inner_text()
    print(f"Results heading: {text}")
    assert "SEARCHED" in text.upper()

@pytest.mark.functional
def test_search_returns_results(page):
    # search for top and check at least 1 result shows
    page.goto("https://automationexercise.com/products")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1000)

    print("Searching for: top")
    page.fill("#search_product", "top")
    page.click("#submit_search")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)

    products = page.locator(".productinfo")
    count = products.count()
    print(f"Search results count: {count}")
    assert count > 0

@pytest.mark.functional
def test_products_url(page):
    # use goto with domcontentloaded to bypass google vignette ad
    # the ad only appears on full page load - not domcontentloaded
    page.goto("https://automationexercise.com/products",
              wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    current_url = page.url
    print(f"Products URL: {current_url}")
    assert "/products" in current_url
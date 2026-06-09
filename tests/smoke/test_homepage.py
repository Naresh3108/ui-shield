# test_homepage.py
# these are smoke tests for the homepage
# smoke tests are quick checks to make sure
# the website is up and working before we run bigger tests

import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_homepage_title(page):
    # check the page title is correct
    home = HomePage(page)
    title = home.get_title()
    assert "Automation Exercise" in title

@pytest.mark.smoke
def test_homepage_loads(page):
    # check that the homepage actually loads
    home = HomePage(page)
    is_home = home.is_home_page()
    assert is_home == True

@pytest.mark.smoke
def test_homepage_url(page):
    # check we are on the right URL
    current_url = page.url
    print(f"Current URL: {current_url}")
    assert "automationexercise.com" in current_url

@pytest.mark.smoke
def test_logo_is_visible(page):
    # check the logo shows on the homepage
    home = HomePage(page)
    logo_visible = home.is_logo_visible()
    assert logo_visible == True

@pytest.mark.smoke
def test_page_loads_fast(page):
    # check the page loaded in under 5 seconds
    import time
    start = time.time()
    page.goto("https://automationexercise.com")
    end = time.time()
    load_time = end - start
    print(f"Page loaded in: {load_time:.2f} seconds")
    assert load_time < 5
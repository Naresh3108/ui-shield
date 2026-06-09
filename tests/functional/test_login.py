# test_login.py
# these are functional tests for the login page
# we test both successful and failed login scenarios

import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

# valid test account on automationexercise.com
TEST_EMAIL = "nareshtest@gmail.com"
TEST_PASSWORD = "Test@1234"

@pytest.mark.functional
def test_login_page_loads(page):
    # go to login page and check it loaded
    home = HomePage(page)
    home.click_signup_login()

    # check the login form is visible
    login = LoginPage(page)
    assert login.is_login_form_visible() == True

@pytest.mark.functional
def test_signup_form_visible(page):
    # check the signup form is also on the same page
    home = HomePage(page)
    home.click_signup_login()

    login = LoginPage(page)
    assert login.is_signup_form_visible() == True

@pytest.mark.functional
def test_login_with_wrong_password(page):
    # try logging in with wrong password
    # should show an error message
    home = HomePage(page)
    home.click_signup_login()

    login = LoginPage(page)
    login.login("wrong@email.com", "wrongpassword")

    # check error message appears
    error = login.get_login_error()
    assert error is not None

@pytest.mark.functional
def test_login_page_title(page):
    # check the login page has correct title
    home = HomePage(page)
    home.click_signup_login()

    login = LoginPage(page)
    title = login.get_title()
    assert "Automation Exercise" in title

@pytest.mark.functional
def test_login_url(page):
    # check we are on the correct login URL
    home = HomePage(page)
    home.click_signup_login()

    current_url = page.url
    print(f"Login URL: {current_url}")
    assert "/login" in current_url
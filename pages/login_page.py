# login_page.py
# this is the Page Object for the login page
# it handles all actions related to login and signup

class LoginPage:

    def __init__(self, page):
        # save the page to use in all methods
        self.page = page

    def get_title(self):
        # get the page title to confirm we are on login page
        title = self.page.title()
        print(f"Login page title: {title}")
        return title

    def is_login_form_visible(self):
        # check if the login form is showing
        login_form = self.page.locator("h2:has-text('Login to your account')")
        return login_form.is_visible()

    def is_signup_form_visible(self):
        # check if the signup form is showing
        signup_form = self.page.locator("h2:has-text('New User Signup!')")
        return signup_form.is_visible()

    def login(self, email, password):
        # fill in email and password and click login
        print(f"Logging in with email: {email}")
        self.page.fill("input[data-qa='login-email']", email)
        self.page.fill("input[data-qa='login-password']", password)
        self.page.click("button[data-qa='login-button']")
        print("Clicked login button")

    def signup(self, name, email):
        # fill in name and email and click signup
        print(f"Signing up with name: {name}, email: {email}")
        self.page.fill("input[data-qa='signup-name']", name)
        self.page.fill("input[data-qa='signup-email']", email)
        self.page.click("button[data-qa='signup-button']")
        print("Clicked signup button")

    def get_login_error(self):
        # get the error message when login fails
        error = self.page.locator("p:has-text('Your email or password is incorrect!')")
        if error.is_visible():
            print("Login error message found")
            return error.inner_text()
        return None
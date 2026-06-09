# home_page.py
# this is the Page Object for the homepage
# Page Object Model (POM) means we keep all the homepage
# actions and locators in one place
# instead of writing the same selectors in every test

class HomePage:

    def __init__(self, page):
        # save the page so we can use it in all methods
        self.page = page

    def get_title(self):
        # get the title of the page
        title = self.page.title()
        print(f"Page title is: {title}")
        return title

    def is_logo_visible(self):
        # check if the logo is visible on the homepage
        logo = self.page.locator("img[src='/static/images/home/logo.png']")
        return logo.is_visible()

    def click_signup_login(self):
        # click the Signup / Login button in the nav bar
        self.page.click("a[href='/login']")
        print("Clicked Signup/Login button")

    def click_products(self):
        # click the Products link in the nav bar
        self.page.click("a[href='/products']")
        print("Clicked Products link")

    def click_cart(self):
        # click the Cart link in the nav bar
        self.page.click("a[href='/view_cart']")
        print("Clicked Cart link")

    def search_product(self, product_name):
        # type a product name in the search bar and search
        self.page.fill("#search_product", product_name)
        self.page.click("#submit_search")
        print(f"Searched for: {product_name}")

    def is_home_page(self):
        # check if we are on the homepage
        # the homepage has a slider section
        slider = self.page.locator("#slider")
        return slider.is_visible()
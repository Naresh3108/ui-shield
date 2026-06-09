# product_page.py
# this is the Page Object for the products page
# handles searching, viewing and adding products to cart

class ProductPage:

    def __init__(self, page):
        # save the page to use in all methods
        self.page = page

    def is_products_page(self):
        # check if we are on the products page
        heading = self.page.locator("h2:has-text('All Products')")
        return heading.is_visible()

    def search_product(self, product_name):
        # search for a product by name
        print(f"Searching for product: {product_name}")
        self.page.fill("#search_product", product_name)
        self.page.click("#submit_search")

    def get_search_results_title(self):
        # get the title of search results
        title = self.page.locator("h2:has-text('Searched Products')")
        if title.is_visible():
            return title.inner_text()
        return None

    def get_product_count(self):
        # count how many products are showing on the page
        products = self.page.locator(".productinfo")
        count = products.count()
        print(f"Found {count} products on the page")
        return count

    def click_first_product(self):
        # click view product on the first item
        self.page.locator(".choose a").first.click()
        print("Clicked first product")

    def add_first_product_to_cart(self):
        # hover over first product and click Add to Cart
        self.page.locator(".productinfo").first.hover()
        self.page.locator(".add-to-cart").first.click()
        print("Added first product to cart")
"""Product details page. Uses BaseActions + locators from JSON."""
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    """Product details. All interactions via self.actions and locators.json."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "")

    def get_product_title(self) -> str:
        """Uses product_details.product_title."""
        return self.actions.get_text("product_details", "product_title")

    def get_product_price(self) -> str:
        """Uses product_details.product_price."""
        return self.actions.get_text("product_details", "product_price")

    def is_add_to_cart_visible(self) -> bool:
        """Uses product_details.add_to_cart_button."""
        return self.actions.is_displayed("product_details", "add_to_cart_button")

    def click_add_to_cart(self) -> None:
        """Uses product_details.add_to_cart_button."""
        self.actions.click("product_details", "add_to_cart_button")

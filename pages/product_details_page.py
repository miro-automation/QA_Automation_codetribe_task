"""Product details page. Uses BaseActions + locators from JSON."""
from typing import Optional

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

    def verify_title_not_empty(self) -> Optional[str]:
        """Verify product title (h1) exists and is not empty. Returns None if ok, else error message."""
        try:
            title = self.get_product_title()
            if not (title or "").strip():
                return "Product title (h1) is empty."
            return None
        except Exception as e:
            return f"Product title check failed: {e}"

    def verify_price_valid(self) -> Optional[str]:
        """Verify product price is non-empty and numeric (digits and dot). Returns None if ok, else error message."""
        try:
            price = self.get_product_price()
            s = (price or "").strip()
            if not s:
                return "Product price is empty."
            if not all(c.isdigit() or c == "." for c in s):
                return f"Product price is not numeric: {price!r}"
            return None
        except Exception as e:
            return f"Product price check failed: {e}"

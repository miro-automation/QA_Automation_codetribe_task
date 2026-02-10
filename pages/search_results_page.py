"""Search results page. Uses BaseActions + locators from JSON."""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    """Search results. All element access via self.actions and locators.json."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "")

    def get_result_products(self) -> list[WebElement]:
        """Return list of product item elements. Uses search_results.result_products."""
        return self.actions.find_elements("search_results", "result_products")

    def get_product_title_link(self, index: int = 0) -> WebElement:
        """Get product title link by index. Uses search_results.product_title_link (first match)."""
        elements = self.actions.find_elements("search_results", "product_title_link")
        if not elements or index >= len(elements):
            raise IndexError(f"No product title link at index {index}")
        return elements[index]

    def click_product_at_index(self, index: int = 0) -> None:
        """Open product details by clicking product link at index."""
        self.get_product_title_link(index).click()

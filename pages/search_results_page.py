"""Search results page. Verification of product-grid and item-box structure."""
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.data_loader import get_value
from config.settings import IMPLICIT_WAIT
from pages.base_page import BasePage

# Output folder for generated lists (e.g. product names)
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


class SearchResultsPage(BasePage):
    """Search results. Verifies all product-grid item-boxes contain keyword."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "")

    def verify_products_contain_build(self) -> None:
        """Verify all results contain the keyword from static data (Products.Build)."""
        keyword = get_value("Products", "Build")
        self.verify_all_products_contain_keyword(keyword)

    def verify_all_products_contain_keyword(self, keyword: str) -> None:
        """
        In every div.product-grid, for every div.item-box:
        - must have child .product-item
        - must have child .details
        - inside h2, <a> must contain keyword.
        Raises AssertionError if any box fails.
        """
        # Wait for search results to load (avoids stale element)
        WebDriverWait(self.driver, IMPLICIT_WAIT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid div.item-box"))
        )

        # Single selector – no grid references kept (avoids StaleElementReference)
        boxes = self.driver.find_elements(By.CSS_SELECTOR, "div.product-grid div.item-box")
        assert len(boxes) > 0, "No div.item-box elements found in product-grid"

        for idx, box in enumerate(boxes):
            try:
                product_item = box.find_element(By.CSS_SELECTOR, ".product-item")
            except Exception as e:
                raise AssertionError(
                    f"item-box[{idx}] has no child with class 'product-item'"
                ) from e
            try:
                details = product_item.find_element(By.CSS_SELECTOR, ".details")
            except Exception as e:
                raise AssertionError(
                    f"item-box[{idx}] has no child with class 'details'"
                ) from e
            try:
                h2_a = details.find_element(By.CSS_SELECTOR, "h2 a")
            except Exception as e:
                raise AssertionError(
                    f"item-box[{idx}] has no h2 > a inside .details"
                ) from e
            if keyword.lower() not in h2_a.text.lower():
                raise AssertionError(
                    f"Keyword '{keyword}' not found in product (item-box[{idx}]): '{h2_a.text}'"
                )

    def get_product_names_from_results(self) -> list[str]:
        """
        Get all product names from search results.
        Structure: .search-results .product-grid .item-box .product-item .details h2 a (text).
        """
        WebDriverWait(self.driver, IMPLICIT_WAIT).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.search-results div.product-grid div.item-box .product-item .details h2 a")
            )
        )
        links = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.search-results div.product-grid div.item-box .product-item .details h2 a",
        )
        return [el.text.strip() for el in links if el.text]

    def write_product_names_list(self, filename: str = "test_pa_search_product_key_word_list.txt") -> Path:
        """
        Get product names from current results and write them to output/<filename>.
        Returns the path to the created file.
        """
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        filepath = OUTPUT_DIR / filename
        names = self.get_product_names_from_results()
        filepath.write_text("\n".join(names), encoding="utf-8")
        return filepath

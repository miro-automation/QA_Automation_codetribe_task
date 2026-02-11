"""Search results page. Verification of product-grid and item-box structure."""
from pathlib import Path
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.data_loader import get_value
from config.settings import BASE_URL, IMPLICIT_WAIT
from pages.base_page import BasePage

# Output folder for generated lists (e.g. product names)
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def _name_is_valid(text: str) -> bool:
    """
    Name must contain at least one letter; not empty/whitespace; not only digits/special chars.
    """
    s = (text or "").strip()
    return len(s) > 0 and any(c.isalpha() for c in s)


def _price_is_valid(text: str) -> bool:
    """
    Price must be only digits and optionally dot (e.g. 800.00). No letters, no other special chars.
    """
    s = (text or "").strip()
    if len(s) == 0:
        return False
    return all(c in "0123456789." for c in s) and any(c.isdigit() for c in s)


class SearchResultsPage(BasePage):
    """Search results. Verifies all product-grid item-boxes contain keyword."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "")

    def verify_products_contain_build(self) -> Optional[str]:
        """Verify all results contain the keyword from static data (Products.Build). Returns None if ok, else error message."""
        keyword = get_value("Products", "Build")
        return self.verify_all_products_contain_keyword(keyword)

    def verify_all_products_contain_keyword(self, keyword: str) -> Optional[str]:
        """
        In every div.product-grid, for every div.item-box:
        - must have child .product-item
        - must have child .details
        - inside h2, <a> must contain keyword.
        Returns None if all pass, else error message string.
        """
        try:
            WebDriverWait(self.driver, IMPLICIT_WAIT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid div.item-box"))
            )
            boxes = self.driver.find_elements(By.CSS_SELECTOR, "div.product-grid div.item-box")
            if len(boxes) == 0:
                return "No div.item-box elements found in product-grid"

            for idx, box in enumerate(boxes):
                try:
                    product_item = box.find_element(By.CSS_SELECTOR, ".product-item")
                except Exception as e:
                    return f"item-box[{idx}] has no child with class 'product-item': {e}"
                try:
                    details = product_item.find_element(By.CSS_SELECTOR, ".details")
                except Exception as e:
                    return f"item-box[{idx}] has no child with class 'details': {e}"
                try:
                    h2_a = details.find_element(By.CSS_SELECTOR, "h2 a")
                except Exception as e:
                    return f"item-box[{idx}] has no h2 > a inside .details: {e}"
                if keyword.lower() not in h2_a.text.lower():
                    return f"Keyword '{keyword}' not found in product (item-box[{idx}]): '{h2_a.text}'"
            return None
        except Exception as e:
            return str(e)

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

    def verify_each_result_has_valid_name_and_price(self) -> Optional[str]:
        """
        For each item-box: validate that the name (h2 a) contains letters,
        and that the price (div.add-info span numeric value) is only digits and dot.
        Returns None if all pass, else error message string.
        """
        try:
            WebDriverWait(self.driver, IMPLICIT_WAIT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid div.item-box"))
            )
            boxes = self.driver.find_elements(By.CSS_SELECTOR, "div.product-grid div.item-box")
            if len(boxes) == 0:
                return "No div.item-box elements found in product-grid"

            for idx, box in enumerate(boxes):
                product_item = box.find_element(By.CSS_SELECTOR, ".product-item")
                details = product_item.find_element(By.CSS_SELECTOR, ".details")

                try:
                    name_el = details.find_element(By.CSS_SELECTOR, "h2 a")
                    name_text = name_el.text
                except Exception as e:
                    return f"item-box[{idx}]: no h2 a (product name) in .details: {e}"
                if not _name_is_valid(name_text):
                    return f"item-box[{idx}]: product name must contain letters (got: {name_text!r})"

                try:
                    add_info = details.find_element(By.CSS_SELECTOR, "div.add-info")
                    spans = add_info.find_elements(By.CSS_SELECTOR, "span")
                except Exception as e:
                    return f"item-box[{idx}]: no div.add-info in .details: {e}"

                price_text = None
                for span in spans:
                    t = (span.text or "").strip()
                    if t and _price_is_valid(t):
                        price_text = t
                        break
                if price_text is None:
                    return f"item-box[{idx}]: no valid price (digits and . only) in div.add-info spans (spans: {[s.text for s in spans]})"
            return None
        except Exception as e:
            return str(e)

    def verify_first_item_has_add_to_cart(self) -> Optional[str]:
        """Verify that the first search result item has a visible 'Add to cart' button. Returns None if ok, else error message."""
        try:
            WebDriverWait(self.driver, IMPLICIT_WAIT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid div.item-box input[value='Add to cart']"))
            )
            btn = self.driver.find_element(By.CSS_SELECTOR, "div.product-grid div.item-box input[value='Add to cart']")
            if not btn.is_displayed():
                return "First item 'Add to cart' button is not visible."
            return None
        except Exception as e:
            return f"First item has no 'Add to cart' button or not found: {e}"

    def open_first_product_in_current_tab(self) -> None:
        """Open the first product's details in the current tab (via href to avoid new window)."""
        link = WebDriverWait(self.driver, IMPLICIT_WAIT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid div.item-box .product-item .details h2 a"))
        )
        href = link.get_attribute("href") or ""
        if not href:
            raise ValueError("First product link has no href.")
        base = BASE_URL.rstrip("/")
        full_url = href if href.startswith("http") else (base + "/" + href.lstrip("/"))
        self.driver.get(full_url)

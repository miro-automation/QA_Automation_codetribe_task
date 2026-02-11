"""Category page (e.g. Apparel & Shoes). Navigation, product grid, pagination, sorting."""
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import BASE_URL, IMPLICIT_WAIT
from pages.base_page import BasePage


def _full_url(href: str) -> str:
    """Build full URL from relative or absolute href."""
    href = (href or "").strip()
    if not href:
        raise ValueError("href is empty")
    if href.startswith("http"):
        return href
    base = BASE_URL.rstrip("/")
    return base + ("/" if not href.startswith("/") else "") + href


class CategoryPage(BasePage):
    """Apparel & Shoes category: open, verify products, pagination (navigate via href to stay in same tab)."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "")

    def open_apparel_shoes(self) -> None:
        """Navigate to Apparel & Shoes using link href (same tab)."""
        href = self.actions.get_attribute("category", "apparel_shoes_link", "href")
        self.driver.get(_full_url(href))

    def verify_products_displayed(self) -> Optional[str]:
        """Verify product grid and that each item-box has .product-item with .picture and .details. Returns None if ok."""
        try:
            self.actions.find_element("category", "product_grid")
            boxes = self.actions.find_elements("category", "item_boxes")
            if not boxes:
                return "No product item-boxes found in product-grid."
            for i, box in enumerate(boxes):
                try:
                    box.find_element(By.CSS_SELECTOR, ".product-item .picture")
                    box.find_element(By.CSS_SELECTOR, ".product-item .details")
                except Exception as e:
                    return f"Item-box[{i}]: missing .product-item .picture or .details: {e}"
            return None
        except Exception as e:
            return str(e)

    def verify_pager_present(self) -> Optional[str]:
        """Verify pagination block is present and visible."""
        try:
            if not self.actions.is_displayed("category", "pager"):
                return "Pager (div.pager) is not visible."
            return None
        except Exception as e:
            return str(e)

    def verify_next_visible(self) -> Optional[str]:
        """Verify Next page link is visible."""
        try:
            if not self.actions.is_displayed("category", "next_page_link"):
                return "Next page link is not visible."
            return None
        except Exception as e:
            return str(e)

    def verify_previous_visible(self) -> Optional[str]:
        """Verify Previous page link is visible."""
        try:
            if not self.actions.is_displayed("category", "previous_page_link"):
                return "Previous page link is not visible."
            return None
        except Exception as e:
            return str(e)

    def verify_current_page_number(self, expected: int) -> Optional[str]:
        """Verify current page number in pager. Returns None if ok."""
        try:
            el = self.actions.find_element("category", "current_page")
            text = (el.text or "").strip()
            if text != str(expected):
                return f"Expected current page {expected}, got: {text!r}"
            return None
        except Exception as e:
            return str(e)

    def go_to_next_page(self) -> None:
        """Go to next page via href (no click on link to avoid new tab)."""
        el = self.actions.find_element("category", "next_page_link")
        href = el.get_attribute("href")
        self.driver.get(_full_url(href))

    def go_to_previous_page(self) -> None:
        """Go to previous page via href (no click on link)."""
        el = self.actions.find_element("category", "previous_page_link")
        href = el.get_attribute("href")
        self.driver.get(_full_url(href))

    def go_to_page_2(self) -> None:
        """Go to page 2 via href of '2' link (no click on link)."""
        el = self.actions.find_element("category", "page_2_link")
        href = el.get_attribute("href")
        self.driver.get(_full_url(href))

    def go_to_page_1(self) -> None:
        """Go to page 1 via href of '1' link (no click on link)."""
        el = self.actions.find_element("category", "page_1_link")
        href = el.get_attribute("href")
        self.driver.get(_full_url(href))

    def select_sort_by(self, option_visible_text: str) -> None:
        """Select sort option from dropdown (id=products-orderby). Waits for page to reload after selection."""
        el = self.actions.find_element("category", "sort_dropdown")
        select = Select(el)
        select.select_by_visible_text(option_visible_text)
        WebDriverWait(self.driver, IMPLICIT_WAIT).until(EC.url_contains("orderby"))
        WebDriverWait(self.driver, IMPLICIT_WAIT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-grid div.item-box"))
        )

    def get_product_names_on_page(self) -> List[str]:
        """Get product names (h2 a text) from all item-boxes on the current page."""
        boxes = self.actions.find_elements("category", "item_boxes")
        names = []
        for box in boxes:
            try:
                el = box.find_element(By.CSS_SELECTOR, ".product-item .details h2 a")
                t = (el.text or "").strip()
                if t:
                    names.append(t)
            except Exception:
                pass
        return names

    def get_product_prices_on_page(self) -> List[float]:
        """Get product prices from all item-boxes on the current page. Parses numeric span in div.add-info."""
        boxes = self.actions.find_elements("category", "item_boxes")
        prices = []
        for box in boxes:
            try:
                add_info = box.find_element(By.CSS_SELECTOR, ".product-item .details div.add-info")
                for span in add_info.find_elements(By.CSS_SELECTOR, "span"):
                    t = (span.text or "").strip()
                    if t and all(c in "0123456789." for c in t) and any(c.isdigit() for c in t):
                        prices.append(float(t.replace(",", ".")))
                        break
            except Exception:
                pass
        return prices

    def verify_sorted_name_a_to_z(self) -> Optional[str]:
        """Verify product names on current page are sorted A to Z (case-insensitive). Returns None if ok."""
        names = self.get_product_names_on_page()
        if len(names) < 2:
            return None
        expected = sorted(names, key=str.lower)
        if names != expected:
            return f"Names not A–Z sorted: got {names[:5]}... expected {expected[:5]}..."
        return None

    def verify_sorted_name_z_to_a(self) -> Optional[str]:
        """Verify product names on current page are sorted Z to A (case-insensitive). Returns None if ok."""
        names = self.get_product_names_on_page()
        if len(names) < 2:
            return None
        expected = sorted(names, key=str.lower, reverse=True)
        if names != expected:
            return f"Names not Z–A sorted: got {names[:5]}... expected {expected[:5]}..."
        return None

    def verify_sorted_price_low_to_high(self) -> Optional[str]:
        """Verify product prices on current page are sorted low to high. Returns None if ok."""
        prices = self.get_product_prices_on_page()
        if len(prices) < 2:
            return None
        if prices != sorted(prices):
            return f"Prices not low-to-high: got {prices[:5]}..."
        return None

    def verify_sorted_price_high_to_low(self) -> Optional[str]:
        """Verify product prices on current page are sorted high to low. Returns None if ok."""
        prices = self.get_product_prices_on_page()
        if len(prices) < 2:
            return None
        if prices != sorted(prices, reverse=True):
            return f"Prices not high-to-low: got {prices[:5]}..."
        return None

    def verify_sort_created_on_applied(self) -> Optional[str]:
        """Verify 'Created on' sort is applied: URL contains orderby=15 and products are displayed."""
        try:
            if "orderby=15" not in (self.driver.current_url or ""):
                return "URL does not contain orderby=15 (Created on)."
            err = self.verify_products_displayed()
            return err
        except Exception as e:
            return str(e)

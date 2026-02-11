"""Category page (e.g. Apparel & Shoes). Navigation, product grid and pagination."""
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from config.settings import BASE_URL
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

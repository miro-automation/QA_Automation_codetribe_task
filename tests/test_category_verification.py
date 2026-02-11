"""
Category Verification: navigate to Apparel & Shoes, verify products and pagination on both pages.
"""
import pytest

from pages.category_page import CategoryPage

pytestmark = [pytest.mark.order(3)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.category_verification
def test_category_verification(driver):
    """Steps:
    1. Navigate to Apparel & Shoes category.
    2. Assert products are displayed and pager (Next) is present on page 1.
    3. Go to page 2.
    4. Assert products are displayed and current page is 2.
    """
    assert driver is not None, "Driver fixture should be available."
    category = CategoryPage(driver)
    category.open_apparel_shoes()

    err = category.verify_products_displayed()
    assert err is None, err or "Products (item-box with picture and details) should be displayed on page 1."

    err = category.verify_pager_present()
    assert err is None, err or "Pagination (div.pager) should be present."

    err = category.verify_next_visible()
    assert err is None, err or "Next page link should be visible on page 1."

    category.go_to_next_page()

    err = category.verify_products_displayed()
    assert err is None, err or "Products should be displayed on page 2."

    err = category.verify_current_page_number(2)
    assert err is None, err or "Current page should be 2 after Next."

"""
Sort products by Price: High to Low. Verify order on page 1 and page 2.
"""
import pytest

from pages.category_page import CategoryPage

pytestmark = [pytest.mark.order(3)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.sorting
def test_sort_price_high_to_low(driver):
    """Steps:
    1. Open Apparel & Shoes; select sort 'Price: High to Low'.
    2. Assert products on page 1 are sorted by price descending.
    3. Go to page 2; assert products on page 2 are sorted by price descending.
    """
    assert driver is not None, "Driver fixture should be available."
    category = CategoryPage(driver)
    category.open_apparel_shoes()
    category.select_sort_by("Price: High to Low")

    err = category.verify_sorted_price_high_to_low()
    assert err is None, err or "Products on page 1 should be sorted Price High to Low."

    category.go_to_next_page()
    err = category.verify_sorted_price_high_to_low()
    assert err is None, err or "Products on page 2 should be sorted Price High to Low."

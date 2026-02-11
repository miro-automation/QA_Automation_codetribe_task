"""
Sort products by Created on. Verify sort is applied (URL orderby=15) and products displayed on page 1 and page 2.
"""
import pytest

from pages.category_page import CategoryPage

pytestmark = [pytest.mark.order(3)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.sorting
def test_sort_created_on(driver):
    """Steps:
    1. Open Apparel & Shoes; select sort 'Created on'.
    2. Assert sort is applied (URL/product list) and products displayed on page 1.
    3. Go to page 2; assert products displayed and sort applied on page 2.
    """
    assert driver is not None, "Driver fixture should be available."
    category = CategoryPage(driver)
    category.open_apparel_shoes()
    category.select_sort_by("Created on")

    err = category.verify_sort_created_on_applied()
    assert err is None, err or "Created on sort should be applied and products displayed on page 1."

    category.go_to_next_page()
    err = category.verify_sort_created_on_applied()
    assert err is None, err or "Created on sort should be applied and products displayed on page 2."

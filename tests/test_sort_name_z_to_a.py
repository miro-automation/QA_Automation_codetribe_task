"""
Sort products by Name: Z to A. Verify order on page 1 and page 2.
"""
import pytest

from pages.category_page import CategoryPage


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.sorting
def test_sort_name_z_to_a(driver):
    """Open Apparel & Shoes, select Name: Z to A, verify sorting on page 1 and page 2."""
    assert driver is not None, "Driver fixture should be available."
    category = CategoryPage(driver)
    category.open_apparel_shoes()
    category.select_sort_by("Name: Z to A")

    err = category.verify_sorted_name_z_to_a()
    assert err is None, err or "Products on page 1 should be sorted Name Z to A."

    category.go_to_next_page()
    err = category.verify_sorted_name_z_to_a()
    assert err is None, err or "Products on page 2 should be sorted Name Z to A."

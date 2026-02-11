"""
Sort products by Name: A to Z. Verify order on page 1 and page 2.
"""
import pytest

from pages.category_page import CategoryPage

pytestmark = [pytest.mark.order(3)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.sorting
def test_sort_name_a_to_z(driver):
    """Steps:
    1. Open Apparel & Shoes; select sort 'Name: A to Z'.
    2. Assert products on page 1 are sorted A to Z.
    3. Go to page 2; assert products on page 2 are sorted A to Z.
    """
    assert driver is not None, "Driver fixture should be available."
    category = CategoryPage(driver)
    category.open_apparel_shoes()
    category.select_sort_by("Name: A to Z")

    err = category.verify_sorted_name_a_to_z()
    assert err is None, err or "Products on page 1 should be sorted Name A to Z."

    category.go_to_next_page()
    err = category.verify_sorted_name_a_to_z()
    assert err is None, err or "Products on page 2 should be sorted Name A to Z."

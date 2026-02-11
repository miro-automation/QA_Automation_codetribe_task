"""
Pagination flow: Next, Previous, page 2, page 1 with element checks at each step.
"""
import pytest

from pages.category_page import CategoryPage


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.pagination
def test_pagination_flow(driver):
    """Apparel & Shoes: verify page 1 -> Next -> verify page 2 -> Previous -> page 1 -> go to 2 -> go to 1; assert elements at each step."""
    assert driver is not None, "Driver fixture should be available."
    category = CategoryPage(driver)
    category.open_apparel_shoes()

    err = category.verify_products_displayed()
    assert err is None, err or "Products should be displayed on page 1."
    err = category.verify_pager_present()
    assert err is None, err or "Pager should be present on page 1."
    err = category.verify_next_visible()
    assert err is None, err or "Next should be visible on page 1."
    err = category.verify_current_page_number(1)
    assert err is None, err or "Current page should be 1."

    category.go_to_next_page()

    err = category.verify_previous_visible()
    assert err is None, err or "Previous should be visible on page 2."
    err = category.verify_current_page_number(2)
    assert err is None, err or "Current page should be 2 after Next."
    err = category.verify_products_displayed()
    assert err is None, err or "Products should be displayed on page 2."

    category.go_to_previous_page()

    err = category.verify_products_displayed()
    assert err is None, err or "Products should be displayed after Previous (page 1)."
    err = category.verify_current_page_number(1)
    assert err is None, err or "Current page should be 1 after Previous."

    category.go_to_page_2()

    err = category.verify_previous_visible()
    assert err is None, err or "Previous should be visible on page 2 (via page 2 link)."
    err = category.verify_current_page_number(2)
    assert err is None, err or "Current page should be 2 after clicking page 2."
    err = category.verify_products_displayed()
    assert err is None, err or "Products should be displayed on page 2."

    category.go_to_page_1()

    err = category.verify_products_displayed()
    assert err is None, err or "Products should be displayed on page 1 after clicking page 1."
    err = category.verify_current_page_number(1)
    assert err is None, err or "Current page should be 1 at end of flow."

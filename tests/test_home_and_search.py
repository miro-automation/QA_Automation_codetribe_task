"""
Tests: home and search.
Only method calls – all logic and data in page objects (OOP).
"""
import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.smoke
def test_pa_search_box_visible(driver):
    """Search field is visible."""
    assert driver is not None, "Driver fixture should be available."
    home = HomePage(driver)
    assert home.is_search_visible(), "Search field (Products.search_button) should be visible on home page."


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.search
def test_pa_search_product_key_word(driver):
    """Search by Build (static data), verify results contain keyword, write product names to list file."""
    assert driver is not None, "Driver fixture should be available."
    home = HomePage(driver)
    home.search_build()

    results = SearchResultsPage(driver)
    err = results.verify_products_contain_build()
    assert err is None, err or "Search results should all contain the keyword (Build)."
    results.write_product_names_list()

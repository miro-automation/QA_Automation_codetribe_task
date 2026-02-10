"""
Tests: home and search.
Only method calls – all logic and data in page objects (OOP).
"""
import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_pa_search_box_visible(driver):
    """Search field is visible."""
    home = HomePage(driver)
    assert home.is_search_visible()


def test_pa_search_product_key_word(driver):
    """Search by Build (static data), verify results contain keyword, write product names to list file."""
    home = HomePage(driver)
    home.search_build()

    results = SearchResultsPage(driver)
    results.verify_products_contain_build()
    results.write_product_names_list()

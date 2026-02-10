"""
Automated tests: home and search.
Tests only call page methods; no direct Selenium or locator logic here.
"""
import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_search_box_visible(driver):
    """Search input is present on home page (uses actions + locators from JSON)."""
    home = HomePage(driver)
    assert home.actions.is_displayed("home_page", "search_input")


def test_search_returns_results(driver):
    """Search for 'computer' and verify results are shown."""
    home = HomePage(driver)
    home.search("computer")
    results = SearchResultsPage(driver)
    products = results.get_result_products()
    assert len(products) > 0

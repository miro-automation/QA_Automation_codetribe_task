"""
Test: validate product name and price for each search result.
Only method calls – logic in page objects.
"""
import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

pytestmark = [pytest.mark.order(3)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.search
@pytest.mark.product_validation
def test_validate_product_name_and_price(driver):
    """Steps:
    1. Search for Build.
    2. For each search result, assert product name contains letters and price is valid (digits and decimal only).
    """
    assert driver is not None, "Driver fixture should be available."
    home = HomePage(driver)
    home.search_build()

    results = SearchResultsPage(driver)
    err = results.verify_each_result_has_valid_name_and_price()
    assert err is None, err or "Each search result should have valid name (letters) and price (digits and . only)."

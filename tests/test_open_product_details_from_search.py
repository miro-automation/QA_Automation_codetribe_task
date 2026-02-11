"""
Test: open first product from search results and verify product details page.
Asserts: first item has Add to cart; details page has non-empty title, valid price, Add to cart visible.
"""
import pytest

from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.search_results_page import SearchResultsPage

pytestmark = [pytest.mark.order(3)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.search
@pytest.mark.product_validation
def test_open_product_details_from_search(driver):
    """Search by Build; assert first result has Add to cart; open first product in current tab; verify title, price, Add to cart on details page."""
    assert driver is not None, "Driver fixture should be available."
    home = HomePage(driver)
    home.search_build()

    results = SearchResultsPage(driver)
    err = results.verify_first_item_has_add_to_cart()
    assert err is None, err or "First search result item should have visible 'Add to cart' button."

    results.open_first_product_in_current_tab()

    details = ProductDetailsPage(driver)
    err = details.verify_title_not_empty()
    assert err is None, err or "Product details page should have non-empty title (h1)."

    err = details.verify_price_valid()
    assert err is None, err or "Product details page should show a numeric, non-empty price."

    assert details.is_add_to_cart_visible(), "Product details page should show 'Add to cart' button."

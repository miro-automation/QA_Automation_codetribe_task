"""
Login with credentials from last successful registration; assert user is on home with email and Log out visible.
"""
import pytest

from core.registered_user import load_registered_user
from pages.login_page import LoginPage


pytestmark = [pytest.mark.pa, pytest.mark.ui, pytest.mark.login, pytest.mark.order(2)]


def test_login_success(driver):
    """Use saved registered user credentials; login; assert header shows email and Log out link (user on home)."""
    assert driver is not None, "Driver fixture should be available."
    try:
        creds = load_registered_user()
    except FileNotFoundError:
        pytest.skip("No saved registered user. Run test_register_success first (registration tests must run before login).")
    email = creds["email"]
    password = creds["password"]

    page = LoginPage(driver)
    page.login_with(email, password)

    assert page.is_logout_link_visible(), "After successful login, 'Log out' link should be visible in header."
    assert page.is_logged_in_as(email), (
        f"Header should show logged-in user email ({email}). "
        "User should be on home with email and Log out visible."
    )

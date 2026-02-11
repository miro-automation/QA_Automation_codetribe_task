"""
Login with saved registered user, then click Log out; assert user is logged out (Log in link visible again).
"""
import pytest

from core.registered_user import load_registered_user
from pages.login_page import LoginPage


pytestmark = [pytest.mark.pa, pytest.mark.ui, pytest.mark.login, pytest.mark.order(2)]


def test_logout(driver):
    """Login with saved credentials, then click Log out; assert Log out disappears and Log in is visible."""
    assert driver is not None, "Driver fixture should be available."
    try:
        creds = load_registered_user()
    except FileNotFoundError:
        pytest.skip("No saved registered user. Run test_register_success first.")
    page = LoginPage(driver)
    page.login_with(creds["email"], creds["password"])
    assert page.is_logout_link_visible(), "Precondition: user must be logged in before logout."

    page.actions.click("login", "logout_link")

    assert page.is_logout_link_absent(), "After logout, 'Log out' link should not be visible."
    assert page.actions.is_displayed("login", "login_link"), (
        "After logout, 'Log in' link should be visible again in header."
    )

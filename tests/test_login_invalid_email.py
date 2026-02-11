"""
Login with invalid email (wrong format or non-existent); assert user is not logged in.
"""
import pytest

from pages.login_page import LoginPage


pytestmark = [pytest.mark.pa, pytest.mark.ui, pytest.mark.login, pytest.mark.order(2)]


def test_login_invalid_email(driver):
    """Steps:
    1. Enter invalid/non-existent email and any password.
    2. Click Login.
    3. Assert Log out link is not visible (login failed).
    """
    assert driver is not None, "Driver fixture should be available."
    page = LoginPage(driver)
    page.login_with("nonexistent@invalid.example", "SomePass123!")

    assert page.is_logout_link_absent(), (
        "User must not be logged in when using invalid/non-existent email."
    )

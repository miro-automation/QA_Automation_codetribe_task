"""
Login with valid-format email but wrong password; assert user is not logged in.
"""
import pytest

from pages.login_page import LoginPage


pytestmark = [pytest.mark.pa, pytest.mark.ui, pytest.mark.login, pytest.mark.order(2)]


def test_login_invalid_password(driver):
    """Login with valid email and wrong password; assert Log out is not visible (login failed)."""
    assert driver is not None, "Driver fixture should be available."
    page = LoginPage(driver)
    page.login_with("anyuser@example.com", "WrongPassword123!")

    assert page.is_logout_link_absent(), (
        "User must not be logged in when password is incorrect."
    )

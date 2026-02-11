"""
Login with empty email and password; assert user is not logged in.
"""
import pytest

from pages.login_page import LoginPage


pytestmark = [pytest.mark.pa, pytest.mark.ui, pytest.mark.login, pytest.mark.order(2)]


def test_login_empty_fields(driver):
    """Steps:
    1. Open login page; leave email and password empty.
    2. Click Login.
    3. Assert Log out link is not visible (user not logged in).
    """
    assert driver is not None, "Driver fixture should be available."
    page = LoginPage(driver)
    page.open_login_page()
    page.click_login_button()

    assert page.is_logout_link_absent(), (
        "User must not be logged in when email and password are empty."
    )

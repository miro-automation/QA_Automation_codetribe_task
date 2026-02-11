"""
Register: fill all fields with spaces only and assert required validation.
"""
import pytest

from pages.register_page import RegisterPage, load_register_data

pytestmark = [pytest.mark.order(1)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.register
def test_register_empty_spaces(driver):
    """Fill form with only spaces; submit; assert required validation messages."""
    assert driver is not None, "Driver fixture should be available."
    data = load_register_data()
    spaces = data.get("empty_spaces", "   ")

    page = RegisterPage(driver)
    page.open_register()
    page.fill_first_name(spaces)
    page.fill_last_name(spaces)
    page.fill_email(spaces)
    page.fill_password(spaces)
    page.fill_confirm_password(spaces)
    page.click_register()

    assert "First name is required." in page.get_validation_message("first_name"), (
        "First name required when only spaces."
    )
    assert "Last name is required." in page.get_validation_message("last_name"), (
        "Last name required when only spaces."
    )
    assert "Email is required." in page.get_validation_message("email"), (
        "Email required when only spaces."
    )
    assert "Password is required." in page.get_validation_message("password"), (
        "Password required when only spaces."
    )

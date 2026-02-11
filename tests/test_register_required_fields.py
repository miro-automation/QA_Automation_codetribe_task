"""
Register: submit empty form and assert all required field validation messages.
"""
import pytest

from pages.register_page import RegisterPage

pytestmark = [pytest.mark.order(1)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.register
def test_register_required_fields(driver):
    """Steps:
    1. Open register page.
    2. Click Register without filling any field.
    3. Assert validation messages for First name, Last name, Email, Password, Confirm password.
    """
    assert driver is not None, "Driver fixture should be available."
    page = RegisterPage(driver)
    page.open_register()
    page.click_register()

    assert "First name is required." in page.get_validation_message("first_name"), (
        "First name required message should appear."
    )
    assert "Last name is required." in page.get_validation_message("last_name"), (
        "Last name required message should appear."
    )
    assert "Email is required." in page.get_validation_message("email"), (
        "Email required message should appear."
    )
    assert "Password is required." in page.get_validation_message("password"), (
        "Password required message should appear."
    )
    assert "Password is required." in page.get_validation_message("confirm_password"), (
        "Confirm password required message should appear."
    )

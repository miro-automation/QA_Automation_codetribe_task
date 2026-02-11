"""
Register: valid names and passwords but invalid email format; assert 'Wrong email'.
"""
import pytest

from pages.register_page import RegisterPage, load_register_data

pytestmark = [pytest.mark.order(1)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.register
def test_register_invalid_email(driver):
    """Fill valid names and passwords but invalid email; assert Wrong email message."""
    assert driver is not None, "Driver fixture should be available."
    data = load_register_data()
    valid = data["valid"]
    invalid_email = data.get("invalid_email", "notanemail")

    page = RegisterPage(driver)
    page.open_register()
    page.select_gender_female()
    page.fill_first_name(valid["first_name"])
    page.fill_last_name(valid["last_name"])
    page.fill_email(invalid_email)
    page.fill_password(valid["password"])
    page.fill_confirm_password(valid["password"])
    page.click_register()

    msg = page.get_validation_message("email")
    assert "Wrong email" in msg, f"Expected 'Wrong email' in validation message, got: {msg!r}"

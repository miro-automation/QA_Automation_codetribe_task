"""
Register: valid data but Confirm password different from Password; assert mismatch message.
"""
import pytest

from pages.register_page import RegisterPage, load_register_data

pytestmark = [pytest.mark.order(1)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.register
def test_register_password_mismatch(driver):
    """Steps:
    1. Open register page; select gender; fill valid first name, last name, email, password.
    2. Fill Confirm password with a different value.
    3. Click Register.
    4. Assert validation message: password and confirmation do not match.
    """
    assert driver is not None, "Driver fixture should be available."
    data = load_register_data()
    valid = data["valid"]
    other_password = data.get("password_mismatch_confirm", "OtherPass456!")

    page = RegisterPage(driver)
    page.open_register()
    page.select_gender_male()
    page.fill_first_name(valid["first_name"])
    page.fill_last_name(valid["last_name"])
    page.fill_email(valid["email"])
    page.fill_password(valid["password"])
    page.fill_confirm_password(other_password)
    page.click_register()

    msg = page.get_validation_message("confirm_password")
    assert "password and confirmation password do not match" in msg, (
        f"Expected password mismatch message, got: {msg!r}"
    )

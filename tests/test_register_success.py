"""
Register: fill all fields with valid data from register_data.json; assert registration completed.
"""
import time

import pytest

from pages.register_page import RegisterPage, load_register_data


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.register
def test_register_success(driver):
    """Fill form with valid data (unique email); submit; assert 'Your registration completed'."""
    assert driver is not None, "Driver fixture should be available."
    data = load_register_data()
    valid = data["valid"]
    unique_email = f"test.{int(time.time())}@example.com"

    page = RegisterPage(driver)
    page.open_register()
    page.select_gender_female()
    page.fill_first_name(valid["first_name"])
    page.fill_last_name(valid["last_name"])
    page.fill_email(unique_email)
    page.fill_password(valid["password"])
    page.fill_confirm_password(valid["password"])
    page.click_register()

    assert page.is_registration_success(), (
        "Expected 'Your registration completed' message after valid registration."
    )

"""
Register: fill all fields with valid data from register_data.json; assert registration completed.
Saves email and password to output/last_registered_user.json for login tests.
Uses a unique email per run (timestamp) so we never hit 'already registered' when re-running tests.
"""
import time

import pytest

from core.registered_user import save_registered_user
from pages.register_page import RegisterPage, load_register_data

pytestmark = [pytest.mark.order(1)]


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.register
def test_register_success(driver):
    """Fill form with valid data (unique email per run); submit; assert 'Your registration completed'; save credentials for login."""
    assert driver is not None, "Driver fixture should be available."
    data = load_register_data()
    valid = data["valid"]
    # Unique email every run so we avoid "already registered" when tests are run multiple times
    unique_email = f"test.{time.time_ns()}@example.com"

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
    save_registered_user(unique_email, valid["password"])

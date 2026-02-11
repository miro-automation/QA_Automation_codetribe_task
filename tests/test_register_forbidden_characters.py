"""
Register: forbidden characters in name field.
Expected: validation message on form. Test MUST FAIL if application shows 'internal error' page (bug).
"""
import pytest

from core.bug_reporter import record_bug
from pages.register_page import RegisterPage, load_register_data


@pytest.mark.pa
@pytest.mark.ui
@pytest.mark.register
def test_register_forbidden_characters(driver):
    """Fill first name with forbidden characters. Fail if app shows internal error page; expect validation message."""
    assert driver is not None, "Driver fixture should be available."
    data = load_register_data()
    valid = data["valid"]
    forbidden = data.get("forbidden_chars_name", "<script>alert(1)</script>")

    page = RegisterPage(driver)
    page.open_register()
    page.fill_first_name(forbidden)
    page.fill_last_name(valid["last_name"])
    page.fill_email(valid["email"])
    page.fill_password(valid["password"])
    page.fill_confirm_password(valid["password"])
    page.click_register()

    if page.is_internal_error_page():
        record_bug(
            test_id="test_register_forbidden_characters",
            summary="Application showed 'internal error' page (errorpage.htm) instead of validation message on register form.",
            details={
                "URL": page.driver.current_url,
                "Scenario": "First name contained forbidden characters (e.g. script tag); expected client-side validation.",
            },
        )
        pytest.fail(
            "Application showed 'internal error' page (errorpage.htm). "
            "Expected validation message on register form, not a server error. This is a BUG."
        )

    assert not page.is_registration_success(), (
        "Registration must not succeed when first name contains forbidden characters."
    )
    first_name_msg = page.get_validation_message("first_name")
    assert first_name_msg, (
        "Expected validation message for first name when it contains forbidden characters."
    )

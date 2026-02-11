"""Register page. Form fill and validation message helpers."""
import json
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import BASE_URL
from pages.base_page import BasePage

_REGISTER_DATA_PATH = Path(__file__).resolve().parent.parent / "config" / "register_data.json"
_VALIDATION_KEYS = {
    "first_name": "validation_first_name",
    "last_name": "validation_last_name",
    "email": "validation_email",
    "password": "validation_password",
    "confirm_password": "validation_confirm_password",
}


def load_register_data() -> dict:
    """Load register_data.json."""
    with open(_REGISTER_DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


class RegisterPage(BasePage):
    """Registration form. All interactions via self.actions and locators from JSON."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "register")

    def open_register(self) -> None:
        """Navigate to register page."""
        self.driver.get(f"{BASE_URL.rstrip('/')}/register")

    def fill_first_name(self, text: str) -> None:
        self.actions.send_keys("register", "first_name", text or "")

    def fill_last_name(self, text: str) -> None:
        self.actions.send_keys("register", "last_name", text or "")

    def fill_email(self, text: str) -> None:
        self.actions.send_keys("register", "email", text or "")

    def fill_password(self, text: str) -> None:
        self.actions.send_keys("register", "password", text or "")

    def fill_confirm_password(self, text: str) -> None:
        self.actions.send_keys("register", "confirm_password", text or "")

    def select_gender_male(self) -> None:
        self.actions.click("register", "gender_male")

    def select_gender_female(self) -> None:
        self.actions.click("register", "gender_female")

    def click_register(self) -> None:
        self.actions.click("register", "register_button")

    def get_validation_message(self, field: str) -> str:
        """Get visible validation error text for field (first_name, last_name, email, password, confirm_password)."""
        key = _VALIDATION_KEYS.get(field)
        if not key:
            return ""
        try:
            return (self.actions.get_text("register", key) or "").strip()
        except Exception:
            return ""

    def is_registration_success(self) -> bool:
        """Return True if 'Your registration completed' message is visible (successful registration)."""
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        from config.settings import IMPLICIT_WAIT
        try:
            el = WebDriverWait(self.driver, IMPLICIT_WAIT).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Your registration completed')]")
                )
            )
            return el.is_displayed()
        except Exception:
            return False

    def is_internal_error_page(self) -> bool:
        """Return True if the application showed 'internal error' page (errorpage.htm). This is a BUG - test should fail."""
        try:
            url = (self.driver.current_url or "").lower()
            if "errorpage" in url or "aspxerrorpath" in url:
                return True
            body = (self.driver.find_element(By.TAG_NAME, "body").text or "").lower()
            return "internal error occurred" in body
        except Exception:
            return False


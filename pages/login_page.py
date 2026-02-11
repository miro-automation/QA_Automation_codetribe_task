"""Login page: click Log in link, fill credentials, submit; check logged-in state (email in header, Log out)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import BASE_URL, IMPLICIT_WAIT, SHORT_WAIT
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login flow and logged-in checks. Uses locators from login section."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "")

    def click_login_link(self) -> None:
        """Click 'Log in' in header (a.ico-login)."""
        self.actions.click("login", "login_link")

    def open_login_page(self) -> None:
        """Navigate directly to login page."""
        self.driver.get(f"{BASE_URL.rstrip('/')}/login")

    def fill_email(self, text: str) -> None:
        self.actions.send_keys("login", "email", text or "")

    def fill_password(self, text: str) -> None:
        self.actions.send_keys("login", "password", text or "")

    def click_login_button(self) -> None:
        """Click the 'Log in' submit button on the login form."""
        self.actions.click("login", "login_button")

    def login_with(self, email: str, password: str) -> None:
        """Open login page, fill email and password, submit."""
        self.open_login_page()
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()

    def is_logout_link_visible(self, timeout: int | None = None) -> bool:
        """Return True if 'Log out' link is visible (user is logged in). Use timeout for wait (default IMPLICIT_WAIT)."""
        t = timeout if timeout is not None else IMPLICIT_WAIT
        return self.actions.is_displayed("login", "logout_link", timeout=t)

    def is_logout_link_absent(self) -> bool:
        """Return True if 'Log out' link is not visible within SHORT_WAIT (use when expecting user not logged in)."""
        return not self.actions.is_displayed("login", "logout_link", timeout=SHORT_WAIT)

    def get_header_account_text(self) -> str:
        """Return text of the account link in header (usually the email when logged in)."""
        try:
            return (self.actions.get_text("login", "header_account_link") or "").strip()
        except Exception:
            return ""

    def is_logged_in_as(self, email: str) -> bool:
        """Return True if user is logged in (Log out visible) and header or page shows the given email."""
        if not self.is_logout_link_visible():
            return False
        account_text = self.get_header_account_text()
        if email.strip().lower() in (account_text or "").lower():
            return True
        try:
            body = (self.driver.find_element(By.TAG_NAME, "body").text or "").lower()
        except Exception:
            body = ""
        return email.strip().lower() in body

"""Home page. All interactions use core.BaseActions and locators from JSON."""
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class HomePage(BasePage):
    """Home page of Demo Web Shop. Methods only call self.actions with section/key."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "")

    def search(self, search_term: str) -> None:
        """Type in search box and submit. Uses locators: home_page.search_input, home_page.search_button."""
        self.actions.send_keys("home_page", "search_input", search_term)
        self.actions.click("home_page", "search_button")

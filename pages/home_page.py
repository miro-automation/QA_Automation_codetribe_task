"""Home page. All interactions use core.BaseActions and locators from JSON."""
from selenium.webdriver.remote.webdriver import WebDriver

from config.data_loader import get_value
from pages.base_page import BasePage


class HomePage(BasePage):
    """Home page of Demo Web Shop. Methods only call self.actions with section/key."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "")

    def is_search_visible(self) -> bool:
        """True if search field is displayed. Locators stay in page object."""
        return self.actions.is_displayed("Products", "search_button")

    def click_search_input(self) -> None:
        """Click on search field (Products.search_button, id: small-searchterms)."""
        self.actions.click("Products", "search_button")

    def type_search(self, text: str) -> None:
        """Type into search field. Uses Products.search_button."""
        self.actions.send_keys("Products", "search_button", text)

    def click_search_submit(self) -> None:
        """Click submit inside div.search-box (Products.search_submit)."""
        self.actions.click("Products", "search_submit")

    def search_with_keyword(self, keyword: str) -> None:
        """Click search, type keyword, submit. Single call for the full flow."""
        self.click_search_input()
        self.type_search(keyword)
        self.click_search_submit()

    def search_build(self) -> None:
        """Search by keyword from static data (Products.Build)."""
        keyword = get_value("Products", "Build")
        self.search_with_keyword(keyword)

    def search(self, search_term: str) -> None:
        """Type in search box. Uses locators: Products.search_button (id: small-searchterms)."""
        self.actions.send_keys("Products", "search_button", search_term)

"""Configuration for Demo Web Shop. Single source for URL and timeouts."""
from typing import Final

BASE_URL: Final[str] = "https://demowebshop.tricentis.com/"
IMPLICIT_WAIT: Final[int] = 10
PAGE_LOAD_TIMEOUT: Final[int] = 30
# Short wait when we expect an element to be absent (e.g. "not logged in" checks)
SHORT_WAIT: Final[int] = 2

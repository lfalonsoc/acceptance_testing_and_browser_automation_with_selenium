from typing import Any, Tuple

from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE: Tuple[Any, str] = (By.TAG_NAME, 'h1')
    NAV_LINKS: Tuple[Any, str] = (By.CLASS_NAME, 'nav-link')
from typing import Any, Tuple

from selenium.webdriver.common.by import By


class HomePageLocators:
    NAVIGATION_LINK: Tuple[Any, str] = (By.ID, 'blog-link')
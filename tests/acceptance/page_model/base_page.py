from typing import Any

from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver: Any) -> None:
        self.driver: Any = driver
    
    @property
    def url(self) -> str:
        return 'http://127.0.0.1:5000'
    
    @property
    def title(self) -> Any:
        return self.driver.find_element(*BasePageLocators.TITLE)
    
    @property
    def navigation(self) -> Any:
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

from typing import Any

from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):    
    @property
    def url(self) -> str:
        return super(HomePage, self).url + '/'
    
    @property
    def blog_link(self) -> Any:
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)
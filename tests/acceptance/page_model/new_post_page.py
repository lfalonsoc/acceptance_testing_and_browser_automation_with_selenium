from typing import Any

from selenium.webdriver.common.by import By

from tests.acceptance.locators.new_post_page import NewPostPageLocators
from tests.acceptance.page_model.base_page import BasePage


class NewPostPage(BasePage):
    @property
    def url(self) -> Any:
        return super(NewPostPage, self).url + '/post'

    @property
    def form(self) -> Any:
        return self.driver.find_element(*NewPostPageLocators.NEW_POST_FORM)

    @property
    def submit_button(self) -> Any:
        return self.driver.find_element(*NewPostPageLocators.SUBMIT_BUTTON)

    def form_field(self, name: str) -> Any:
        return self.driver.find_element(By.NAME, name)

from typing import Any

from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')


@given('I wait for the posts to load')
def step_impl(context: Any) -> None:
    WebDriverWait(context.driver, 10).until(
        expected_conditions.visibility_of_element_located(
            BlogPageLocators.POSTS_SECTION
        )
    )
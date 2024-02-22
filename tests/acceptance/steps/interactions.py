from typing import Any

from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


# @when('I click on the link with id "blog-link"')
@when('I click on the "(.*)" link') # Se cambia por expresión regular
def step_impl(context: Any, link_text: str) -> None:
    page: BasePage = BasePage(context.driver)
    links: Any = page.navigation
    
    matching_links: list[Any] =[l for l in links if l.text == link_text]
    
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context: Any, content: str, field_name: str) -> None:
    page: NewPostPage = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I press the submit button')
def step_impl(context: Any) -> None:
    page: Any = NewPostPage(context.driver)
    page.submit_button.click()

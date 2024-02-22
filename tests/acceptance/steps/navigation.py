from typing import Any

from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context: Any) -> None:
    context.driver = webdriver.Firefox()
    page: HomePage = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context: Any) -> None:
    context.driver = webdriver.Firefox()
    page: BlogPage = BlogPage(context.driver)
    context.driver.get(page.url)


@given('I am on the new post page')
def step_impl(context: Any) -> None:
    context.driver = webdriver.Firefox()
    page: NewPostPage = NewPostPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context: Any) -> None:
    expected_url: BlogPage = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context: Any) -> None:
    expected_url: HomePage = HomePage(context.driver).url
    assert context.driver.current_url == expected_url

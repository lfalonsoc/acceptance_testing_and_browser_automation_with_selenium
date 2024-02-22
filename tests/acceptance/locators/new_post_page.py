from typing import Any, Tuple

from selenium.webdriver.common.by import By


class NewPostPageLocators:
    NEW_POST_FORM: Tuple[Any, str] = (By.ID, 'post-form')
    TITLE_FIELD: Tuple[Any, str] = (By.ID, 'title')
    CONTENT_FIELD: Tuple[Any, str] = (By.ID, 'content')
    SUBMIT_BUTTON: Tuple[Any, str] = (By.ID, 'create-post')
from typing import Any, Tuple

from selenium.webdriver.common.by import By


class BlogPageLocators:
    ADD_POST_LINK: Tuple[Any, str] = (By.ID, 'add-post-link')
    POSTS_SECTION: Tuple[Any, str] = (By.ID, 'posts')
    POST: Tuple[Any, str] = (By.CLASS_NAME, 'post-link')
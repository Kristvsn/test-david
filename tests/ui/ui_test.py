import pytest
from pages.some_page import SomePage
from tests.ui.helpers.assertions import UIAssertions

@pytest.mark.ui
def test_button_redirects_to_json_server(page, get_base_url):
    """
    Тест редиректа по нажатию на кнопку.

    :param page: объект страницы
    :param get_base_url: fixture для установки base url
    """
    some_page = SomePage(page, get_base_url)
    some_page.open_page()

    button = some_page.get_json_server_button("JSON Server")
    UIAssertions.assert_element_visible(button)
    button.click()

    UIAssertions.assert_url_contains(page, "json-server")

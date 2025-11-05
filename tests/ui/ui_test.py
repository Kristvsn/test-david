import pytest
from pages.some_page import SomePage
from tests.ui.helpers.assertions import UIAssertions

@pytest.mark.ui
def test_button_redirects_to_json_server(page, get_base_url):
    """,scnhj
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

@pytest.mark.ui
def test_filter_vklady(page, get_base_url):
    vklady_page = SomePage(page, get_base_url)
    vklady_page.open()

    vklady_page.click_all_filters("Все фильтры")
    page.wait_for_timeout(4000)
    vklady_page.choose_opening_method("Онлайн")
    page.wait_for_timeout(2000)

@pytest.mark.ui
def test_check_mfo_terms(page, get_base_url):
    some_page = SomePage(page, get_base_url)
    some_page.open()

    elements = some_page.get_popup_element()
    expected_texts = [
        "Чтобы заполнить анкету и узнать персональные условия по займу",
        "Оформление за 5 минут",
        "Высокая вероятность одобрения",
        "Без скрытых условий"
    ]

    UIAssertions.assert_check_many_texts(elements, expected_texts)

@pytest.mark.ui
def test_calendar(page, get_base_url):
    vklady_page = SomePage(page, get_base_url)
    vklady_page.open()

    # page.wait_for_timeout(2000)
    vklady_page.input_date(1)
    # page.wait_for_timeout(3000)
    page.wait_for_timeout(3000)

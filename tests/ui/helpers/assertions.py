class UIAssertions:
    """
    Асерты для проверок.

    """

    @staticmethod
    def assert_text_equals(element, expected_text: str):
        """
        Асерт проверки текста.

        :param element: элемент для проверки (НЕ селектор)
        :param expected_text: ожидаемый текст
        """
        actual_text = element.text
        assert actual_text == expected_text, (
            f'Ожидался текст: "{expected_text}", но получен: "{actual_text}"'
        )

    @staticmethod
    def assert_element_visible(element):
        """
        Асерт проверки отображения элемента.

        :param element: элемент для проверки (НЕ селектор)
        """
        assert element.is_visible(), "Элемент не отображается на странице"

    @staticmethod
    def assert_url_contains(page, expected_part: str):
        """
        Асерт проверки подстроки в url.

        :param page: объект страницы
        :param expected_part: подстрока, которую ожидаем увидеть в url
        """
        current_url = page.url
        assert expected_part in current_url, f"Ожидали, что URL содержит '{expected_part}', но получили '{current_url}'"

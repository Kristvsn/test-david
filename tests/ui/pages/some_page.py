from tests.ui.pages.base_page import BasePage

class SomePage(BasePage):
    JSON_SERVER_BUTTON_XPATH = "//a[text()='{text}']"
    ENDPOINT='/'
    """
    Методы/ для работы с какой-нибудь страницей UI.

    Методы позволяют работать с конкретными элементами
    страницы.
    """

    def open(self):
        """
        Открывает корневую страницу /.
        """
        self.open_page(self.ENDPOINT)

    def click_button(self, text: str = "JSON Server"):
        """
        Кликает на кнопку с текстом.

        :param text: текст кнопки - по дефолту JSON Server
        """
        xpath = self.JSON_SERVER_BUTTON_XPATH.format(text=text)
        self.click(xpath)

    def get_json_server_button(self, text: str = "JSON Server"):
        """
        Забирает элемент с текстом для дальнейшей работы с ним

        :param text: текст кнопки - по дефолту JSON Server
        """
        xpath = self.JSON_SERVER_BUTTON_XPATH.format(text=text)
        return self.find(xpath)

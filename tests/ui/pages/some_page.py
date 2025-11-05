from tests.ui.pages.base_page import BasePage
from tests.ui.locators.locators import SomePageLocators
from tests.ui.helpers.assertions import UIAssertions

class SomePage(BasePage):
    JSON_SERVER_BUTTON_XPATH = "//a[text()='{text}']"
    ENDPOINT="/vzr/"
    FILTERS_BUTTON = "[class*='DepositFilters_button']"
    OPENING_METHOD_CHECKBOX = "label[data-qa='Radio'] span"

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

    def click_all_filters(self, text: str):
        self.click_by_selector_and_exact_text(self.FILTERS_BUTTON, text)

    def choose_opening_method(self, text: str):
        self.click_by_selector_and_exact_text(self.OPENING_METHOD_CHECKBOX, text)

    def get_popup_element(self):
       return self.find(str(SomePageLocators.POP_UP_TERMS))

    def input_date(self, offset_days: int):
        self.click(SomePageLocators.DATE_INPUT)
        day = UIAssertions.generate_day_after_offset(offset_days)
        self.page.locator(SomePageLocators.CALENDAR_DAY).get_by_text(day).nth(0).click()


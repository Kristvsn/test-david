class BasePage:
    """
    Базовые методы для работы с UI.

    Методы позволяют открываеть страницу, находить элементы на странице
    кликать на элемент, заполнять, находить текст.
    """

    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open_page(self, endpoint: str = ""):
        """
        Открывает страницу.

        :param endpoint: эндпоинт к base url
        """
        full_url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        self.page.goto(full_url)

    def find(self, selector: str):
        """
        Находит элемент на странице и возвращает его.

        :param selector: локатор на странице
        """
        return self.page.locator(selector)

    def click(self, selector: str):
        """
         Кликает на элемент.

         :param selector: локатор на странице
         """
        self.page.locator(selector).click()

    def type(self, selector: str, text: str):
        """
         Заполняет input.

         :param selector: локатор на странице
         :param text: текст, которым надо заполнить
         """
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str):
        """
         Забирает и возвращает текст из элемента.

         :param selector: локатор на странице
         """
        return self.page.locator(selector).inner_text()

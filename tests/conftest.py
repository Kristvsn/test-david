# conftest.py
import os
import logging
import pytest
from dotenv import load_dotenv
from tests.api.api_frame.todo_api import TodoApi
from tests.api.api_frame.mock_api import MockApi
from tests.api.api_frame.inventory_api import PetstoreApi

# ✅ Загружаем .env один раз при старте pytest
load_dotenv()

# 🔧 Логирование
def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("test.log")
        ]
    )
    logging.info("Логирование инициализировано через conftest.py")

# 🌐 BASE_URL из .env
@pytest.fixture(scope="session")
def get_base_url() -> str:
    base_url = os.getenv("BASE_URL")
    if not base_url:
        pytest.fail("BASE_URL не задан в .env")
    return base_url

# 🔢 COUNT из .env
@pytest.fixture(scope="session")
def get_default_count_todo_items() -> int:
    count = os.getenv("DEFAULT_COUNT_TODO_ITEMS", "5")
    try:
        return int(count)
    except ValueError:
        pytest.fail("DEFAULT_COUNT_TODO_ITEMS должен быть числом")

# 📦 API-клиент
@pytest.fixture()
def get_todo_data(get_base_url):
    return TodoApi(get_base_url)

@pytest.fixture()
def get_mock(get_base_url):
    return MockApi(get_base_url)

# 🧭 Playwright Page
@pytest.fixture()
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def get_petstore_url() -> str:
    petstore_url = os.getenv("PETSTORE_URL")
    if not petstore_url:
        pytest.fail("PETSTORE_URL не задан в .env")
    return petstore_url

@pytest.fixture()
def get_petstore_data(get_petstore_url):
    return PetstoreApi(get_petstore_url)
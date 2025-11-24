import pytest
from requests import Response
from tests.api.helpers.assertions import Assertions

@pytest.mark.inventory
def test_get_inventory(get_petstore_data):
    """
    Проверка получения списка питомцев
    Ожидаем статус кода 200 и json-ответ
    """
    for_response:Response= get_petstore_data.get_inventory()
    Assertions.assert_status_code(for_response, 200)
    Assertions.assert_json_is_dict(for_response)

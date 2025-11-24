from tests.api.api_frame.base_api import BaseApi
import requests

class PetstoreApi(BaseApi):
    ENDPOINT_URL:str='v2/store/inventory'

    def get_inventory(self)->requests.Response:
        """
        Получение списка всех питомцев
        """
        return self.get_request(endpoint=self.ENDPOINT_URL)
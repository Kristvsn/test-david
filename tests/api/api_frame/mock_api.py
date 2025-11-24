from tests.api.api_frame.base_api import BaseApi
import requests

class MockApi(BaseApi):
    USER_ENDPOINT: str = 'user/42'

    def user42(self) -> requests.Response:
        return self.get_request(self.USER_ENDPOINT)

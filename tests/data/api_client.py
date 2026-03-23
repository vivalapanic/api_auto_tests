import requests
from tests.data import auf_data


class APIclient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = auf_data.base_url
        self.token = None

    def auth(self):
        url = f"{self.base_url}/auth"

        response = self.session.post(url, json=auf_data.credentials)

        assert response.status_code == 200, "Auth failed"

        self.token = response.json().get("token")
        assert self.token is not None, "No token received"

        self.session.cookies.set("token", self.token)

        return response
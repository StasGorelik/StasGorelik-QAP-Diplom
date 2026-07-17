import json

import requests


class HttpClient:
    DOMAIN = "http://localhost:8000"

    def make_request(self, method, url, body: dict | None = None, headers: dict | None = None):
        response = requests.request(
            method, self.DOMAIN + url, data=json.dumps(body), headers=headers)

        try:
            response.raise_for_status()
            if response.status_code == 204 or not response.text.strip():
                return {}

            response_json = response.json()
            return response_json
        except requests.exceptions.HTTPError:
            return None

    def get(self, url, headers: dict | None = None):
        return self.make_request(method='GET', url=url, headers=headers)

    def post(self, url, body: dict | None = None, headers: dict | None = None):
        return self.make_request(method='POST', url=url, body=body, headers=headers)

    def put(self, url, body: dict | None = None, headers: dict | None = None):
        return self.make_request(method='PUT', url=url, body=body, headers=headers)

    def delete(self, url, headers: dict | None = None):
        return self.make_request(method='DELETE', url=url, headers=headers)

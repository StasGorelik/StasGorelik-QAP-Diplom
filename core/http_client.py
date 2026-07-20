import json
import requests
from core.log_base import logger


class HttpClient:
    DOMAIN = "http://localhost:8000"

    def make_request(self, method, url, body: dict | None = None, headers: dict | None = None):
        logger.info(f"Отправка запроса: {method} {self.DOMAIN + url}")
        response = requests.request(
            method, self.DOMAIN + url, data=json.dumps(body), headers=headers)

        try:
            logger.info(f"Получен ответ [{response.status_code}] для {response.url}")
            response.raise_for_status()
            if not response.text:
                logger.info('%s: No content (status %s)', response.url, response.status_code)
                return {}

            response_json = response.json()
            logger.info(f'{response.url}::{response_json}')
            return response_json
        except requests.exceptions.HTTPError as err:
            logger.error(f'Ошибка {err}')
            return None

    def get(self, url, headers: dict | None = None):
        return self.make_request(method='GET', url=url, headers=headers)

    def post(self, url, body: dict | None = None, headers: dict | None = None):
        return self.make_request(method='POST', url=url, body=body, headers=headers)

    def put(self, url, body: dict | None = None, headers: dict | None = None):
        return self.make_request(method='PUT', url=url, body=body, headers=headers)

    def delete(self, url, headers: dict | None = None):
        return self.make_request(method='DELETE', url=url, headers=headers)

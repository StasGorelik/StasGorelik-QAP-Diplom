from core.http_client import HttpClient
from models.token import TokenResponse


class AuthServise(HttpClient):
    auth_url = '/auth'

    def login(self, email, password):
        body = {
            "email": email,
            "password": password
        }

        return TokenResponse(**HttpClient().post(f'{self.auth_url}/login', body=body))

    def registration_user(self, username, email, password):
        body = {
            "username": username,
            "email": email,
            "password": password
        }

        return TokenResponse(**HttpClient().post(f'{self.auth_url}/register', body=body))

from core.http_client import HttpClient
from models.user import UserResponse


class GetUserService(HttpClient):
    users_url = '/users'

    def get_users_list(self, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        users = self.get(
            f"{self.users_url}/?skip=0&limit=100", headers=headers)

        users_objects = [UserResponse(**user) for user in users]
        return users_objects

    def get_user_me(self, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }

        return UserResponse(**HttpClient().get(f"{self.users_url}/me", headers=headers))

    def update_user(self, username, email, role, user_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }

        body = {
            "username": username,
            "email": email,
            "role": role,
            "avatar_url": "string"
        }

        return UserResponse(**HttpClient().put(f"{self.users_url}/{user_id}", headers=headers, body=body))

    def delete_user(self, user_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "*/*"
        }

        return self.delete(f"{self.users_url}/{user_id}", headers=headers)

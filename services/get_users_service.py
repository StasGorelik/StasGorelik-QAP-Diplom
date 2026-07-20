from core.http_client import HttpClient
from models.user import UserResponse
from models.tasks import TaskResponse


class GetUserService(HttpClient):
    users_url = '/users'

    def get_users_list(self, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        users = self.get(
            f"{self.users_url}/?skip=0&limit=200", headers=headers)

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

    def get_user_me_tasks(self, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }

        tasks = self.get(f"{self.users_url}/me/tasks?skip=0&limit=100", headers=headers)

        tasks_objects = [TaskResponse(**task) for task in tasks]

        return tasks_objects

    def get_public_users_list(self):

        headers = {
            "accept": "application/json"
        }
        users = self.get(
            f"{self.users_url}/public?skip=0&limit=100", headers=headers)

        users_objects = [UserResponse(**user) for user in users]
        return users_objects

    def update_user_avatar(self, access_token, user_id):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        body = {
            "avatar_url": "New_AVATAR"
        }

        return self.put(f"{self.users_url}/{user_id}/avatar]", headers=headers, body=body)

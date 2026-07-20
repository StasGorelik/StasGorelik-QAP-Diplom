from core.http_client import HttpClient
from models.tasks import TaskResponse


class TaskService(HttpClient):
    tasks_url = '/boards'

    def create_task(self, title, description, board_id, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        body = {
            "title": title,
            "description": description,
            "status": "todo",
            "priority": "medium",
            "assignee_id": 0
        }
        return TaskResponse(**HttpClient().post(f"{self.tasks_url}/{board_id}/tasks", body=body, headers=headers))

    def get_task_by_id(self, board_id, task_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return TaskResponse(**HttpClient().get(f"{self.tasks_url}/{board_id}/tasks/{task_id}", headers=headers))

    def delete_task(self, board_id, task_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return HttpClient().delete(f"{self.tasks_url}/{board_id}/tasks/{task_id}", headers=headers)

    def update_task(self, title, description, board_id, task_id, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        body = {
            "title": title,
            "description": description,
            "status": "todo",
            "priority": "medium",
            "assignee_id": 0
        }
        return TaskResponse(**HttpClient().put(f"{self.tasks_url}/{board_id}/tasks/{task_id}",
                                               body=body, headers=headers))

    def remove_task_to_another_board(self, board_id, task_id, target_board_id, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }

        return TaskResponse(**HttpClient().put(f"{self.tasks_url}/{board_id}/tasks/{task_id}/move-to/{target_board_id}",
                                               headers=headers))

    def change_task_status(self, task_id, new_status, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return TaskResponse(**HttpClient().put(f"/tasks/{task_id}/status/{new_status}", headers=headers))

    def upgrate_task_status(self, task_id, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return TaskResponse(**HttpClient().put(f"/tasks/{task_id}/next-status", headers=headers))

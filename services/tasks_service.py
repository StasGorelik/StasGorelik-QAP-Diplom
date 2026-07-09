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

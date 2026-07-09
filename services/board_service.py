from core.http_client import HttpClient
from models.board import BoardResponse


class BoardService(HttpClient):
    boards_url = '/boards'

    def create_board(self, title, description, access_token):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        body = {"title": title,
                "description": description,
                "public": True}

        return BoardResponse(**HttpClient().post(f"{self.boards_url}", body=body, headers=headers))

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

    def get_list_of_my_boards(self, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        boards = self.get(f"{self.boards_url}/?skip=0&limit=100&archived=false", headers=headers)
        boards_objects = [BoardResponse(**board) for board in boards]
        return boards_objects

    def get_public_board(self, board_id):
        headers = {
            "accept": "application/json"
        }
        return self.get(f"{self.boards_url}/public/{board_id}", headers=headers)

    def get_board_by_id(self, board_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return self.get(f"{self.boards_url}/{board_id}", headers=headers)

    def update_board(self, title, description, access_token, board_id):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        body = {
            "title": title,
            "description": description,
            "public": True,
            "archived": False
        }

        return BoardResponse(**HttpClient().put(f"{self.boards_url}/{board_id}", body=body, headers=headers))

    def delete_board(self, board_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return self.delete(f"{self.boards_url}/{board_id}", headers=headers)

    def add_member_on_board(self, board_id, user_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return self.post(f"{self.boards_url}/{board_id}/members/{user_id}", headers=headers)

    def delete_member_from_board(self, board_id, user_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return self.delete(f"{self.boards_url}/{board_id}/members/{user_id}", headers=headers)

    def get_board_members(self, board_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        members = self.get(f"{self.boards_url}/{board_id}/members", headers=headers)
        members_objects = [member for member in members]
        return members_objects

    def get_stats_from_board(self, board_id, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
        }
        return self.get(f"{self.boards_url}/{board_id}/stats", headers=headers)

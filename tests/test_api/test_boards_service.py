import pytest

from services.auth_service import AuthServise
from faker import Faker
from services.get_users_service import GetUserService
from services.board_service import BoardService


@pytest.mark.board1
def test_create_board():
    register_user = AuthServise().registration_user(Faker().user_name(),
                                                    Faker().email(), "ASDASDA111")

    create_board = BoardService().create_board(title="New",
                                               description="This board is created",
                                               access_token=register_user.access_token)

    assert create_board.title == "New"
    assert create_board.description == "This board is created"


@pytest.mark.board2
def test_get_board_by_id():
    login_user = AuthServise().login('admin@example.com', 'admin123')

    create_board = BoardService().create_board(title="New_new",
                                               description="This board is created",
                                               access_token=login_user.access_token)

    get_board = BoardService().get_board_by_id(board_id=create_board.id, access_token=login_user.access_token)
    assert get_board["title"] == "New_new"


@pytest.mark.board3
def test_get_private_board():
    get_privite_board = BoardService().get_public_board(board_id=1)

    assert get_privite_board is None


@pytest.mark.board4
def test_get_list_bords_created_by_this_user():
    register_user = AuthServise().registration_user(Faker().user_name(),
                                                    Faker().email(), "ASDASDA111")

    BoardService().create_board(title="Created_By_New_User_Board",
                                description="This board is created by new user",
                                access_token=register_user.access_token)

    get_list_of_user_boards = BoardService().get_list_of_my_boards(access_token=register_user.access_token)

    assert len(get_list_of_user_boards) != 0


@pytest.mark.board5
def test_update_board():
    login_user = AuthServise().login('admin@example.com', 'admin123')

    create_board = BoardService().create_board(title="New_new_new",
                                               description="This board is created",
                                               access_token=login_user.access_token)

    update_board = BoardService().update_board(title="Updated_Board",
                                               description="This board is updated",
                                               access_token=login_user.access_token, board_id=create_board.id)

    assert update_board.title == "Updated_Board"
    assert update_board.description == "This board is updated"


@pytest.mark.board6
def test_delete_board():
    login_user = AuthServise().login('admin@example.com', 'admin123')

    create_board = BoardService().create_board(title="New_new_new",
                                               description="This board is created",
                                               access_token=login_user.access_token)

    delete_board = BoardService().delete_board(board_id=create_board.id, access_token=login_user.access_token)
    assert delete_board == {}


@pytest.mark.board7
def test_add_member_to_the_board():
    register_user_1 = AuthServise().registration_user(Faker().user_name(),
                                                      Faker().email(), "ASDASDA111")
    register_user_2 = AuthServise().registration_user(Faker().user_name(),
                                                      Faker().email(), "ASDASDA111")
    get_new_user_info = GetUserService().get_user_me(access_token=register_user_2.access_token)
    create_board = BoardService().create_board(title="New_board_with_2_users",
                                               description="This board is created",
                                               access_token=register_user_1.access_token)

    add_member_to_the_board = BoardService().add_member_on_board(
        board_id=create_board.id, user_id=get_new_user_info.id, access_token=register_user_1.access_token)
    assert add_member_to_the_board["message"] == "User added to board"


@pytest.mark.board8
def test_delete_member_from_board():
    register_user_1 = AuthServise().registration_user(Faker().user_name(),
                                                      Faker().email(), "ASDASDA111")
    register_user_2 = AuthServise().registration_user(Faker().user_name(),
                                                      Faker().email(), "ASDASDA111")
    get_new_user_info = GetUserService().get_user_me(access_token=register_user_2.access_token)
    create_board = BoardService().create_board(title="New_board_with_2_users",
                                               description="This board is created",
                                               access_token=register_user_1.access_token)

    # добавление человечка на доску
    BoardService().add_member_on_board(board_id=create_board.id,
                                       user_id=get_new_user_info.id,
                                       access_token=register_user_1.access_token)

    delete_member = BoardService().delete_member_from_board(board_id=create_board.id,
                                                            user_id=get_new_user_info.id,
                                                            access_token=register_user_1.access_token)

    assert delete_member == {}


@pytest.mark.board9
def test_get_list_of_member_on_the_board():
    register_user_1 = AuthServise().registration_user(Faker().user_name(),
                                                      Faker().email(), "ASDASDA111")
    register_user_2 = AuthServise().registration_user(Faker().user_name(),
                                                      Faker().email(), "ASDASDA111")
    get_new_user_info = GetUserService().get_user_me(access_token=register_user_2.access_token)
    create_board = BoardService().create_board(title="New_board_with_2_users",
                                               description="This board is created",
                                               access_token=register_user_1.access_token)
    # Добавляю пользователя на доску
    BoardService().add_member_on_board(
        board_id=create_board.id, user_id=get_new_user_info.id, access_token=register_user_1.access_token)

    get_list_members_of_the_board = BoardService().get_board_members(
        board_id=create_board.id, access_token=register_user_1.access_token)
    assert len(get_list_members_of_the_board) > 1


@pytest.mark.board10
def test_stats_on_the_board():
    login_user = AuthServise().login('admin@example.com', 'admin123')
    board_id = 1
    get_stats_of_board = BoardService().get_stats_from_board(board_id=board_id, access_token=login_user.access_token)
    assert get_stats_of_board["total"]
    assert get_stats_of_board["todo"]
    assert get_stats_of_board["in_progress"]
    assert get_stats_of_board["done"]

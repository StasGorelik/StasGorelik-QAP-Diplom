import pytest

from services.auth_service import AuthServise
from faker import Faker
from services.get_users_service import GetUserService
from services.board_service import BoardService
from services.tasks_service import TaskService


@pytest.mark.api1
def test_get_users_info():
    response_login = AuthServise().login('admin@example.com', 'admin123')

    response_get_users = GetUserService().get_users_list(response_login.access_token)
    len_before_registration = len(response_get_users)

    response_registration = AuthServise().registration_user(Faker().user_name(),
                                                            Faker().email(), "ASDASDA111")

    response_get_users = GetUserService().get_users_list(response_login.access_token)
    len_after_registration = len(response_get_users)

    assert len_before_registration < len_after_registration


# представим, что имя пользователя должно быть только строкой и размерами от 6 до 10 символов
@pytest.mark.parametrize("username",
                         ["gavga", "sixsim", "sevensi", "ninesimbo",
                          "tensimbols", "elevensimbo", 123456, "!&%$^#@!"])
@pytest.mark.api2
def test_update_user(username):
    response_login_admin = AuthServise().login('admin@example.com', 'admin123')

    response_registration = AuthServise().registration_user(Faker().user_name(),
                                                            Faker().email(), "ASDASDA111")

    response_get_user_me = GetUserService().get_user_me(
        response_registration.access_token)
    user_id = response_get_user_me.id

    response_update_user = GetUserService().update_user(username=username, email=Faker().email(
    ), role="user", user_id=user_id, access_token=response_login_admin.access_token)

    assert response_update_user.username == username


@pytest.mark.api3
def test_delete_user():
    login_admin = AuthServise().login('admin@example.com', 'admin123')

    new_user = AuthServise().registration_user(Faker().user_name(),
                                               Faker().email(), "ASDASDA111")

    user_me = GetUserService().get_user_me(
        new_user.access_token)
    user_id = user_me.id

    response_get_users = GetUserService().get_users_list(login_admin.access_token)
    len_before_delete_user = len(response_get_users)

    delete_user = GetUserService().delete_user(user_id, login_admin.access_token)

    response_get_users = GetUserService().get_users_list(login_admin.access_token)
    len_after_delete_user = len(response_get_users)

    assert len_before_delete_user > len_after_delete_user


@pytest.mark.api4
def test_search_tasks():
    login_admin = AuthServise().login('admin@example.com', 'admin123')
    create_board = BoardService().create_board(title="Testing",
                                               description="Testing board", access_token=login_admin.access_token)

    board_id = create_board.id

    create_task = TaskService().create_task(title="APIS", description="TASK FOR API",
                                            board_id=board_id, access_token=login_admin.access_token)

    created_task_id = create_task.id

    search_task = TaskService().get_task_by_id(
        board_id=board_id, task_id=created_task_id, access_token=login_admin.access_token)

    assert search_task.title == create_task.title
    assert search_task.description == create_task.description

# представим, что тайтл таски должно быть только строкой и размерами от 6 до 10 символов и только строкой


@pytest.mark.parametrize("title",
                         ["APITE", "APITES", "APITEST", "ApitestsP",
                          "ApitestsPy", "ApitestsPyt", 123456, "!&%$^#@!"])
@pytest.mark.api5
def test_create_tasks(title):
    login_admin = AuthServise().login('admin@example.com', 'admin123')
    create_board = BoardService().create_board(title="TEST",
                                               description="Testing board", access_token=login_admin.access_token)

    board_id = create_board.id

    create_task = TaskService().create_task(title=title, description="TASK FOR API",
                                            board_id=board_id, access_token=login_admin.access_token)

    assert create_task.title == title

@pytest.mark.api6
def test_delete_tasks():
    login_admin = AuthServise().login('admin@example.com', 'admin123')
    create_board = BoardService().create_board(title="Testing",
                                               description="Testing board", access_token=login_admin.access_token)

    board_id = create_board.id

    create_task = TaskService().create_task(title="APIS", description="TASK FOR API",
                                            board_id=board_id, access_token=login_admin.access_token)

    created_task_id = create_task.id

    delete_task = TaskService().delete_task(board_id=board_id,
                                            task_id=created_task_id, access_token=login_admin.access_token)
#я в шоке что получилось, пеп8 и пайкеши из гитхаба удалю к диплому
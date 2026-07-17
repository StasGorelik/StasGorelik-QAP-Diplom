import pytest

from services.auth_service import AuthServise
from faker import Faker
from services.get_users_service import GetUserService
from services.board_service import BoardService
from services.tasks_service import TaskService


@pytest.mark.parametrize("password", ["fivee", "sixxxx", "seven77", 123123])
@pytest.mark.api1
def test_registration_user(password):
    registration_user = AuthServise().registration_user(Faker().user_name(), Faker().email(), password=password)

    assert registration_user.access_token


@pytest.mark.api2
def test_get_users_info():
    response_login = AuthServise().login('admin@example.com', 'admin123')

    response_get_users = GetUserService().get_users_list(response_login.access_token)
    len_before_registration = len(response_get_users)

    # регистрация пользователя
    AuthServise().registration_user(Faker().user_name(),
                                    Faker().email(), "ASDASDA111")

    response_get_users = GetUserService().get_users_list(response_login.access_token)
    len_after_registration = len(response_get_users)

    assert len_before_registration < len_after_registration


# представим, что имя пользователя должно быть только строкой и размерами от 6 до 10 символов
@pytest.mark.parametrize("username",
                         ["aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaaa",
                          "aaaaaaaaaa", "aaaaaaaaaaa", 123456, "!&%$^#@!"])
@pytest.mark.api3
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


@pytest.mark.api4
def test_delete_user():
    login_admin = AuthServise().login('admin@example.com', 'admin123')

    new_user = AuthServise().registration_user(Faker().user_name(),
                                               Faker().email(), "ASDASDA111")

    user_me = GetUserService().get_user_me(
        new_user.access_token)
    user_id = user_me.id

    response_get_users = GetUserService().get_users_list(login_admin.access_token)
    len_before_delete_user = len(response_get_users)

    # удаление пользователя
    GetUserService().delete_user(user_id, login_admin.access_token)

    response_get_users = GetUserService().get_users_list(login_admin.access_token)
    len_after_delete_user = len(response_get_users)

    assert len_before_delete_user > len_after_delete_user


@pytest.mark.api5
def test_get_my_tasks_is_created():
    register_user = AuthServise().registration_user(Faker().user_name(),
                                                    Faker().email(), "ASDASDA111")

    create_board = BoardService().create_board(title="Testing",
                                               description="Testing board", access_token=register_user.access_token)

    board_id = create_board.id

    # пользователь создает задачу на доске
    TaskService().create_task(title=Faker().name(), description="TASK CRATED BY NEW USER",
                              board_id=board_id, access_token=register_user.access_token)

    my_tasks = GetUserService().get_user_me_tasks(access_token=register_user.access_token)

    assert len(my_tasks) != 0


@pytest.mark.api6
def test_get_public_users():
    response_get_public_list_users = GetUserService().get_public_users_list()

    assert len(response_get_public_list_users) != 0

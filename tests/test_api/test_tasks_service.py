import pytest


from services.auth_service import AuthServise
from services.board_service import BoardService
from services.tasks_service import TaskService


@pytest.mark.task1
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
@pytest.mark.task2
def test_create_tasks(title):
    login_admin = AuthServise().login('admin@example.com', 'admin123')
    create_board = BoardService().create_board(title="TEST",
                                               description="Testing board", access_token=login_admin.access_token)

    board_id = create_board.id

    create_task = TaskService().create_task(title=title, description="TASK FOR API",
                                            board_id=board_id, access_token=login_admin.access_token)

    assert create_task.title == title


@pytest.mark.task3
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

    assert delete_task == {}


@pytest.mark.task4
def test_update_tasks():
    login_admin = AuthServise().login('admin@example.com', 'admin123')
    create_board = BoardService().create_board(title="Testing",
                                               description="Testing board", access_token=login_admin.access_token)

    create_task = TaskService().create_task(title="APIS", description="TASK FOR API",
                                            board_id=create_board.id, access_token=login_admin.access_token)

    update_task = TaskService().update_task(title="Updatet_Task", description="DESCRIPTION AFTER UPDATE",
                                            board_id=create_board.id, task_id=create_task.id, access_token=login_admin.access_token)

    assert update_task.title == "Updatet_Task"
    assert update_task.description == "DESCRIPTION AFTER UPDATE"


@pytest.mark.task5
def test_move_task_at_another_board():
    login_admin = AuthServise().login('admin@example.com', 'admin123')
    create_board = BoardService().create_board(title="Testing",
                                               description="Testing board", access_token=login_admin.access_token)
    create_board_target = BoardService().create_board(title="Testing",
                                                      description="Testing board", access_token=login_admin.access_token)

    create_task = TaskService().create_task(title="APIS", description="TASK FOR API",
                                            board_id=create_board.id, access_token=login_admin.access_token)

    remove_task_to_another_board = TaskService().remove_task_to_another_board(board_id=create_board.id,
                                                                              task_id=create_task.id,
                                                                              target_board_id=create_board_target.id,
                                                                              access_token=login_admin.access_token)

    assert remove_task_to_another_board.board_id == create_board_target.id


@pytest.mark.task6
def test_task_status_is_change():
    login_admin = AuthServise().login('admin@example.com', 'admin123')
    create_board = BoardService().create_board(title="TestingStatus",
                                               description="Testing board for status check",
                                               access_token=login_admin.access_token)

    create_task = TaskService().create_task(title="TestingStatus", description="Testing task for status check",
                                            board_id=create_board.id, access_token=login_admin.access_token)

    change_the_task_status = TaskService().change_task_status(
        create_task.id, new_status="in_progress", access_token=login_admin.access_token)

    assert change_the_task_status.status == "in_progress"


@pytest.mark.task7
def test_task_status_is_upgrade():
    login_admin = AuthServise().login('admin@example.com', 'admin123')
    create_board = BoardService().create_board(title="TestingStatus",
                                               description="Testing board for status check",
                                               access_token=login_admin.access_token)

    create_task = TaskService().create_task(title="TestingStatus", description="Testing task for status check",
                                            board_id=create_board.id, access_token=login_admin.access_token)

    upgrade_task_status = TaskService().upgrate_task_status(task_id=create_task.id,
                                                            access_token=login_admin.access_token)

    assert upgrade_task_status.status == "in_progress"

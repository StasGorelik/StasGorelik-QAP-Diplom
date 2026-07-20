import allure
import pytest

from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.boards_page import BoardsPage
from pages.tasks_page import TasksPage
from pages.admin_board_page import AdminPage
from pages.register_page import RegisterPage


@allure.title("Открытие страницы dashboard")
@pytest.mark.only1
def test_dashboard_page_opened(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_fill_out_of_form()

    authorization.autorization_submit_button_click()

    dashboard_page = DashboardPage(page)

    dashboard_page.verify_that_empty_page_opened()


@allure.title("Открытие страницы dashboard")
@pytest.mark.only2
def test_boards_page_opened(page: Page):
    authorization = LoginPage(page)
    dashboard_page = DashboardPage(page)
    boards_page = BoardsPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_fill_out_of_form()

    authorization.autorization_submit_button_click()

    dashboard_page.click_sidebar_boards_link()

    boards_page.verify_that_empty_page_opened()


@allure.title("Открытие страницы tasks")
@pytest.mark.only3
def test_tasks_page_opened(page: Page):
    authorization = LoginPage(page)
    tasks_page = TasksPage(page)
    dashboard_page = DashboardPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_fill_out_of_form()

    authorization.autorization_submit_button_click()

    dashboard_page.sidebar_tasks_link_click()

    tasks_page.verify_that_empty_page_opened()


@allure.title("Открытие страницы авторизации")
@pytest.mark.only4
def test_authorization(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_fill_out_of_form()
    authorization.autorization_submit_button_click()

    dashboard_page = DashboardPage(page)

    dashboard_page.verify_that_empty_page_opened()


@allure.title("Открытие страницы авторизации и проверка выпадающей информации")
@pytest.mark.only5
def test_authorization_user_dropdown_info_is_visible(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_fill_out_of_form()
    authorization.autorization_submit_button_click()

    dashboard_page = DashboardPage(page)

    dashboard_page.user_section_is_visible()
    dashboard_page.user_section_click()
    dashboard_page.user_section_dropdown_is_visible()


@allure.title("Проверка кнопки выхода")
@pytest.mark.only6
def test_quit(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_fill_out_of_form()
    authorization.autorization_submit_button_click()

    dashboard_page = DashboardPage(page)

    dashboard_page.user_section_is_visible()
    dashboard_page.user_section_click()
    dashboard_page.header_logout_button_click()


@allure.title("Проверка видимости панели админа")
@pytest.mark.admin1
def test_admin_panel(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_admin_fill_out_of_form()
    authorization.autorization_submit_button_click()

    dashboard_page = DashboardPage(page)
    dashboard_page.sidebar_admin_link_click()

    admin_page = AdminPage(page)
    admin_page.verify_that_empty_page_opened()


@allure.title("Проверка видимости панели с именем")
@pytest.mark.admin2
def test_header_user_dropdown_name(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_admin_fill_out_of_form()
    authorization.autorization_submit_button_click()

    dashboard_page = DashboardPage(page)
    dashboard_page.sidebar_admin_link_click()

    admin_page = AdminPage(page)
    admin_page.verify_that_empty_page_opened()

    admin_page.header_user_info_click()
    admin_page.header_user_dropdown_name_is_visible()


@allure.title("Проверка страницы регистрации")
@pytest.mark.register
def test_register_page_opened(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.auth_form_link_click()

    register_page = RegisterPage(page)

    register_page.verify_that_empty_page_opened()

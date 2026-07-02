from playwright.sync_api import Page
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.boards_page import BoardsPage
from pages.tasks_page import TasksPage


@pytest.mark.only1
def test_dashboard_page_opened(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_fill_out_of_form()

    authorization.autorization_submit_button_click()

    dashboard_page = DashboardPage(page)

    dashboard_page.verify_that_empty_page_opened()


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


@pytest.mark.only4
def test_authorization(page: Page):
    authorization = LoginPage(page)
    authorization.open()
    authorization.verify_that_empty_page_opened()
    authorization.autorization_fill_out_of_form()
    authorization.autorization_submit_button_click()

    dashboard_page = DashboardPage(page)

    dashboard_page.verify_that_empty_page_opened()


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
    

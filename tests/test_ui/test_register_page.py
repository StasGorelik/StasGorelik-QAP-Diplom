from playwright.sync_api import Page
import pytest
from pages.register_page import RegisterPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.mark.register1
def test_register_page_is_opened(page: Page):
    register_page = RegisterPage(page)
    register_page.open()

    register_page.verify_that_empty_page_opened()


@pytest.mark.register2
def test_registration_is_seccess(page: Page):
    register_page = RegisterPage(page)
    register_page.open()

    register_page.verify_that_empty_page_opened()

    register_page.registration_fill_out_of_form()
    register_page.register_submit_button_click()

    dashboard_page = DashboardPage(page)
    dashboard_page.verify_that_empty_page_opened()
    dashboard_page.toast_message_verification_is_visible()


@pytest.mark.register3
def test_login_page_is_opened(page: Page):
    register_page = RegisterPage(page)
    register_page.open()

    register_page.verify_that_empty_page_opened()
    register_page.auth_from_link_button_click()

    login_page = LoginPage(page)
    login_page.verify_that_empty_page_opened()

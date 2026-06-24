from core.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path = "dashboard"

        self.dashboard_title = self.page.locator('[data-qa="dashboard-title"]')
        self.dashboard_create_board_button = self.page.locator(
            '[data-qa="dashboard-create-board-button"]'
        )
        self.brand_title = self.page.locator(".brand-title")
        self.header_username = self.page.locator('[data-qa="header-username"]').filter(
            has_text="bob_user"
        )
        self.header_user_dropdown_info = self.page.locator(".header-user-dropdown-info")
        self.header_logout_button = self.page.locator(
            '[data-qa="header-logout-button"]'
        )
        self.sidebar_boards_link = self.page.locator('[data-qa="sidebar-boards-link"]')
        self.sidebar_tasks_link = self.page.locator('[data-qa="sidebar-tasks-link"]')

    def open(self):
        self.goto(self.path)

    def verify_that_empty_page_opened(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_create_board_button).to_be_visible()
        expect(self.brand_title).to_be_visible()

    def user_section_is_visible(self):
        expect(self.header_username).to_be_visible()

    def user_section_click(self):
        self.header_username.click()

    def user_section_dropdown_is_visible(self):
        expect(self.header_user_dropdown_info).to_be_visible()

    def header_logout_button_click(self):
        self.header_logout_button.click()

    def click_sidebar_boards_link(self):
        self.sidebar_boards_link.click()

    def sidebar_tasks_link_click(self):
        self.sidebar_tasks_link.click()

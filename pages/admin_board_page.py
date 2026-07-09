from core.base_page import BasePage
from playwright.sync_api import Page, expect


class AdminPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path = "automation-lab/admin"

        self.admin_page_title = self.page.locator(
            '.admin-page-title').filter(has_text="Административная панель")
        self.admin_section_title = self.page.locator(
            '.admin-section-title').filter(has_text="Управление пользователями")
        self.header_user_info = self.page.locator(
            '[data-qa="header-user-info"]')
        self.header_user_dropdown_name = self.page.locator(
            '.header-user-dropdown-name').filter(has_text="admin")

    def open(self):
        self.goto(self.path)

    def verify_that_empty_page_opened(self):
        expect(self.admin_page_title).to_be_visible()
        expect(self.admin_section_title).to_be_visible()
        expect(self.header_user_info).to_be_visible()

    def header_user_info_click(self):
        self.header_user_info.click()

    def header_user_dropdown_name_is_visible(self):
        expect(self.header_user_dropdown_name).to_be_visible()

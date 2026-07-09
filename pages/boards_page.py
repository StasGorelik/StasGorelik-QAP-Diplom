from core.base_page import BasePage
from playwright.sync_api import Page, expect


class BoardsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path = "boards"

        self.boards_page = self.page.locator('[data-qa="boards-page"]')
        self.boards_create_board_button = self.page.locator(
            '[data-qa="boards-create-board-button"]')
        self.boards_filters = self.page.locator('[data-qa="boards-filters"]')
        self.admin_section_title = self.page.locator('.admin-section-title')

    def open(self):
        self.goto(self.path)

    def verify_that_empty_page_opened(self):
        expect(self.boards_page).to_be_visible()
        expect(self.boards_create_board_button).to_be_visible()
        expect(self.boards_filters).to_be_visible()
        expect(self.admin_section_title).to_be_visible()

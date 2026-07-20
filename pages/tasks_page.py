from core.base_page import BasePage
from playwright.sync_api import Page, expect


class TasksPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path = "tasks"

        self.tasks_page_title = self.page.locator(
            '[data-qa="tasks-page-title"]')
        self.tasks_filters = self.page.locator('[data-qa="tasks-filters"]')
        self.admin_section_title = self.page.locator('.admin-section-title')
        self.tasks_search_input = self.page.locator(
            '[data-qa="tasks-search-input"]')

    def open(self):
        self.goto(self.path)

    def verify_that_empty_page_opened(self):
        expect(self.tasks_page_title).to_be_visible()
        expect(self.tasks_filters).to_be_visible()
        expect(self.admin_section_title).to_be_visible()
        expect(self.tasks_search_input).to_be_visible()

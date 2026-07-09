from core.base_page import BasePage
from playwright.sync_api import Page, expect


class ClicksPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path = "automation-lab/clicks"

        self.case_card = self.page.locator('.case-card')
        self.header = self.page.locator('.header')
        self.page_title = self.page.locator(
            '.page-title').filter(has_text="Клики и взаимодействия")

    def open(self):
        self.goto(self.path)

    def verify_that_empty_page_opened(self):
        expect(self.case_card).to_be_visible()
        expect(self.header).to_be_visible()
        expect(self.page_title).to_be_visible()

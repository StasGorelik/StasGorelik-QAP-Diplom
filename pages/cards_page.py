from core.base_page import BasePage
from playwright.sync_api import Page, expect


class CardsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path = "automation-lab/cards"

        self.header = self.page.locator('.header')
        self.page_itle = self.page.locator(
            '.page-title').filter(has_text="Карточки подгружаются асинхронно")
        self.case_card = self.page.locator('.case-card')
        self.case_element = self.page.locator('.case-element')
        self.cards_grid = self.page.locator('.cards-grid')
        self.trigger_btn = self.page.locator('.trigger-btn')

    def open(self):
        self.goto(self.path)

    def verify_that_empty_page_opened(self):
        expect(self.header).to_be_visible()
        expect(self.case_card).to_be_visible()
        expect(self.page_itle).to_be_visible()
        expect(self.case_element).to_be_visible()

    def trigger_btn_click(self):
        self.trigger_btn.click()

    def cards_grid_is_visible(self):
        expect(self.cards_grid).to_be_visible()

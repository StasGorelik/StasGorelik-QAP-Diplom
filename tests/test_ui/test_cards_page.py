import allure
import pytest

from playwright.sync_api import Page
from pages.cards_page import CardsPage


@allure.title("Открытие страницы с карточками")
@pytest.mark.cards1
def test_clicks_page_opened(page: Page):
    cards_page = CardsPage(page)
    cards_page.open()

    cards_page.verify_that_empty_page_opened()


@allure.title("Видимость поля карт на странице с карточками")
@pytest.mark.cards2
def test_cards_grid_is_opened(page: Page):
    cards_page = CardsPage(page)
    cards_page.open()
    cards_page.verify_that_empty_page_opened()

    cards_page.trigger_btn_click()
    cards_page.cards_grid_is_visible()

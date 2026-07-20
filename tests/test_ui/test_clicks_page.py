import allure
from playwright.sync_api import Page
import pytest
from pages.clicks_page import ClicksPage


@allure.title("Открытие страницы с кликами")
@pytest.mark.clicks
def test_clicks_page_opened(page: Page):
    clicks_page = ClicksPage(page)
    clicks_page.open()

    clicks_page.verify_that_empty_page_opened()

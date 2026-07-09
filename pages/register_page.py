from core.base_page import BasePage
from playwright.sync_api import Page, expect
from faker import Faker


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path = "register"

        self.register_form_container = self.page.locator(
            '[data-qa="register-form-container"]')
        self.register_title = self.page.locator(
            '[data-qa="register-title"]').filter(has_text="Регистрация")
        self.header_content = self.page.locator('.header-content')
        self.auth_form_link_button = self.page.locator(".auth-form-link")
        self.register_username_input = self.page.locator(
            '[data-qa="register-username-input"]')
        self.register_email_input = self.page.locator(
            '[data-qa="register-email-input"]')
        self.register_password_input = self.page.locator(
            '[data-qa="register-password-input"]')
        self.register_confirm_password_input = self.page.locator(
            '[data-qa="register-confirm-password-input"]')
        self.register_submit_button = self.page.locator(
            '[data-qa="register-submit-button"]')

    def open(self):
        self.goto(self.path)

    def verify_that_empty_page_opened(self):
        expect(self.register_form_container).to_be_visible()
        expect(self.register_title).to_be_visible()
        expect(self.header_content).to_be_visible()

    def registration_fill_out_of_form(self):
        self.register_username_input.fill(Faker().user_name())
        self.register_email_input.fill(Faker().email())
        self.register_password_input.fill("password123")
        self.register_confirm_password_input.fill("password123")

    def register_submit_button_click(self):
        self.register_submit_button.click()

    def auth_from_link_button_click(self):
        self.auth_form_link_button.click()

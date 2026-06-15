from core.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.path = "login"

        self.login_form_container = self.page.locator('[data-qa="login-form-container"]')
        self.login_email_input = self.page.locator('[data-qa="login-email-input"]')    
        self.login_password_input = self.page.locator('[data-qa="login-password-input"]')
        self.login_submit_button = self.page.locator('[data-qa="login-submit-button"]')


    def open(self):
        self.goto(self.path)

    def verify_that_empty_page_opened(self):        
        expect(self.login_form_container).to_be_visible()
        expect(self.login_email_input).to_be_visible()
        expect(self.login_password_input).to_be_visible()
        expect(self.login_submit_button).to_be_visible()
    
    
    def autorization_fill_out_of_form(self):
        self.login_email_input.fill("bob@example.com")
        self.login_password_input.fill("password123")
        
    def autorization_submit_button_click(self):
        self.login_submit_button.click()
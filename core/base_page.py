class BasePage():

    def __init__(self, page):
        self.page = page
        self.domain = "http://localhost:3000/"

    def goto(self, url):
        self.page.goto(f"{self.domain}{url}")

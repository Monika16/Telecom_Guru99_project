from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.page = page

    def load(self):
        self.page.goto("https://demo.guru99.com/telecom/index.html")

    def add_customer(self, username, lastname, email, address, phone):
        self.page.locator("label[for='done']").click()
        self.page.get_by_placeholder("FirstName").fill(username)
        self.page.get_by_placeholder("LastName").fill(lastname)
        self.page.get_by_placeholder("Email").fill(email)
        self.page.get_by_placeholder("Enter your address").fill(address)
        self.page.get_by_placeholder("Mobile Number").fill(phone)
        self.page.locator("input[name='submit']").click()


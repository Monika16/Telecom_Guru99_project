from playwright.sync_api import Page

from pages.login_page import LoginPage


def test_login_page(page:Page):
    login_page = LoginPage(page)
    login_page.load()

    assert "Guru99 telecom" in page.get_by_role("link", name="Guru99 telecom").inner_text()
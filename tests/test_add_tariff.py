from playwright.sync_api import Page

from pages.login_page import LoginPage


def test_add_tariff(page:Page, add_customer:str):
    login_page = LoginPage(page)
    login_page.load()
    page.get_by_role("link", name="Add Tariff Plan to Customer").click()
    page.get_by_placeholder("Enter Your Customer ID").fill(add_customer)
    page.locator("input[name='submit']").click()
    page.locator("label[for='sele']").dispatch_event("click")
    page.locator("input[value='Add Tariff Plan to Customer']").click()
    success_text = page.locator(".inner h2").inner_text()
    print(success_text)
    assert "Congratulation" in success_text
    page.wait_for_timeout(2000)



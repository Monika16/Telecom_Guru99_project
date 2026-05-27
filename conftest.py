import pytest
from playwright.async_api import Page

from pages.login_page import LoginPage

@pytest.fixture
def add_customer(page:Page):
    login_page = LoginPage(page)
    login_page.load()
    page.get_by_role("link", name="Add Customer").click()
    page.wait_for_timeout(2000)
    login_page.add_customer("John", "Doe", "john.doe@mail.com",
                            "4529 Maple View Drive Bellevue WA 98004",
                            "+1234567890")

    # get customer ID and assert
    table_rows = page.locator("table tbody tr").all()
    data = table_rows[0].locator("td").all()
    customer_id = data[1].locator("h3").inner_text()

    return customer_id
import pytest
from playwright.sync_api import Page, expect
from pages.add_beneficiary_page import AddBeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page):
    return AddBeneficiaryPage(page)

def test_add_beneficiary_valid(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.navigate_to_section()
    beneficiary_page.open_form()
    beneficiary_page.fill_account_number("1234567890")
    beneficiary_page.fill_ifsc_code("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.success_notification()).to_be_visible()

def test_add_beneficiary_edge_values(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.open_form()
    beneficiary_page.fill_account_number("1000000000")
    beneficiary_page.fill_ifsc_code("1BCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.success_notification()).to_be_visible()

def test_add_beneficiary_invalid_ifsc(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.open_form()
    beneficiary_page.fill_account_number("1234567890")
    beneficiary_page.fill_ifsc_code("ABC12")
    beneficiary_page.click_add()
    expect(beneficiary_page.error_message()).to_have_text("IFSC code must be 11 alphanumeric characters")

@pytest.mark.parametrize("account", ["12AB567890", "ABCD123456"])
def test_add_beneficiary_non_numeric_account(beneficiary_page: AddBeneficiaryPage, account):
    beneficiary_page.open_form()
    beneficiary_page.fill_account_number(account)
    beneficiary_page.fill_ifsc_code("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.error_message()).to_have_text("Account number must be numeric and 10‑16 digits long")

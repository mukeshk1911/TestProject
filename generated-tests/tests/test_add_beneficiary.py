import pytest
from playwright.sync_api import Page, expect
from pages.add_beneficiary_page import AddBeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page) -> AddBeneficiaryPage:
    return AddBeneficiaryPage(page)

def test_add_beneficiary_valid(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.navigate()
    beneficiary_page.enter_account_number("123456789012")
    beneficiary_page.enter_ifsc("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.success_message()).to_be_visible()
    expect(beneficiary_page.success_message()).to_have_text("Beneficiary added successfully")

def test_add_beneficiary_invalid_ifsc(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.navigate()
    beneficiary_page.enter_account_number("123456789012")
    beneficiary_page.enter_ifsc("AB12")
    beneficiary_page.click_add()
    expect(beneficiary_page.error_message()).to_be_visible()
    expect(beneficiary_page.error_message()).to_have_text("Invalid IFSC format")
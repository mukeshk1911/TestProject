import pytest
from playwright.sync_api import Page, expect
from pages.beneficiary_page import BeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page):
    return BeneficiaryPage(page)

def test_add_beneficiary_success(beneficiary_page: BeneficiaryPage):
    beneficiary_page.navigate_to_add()
    beneficiary_page.fill_form(account_number="123456789012", ifsc="ABCD0123456", name="John Doe")
    beneficiary_page.submit()
    expect(beneficiary_page.toast).to_have_text("Beneficiary added successfully")
    beneficiary_page.verify_in_list(account_number="123456789012")

def test_add_beneficiary_invalid_ifsc(beneficiary_page: BeneficiaryPage):
    beneficiary_page.navigate_to_add()
    beneficiary_page.fill_form(account_number="123456789012", ifsc="INVALIDIFSC", name="John Doe")
    beneficiary_page.submit()
    expect(beneficiary_page.error_message).to_have_text("Invalid IFSC format")

def test_add_beneficiary_non_numeric_account(beneficiary_page: BeneficiaryPage):
    beneficiary_page.navigate_to_add()
    beneficiary_page.fill_form(account_number="abc123def", ifsc="QRST0001234", name="John Doe")
    beneficiary_page.submit()
    expect(beneficiary_page.error_message).to_have_text("Account number must be numeric and 10‑16 digits")

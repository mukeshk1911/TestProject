import pytest
from playwright.sync_api import Page, expect
from pages.beneficiary_page import BeneficiaryPage
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page):
    return BeneficiaryPage(page)

@pytest.fixture(scope="function")
def transfer_page(page: Page):
    return TransferPage(page)

def test_add_beneficiary_valid(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto_add_beneficiary()
    beneficiary_page.fill_account_number("123456789012")
    beneficiary_page.fill_ifsc("MNOP0123456")
    beneficiary_page.fill_name("John Doe")
    beneficiary_page.submit()
    expect(beneficiary_page.success_toast()).to_be_visible()
    expect(beneficiary_page.beneficiary_in_list("John Doe")).to_be_visible()

def test_transfer_with_correct_otp(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.proceed()
    transfer_page.enter_otp("123456")
    transfer_page.confirm()
    expect(transfer_page.success_message()).to_have_text("Transfer successful")

def test_add_beneficiary_invalid_account(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto_add_beneficiary()
    beneficiary_page.fill_account_number("ABC123")
    beneficiary_page.fill_ifsc("ABCD0123456")
    beneficiary_page.submit()
    expect(beneficiary_page.validation_error()).to_have_text("Account number must be numeric and 10‑16 digits")

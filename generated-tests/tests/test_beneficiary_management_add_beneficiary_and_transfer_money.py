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

def test_add_beneficiary_success(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto_add_page()
    beneficiary_page.enter_account_number("123456789012")
    beneficiary_page.enter_ifsc("ABCD0123456")
    beneficiary_page.submit()
    expect(beneficiary_page.success_toast).to_have_text("Beneficiary added successfully")

def test_transfer_money_success(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount("5000")
    transfer_page.proceed()
    transfer_page.enter_otp("123456")
    transfer_page.confirm()
    expect(transfer_page.confirmation_message).to_have_text("Transfer completed successfully")

def test_transfer_amount_exceeds_limit(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount("200000")
    transfer_page.proceed()
    expect(transfer_page.error_message).to_have_text("Transfer amount exceeds limit")

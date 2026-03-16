import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage
from pages.beneficiary_page import BeneficiaryPage

@pytest.fixture(scope="function")
def transfer_page(page: Page):
    return TransferPage(page)

@pytest.fixture(scope="function")
def beneficiary_page(page: Page):
    return BeneficiaryPage(page)

def test_successful_transfer_with_correct_otp(page: Page, transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.click_proceed()
    transfer_page.enter_otp("123456")
    transfer_page.confirm_transfer()
    expect(transfer_page.success_message()).to_have_text("Transfer successful")

def test_transfer_blocked_by_incorrect_otp(page: Page, transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.click_proceed()
    transfer_page.enter_otp("000000")
    transfer_page.confirm_transfer()
    expect(transfer_page.error_message()).to_have_text("Invalid OTP")

def test_add_valid_beneficiary(page: Page, beneficiary_page: BeneficiaryPage):
    beneficiary_page.navigate_to_add()
    beneficiary_page.enter_account_number("123456789012")
    beneficiary_page.enter_ifsc("ABCD0123456")
    beneficiary_page.submit()
    expect(beneficiary_page.success_notification()).to_have_text("Beneficiary added successfully")

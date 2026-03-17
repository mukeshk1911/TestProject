import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page: Page):
    return TransferPage(page)

def test_add_beneficiary_success(transfer_page: TransferPage):
    transfer_page.goto_add_beneficiary()
    transfer_page.enter_account_number("123456789012")
    transfer_page.enter_ifsc("ABCD0123456")
    transfer_page.save_beneficiary()
    expect(transfer_page.beneficiary_success_message).to_have_text("Beneficiary added successfully")

def test_transfer_within_limit_success(transfer_page: TransferPage):
    transfer_page.goto_transfer()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount("5000")
    transfer_page.submit_transfer()
    transfer_page.enter_otp("123456")
    expect(transfer_page.confirmation_message).to_have_text("Transfer successful")

def test_transfer_otp_failure_cancels(transfer_page: TransferPage):
    transfer_page.goto_transfer()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount("3000")
    transfer_page.submit_transfer()
    for _ in range(3):
        transfer_page.enter_otp("000000")
    expect(transfer_page.error_message).to_have_text("OTP verification failed. Transaction cancelled.")

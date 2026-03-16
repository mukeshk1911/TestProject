import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page: Page):
    return TransferPage(page)

def test_add_beneficiary_valid(transfer_page: TransferPage):
    transfer_page.navigate_to_add_beneficiary()
    transfer_page.enter_account_number("123456789012")
    transfer_page.enter_ifsc("ABCD0123456")
    transfer_page.click_add_beneficiary()
    expect(transfer_page.success_notification).to_have_text("Beneficiary added successfully")

def test_transfer_with_correct_otp(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount("5000")
    transfer_page.click_proceed()
    transfer_page.enter_otp("123456")
    transfer_page.click_confirm()
    expect(transfer_page.confirmation_message).to_have_text("Transfer successful")

def test_transfer_with_incorrect_otp(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount("5000")
    transfer_page.click_proceed()
    transfer_page.enter_otp("000000")
    transfer_page.click_confirm()
    expect(transfer_page.error_message).to_have_text("Invalid OTP")

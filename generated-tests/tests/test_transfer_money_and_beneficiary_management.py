import pytest
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page):
    return TransferPage(page)

def test_add_beneficiary_success(transfer_page):
    transfer_page.navigate_to_add_beneficiary()
    transfer_page.add_beneficiary(account_number="123456789012", ifsc="ABCD0123456")
    assert transfer_page.is_success_notification_visible("Beneficiary added successfully")

def test_transfer_with_correct_otp(transfer_page):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.click_proceed()
    transfer_page.enter_otp("123456")
    transfer_page.confirm_transfer()
    assert transfer_page.is_confirmation_message_visible("Transfer successful")

def test_transfer_with_incorrect_otp(transfer_page):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.click_proceed()
    transfer_page.enter_otp("000000")
    transfer_page.confirm_transfer()
    assert transfer_page.is_error_message_visible("Invalid OTP")

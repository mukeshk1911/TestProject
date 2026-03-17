import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page: Page) -> TransferPage:
    return TransferPage(page)

def test_successful_transfer_with_correct_otp(transfer_page: TransferPage):
    transfer_page.navigate_to_transfer()
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.request_otp()
    transfer_page.enter_otp("123456")
    transfer_page.confirm_transfer()
    expect(transfer_page.success_message()).to_be_visible()

def test_transfer_blocked_by_incorrect_otp(transfer_page: TransferPage):
    transfer_page.navigate_to_transfer()
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.request_otp()
    transfer_page.enter_otp("000000")
    transfer_page.confirm_transfer()
    expect(transfer_page.error_message()).to_have_text("Invalid OTP")

def test_add_new_beneficiary(transfer_page: TransferPage):
    transfer_page.navigate_to_beneficiary_management()
    transfer_page.click_add_beneficiary()
    transfer_page.fill_beneficiary_details(account="1234567890", ifsc="ABCD0123456", name="John Doe")
    transfer_page.save_beneficiary()
    expect(transfer_page.beneficiary_toast()).to_have_text("Beneficiary added successfully")
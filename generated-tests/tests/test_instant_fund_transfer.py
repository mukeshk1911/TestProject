import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page: Page) -> TransferPage:
    return TransferPage(page)

def test_successful_transfer(transfer_page: TransferPage):
    transfer_page.navigate_to_transfer()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount(5000)
    transfer_page.click_continue()
    transfer_page.enter_otp("123456")
    transfer_page.confirm_transfer()
    expect(transfer_page.success_toast()).to_be_visible()
    expect(transfer_page.transaction_in_history(5000, "John Doe")).to_be_true()

def test_transfer_exceeds_limit(transfer_page: TransferPage):
    transfer_page.navigate_to_transfer()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount(150000)
    transfer_page.click_continue()
    expect(transfer_page.error_message()).to_have_text("Transfer amount exceeds limit of ₹1,00,000")

def test_otp_failure_cancels_transaction(transfer_page: TransferPage):
    transfer_page.navigate_to_transfer()
    transfer_page.enter_amount(2500)
    transfer_page.click_continue()
    for _ in range(3):
        transfer_page.enter_otp("000000")
        transfer_page.confirm_transfer()
    expect(transfer_page.error_message()).to_have_text("OTP attempts exceeded, transaction cancelled")
    expect(transfer_page.transaction_in_history(2500, "John Doe")).to_be_false()

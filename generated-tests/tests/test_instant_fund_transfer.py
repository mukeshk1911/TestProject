import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page: Page) -> TransferPage:
    return TransferPage(page)

def test_add_beneficiary_valid(transfer_page: TransferPage):
    transfer_page.navigate_to_beneficiary_management()
    transfer_page.add_beneficiary(account="123456789012", ifsc="ABCD0123456", name="John Doe")
    expect(transfer_page.success_toast).to_be_visible()
    expect(transfer_page.beneficiary_in_list("John Doe")).to_be_true()

def test_successful_transfer_existing_beneficiary(transfer_page: TransferPage):
    transfer_page.open_transfer_screen()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount(5000)
    transfer_page.click_continue()
    transfer_page.enter_otp("123456")
    transfer_page.click_confirm()
    expect(transfer_page.confirmation_message).to_have_text("Transfer successful")
    expect(transfer_page.transaction_in_history(5000, "John Doe")).to_be_true()

def test_otp_verification_flow(transfer_page: TransferPage):
    transfer_page.open_transfer_screen()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount(2500)
    transfer_page.click_continue()
    transfer_page.enter_otp("654321")
    transfer_page.click_confirm()
    expect(transfer_page.success_notification).to_be_visible()

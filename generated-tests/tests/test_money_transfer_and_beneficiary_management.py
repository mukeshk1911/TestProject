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
    transfer_page.click_add_beneficiary()
    expect(transfer_page.success_message).to_have_text("Beneficiary added successfully")

def test_transfer_money_success(transfer_page: TransferPage):
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount("5000")
    transfer_page.click_proceed()
    transfer_page.enter_otp("123456")
    transfer_page.click_confirm_transfer()
    expect(transfer_page.confirmation_message).to_have_text("Transfer completed successfully")

def test_transfer_amount_exceeds_limit(transfer_page: TransferPage):
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount("100001")
    transfer_page.click_proceed()
    expect(transfer_page.error_message).to_have_text("Transfer amount exceeds limit")

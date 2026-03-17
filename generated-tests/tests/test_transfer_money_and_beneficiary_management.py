import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page: Page) -> TransferPage:
    return TransferPage(page)

def test_add_valid_beneficiary(transfer_page: TransferPage):
    transfer_page.navigate_to_add_beneficiary()
    transfer_page.add_beneficiary(name="John Doe", account_number="123456789012", ifsc="ABCD0123456")
    expect(transfer_page.beneficiary_in_list("John Doe")).to_be_visible()

def test_successful_transfer(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.proceed()
    transfer_page.enter_otp("123456")
    transfer_page.confirm_transfer()
    expect(transfer_page.success_notification()).to_have_text("Transfer successful")

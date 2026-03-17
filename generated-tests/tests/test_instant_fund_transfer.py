import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page: Page) -> TransferPage:
    return TransferPage(page)

def test_add_valid_beneficiary(transfer_page: TransferPage):
    transfer_page.navigate_to_beneficiary_management()
    transfer_page.click_add_beneficiary()
    transfer_page.fill_beneficiary_form(account="123456789012", ifsc="ABCD0123456", name="John Doe")
    transfer_page.save_beneficiary()
    expect(transfer_page.beneficiary_in_list("John Doe")).to_be_visible()

def test_successful_transfer(transfer_page: TransferPage):
    transfer_page.open_transfer_screen()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount(5000)
    transfer_page.click_continue()
    transfer_page.enter_otp("123456")
    transfer_page.confirm_transfer()
    expect(transfer_page.success_toast()).to_have_text("Transfer successful")

import pytest
from playwright.sync_api import Page, expect
from pages.beneficiary_page import BeneficiaryPage
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page):
    return BeneficiaryPage(page)

@pytest.fixture(scope="function")
def transfer_page(page: Page):
    return TransferPage(page)

def test_add_beneficiary_success(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto()
    beneficiary_page.enter_account_number("123456789012")
    beneficiary_page.enter_ifsc("QRST0001234")
    beneficiary_page.submit()
    expect(beneficiary_page.success_toast).to_be_visible()

def test_instant_transfer_success(transfer_page: TransferPage):
    transfer_page.goto()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount("5000")
    transfer_page.proceed()
    transfer_page.enter_otp("123456")
    expect(transfer_page.confirmation_message).to_have_text("Transfer successful")

def test_otp_verification_success(transfer_page: TransferPage):
    transfer_page.initiate_transfer()
    transfer_page.enter_otp("654321")
    expect(transfer_page.success_banner).to_be_visible()

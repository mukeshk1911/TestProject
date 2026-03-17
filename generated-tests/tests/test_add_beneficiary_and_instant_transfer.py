import pytest
from playwright.sync_api import Page, expect
from pages.beneficiary_page import BeneficiaryPage
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def login(page: Page):
    # Assume login helper exists
    page.goto("https://banking.example.com/login")
    page.fill("#username", "testuser")
    page.fill("#password", "Password123")
    page.click("#loginButton")
    expect(page).to_have_url("/dashboard")
    return page

def test_add_beneficiary_success(login: Page):
    beneficiary_page = BeneficiaryPage(login)
    beneficiary_page.navigate()
    beneficiary_page.add_beneficiary("123456789012", "MNOP0123456", "John Doe")
    expect(beneficiary_page.success_message).to_be_visible()

def test_instant_transfer_success(login: Page):
    transfer_page = TransferPage(login)
    transfer_page.initiate_transfer("John Doe", 5000)
    transfer_page.enter_otp("654321")
    expect(transfer_page.confirmation_message).to_have_text("Transfer successful")

def test_transfer_otp_failure(login: Page):
    transfer_page = TransferPage(login)
    transfer_page.initiate_transfer("John Doe", 2000)
    for otp in ["111111", "222222", "333333"]:
        transfer_page.enter_otp(otp)
        expect(transfer_page.error_message).to_be_visible()
    expect(transfer_page.cancellation_message).to_have_text("Transaction cancelled")

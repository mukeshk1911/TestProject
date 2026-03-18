import pytest
from playwright.sync_api import Page, expect
from pages.beneficiary_page import BeneficiaryPage
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def login(page: Page):
    # Assume login helper exists
    page.goto("https://bank.example.com/login")
    page.fill("#username", "test_user")
    page.fill("#password", "Password123")
    page.click("#loginButton")
    expect(page).to_have_url("/dashboard")
    return page

def test_add_beneficiary_success(login: Page):
    ben_page = BeneficiaryPage(login)
    ben_page.navigate()
    ben_page.add_beneficiary(account_number="123456789012", ifsc="ABCD0123456")
    expect(ben_page.success_toast).to_be_visible()

def test_transfer_money_success(login: Page):
    transfer = TransferPage(login)
    transfer.select_beneficiary("John Doe")
    transfer.enter_amount(5000)
    transfer.proceed()
    transfer.enter_otp("123456")
    expect(transfer.confirmation_message).to_have_text("Transfer successful")

def test_transfer_exceeds_limit(login: Page):
    transfer = TransferPage(login)
    transfer.select_beneficiary("John Doe")
    transfer.enter_amount(200000)
    transfer.proceed()
    expect(transfer.error_message).to_have_text("Transfer amount exceeds daily limit")

import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage
from pages.beneficiary_page import BeneficiaryPage

@pytest.fixture(scope="function")
def login(page: Page):
    # Assume login helper exists
    page.goto("https://bank.example.com/login")
    page.fill("#username", "testuser")
    page.fill("#password", "Password123!")
    page.click("button:has-text('Login')")
    expect(page).to_have_url("/dashboard")
    return page

def test_add_beneficiary_success(login: Page):
    beneficiary_page = BeneficiaryPage(login)
    beneficiary_page.navigate()
    beneficiary_page.add_beneficiary(account="123456789012", ifsc="QRST0001234")
    expect(login.locator("text=Beneficiary added successfully")).to_be_visible()

def test_transfer_within_limit(login: Page):
    transfer_page = TransferPage(login)
    transfer_page.navigate()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount("5000")
    transfer_page.proceed()
    transfer_page.enter_otp("123456")
    expect(login.locator("text=Transaction confirmed")).to_be_visible()

def test_otp_verification_success(login: Page):
    transfer_page = TransferPage(login)
    transfer_page.initiate_transfer_for_beneficiary("John Doe", "2000")
    transfer_page.enter_otp("654321")
    expect(login.locator("text=Transaction successful")).to_be_visible()

import pytest
from playwright.sync_api import Page, expect
from pages.beneficiary_page import BeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page) -> BeneficiaryPage:
    return BeneficiaryPage(page)

def test_add_beneficiary_valid(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto_add_beneficiary()
    beneficiary_page.fill_account_number("123456789012")
    beneficiary_page.fill_ifsc("ABCD0123456")
    beneficiary_page.fill_name("John Doe")
    beneficiary_page.click_add()
    expect(beneficiary_page.success_message()).to_have_text("Beneficiary added successfully")

def test_transfer_within_limits(beneficiary_page: BeneficiaryPage):
    beneficiary_page.select_beneficiary("John Doe")
    beneficiary_page.enter_amount("5000")
    beneficiary_page.proceed_to_otp()
    beneficiary_page.enter_otp("123456")
    beneficiary_page.confirm_transfer()
    expect(beneficiary_page.transfer_success_message()).to_have_text("Transfer successful")

def test_otp_successful(beneficiary_page: BeneficiaryPage):
    beneficiary_page.enter_otp("654321")
    beneficiary_page.verify_otp()
    expect(beneficiary_page.transaction_success_message()).to_have_text("Transaction completed")
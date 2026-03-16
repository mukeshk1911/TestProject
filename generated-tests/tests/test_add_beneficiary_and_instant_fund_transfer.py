import pytest
from playwright.sync_api import Page, expect
from pages.beneficiary_page import BeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page) -> BeneficiaryPage:
    return BeneficiaryPage(page)

def test_add_beneficiary_success(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto_add_beneficiary()
    beneficiary_page.enter_account_number("123456789012")
    beneficiary_page.enter_ifsc("ABCD0123456")
    beneficiary_page.enter_name("John Doe")
    beneficiary_page.click_add()
    expect(beneficiary_page.success_toast()).to_have_text("Beneficiary added successfully")

def test_add_beneficiary_invalid_account(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto_add_beneficiary()
    beneficiary_page.enter_account_number("12AB34CD56")
    beneficiary_page.enter_ifsc("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.error_toast()).to_have_text("Invalid account number format")

def test_transfer_otp_lockout(page: Page):
    # Assuming user is already on transfer screen with beneficiary selected
    page.fill("input[name='otp']", "111111")
    page.click("button:has-text('Verify OTP')")
    page.click("button:has-text('Verify OTP')")
    page.click("button:has-text('Verify OTP')")
    expect(page.locator("text=Maximum OTP attempts exceeded. Transaction cancelled.")).to_be_visible()

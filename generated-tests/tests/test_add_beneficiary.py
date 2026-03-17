import pytest
from playwright.sync_api import Page, expect
from pages.add_beneficiary_page import AddBeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page):
    # Assume login is handled by a separate fixture
    return AddBeneficiaryPage(page)

def test_successful_add_beneficiary(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.open_add_form()
    beneficiary_page.fill_account_number("123456789012")
    beneficiary_page.fill_ifsc("MNOP0123456")
    beneficiary_page.submit()
    expect(beneficiary_page.success_toast).to_be_visible()
    expect(beneficiary_page.success_toast).to_have_text("Beneficiary added successfully")
    expect(beneficiary_page.is_beneficiary_in_list("123456789012")).to_be_true()

def test_add_beneficiary_invalid_account(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.open_add_form()
    beneficiary_page.fill_account_number("abc123")
    beneficiary_page.fill_ifsc("QRST0001234")
    beneficiary_page.submit()
    expect(beneficiary_page.error_message).to_be_visible()
    expect(beneficiary_page.error_message).to_have_text("Account number must be numeric and 10‑16 digits")

def test_add_beneficiary_session_expired(page: Page):
    # Simulate session expiration by clearing cookies
    page.context.clear_cookies()
    page.goto("https://example.com/beneficiaries/add")
    # The page should redirect to login or show session expired banner
    expect(page).to_have_url("**/login**")

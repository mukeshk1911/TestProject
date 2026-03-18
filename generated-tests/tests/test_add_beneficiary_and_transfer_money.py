import pytest
from playwright.sync_api import Page, expect
from pages.beneficiary_page import BeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page):
    return BeneficiaryPage(page)

def test_add_beneficiary_valid(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto_add_beneficiary()
    beneficiary_page.enter_account_number("123456789012")
    beneficiary_page.enter_ifsc("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.success_notification).to_have_text("Beneficiary added successfully")

def test_add_beneficiary_invalid_account(beneficiary_page: BeneficiaryPage):
    beneficiary_page.goto_add_beneficiary()
    beneficiary_page.enter_account_number("ABCDEF1234")
    beneficiary_page.enter_ifsc("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.error_message).to_have_text("Account number must be numeric and 10-16 digits")

def test_transfer_requires_otp(page: Page):
    # Assuming TransferPage is defined similarly
    from pages.transfer_page import TransferPage
    transfer = TransferPage(page)
    transfer.select_beneficiary("John Doe")
    transfer.enter_amount("5000")
    transfer.click_proceed()
    transfer.enter_otp("111111")
    transfer.enter_otp("222222")
    transfer.enter_otp("333333")
    expect(transfer.cancellation_message).to_have_text("OTP verification failed")

def test_add_beneficiary_api(requests):
    payload = {"accountNumber": "123456789012", "ifsc": "ABCD0123456", "name": "John Doe"}
    headers = {"Authorization": f"Bearer {request.env.get('API_TOKEN')}"}
    response = requests.post("https://api.bankapp.com/v1/beneficiaries", json=payload, headers=headers)
    assert response.status_code == 201
    assert "beneficiaryId" in response.json()

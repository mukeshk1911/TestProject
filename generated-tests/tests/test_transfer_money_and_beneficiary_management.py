import pytest
from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def transfer_page(page: Page) -> TransferPage:
    return TransferPage(page)

def test_add_valid_beneficiary(transfer_page: TransferPage):
    transfer_page.go_to_add_beneficiary()
    transfer_page.enter_account_number("123456789012")
    transfer_page.enter_ifsc("ABCD0123456")
    transfer_page.submit_beneficiary()
    expect(transfer_page.success_notification).to_have_text("Beneficiary added successfully")

def test_transfer_with_correct_otp(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.proceed()
    transfer_page.enter_otp("123456")
    transfer_page.confirm_transfer()
    expect(transfer_page.confirmation_message).to_have_text("Transfer successful")

def test_transfer_with_incorrect_otp(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(5000)
    transfer_page.proceed()
    transfer_page.enter_otp("000000")
    transfer_page.confirm_transfer()
    expect(transfer_page.error_message).to_have_text("Invalid OTP")

def test_transfer_exceeds_limit(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(150000)
    transfer_page.proceed()
    expect(transfer_page.error_message).to_have_text("Transfer amount exceeds the allowed limit")

def test_add_invalid_beneficiary(transfer_page: TransferPage):
    transfer_page.go_to_add_beneficiary()
    transfer_page.enter_account_number("ABC123")
    transfer_page.enter_ifsc("ABCD0123456")
    transfer_page.submit_beneficiary()
    expect(transfer_page.error_message).to_have_text("Account number must be numeric and 10‑16 digits")

def test_minimum_amount_transfer(transfer_page: TransferPage):
    transfer_page.select_beneficiary("BEN123")
    transfer_page.enter_amount(1)
    transfer_page.proceed()
    transfer_page.enter_otp("123456")
    transfer_page.confirm_transfer()
    expect(transfer_page.confirmation_message).to_have_text("Transfer successful")

def test_transaction_history_api(requests):
    response = requests.get("https://bank.example.com/api/transactions", params={"userId": "USER123"})
    assert response.status_code == 200
    data = response.json()
    latest = data[0]
    assert latest["amount"] == 5000
    assert latest["beneficiaryId"] == "BEN123"
    assert latest["status"] == "Success"
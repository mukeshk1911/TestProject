import pytest
from playwright.sync_api import Page, expect
from pages.banking_page import BankingPage

@pytest.fixture(scope="function")
def banking_page(page: Page) -> BankingPage:
    return BankingPage(page)

def test_add_beneficiary_success(banking_page: BankingPage):
    banking_page.navigate_to_add_beneficiary()
    banking_page.add_beneficiary(account_number="123456789012", ifsc="ABCD0123456")
    expect(banking_page.page.locator("text=Beneficiary added successfully")).to_be_visible()

def test_successful_transfer_with_correct_otp(banking_page: BankingPage):
    banking_page.navigate_to_transfer()
    banking_page.select_beneficiary("BEN123")
    banking_page.enter_amount(5000)
    banking_page.proceed_to_otp()
    banking_page.enter_otp("123456")
    banking_page.confirm_transfer()
    expect(banking_page.page.locator("text=Transfer completed")).to_be_visible()

def test_transfer_blocked_by_incorrect_otp(banking_page: BankingPage):
    banking_page.navigate_to_transfer()
    banking_page.select_beneficiary("BEN123")
    banking_page.enter_amount(5000)
    banking_page.proceed_to_otp()
    banking_page.enter_otp("000000")
    banking_page.confirm_transfer()
    expect(banking_page.page.locator("text=Invalid OTP")).to_be_visible()

def test_transaction_history_api():
    import requests
    response = requests.get("https://example.com/api/transactions", params={"userId": "USER123"})
    assert response.status_code == 200
    data = response.json()
    assert any(tx["status"] == "Success" and tx["amount"] == 5000 for tx in data["transactions"])

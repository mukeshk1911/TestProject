import pytest
from playwright.sync_api import Page, expect
from pages.banking_page import BankingPage

@pytest.fixture(scope="function")
def banking_page(page: Page) -> BankingPage:
    return BankingPage(page)

def test_add_beneficiary_success(banking_page: BankingPage):
    banking_page.goto_add_beneficiary()
    banking_page.fill_account_number("123456789012")
    banking_page.fill_ifsc("MNOP0123456")
    banking_page.fill_name("John Doe")
    banking_page.click_add()
    expect(banking_page.success_toast()).to_be_visible()
    expect(banking_page.beneficiary_in_list("John Doe")).to_be_visible()

def test_transfer_with_correct_otp(banking_page: BankingPage):
    banking_page.select_beneficiary("John Doe")
    banking_page.enter_amount("5000")
    banking_page.click_proceed()
    banking_page.enter_otp("123456")
    banking_page.confirm_transfer()
    expect(banking_page.transfer_success_message()).to_be_visible()

def test_transfer_with_incorrect_otp(banking_page: BankingPage):
    banking_page.select_beneficiary("John Doe")
    banking_page.enter_amount("5000")
    banking_page.click_proceed()
    banking_page.enter_otp("000000")
    banking_page.confirm_transfer()
    expect(banking_page.error_message()).to_have_text("Invalid OTP")

def test_transaction_history_api(requests):
    response = requests.get("https://api.bank.com/api/transactions", params={"userId": "USER123"})
    assert response.status_code == 200
    data = response.json()
    latest = data[0]
    assert latest["amount"] == 5000
    assert latest["beneficiary"] == "John Doe"
    assert latest["status"] == "Success"
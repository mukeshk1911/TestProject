import pytest
import json
from playwright.sync_api import Page, expect

from pages.transfer_page import TransferPage
from pages.beneficiary_page import BeneficiaryPage
from pages.api_helper import APIHelper

@pytest.fixture(scope="function")
def login(page: Page):
    # Assume login helper exists
    page.goto("https://bank.example.com/login")
    page.fill("#username", "test_user")
    page.fill("#password", "Password123")
    page.click("button[type='submit']")
    expect(page).to_have_url("/dashboard")
    return page

def test_add_valid_beneficiary(login: Page):
    beneficiary_page = BeneficiaryPage(login)
    beneficiary_page.navigate_to()
    beneficiary_page.add_beneficiary(account="123456789012", ifsc="ABCD0123456", name="John Doe")
    expect(beneficiary_page.success_toast).to_be_visible()
    expect(beneficiary_page.beneficiary_in_list("John Doe")).to_be_true()

def test_successful_transfer(login: Page):
    transfer_page = TransferPage(login)
    transfer_page.open()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount(5000)
    transfer_page.proceed_to_otp()
    transfer_page.enter_otp("123456")
    transfer_page.confirm()
    expect(transfer_page.success_notification).to_be_visible()

def test_otp_failure_cancels_transaction(login: Page):
    transfer_page = TransferPage(login)
    transfer_page.open()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount(2500)
    transfer_page.proceed_to_otp()
    for _ in range(3):
        transfer_page.enter_otp("000000")
        transfer_page.confirm()
    expect(transfer_page.error_message).to_have_text("OTP attempts exceeded, transaction cancelled")

def test_transaction_history_api(login: Page):
    # Perform a transfer via UI first
    transfer_page = TransferPage(login)
    transfer_page.open()
    transfer_page.select_beneficiary("John Doe")
    transfer_page.enter_amount(1500)
    transfer_page.proceed_to_otp()
    transfer_page.enter_otp("654321")
    transfer_page.confirm()
    expect(transfer_page.success_notification).to_be_visible()

    # Capture details
    txn_details = transfer_page.get_last_transaction_details()

    # Call API
    api = APIHelper()
    response = api.get("/api/transactions", headers={"Authorization": "Bearer abc123"})
    assert response.status_code == 200
    data = response.json()
    matching = [t for t in data if t["amount"] == txn_details["amount"] and t["beneficiary"] == txn_details["beneficiary"]]
    assert matching, "New transaction not found in API response"

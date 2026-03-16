import pytest
from playwright.sync_api import Page, expect
from pages.add_beneficiary_page import AddBeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page) -> AddBeneficiaryPage:
    return AddBeneficiaryPage(page)

def test_add_beneficiary_valid(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.open_form()
    beneficiary_page.fill_account("1234567890")
    beneficiary_page.fill_ifsc("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.success_notification()).to_be_visible()

def test_add_beneficiary_non_numeric_account(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.open_form()
    beneficiary_page.fill_account("12AB567890")
    beneficiary_page.fill_ifsc("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.error_message()).to_have_text("Account number must be numeric and 10‑16 digits long")

def test_add_beneficiary_invalid_ifsc(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.open_form()
    beneficiary_page.fill_account("1234567890")
    beneficiary_page.fill_ifsc("ABC12")
    beneficiary_page.click_add()
    expect(beneficiary_page.error_message()).to_have_text("IFSC code must be 11 alphanumeric characters")

def test_add_beneficiary_edge_values(beneficiary_page: AddBeneficiaryPage):
    edge_cases = [
        ("1000000000", "1BCD0123456"),
        ("1234567890123456", "ABCD0123456")
    ]
    for account, ifsc in edge_cases:
        beneficiary_page.open_form()
        beneficiary_page.fill_account(account)
        beneficiary_page.fill_ifsc(ifsc)
        beneficiary_page.click_add()
        expect(beneficiary_page.success_notification()).to_be_visible()

def test_unauthorized_api_access(requests):
    payload = {"account_number": "1234567890", "ifsc": "ABCD0123456"}
    response = requests.post("https://example.com/api/beneficiaries", json=payload)
    assert response.status_code == 401
    assert "Authentication required" in response.text

def test_add_beneficiary_api_success(requests, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"account_number": "1234567890", "ifsc": "ABCD0123456"}
    response = requests.post("https://example.com/api/beneficiaries", json=payload, headers=headers)
    assert response.status_code == 201
    json_body = response.json()
    assert "beneficiary_id" in json_body
    assert json_body.get("message") == "Beneficiary added successfully"

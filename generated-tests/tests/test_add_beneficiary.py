import pytest
from playwright.sync_api import Page, expect
from pages.add_beneficiary_page import AddBeneficiaryPage

@pytest.fixture(scope="function")
def beneficiary_page(page: Page) -> AddBeneficiaryPage:
    return AddBeneficiaryPage(page)

def test_add_beneficiary_success(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.navigate_to_section()
    beneficiary_page.open_add_form()
    beneficiary_page.fill_account_number("1234567890")
    beneficiary_page.fill_ifsc_code("ABCD0123456")
    beneficiary_page.click_add()
    expect(beneficiary_page.success_notification()).to_be_visible()

def test_add_beneficiary_invalid_ifsc(beneficiary_page: AddBeneficiaryPage):
    beneficiary_page.open_add_form()
    beneficiary_page.fill_account_number("1234567890")
    beneficiary_page.fill_ifsc_code("ABC12")
    beneficiary_page.click_add()
    expect(beneficiary_page.error_message()).to_have_text("IFSC code must be 11 alphanumeric characters")

def test_add_beneficiary_unauthorized_api(request):
    import requests
    payload = {"account_number": "1234567890", "ifsc": "ABCD0123456"}
    response = requests.post("https://example.com/api/beneficiaries", json=payload)
    assert response.status_code == 401
    assert response.json()["error"] == "Authentication required"

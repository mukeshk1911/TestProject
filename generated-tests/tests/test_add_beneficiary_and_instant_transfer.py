import pytest
from pages.beneficiary_page import BeneficiaryPage
from pages.transfer_page import TransferPage

@pytest.fixture(scope="function")
def setup(page):
    # Assume user is already logged in via fixture or prior step
    yield page

def test_add_beneficiary_success(setup):
    page = setup
    beneficiary = BeneficiaryPage(page)
    beneficiary.navigate()
    beneficiary.add_beneficiary(account_number="123456789012", ifsc="QRST0001234")
    assert beneficiary.is_success_message_displayed()

def test_transfer_within_limit_success(setup):
    page = setup
    transfer = TransferPage(page)
    transfer.navigate()
    transfer.select_beneficiary(name="John Doe")
    transfer.enter_amount("5000")
    transfer.proceed()
    transfer.enter_otp("123456")
    assert transfer.is_transfer_successful()

def test_otp_verification_success(setup):
    page = setup
    transfer = TransferPage(page)
    transfer.initiate_transfer()
    transfer.enter_otp("654321")
    assert transfer.is_transfer_successful()

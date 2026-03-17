class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.url = "/beneficiary/add"
        self.account_input = "#accountNumber"
        self.ifsc_input = "#ifscCode"
        self.add_button = "#addBeneficiaryBtn"
        self.success_toast = "#toastSuccess"

    def navigate(self):
        self.page.goto(self.url)

    def add_beneficiary(self, account_number: str, ifsc: str):
        self.page.fill(self.account_input, account_number)
        self.page.fill(self.ifsc_input, ifsc)
        self.page.click(self.add_button)

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.beneficiary_dropdown = "#beneficiarySelect"
        self.amount_input = "#transferAmount"
        self.proceed_button = "#proceedTransfer"
        self.otp_input = "#otpInput"
        self.verify_otp_button = "#verifyOtpBtn"
        self.confirmation_message = "#transferSuccessMsg"
        self.error_message = "#transferErrorMsg"

    def select_beneficiary(self, name: str):
        self.page.select_option(self.beneficiary_dropdown, label=name)

    def enter_amount(self, amount: int):
        self.page.fill(self.amount_input, str(amount))

    def proceed(self):
        self.page.click(self.proceed_button)

    def enter_otp(self, otp: str):
        self.page.fill(self.otp_input, otp)
        self.page.click(self.verify_otp_button)

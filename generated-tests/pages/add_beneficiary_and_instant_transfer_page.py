class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.url = "/beneficiaries/add"
        self.account_input = "#accountNumber"
        self.ifsc_input = "#ifscCode"
        self.name_input = "#beneficiaryName"
        self.add_button = "#addBeneficiaryBtn"
        self.success_message = self.page.locator(".toast-success")

    def navigate(self):
        self.page.goto(self.url)

    def add_beneficiary(self, account_number, ifsc, name):
        self.page.fill(self.account_input, account_number)
        self.page.fill(self.ifsc_input, ifsc)
        self.page.fill(self.name_input, name)
        self.page.click(self.add_button)

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.url = "/transfer"
        self.beneficiary_dropdown = "#beneficiarySelect"
        self.amount_input = "#transferAmount"
        self.proceed_button = "#proceedBtn"
        self.otp_input = "#otpInput"
        self.submit_otp_button = "#submitOtpBtn"
        self.confirmation_message = self.page.locator(".transfer-success")
        self.error_message = self.page.locator(".otp-error")
        self.cancellation_message = self.page.locator(".transfer-cancelled")

    def initiate_transfer(self, beneficiary_name, amount):
        self.page.goto(self.url)
        self.page.select_option(self.beneficiary_dropdown, label=beneficiary_name)
        self.page.fill(self.amount_input, str(amount))
        self.page.click(self.proceed_button)

    def enter_otp(self, otp):
        self.page.fill(self.otp_input, otp)
        self.page.click(self.submit_otp_button)

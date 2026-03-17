class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.url = "/beneficiaries/add"
        self.account_input = "#accountNumber"
        self.ifsc_input = "#ifscCode"
        self.add_button = "button:has-text('Add Beneficiary')"

    def navigate(self):
        self.page.goto(self.url)

    def add_beneficiary(self, account, ifsc):
        self.page.fill(self.account_input, account)
        self.page.fill(self.ifsc_input, ifsc)
        self.page.click(self.add_button)

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.url = "/transfer"
        self.beneficiary_dropdown = "#beneficiarySelect"
        self.amount_input = "#transferAmount"
        self.proceed_button = "button:has-text('Proceed')"
        self.otp_input = "#otp"
        self.submit_otp_button = "button:has-text('Submit OTP')"

    def navigate(self):
        self.page.goto(self.url)

    def select_beneficiary(self, name):
        self.page.select_option(self.beneficiary_dropdown, label=name)

    def enter_amount(self, amount):
        self.page.fill(self.amount_input, amount)

    def proceed(self):
        self.page.click(self.proceed_button)

    def enter_otp(self, otp):
        self.page.fill(self.otp_input, otp)
        self.page.click(self.submit_otp_button)

    def initiate_transfer_for_beneficiary(self, name, amount):
        self.select_beneficiary(name)
        self.enter_amount(amount)
        self.proceed()
class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.account_input = page.locator('#accountNumber')
        self.ifsc_input = page.locator('#ifscCode')
        self.add_button = page.locator('button#addBeneficiary')
        self.success_toast = page.locator('.toast-success')

    def goto_add_page(self):
        self.page.goto('https://bank.example.com/beneficiaries/add')

    def enter_account_number(self, account_number: str):
        self.account_input.fill(account_number)

    def enter_ifsc(self, ifsc: str):
        self.ifsc_input.fill(ifsc)

    def submit(self):
        self.add_button.click()

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.beneficiary_dropdown = page.locator('#beneficiarySelect')
        self.amount_input = page.locator('#transferAmount')
        self.proceed_button = page.locator('button#proceedTransfer')
        self.otp_input = page.locator('#otp')
        self.confirm_button = page.locator('button#confirmTransfer')
        self.confirmation_message = page.locator('.transfer-confirmation')
        self.error_message = page.locator('.error-message')

    def select_beneficiary(self, beneficiary_id: str):
        self.beneficiary_dropdown.select_option(beneficiary_id)

    def enter_amount(self, amount: str):
        self.amount_input.fill(amount)

    def proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp: str):
        self.otp_input.fill(otp)

    def confirm(self):
        self.confirm_button.click()

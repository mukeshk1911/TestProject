class TransferPage:
    def __init__(self, page):
        self.page = page
        self.add_beneficiary_btn = page.locator("button#addBeneficiary")
        self.account_input = page.locator("input#accountNumber")
        self.ifsc_input = page.locator("input#ifscCode")
        self.success_toast = page.locator("div.toast-success")
        self.error_toast = page.locator("div.toast-error")
        self.beneficiary_dropdown = page.locator("select#beneficiaryList")
        self.amount_input = page.locator("input#transferAmount")
        self.proceed_btn = page.locator("button#proceedTransfer")
        self.otp_input = page.locator("input#otpCode")
        self.confirm_btn = page.locator("button#confirmTransfer")

    def navigate_to_add_beneficiary(self):
        self.page.goto("/beneficiary/add")

    def add_beneficiary(self, account_number: str, ifsc: str):
        self.account_input.fill(account_number)
        self.ifsc_input.fill(ifsc)
        self.add_beneficiary_btn.click()

    def select_beneficiary(self, beneficiary_id: str):
        self.beneficiary_dropdown.select_option(beneficiary_id)

    def enter_amount(self, amount: int):
        self.amount_input.fill(str(amount))

    def proceed(self):
        self.proceed_btn.click()

    def enter_otp(self, otp: str):
        self.otp_input.fill(otp)

    def confirm_transfer(self):
        self.confirm_btn.click()

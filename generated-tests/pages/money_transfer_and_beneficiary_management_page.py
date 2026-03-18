class TransferPage:
    def __init__(self, page):
        self.page = page
        self.add_beneficiary_button = page.locator("button#addBeneficiary")
        self.account_input = page.locator("input#accountNumber")
        self.ifsc_input = page.locator("input#ifscCode")
        self.success_message = page.locator("div.success")
        self.error_message = page.locator("div.error")
        self.beneficiary_dropdown = page.locator("select#beneficiaryList")
        self.amount_input = page.locator("input#transferAmount")
        self.proceed_button = page.locator("button#proceedTransfer")
        self.otp_input = page.locator("input#otpCode")
        self.confirm_button = page.locator("button#confirmTransfer")
        self.confirmation_message = page.locator("div.confirmation")

    def goto_add_beneficiary(self):
        self.page.goto("/beneficiaries/add")

    def enter_account_number(self, account):
        self.account_input.fill(account)

    def enter_ifsc(self, ifsc):
        self.ifsc_input.fill(ifsc)

    def click_add_beneficiary(self):
        self.add_beneficiary_button.click()

    def select_beneficiary(self, name):
        self.beneficiary_dropdown.select_option(label=name)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def click_proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def click_confirm_transfer(self):
        self.confirm_button.click()

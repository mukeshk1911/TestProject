class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.add_beneficiary_url = "/beneficiary/add"
        self.account_input = page.locator("#accountNumber")
        self.ifsc_input = page.locator("#ifscCode")
        self.name_input = page.locator("#beneficiaryName")
        self.add_button = page.locator("button#addBeneficiary")
        self.success_msg = page.locator(".toast-success")
        self.beneficiary_list = page.locator("#beneficiaryList")
        self.amount_input = page.locator("#transferAmount")
        self.proceed_button = page.locator("button#proceedTransfer")
        self.otp_input = page.locator("#otpInput")
        self.verify_otp_button = page.locator("button#verifyOtp")
        self.transfer_success_msg = page.locator(".transfer-success")

    def goto_add_beneficiary(self):
        self.page.goto(self.add_beneficiary_url)

    def fill_account_number(self, number):
        self.account_input.fill(number)

    def fill_ifsc(self, ifsc):
        self.ifsc_input.fill(ifsc)

    def fill_name(self, name):
        self.name_input.fill(name)

    def click_add(self):
        self.add_button.click()

    def success_message(self):
        return self.success_msg

    def select_beneficiary(self, name):
        self.beneficiary_list.locator(f"text={name}").click()

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def proceed_to_otp(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def verify_otp(self):
        self.verify_otp_button.click()

    def transfer_success_message(self):
        return self.transfer_success_msg

    def transaction_success_message(self):
        return self.transfer_success_msg
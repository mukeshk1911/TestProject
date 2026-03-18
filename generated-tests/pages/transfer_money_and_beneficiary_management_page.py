class BankingPage:
    def __init__(self, page):
        self.page = page
        self.add_beneficiary_url = "/beneficiary/add"
        self.account_input = self.page.locator("#accountNumber")
        self.ifsc_input = self.page.locator("#ifscCode")
        self.name_input = self.page.locator("#beneficiaryName")
        self.add_button = self.page.locator("button#addBeneficiary")
        self.success_toast = self.page.locator(".toast-success")
        self.beneficiary_list = self.page.locator("#beneficiaryList")
        self.amount_input = self.page.locator("#transferAmount")
        self.proceed_button = self.page.locator("button#proceedTransfer")
        self.otp_input = self.page.locator("#otpInput")
        self.confirm_button = self.page.locator("button#confirmTransfer")
        self.success_message = self.page.locator(".transfer-success")
        self.error_message = self.page.locator(".error-message")

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

    def success_toast(self):
        return self.success_toast

    def beneficiary_in_list(self, name):
        return self.beneficiary_list.locator(f"text={name}")

    def select_beneficiary(self, name):
        self.beneficiary_list.locator(f"text={name}").click()

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def click_proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def confirm_transfer(self):
        self.confirm_button.click()

    def transfer_success_message(self):
        return self.success_message

    def error_message(self):
        return self.error_message
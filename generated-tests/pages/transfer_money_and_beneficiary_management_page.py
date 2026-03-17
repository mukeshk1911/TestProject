class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.url = "/add-beneficiary"
        self.account_input = page.locator("#accountNumber")
        self.ifsc_input = page.locator("#ifscCode")
        self.name_input = page.locator("#beneficiaryName")
        self.add_button = page.locator("button#addBeneficiary")
        self.toast = page.locator(".toast-success")
        self.error = page.locator(".validation-error")
        self.list_item = lambda name: page.locator(f"//li[contains(text(), '{name}')]")

    def goto_add_beneficiary(self):
        self.page.goto(self.url)

    def fill_account_number(self, number):
        self.account_input.fill(number)

    def fill_ifsc(self, ifsc):
        self.ifsc_input.fill(ifsc)

    def fill_name(self, name):
        self.name_input.fill(name)

    def submit(self):
        self.add_button.click()

    def success_toast(self):
        return self.toast

    def validation_error(self):
        return self.error

    def beneficiary_in_list(self, name):
        return self.list_item(name)

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.beneficiary_dropdown = page.locator("#beneficiarySelect")
        self.amount_input = page.locator("#transferAmount")
        self.proceed_button = page.locator("button#proceed")
        self.otp_input = page.locator("#otpInput")
        self.confirm_button = page.locator("button#confirmTransfer")
        self.success_msg = page.locator(".transfer-success")
        self.error_msg = page.locator(".transfer-error")

    def select_beneficiary(self, beneficiary_id):
        self.beneficiary_dropdown.select_option(beneficiary_id)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def confirm(self):
        self.confirm_button.click()

    def success_message(self):
        return self.success_msg

    def error_message(self):
        return self.error_msg
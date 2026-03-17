class TransferPage:
    def __init__(self, page):
        self.page = page
        self.transfer_url = "/transfer"
        self.beneficiary_mgmt_url = "/beneficiaries"
        self.select_beneficiary_dropdown = self.page.locator("#beneficiary-select")
        self.amount_input = self.page.locator("#amount")
        self.proceed_button = self.page.locator("#proceed")
        self.otp_input = self.page.locator("#otp")
        self.confirm_button = self.page.locator("#confirm")
        self.success_msg = self.page.locator(".toast-success")
        self.error_msg = self.page.locator(".toast-error")
        self.add_beneficiary_btn = self.page.locator("#add-beneficiary")
        self.account_input = self.page.locator("#account-number")
        self.ifsc_input = self.page.locator("#ifsc-code")
        self.name_input = self.page.locator("#beneficiary-name")
        self.save_beneficiary_btn = self.page.locator("#save-beneficiary")
        self.beneficiary_toast = self.page.locator(".toast-beneficiary")

    def navigate_to_transfer(self):
        self.page.goto(self.transfer_url)

    def navigate_to_beneficiary_management(self):
        self.page.goto(self.beneficiary_mgmt_url)

    def select_beneficiary(self, beneficiary_id):
        self.select_beneficiary_dropdown.select_option(beneficiary_id)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def request_otp(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def confirm_transfer(self):
        self.confirm_button.click()

    def success_message(self):
        return self.success_msg

    def error_message(self):
        return self.error_msg

    def click_add_beneficiary(self):
        self.add_beneficiary_btn.click()

    def fill_beneficiary_details(self, account, ifsc, name):
        self.account_input.fill(account)
        self.ifsc_input.fill(ifsc)
        self.name_input.fill(name)

    def save_beneficiary(self):
        self.save_beneficiary_btn.click()

    def beneficiary_toast(self):
        return self.beneficiary_toast
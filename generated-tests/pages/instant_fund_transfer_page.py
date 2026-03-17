class TransferPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.add_beneficiary_btn = page.locator("text=Add Beneficiary")
        self.account_input = page.locator("#accountNumber")
        self.ifsc_input = page.locator("#ifscCode")
        self.save_btn = page.locator("button:has-text('Save')")
        self.beneficiary_success_message = page.locator("#beneficiarySuccess")
        self.transfer_menu = page.locator("text=Transfer Money")
        self.beneficiary_dropdown = page.locator("#beneficiarySelect")
        self.amount_input = page.locator("#transferAmount")
        self.submit_btn = page.locator("button:has-text('Submit')")
        self.otp_input = page.locator("#otpInput")
        self.confirm_btn = page.locator("button:has-text('Confirm OTP')")
        self.confirmation_message = page.locator("#transferSuccess")
        self.error_message = page.locator("#transferError")

    def goto_add_beneficiary(self):
        self.add_beneficiary_btn.click()

    def enter_account_number(self, number: str):
        self.account_input.fill(number)

    def enter_ifsc(self, ifsc: str):
        self.ifsc_input.fill(ifsc)

    def save_beneficiary(self):
        self.save_btn.click()

    def goto_transfer(self):
        self.transfer_menu.click()

    def select_beneficiary(self, name: str):
        self.beneficiary_dropdown.select_option(label=name)

    def enter_amount(self, amount: str):
        self.amount_input.fill(amount)

    def submit_transfer(self):
        self.submit_btn.click()

    def enter_otp(self, otp: str):
        self.otp_input.fill(otp)
        self.confirm_btn.click()
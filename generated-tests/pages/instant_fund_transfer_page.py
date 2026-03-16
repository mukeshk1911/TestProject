class TransferPage:
    def __init__(self, page):
        self.page = page
        self.transfer_url = "/transfer"
        self.beneficiary_dropdown = self.page.locator("#beneficiary-select")
        self.amount_input = self.page.locator("#amount")
        self.continue_button = self.page.locator("button:has-text('Continue')")
        self.otp_input = self.page.locator("#otp")
        self.confirm_button = self.page.locator("button:has-text('Confirm')")
        self.success_toast = self.page.locator(".toast-success")
        self.error_toast = self.page.locator(".toast-error")

    def navigate_to_transfer(self):
        self.page.goto(self.transfer_url)

    def select_beneficiary(self, name):
        self.beneficiary_dropdown.select_option(label=name)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def click_continue(self):
        self.continue_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def confirm_transfer(self):
        self.confirm_button.click()

    def success_toast(self):
        return self.success_toast

    def error_message(self):
        return self.error_toast

    def transaction_in_history(self, amount, beneficiary):
        # Simplified check – in real tests would query UI or API
        row = self.page.locator(f"tr:has-text('{beneficiary}') >> td:has-text('{amount}')")
        return row.count() > 0

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.transfer_button = page.locator("text=Transfer")
        self.beneficiary_dropdown = page.locator("#beneficiary-select")
        self.amount_input = page.locator("#amount")
        self.continue_button = page.locator("text=Continue")
        self.otp_input = page.locator("#otp")
        self.confirm_button = page.locator("text=Confirm")
        self.success_toast = page.locator(".toast-success")
        self.error_message = page.locator(".error-message")

    def navigate_to_transfer(self):
        self.transfer_button.click()

    def select_beneficiary(self, name):
        self.beneficiary_dropdown.select_option(label=name)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def click_continue(self):
        self.continue_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def click_confirm(self):
        self.confirm_button.click()

    def success_toast(self):
        return self.success_toast

    def error_message(self):
        return self.error_message

    def transaction_in_history(self, amount, beneficiary):
        # Placeholder for actual implementation
        return self.page.locator(f"text={beneficiary} >> text={amount}")

    def transaction_exists_in_history(self):
        # Placeholder for checking any transaction exists after cancellation
        return self.page.locator(".transaction-row").count() > 0
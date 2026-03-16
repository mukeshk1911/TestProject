class TransferPage:
    def __init__(self, page):
        self.page = page
        self.beneficiary_menu = page.locator("text=Beneficiary Management")
        self.add_button = page.locator("button:has-text('Add Beneficiary')")
        self.account_input = page.locator("input[name='account']")
        self.ifsc_input = page.locator("input[name='ifsc']")
        self.name_input = page.locator("input[name='name']")
        self.save_button = page.locator("button:has-text('Save')")
        self.success_toast = page.locator(".toast-success")
        self.transfer_button = page.locator("text=Transfer")
        self.amount_input = page.locator("input[name='amount']")
        self.continue_button = page.locator("button:has-text('Continue')")
        self.otp_input = page.locator("input[name='otp']")
        self.confirm_button = page.locator("button:has-text('Confirm')")
        self.confirmation_message = page.locator(".confirmation-message")
        self.success_notification = page.locator(".notification-success")

    def navigate_to_beneficiary_management(self):
        self.beneficiary_menu.click()

    def add_beneficiary(self, account, ifsc, name):
        self.add_button.click()
        self.account_input.fill(account)
        self.ifsc_input.fill(ifsc)
        self.name_input.fill(name)
        self.save_button.click()

    def beneficiary_in_list(self, name):
        return self.page.locator(f".beneficiary-list >> text={name}")

    def open_transfer_screen(self):
        self.transfer_button.click()

    def select_beneficiary(self, name):
        self.page.locator(f".beneficiary-item >> text={name}").click()

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def click_continue(self):
        self.continue_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def click_confirm(self):
        self.confirm_button.click()

    def transaction_in_history(self, amount, beneficiary):
        return self.page.locator(f".transaction-history >> text={beneficiary} >> text={amount}")

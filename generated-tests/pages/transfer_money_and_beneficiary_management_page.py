class TransferPage:
    def __init__(self, page):
        self.page = page
        self.add_beneficiary_button = page.locator("text=Add Beneficiary")
        self.name_input = page.locator("#beneficiary-name")
        self.account_input = page.locator("#beneficiary-account")
        self.ifsc_input = page.locator("#beneficiary-ifsc")
        self.save_button = page.locator("button:has-text('Save')")
        self.beneficiary_list = page.locator("#beneficiary-list")
        self.beneficiary_select = page.locator("select#beneficiary-select")
        self.amount_input = page.locator("#transfer-amount")
        self.proceed_button = page.locator("button:has-text('Proceed')")
        self.otp_input = page.locator("#otp-input")
        self.confirm_button = page.locator("button:has-text('Confirm Transfer')")
        self.notification = page.locator(".toast-message")

    def navigate_to_add_beneficiary(self):
        self.add_beneficiary_button.click()

    def add_beneficiary(self, name, account_number, ifsc):
        self.name_input.fill(name)
        self.account_input.fill(account_number)
        self.ifsc_input.fill(ifsc)
        self.save_button.click()

    def beneficiary_in_list(self, name):
        return self.beneficiary_list.locator(f"text={name}")

    def select_beneficiary(self, beneficiary_id):
        self.beneficiary_select.select_option(beneficiary_id)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def confirm_transfer(self):
        self.confirm_button.click()

    def success_notification(self):
        return self.notification

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.beneficiary_dropdown = page.locator('#beneficiary')
        self.amount_input = page.locator('#amount')
        self.proceed_button = page.locator('button:has-text("Proceed")')
        self.otp_input = page.locator('#otp')
        self.confirm_button = page.locator('button:has-text("Confirm Transfer")')
        self.success_msg = page.locator('.notification.success')
        self.error_msg = page.locator('.notification.error')

    def select_beneficiary(self, beneficiary_id):
        self.beneficiary_dropdown.select_option(beneficiary_id)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def click_proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def confirm_transfer(self):
        self.confirm_button.click()

    def success_message(self):
        return self.success_msg

    def error_message(self):
        return self.error_msg

class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator('button:has-text("Add Beneficiary")')
        self.account_input = page.locator('#accountNumber')
        self.ifsc_input = page.locator('#ifsc')
        self.success_notif = page.locator('.notification.success')

    def navigate_to_add(self):
        self.page.goto('https://bank.example.com/beneficiaries/add')

    def enter_account_number(self, account_number):
        self.account_input.fill(account_number)

    def enter_ifsc(self, ifsc):
        self.ifsc_input.fill(ifsc)

    def submit(self):
        self.add_button.click()

    def success_notification(self):
        return self.success_notif

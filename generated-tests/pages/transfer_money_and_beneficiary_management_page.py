class TransferPage:
    def __init__(self, page):
        self.page = page
        self.add_beneficiary_button = page.locator("button#addBeneficiary")
        self.account_input = page.locator("input#accountNumber")
        self.ifsc_input = page.locator("input#ifsc")
        self.success_notification = page.locator("div.success")
        self.beneficiary_dropdown = page.locator("select#beneficiary")
        self.amount_input = page.locator("input#amount")
        self.proceed_button = page.locator("button#proceed")
        self.otp_input = page.locator("input#otp")
        self.confirm_button = page.locator("button#confirm")
        self.confirmation_message = page.locator("div.confirmation")
        self.error_message = page.locator("div.error")

    def navigate_to_add_beneficiary(self):
        self.page.goto("/add-beneficiary")

    def enter_account_number(self, account):
        self.account_input.fill(account)

    def enter_ifsc(self, ifsc):
        self.ifsc_input.fill(ifsc)

    def click_add_beneficiary(self):
        self.add_beneficiary_button.click()

    def select_beneficiary(self, beneficiary_id):
        self.beneficiary_dropdown.select_option(beneficiary_id)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def click_proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def click_confirm(self):
        self.confirm_button.click()

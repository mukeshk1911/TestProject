class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.url = "/beneficiary/add"
        self.account_input = self.page.locator("#accountNumber")
        self.ifsc_input = self.page.locator("#ifscCode")
        self.add_button = self.page.locator("button#addBeneficiary")
        self.success_msg = self.page.locator("div.success")

    def navigate(self):
        self.page.goto(self.url)

    def add_beneficiary(self, account_number, ifsc):
        self.account_input.fill(account_number)
        self.ifsc_input.fill(ifsc)
        self.add_button.click()

    def is_success_message_displayed(self):
        return self.success_msg.is_visible()

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.url = "/transfer"
        self.beneficiary_dropdown = self.page.locator("select#beneficiary")
        self.amount_input = self.page.locator("#amount")
        self.proceed_button = self.page.locator("button#proceed")
        self.otp_input = self.page.locator("#otp")
        self.confirm_button = self.page.locator("button#confirm")
        self.success_msg = self.page.locator("div.transfer-success")

    def navigate(self):
        self.page.goto(self.url)

    def select_beneficiary(self, name):
        self.beneficiary_dropdown.select_option(label=name)

    def enter_amount(self, amount):
        self.amount_input.fill(amount)

    def proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)
        self.confirm_button.click()

    def is_transfer_successful(self):
        return self.success_msg.is_visible()

    def initiate_transfer(self):
        # Shortcut for tests that start from a pre‑filled state
        self.proceed()

class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.url = "/beneficiaries/add"
        self.account_input = page.locator("#accountNumber")
        self.ifsc_input = page.locator("#ifscCode")
        self.add_button = page.locator("button:has-text('Add Beneficiary')")
        self.success_toast = page.locator(".toast-success")

    def goto(self):
        self.page.goto(self.url)

    def enter_account_number(self, number: str):
        self.account_input.fill(number)

    def enter_ifsc(self, ifsc: str):
        self.ifsc_input.fill(ifsc)

    def submit(self):
        self.add_button.click()

class TransferPage:
    def __init__(self, page):
        self.page = page
        self.url = "/transfer"
        self.beneficiary_dropdown = page.locator("#beneficiarySelect")
        self.amount_input = page.locator("#transferAmount")
        self.proceed_button = page.locator("button:has-text('Proceed')")
        self.otp_input = page.locator("#otpInput")
        self.confirm_button = page.locator("button:has-text('Confirm')")
        self.confirmation_message = page.locator(".transfer-confirmation")
        self.success_banner = page.locator(".success-banner")

    def goto(self):
        self.page.goto(self.url)

    def select_beneficiary(self, name: str):
        self.beneficiary_dropdown.select_option(label=name)

    def enter_amount(self, amount: str):
        self.amount_input.fill(amount)

    def proceed(self):
        self.proceed_button.click()

    def enter_otp(self, otp: str):
        self.otp_input.fill(otp)
        self.confirm_button.click()

    def initiate_transfer(self):
        # shortcut for tests that start from a pre‑filled state
        self.goto()
        self.select_beneficiary("John Doe")
        self.enter_amount("1000")
        self.proceed()
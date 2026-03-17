class BankingPage:
    def __init__(self, page):
        self.page = page
        self.add_beneficiary_btn = page.locator("button#addBeneficiary")
        self.account_input = page.locator("input#accountNumber")
        self.ifsc_input = page.locator("input#ifscCode")
        self.transfer_btn = page.locator("button#transfer")
        self.amount_input = page.locator("input#amount")
        self.proceed_btn = page.locator("button#proceed")
        self.otp_input = page.locator("input#otp")
        self.confirm_btn = page.locator("button#confirmTransfer")

    def navigate_to_add_beneficiary(self):
        self.page.goto("https://example.com/add-beneficiary")

    def add_beneficiary(self, account_number: str, ifsc: str):
        self.account_input.fill(account_number)
        self.ifsc_input.fill(ifsc)
        self.add_beneficiary_btn.click()

    def navigate_to_transfer(self):
        self.page.goto("https://example.com/transfer")

    def select_beneficiary(self, beneficiary_id: str):
        self.page.locator(f"//div[@data-beneficiary-id='{beneficiary_id}']").click()

    def enter_amount(self, amount: int):
        self.amount_input.fill(str(amount))

    def proceed_to_otp(self):
        self.proceed_btn.click()

    def enter_otp(self, otp: str):
        self.otp_input.fill(otp)

    def confirm_transfer(self):
        self.confirm_btn.click()

class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.account_input = page.locator("#accountNumber")
        self.ifsc_input = page.locator("#ifscCode")
        self.add_button = page.locator("button:has-text('Add Beneficiary')")
        self.success_notification = page.locator(".toast-success")
        self.error_message = page.locator(".error-message")

    def goto_add_beneficiary(self):
        self.page.goto("https://app.bank.com/beneficiaries/add")

    def enter_account_number(self, account_number: str):
        self.account_input.fill(account_number)

    def enter_ifsc(self, ifsc_code: str):
        self.ifsc_input.fill(ifsc_code)

    def click_add(self):
        self.add_button.click()

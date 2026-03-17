class AddBeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.url = "/beneficiary/add"
        self.account_input = page.locator("#accountNumber")
        self.ifsc_input = page.locator("#ifscCode")
        self.add_button = page.locator("button#addBeneficiary")
        self.success_toast = page.locator(".toast-success")
        self.error_toast = page.locator(".toast-error")

    def navigate(self):
        self.page.goto(self.url)

    def enter_account_number(self, account_number: str):
        self.account_input.fill(account_number)

    def enter_ifsc(self, ifsc_code: str):
        self.ifsc_input.fill(ifsc_code)

    def click_add(self):
        self.add_button.click()

    def success_message(self):
        return self.success_toast

    def error_message(self):
        return self.error_toast
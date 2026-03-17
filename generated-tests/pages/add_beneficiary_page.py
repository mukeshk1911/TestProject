class AddBeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator("button#addBeneficiary")
        self.account_input = page.locator("input#accountNumber")
        self.ifsc_input = page.locator("input#ifsc")
        self.success_toast = page.locator("div.toast-success")
        self.error_message = page.locator("span.error-message")
        self.beneficiary_rows = page.locator("table#beneficiaryList tbody tr")

    def open_add_form(self):
        self.page.goto("https://example.com/beneficiaries")
        self.page.click("button#openAddForm")

    def fill_account_number(self, account_number: str):
        self.account_input.fill(account_number)

    def fill_ifsc(self, ifsc: str):
        self.ifsc_input.fill(ifsc)

    def submit(self):
        self.add_button.click()

    def is_beneficiary_in_list(self, account_number: str) -> bool:
        row = self.beneficiary_rows.filter(has_text=account_number)
        return row.count() > 0

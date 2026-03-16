class AddBeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator("button:has-text('Add')")
        self.account_input = page.locator("input[name='account_number']")
        self.ifsc_input = page.locator("input[name='ifsc']")
        self.success_toast = page.locator(".toast-success")
        self.error_toast = page.locator(".toast-error")

    def navigate_to_section(self):
        self.page.goto("/beneficiaries")

    def open_form(self):
        self.page.click("text='Add Beneficiary'")

    def fill_account_number(self, account_number: str):
        self.account_input.fill(account_number)

    def fill_ifsc_code(self, ifsc: str):
        self.ifsc_input.fill(ifsc)

    def click_add(self):
        self.add_button.click()

    def success_notification(self):
        return self.success_toast

    def error_message(self):
        return self.error_toast

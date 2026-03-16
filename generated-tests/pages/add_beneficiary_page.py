class AddBeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator("button:has-text('Add')")
        self.account_input = page.locator("input[name='account_number']")
        self.ifsc_input = page.locator("input[name='ifsc']")
        self.success_msg = page.locator(".notification.success")
        self.error_msg = page.locator(".notification.error")

    def navigate_to_section(self):
        self.page.goto("https://example.com/beneficiaries")

    def open_add_form(self):
        self.page.click("button:has-text('Add Beneficiary')")

    def fill_account_number(self, account):
        self.account_input.fill(account)

    def fill_ifsc_code(self, ifsc):
        self.ifsc_input.fill(ifsc)

    def click_add(self):
        self.add_button.click()

    def success_notification(self):
        return self.success_msg

    def error_message(self):
        return self.error_msg
class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator("button:has-text('Add Beneficiary')")
        self.account_input = page.locator("input[name='accountNumber']")
        self.ifsc_input = page.locator("input[name='ifscCode']")
        self.name_input = page.locator("input[name='beneficiaryName']")
        self.success_msg = page.locator(".toast-success")
        self.error_msg = page.locator(".toast-error")

    def goto_add_beneficiary(self):
        self.page.click("text=Add Beneficiary")

    def enter_account_number(self, number: str):
        self.account_input.fill(number)

    def enter_ifsc(self, ifsc: str):
        self.ifsc_input.fill(ifsc)

    def enter_name(self, name: str):
        self.name_input.fill(name)

    def click_add(self):
        self.add_button.click()

    def success_toast(self):
        return self.success_msg

    def error_toast(self):
        return self.error_msg
class TransferPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.beneficiary_menu = page.locator("text=Beneficiary Management")
        self.add_button = page.locator("button:has-text('Add Beneficiary')")
        self.account_input = page.locator("input[name='account']")
        self.ifsc_input = page.locator("input[name='ifsc']")
        self.name_input = page.locator("input[name='name']")
        self.save_button = page.locator("button:has-text('Save')")
        self.transfer_menu = page.locator("text=Transfer")
        self.amount_input = page.locator("input[name='amount']")
        self.continue_button = page.locator("button:has-text('Continue')")
        self.otp_input = page.locator("input[name='otp']")
        self.confirm_button = page.locator("button:has-text('Confirm')")
        self.success_toast = page.locator(".toast-success")

    def navigate_to_beneficiary_management(self):
        self.beneficiary_menu.click()

    def click_add_beneficiary(self):
        self.add_button.click()

    def fill_beneficiary_form(self, account, ifsc, name):
        self.account_input.fill(account)
        self.ifsc_input.fill(ifsc)
        self.name_input.fill(name)

    def save_beneficiary(self):
        self.save_button.click()

    def beneficiary_in_list(self, name):
        return self.page.locator(f"text={name}")

    def open_transfer_screen(self):
        self.transfer_menu.click()

    def select_beneficiary(self, name):
        self.page.locator(f"//div[text()='{name}']").click()

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def click_continue(self):
        self.continue_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def confirm_transfer(self):
        self.confirm_button.click()

    def success_toast(self):
        return self.success_toast

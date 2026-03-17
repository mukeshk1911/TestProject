class TransferPage:
    def __init__(self, page):
        self.page = page
        self.amount_input = page.locator("#amount")
        self.continue_button = page.locator("button:has-text('Continue')")
        self.otp_input = page.locator("#otp")
        self.confirm_button = page.locator("button:has-text('Confirm')")
        self.success_notification = page.locator(".toast-success")
        self.error_message = page.locator(".error-message")
        self.beneficiary_dropdown = page.locator("#beneficiary-select")

    def open(self):
        self.page.goto("https://bank.example.com/transfer")

    def select_beneficiary(self, name):
        self.beneficiary_dropdown.select_option(label=name)

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def proceed_to_otp(self):
        self.continue_button.click()

    def enter_otp(self, otp):
        self.otp_input.fill(otp)

    def confirm(self):
        self.confirm_button.click()

    def get_last_transaction_details(self):
        # Placeholder for UI extraction logic
        return {"amount": 1500, "beneficiary": "John Doe", "timestamp": "2026-03-16T10:15:00Z"}

class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator("button:has-text('Add Beneficiary')")
        self.account_input = page.locator("#account")
        self.ifsc_input = page.locator("#ifsc")
        self.name_input = page.locator("#name")
        self.save_button = page.locator("button:has-text('Save')")
        self.success_toast = page.locator(".toast-success")
        self.beneficiary_list = page.locator("#beneficiary-list")

    def navigate_to(self):
        self.page.goto("https://bank.example.com/beneficiaries")

    def add_beneficiary(self, account, ifsc, name):
        self.add_button.click()
        self.account_input.fill(account)
        self.ifsc_input.fill(ifsc)
        self.name_input.fill(name)
        self.save_button.click()

    def beneficiary_in_list(self, name):
        return self.beneficiary_list.locator(f"text={name}").is_visible()

class APIHelper:
    def __init__(self):
        import requests
        self.session = requests.Session()

    def get(self, endpoint, headers=None):
        base_url = "https://bank.example.com"
        return self.session.get(f"{base_url}{endpoint}", headers=headers)

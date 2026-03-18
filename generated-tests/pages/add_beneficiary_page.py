class BeneficiaryPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator("button#addBeneficiary")
        self.account_input = page.locator("input#accountNumber")
        self.ifsc_input = page.locator("input#ifscCode")
        self.name_input = page.locator("input#beneficiaryName")
        self.save_button = page.locator("button#saveBeneficiary")
        self.toast = page.locator("div.toast-success")
        self.error_message = page.locator("div.validation-error")
        self.list_search = page.locator("input#searchBeneficiary")
        self.list_table = page.locator("table#beneficiaryList")

    def navigate_to_add(self):
        self.page.goto("https://bank.example.com/beneficiaries")
        self.add_button.click()

    def fill_form(self, account_number: str, ifsc: str, name: str = ""):
        self.account_input.fill(account_number)
        self.ifsc_input.fill(ifsc)
        if name:
            self.name_input.fill(name)

    def submit(self):
        self.save_button.click()

    def verify_in_list(self, account_number: str):
        self.page.goto("https://bank.example.com/beneficiaries/list")
        self.list_search.fill(account_number)
        self.list_search.press("Enter")
        expect(self.list_table).to_contain_text(account_number)

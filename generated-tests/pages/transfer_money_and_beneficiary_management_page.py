class TransferPage:
    def __init__(self, page):
        self.page = page
        self.add_beneficiary_url = "/beneficiary/add"
        self.transfer_url = "/transfer"

    def navigate_to_add_beneficiary(self):
        self.page.goto(self.add_beneficiary_url)

    def add_beneficiary(self, account_number: str, ifsc: str):
        self.page.fill("#accountNumber", account_number)
        self.page.fill("#ifscCode", ifsc)
        self.page.click("#addBeneficiaryBtn")

    def select_beneficiary(self, beneficiary_id: str):
        self.page.select_option("#beneficiarySelect", beneficiary_id)

    def enter_amount(self, amount: int):
        self.page.fill("#amount", str(amount))

    def proceed(self):
        self.page.click("#proceedBtn")

    def enter_otp(self, otp: str):
        self.page.fill("#otpInput", otp)

    def confirm_transfer(self):
        self.page.click("#confirmTransferBtn")

    def success_message(self):
        return self.page.locator(".notification.success")

    def error_message(self):
        return self.page.locator(".notification.error")

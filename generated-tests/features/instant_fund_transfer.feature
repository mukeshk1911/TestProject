Feature: Instant Fund Transfer
  As a user of the banking app
  I want to transfer funds instantly and manage beneficiaries
  So that I can send money securely and view transaction history

  Background:
    Given the user is logged in
    And the user has at least one beneficiary

  Scenario: Successful money transfer to an existing beneficiary
    When the user opens the Transfer screen
    And selects a beneficiary "John Doe"
    And enters amount "5000"
    And clicks Continue
    And enters a valid OTP "123456"
    And confirms the transfer
    Then a confirmation message is displayed
    And the transaction appears in the history

  Scenario: Transfer fails when amount exceeds maximum limit
    When the user opens the Transfer screen
    And selects a beneficiary "John Doe"
    And enters amount "150000"
    And clicks Continue
    Then an error message "Transfer amount exceeds limit of ₹1,00,000" is displayed

  Scenario: Transaction is cancelled after three OTP failures
    When the user initiates a transfer of amount "2500"
    And requests OTP
    And enters wrong OTP "000000" three times
    Then an error message "OTP attempts exceeded, transaction cancelled" is displayed
    And no transaction is recorded

  Scenario Outline: Adding a beneficiary with various account details
    When the user navigates to Add Beneficiary screen
    And enters account number "<account>"
    And enters IFSC code "<ifsc>"
    And enters beneficiary name "<name>"
    And clicks Save
    Then "<message>" is displayed

    Examples:
      | account          | ifsc          | name      | message                                 |
      | 123456789012     | ABCD0123456   | Alice     | Beneficiary added successfully          |
      | ABC123           | ABCD0123456   | Bob       | Account number must be numeric and 10‑16 digits |

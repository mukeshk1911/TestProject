Feature: Instant Fund Transfer
  As a user of the banking app
  I want to manage beneficiaries and perform transfers securely
  So that I can move money reliably

  Background:
    Given the user is logged in
    And the user has at least one beneficiary

  Scenario: Add a beneficiary with valid details
    When the user navigates to the Beneficiary Management screen
    And clicks on "Add Beneficiary"
    And enters a valid account number, IFSC code and name
    And saves the beneficiary
    Then a success toast is displayed
    And the new beneficiary appears in the list

  Scenario: Transfer money to an existing beneficiary
    When the user opens the Transfer screen
    And selects a beneficiary
    And enters a valid amount within limits
    And proceeds to OTP verification
    And enters the correct OTP
    Then the transfer is successful
    And the transaction appears in history

  Scenario Outline: Reject invalid beneficiary details
    When the user attempts to add a beneficiary with account "<account>" and IFSC "<ifsc>"
    Then the system shows validation error "<error_message>"

    Examples:
      | account   | ifsc          | error_message                                          |
      | ABC123    | ABCD0123456   | Account number must be numeric and 10‑16 digits       |
      | 123456789 | XYZ1234567    | IFSC code format is invalid                             |

  Scenario: Cancel transaction after three OTP failures
    When the user initiates a transfer
    And enters an incorrect OTP three times
    Then the system displays "OTP attempts exceeded, transaction cancelled"
    And no transaction is recorded

  Scenario: Verify transaction appears in history via API
    Given a successful transfer has been made via UI
    When the user calls GET /api/transactions with a valid token
    Then the response contains the recent transaction with correct amount and beneficiary
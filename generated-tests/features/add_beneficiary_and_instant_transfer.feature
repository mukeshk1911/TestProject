Feature: Add Beneficiary and Instant Transfer
  As a banking user, I want to manage beneficiaries and transfer funds instantly.

  Background:
    Given the user is logged in
    And the user has a valid session

  Scenario: Add a new beneficiary successfully
    When the user navigates to the Add Beneficiary page
    And the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "QRST0001234"
    And the user clicks the "Add Beneficiary" button
    Then the system shows a success message "Beneficiary added successfully"

  Scenario: Transfer funds to a beneficiary within limit
    Given the user has at least one registered beneficiary
    When the user navigates to the Transfer page
    And the user selects a registered beneficiary
    And the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user enters a valid OTP "123456"
    Then the transaction is confirmed and appears in the transaction history

  Scenario: OTP verification flow succeeds
    Given the user initiates a transfer for a registered beneficiary
    When the user receives an OTP
    And the user enters OTP "654321"
    Then the OTP is accepted and the transaction is marked successful

  Scenario Outline: Transfer with various amounts
    Given the user selects a registered beneficiary
    When the user enters transfer amount <amount>
    And the user clicks "Proceed"
    And the user enters OTP "987654"
    Then the transaction is <outcome>

    Examples:
      | amount | outcome                     |
      | 5000   | processed successfully      |
      | 100000 | processed successfully (max) |
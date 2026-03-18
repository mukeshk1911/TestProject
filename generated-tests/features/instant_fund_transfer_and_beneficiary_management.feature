Feature: Instant Fund Transfer and Beneficiary Management
  As a banking user
  I want to manage beneficiaries and perform instant fund transfers securely
  So that I can move money quickly and safely

  Background:
    Given the user is logged in
    And the user is on the dashboard page

  Scenario: Verify adding a beneficiary with valid details
    When the user navigates to the Add Beneficiary screen
    And the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user clicks the Add Beneficiary button
    Then a success notification "Beneficiary added successfully" should be displayed

  Scenario: Verify successful instant fund transfer with correct OTP
    When the user navigates to the Transfer Money page
    And the user selects beneficiary "BEN123"
    And the user enters transfer amount "5000"
    And the user clicks Proceed to request OTP
    And the user enters correct OTP "123456"
    And the user confirms the transfer
    Then a success message "Transfer completed" should be shown
    And the transaction should appear in the transaction history

  Scenario: Verify transfer is blocked when OTP is incorrect
    When the user initiates a transfer of amount "5000" to beneficiary "BEN123"
    And the user requests OTP
    And the user enters incorrect OTP "000000"
    And the user confirms the transfer
    Then an error message "Invalid OTP" should be displayed

  Scenario Outline: Verify transfer amount validation
    When the user attempts to transfer amount "<amount>"
    Then the system should display "<message>"

    Examples:
      | amount   | message                                 |
      | 150000   | Transfer amount exceeds limit           |
      | 0        | Transfer amount must be greater than 0 |
      | -500     | Transfer amount cannot be negative     |

Feature: Transfer Money and Beneficiary Management
  As a banking user
  I want to manage beneficiaries and transfer money securely
  So that I can send funds to my contacts safely

  Background:
    Given the user is logged in
    And the user is on the dashboard page

  Scenario: Add beneficiary with valid details
    When the user navigates to the Add Beneficiary screen
    And the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user clicks the "Add Beneficiary" button
    Then a success notification "Beneficiary added successfully" is displayed

  Scenario: Transfer money with correct OTP
    Given a beneficiary "BEN123" exists
    When the user selects beneficiary "BEN123"
    And the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user enters OTP "123456"
    And the user clicks "Confirm Transfer"
    Then a confirmation message "Transfer successful" is displayed

  Scenario: Transfer blocked when OTP is incorrect
    Given a beneficiary "BEN123" exists
    When the user selects beneficiary "BEN123"
    And the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user enters OTP "000000"
    And the user clicks "Confirm Transfer"
    Then an error message "Invalid OTP" is displayed

  Scenario Outline: Add beneficiary with invalid account number format
    When the user navigates to the Add Beneficiary screen
    And the user enters an invalid account number "<account>"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user clicks the "Add Beneficiary" button
    Then a validation error "Account number must be numeric and 10‑16 digits" is displayed

    Examples:
      | account   |
      | ABC123    |
      | 12345     |
      | 12345678901234567 |

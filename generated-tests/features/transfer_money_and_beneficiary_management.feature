Feature: Transfer Money and Beneficiary Management
  As a banking user
  I want to manage beneficiaries and perform transfers securely
  So that I can move money safely

  Background:
    Given the user is logged in
    And the user is on the Banking dashboard

  Scenario: Add a beneficiary with valid details
    When the user navigates to the Add Beneficiary screen
    And the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user clicks the "Add Beneficiary" button
    Then a success notification "Beneficiary added successfully" is displayed

  Scenario: Transfer money within limits with correct OTP
    Given a beneficiary "BEN123" exists
    When the user selects beneficiary "BEN123"
    And the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user provides correct OTP "123456"
    And the user clicks "Confirm Transfer"
    Then a confirmation message "Transfer successful" is displayed

  Scenario: Transfer fails with incorrect OTP
    Given a beneficiary "BEN123" exists
    When the user selects beneficiary "BEN123"
    And the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user provides incorrect OTP "000000"
    And the user clicks "Confirm Transfer"
    Then an error message "Invalid OTP" is displayed

  Scenario Outline: Validate beneficiary addition errors
    When the user navigates to the Add Beneficiary screen
    And the user enters account number "<account>"
    And the user enters IFSC code "<ifsc>"
    And the user clicks the "Add Beneficiary" button
    Then an error message "<error>" is displayed

    Examples:
      | account   | ifsc           | error                                          |
      | ABC123    | ABCD0123456    | Account number must be numeric and 10‑16 digits |
      | 123456789 | XYZ1234567     | IFSC code format is invalid                    
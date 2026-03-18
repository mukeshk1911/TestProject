Feature: Money Transfer and Beneficiary Management
  As a banking user
  I want to manage beneficiaries and transfer money securely
  So that I can send funds instantly

  Background:
    Given the user is logged in
    And the user is on the dashboard page

  Scenario: Add a new beneficiary with valid details
    When the user navigates to the Add Beneficiary page
    And the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user clicks the "Add Beneficiary" button
    Then the system should display a success message "Beneficiary added successfully"

  Scenario: Transfer money to an existing beneficiary within limit
    Given the beneficiary "John Doe" exists
    When the user selects beneficiary "John Doe"
    And the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user enters a valid OTP "123456"
    And the user clicks "Confirm Transfer"
    Then the system should display a confirmation message "Transfer completed successfully"

  Scenario: Attempt to add beneficiary with invalid account number
    When the user navigates to the Add Beneficiary page
    And the user enters an invalid account number "ABCDEF123"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user clicks the "Add Beneficiary" button
    Then the system should display an error message "Invalid account number format"

  Scenario Outline: Transfer amount validation
    When the user selects beneficiary "John Doe"
    And the user enters transfer amount "<amount>"
    And the user clicks "Proceed"
    Then the system should display "<message>"

    Examples:
      | amount | message                                 |
      | 100001 | "Transfer amount exceeds limit"        |
      | 100000 | "Proceed to OTP verification"          |
      | 0      | "Transfer amount must be greater than 0"
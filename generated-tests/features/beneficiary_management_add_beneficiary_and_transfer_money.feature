Feature: Beneficiary Management
  As a banking user
  I want to add beneficiaries and transfer money securely
  So that I can manage my payments efficiently

  Background:
    Given the user is logged in
    And the user is on the Beneficiary Management dashboard

  Scenario: Add a new beneficiary with valid details
    When the user navigates to the Add Beneficiary page
    And the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user clicks the "Add Beneficiary" button
    Then a success message "Beneficiary added successfully" is displayed

  Scenario: Transfer money to an existing beneficiary
    Given the beneficiary "BEN123" exists
    When the user selects beneficiary "BEN123" on the Transfer Money page
    And the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user enters a valid OTP "123456"
    And the user confirms the transfer
    Then a confirmation message "Transfer completed successfully" is shown

  Scenario Outline: Validate transfer amount limits
    When the user selects beneficiary "BEN123"
    And the user enters transfer amount "<amount>"
    And the user clicks "Proceed"
    Then the system displays "<message>"

    Examples:
      | amount | message                                 |
      | 200000 | "Transfer amount exceeds limit"        |
      | 100000 | "Transfer amount accepted"             |
      | 0      | "Transfer amount must be greater than 0" |

Feature: Transfer Money and Beneficiary Management
  As a banking user
  I want to manage beneficiaries and perform transfers securely
  So that I can move funds safely

  Background:
    Given the user is logged in
    And the user navigates to the Banking dashboard

  Scenario: Successful transfer with correct OTP
    Given the user selects an existing beneficiary
    When the user enters a transfer amount of 5000
    And the user clicks "Proceed"
    And the user provides a valid OTP "123456"
    And the user confirms the transfer
    Then a success message "Transfer successful" is displayed

  Scenario: Transfer blocked due to incorrect OTP
    Given the user selects an existing beneficiary
    When the user enters a transfer amount of 5000
    And the user clicks "Proceed"
    And the user provides an invalid OTP "000000"
    And the user attempts to confirm the transfer
    Then an error message "Invalid OTP" is displayed

  Scenario: Adding a beneficiary with valid details
    Given the user is on the Add Beneficiary page
    When the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user clicks "Add Beneficiary"
    Then a success notification "Beneficiary added successfully" is shown

  Scenario Outline: Transfer amount validation
    Given the user selects an existing beneficiary
    When the user enters a transfer amount of <amount>
    And the user clicks "Proceed"
    Then the system displays <expected_message>

    Examples:
      | amount | expected_message                                 |
      | 0      | "Transfer amount must be greater than zero"    |
      | 150000 | "Transfer amount exceeds the maximum limit"    |
      | 1      | "Transfer amount accepted"                     |

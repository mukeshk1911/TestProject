Feature: Transfer Money and Beneficiary Management
  As a banking user
  I want to manage beneficiaries and perform transfers securely
  So that I can move funds safely

  Background:
    Given the user is logged in
    And the user is on the Dashboard page

  Scenario: Add a beneficiary with valid details
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

  Scenario: Transfer blocked with incorrect OTP
    Given a beneficiary "BEN123" exists
    When the user selects beneficiary "BEN123"
    And the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user enters OTP "000000"
    And the user clicks "Confirm Transfer"
    Then an error message "Invalid OTP" is displayed

  Scenario Outline: Validate transfer amount limits
    When the user selects beneficiary "BEN123"
    And the user enters transfer amount "<amount>"
    And the user clicks "Proceed"
    Then the system response should be "<expected>"

    Examples:
      | amount | expected                                 |
      | 150000 | "Transfer amount exceeds the limit"     |
      | 1      | "Transfer amount accepted"              |
      | 5000   | "Transfer amount accepted"              |
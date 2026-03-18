Feature: Transfer Money and Beneficiary Management
  Background:
    Given the user is logged into the mobile banking app

  Scenario: Verify adding a beneficiary with valid details
    When the user navigates to the Add Beneficiary page
    And the user enters account number "123456789012"
    And the user enters IFSC code "MNOP0123456"
    And the user enters beneficiary name "John Doe"
    And the user clicks the "Add Beneficiary" button
    Then a success toast/message is displayed
    And the beneficiary appears in the beneficiary list

  Scenario: Verify transferring money within allowed limits with correct OTP
    Given the user is on the Transfer Money page with a saved beneficiary
    When the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user provides correct OTP "123456"
    And the user clicks "Confirm Transfer"
    Then a confirmation message is shown indicating the transfer was successful

  Scenario: Verify OTP verification blocks transfer when OTP is incorrect
    Given the user is on the Transfer Money page with a saved beneficiary
    When the user enters transfer amount "5000"
    And the user clicks "Proceed"
    And the user provides incorrect OTP "000000"
    And the user clicks "Confirm Transfer"
    Then an error message is displayed indicating invalid OTP and the transfer is not completed

  Scenario Outline: Verify validation errors for invalid inputs
    When the user navigates to the Add Beneficiary page
    And the user enters account number "<account_number>"
    And the user enters IFSC code "<ifsc>"
    And the user clicks the "Add Beneficiary" button
    Then a validation error "<error_message>" is displayed

    Examples:
      | account_number | ifsc          | error_message                                          |
      | ABC123         | ABCD0123456   | Account number must be numeric and 10‑16 digits       |
      | 150000         | N/A           | Transfer amount exceeds the allowed limit (₹100,000)  |
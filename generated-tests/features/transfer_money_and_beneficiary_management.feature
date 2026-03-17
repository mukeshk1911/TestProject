Feature: Transfer Money and Beneficiary Management
  Background:
    Given the user is logged in

  Scenario: Adding a beneficiary with valid details
    Given the user navigates to the Add Beneficiary screen
    When the user enters a valid account number "123456789012" and IFSC "ABCD0123456"
    And the user clicks the Add Beneficiary button
    Then a success message is displayed

  Scenario: Transferring money within limits with correct OTP
    Given the user selects beneficiary "BEN123"
    When the user enters amount "5000" and proceeds
    And the user provides correct OTP "123456"
    Then the transfer is completed and a confirmation message appears

  Scenario: Transfer fails with incorrect OTP
    Given the user selects beneficiary "BEN123"
    When the user enters amount "5000" and proceeds
    And the user provides incorrect OTP "000000"
    Then an error message about invalid OTP is shown

  Scenario Outline: Validate error handling for invalid inputs
    Given the user is on the <page> page
    When the user enters <input> and submits
    Then the system shows error message "<error>"
    Examples:
      | page            | input                     | error                                          |
      | Add Beneficiary | account number "ABC123"   | Account number must be numeric and 10‑16 digits |
      | Transfer Money  | amount "150000"           | Transfer amount exceeds the allowed limit   |
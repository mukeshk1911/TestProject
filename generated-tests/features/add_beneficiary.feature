Feature: Add Beneficiary
  As a logged‑in user
  I want to add beneficiaries
  So that I can transfer funds to them

  Background:
    Given the user is logged in
    And the user is on the Add Beneficiary page

  Scenario: Add beneficiary with valid details
    When the user enters account number "1234567890"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add button
    Then a success notification is displayed
    And the beneficiary appears in the list

  Scenario: Add beneficiary with edge account number and IFSC pattern
    When the user enters account number "1000000000"
    And the user enters IFSC code "1BCD0123456"
    And the user clicks the Add button
    Then a success notification is displayed

  Scenario: Attempt to add beneficiary with invalid IFSC format
    When the user enters account number "1234567890"
    And the user enters IFSC code "ABC12"
    And the user clicks the Add button
    Then an error message "IFSC code must be 11 alphanumeric characters" is shown

  Scenario Outline: Attempt to add beneficiary with non‑numeric account number
    When the user enters account number "<account>"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add button
    Then an error message "Account number must be numeric and 10‑16 digits long" is shown

    Examples:
      | account      |
      | 12AB567890   |
      | ABCD123456   |

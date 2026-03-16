Feature: Add Beneficiary Management
  As a logged‑in user
  I want to add beneficiaries
  So that I can transfer funds to them

  Background:
    Given the user is authenticated
    And the user is on the Add Beneficiary page

  Scenario: Successfully add a beneficiary with valid data
    When the user enters account number "1234567890"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add button
    Then a success notification is displayed
    And the new beneficiary appears in the beneficiary list

  Scenario: Attempt to add beneficiary with non‑numeric account number
    When the user enters account number "12AB567890"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add button
    Then an error message "Account number must be numeric and 10‑16 digits long" is shown

  Scenario: Attempt to add beneficiary with invalid IFSC format
    When the user enters account number "1234567890"
    And the user enters IFSC code "ABC12"
    And the user clicks the Add button
    Then an error message "IFSC code must be 11 alphanumeric characters" is shown

  Scenario Outline: Add beneficiary with various valid edge values
    When the user enters account number "<account>"
    And the user enters IFSC code "<ifsc>"
    And the user clicks the Add button
    Then a success notification is displayed

    Examples:
      | account      | ifsc          |
      | 1000000000   | 1BCD0123456   |
      | 1234567890123456 | ABCD0123456 |
      | 9876543210   | XZYB0987654   |
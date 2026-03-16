Feature: Add Beneficiary Management
  As a logged‑in user
  I want to manage beneficiaries
  So that I can add valid beneficiaries and receive appropriate feedback

  Background:
    Given the user is logged in
    And the user is on the Add Beneficiary page

  Scenario: Add beneficiary with valid details
    When the user enters account number "1234567890"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the "Add" button
    Then a success notification is displayed
    And the new beneficiary appears in the list

  Scenario: Add beneficiary with non‑numeric account number
    When the user enters account number "12AB567890"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the "Add" button
    Then an error message "Account number must be numeric and 10‑16 digits long" is displayed

  Scenario: Unauthorized access to Add Beneficiary API
    When the user sends a POST request to "/api/beneficiaries" without an Authorization header
    Then the response status is 401
    And the response body contains "Authentication required"

  Scenario Outline: Add beneficiary with various edge values
    When the user enters account number "<account>"
    And the user enters IFSC code "<ifsc>"
    And the user clicks the "Add" button
    Then a success notification is displayed

    Examples:
      | account      | ifsc          |
      | 1000000000   | 1BCD0123456   |
      | 1234567890123456 | ABCD0123456 |

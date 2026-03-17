Feature: Add Beneficiary Management
  As a bank customer
  I want to manage my beneficiaries
  So that I can transfer money easily

  Background:
    Given the user is logged in
    And the user is on the Add Beneficiary page

  Scenario: Add beneficiary with valid details
    When the user enters account number "123456789012"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add Beneficiary button
    Then a success notification "Beneficiary added successfully" is displayed

  Scenario: Add beneficiary with invalid IFSC format
    When the user enters account number "123456789012"
    And the user enters IFSC code "AB12"
    And the user clicks the Add Beneficiary button
    Then an error message "Invalid IFSC format" is displayed

  Scenario: Add duplicate beneficiary
    Given a beneficiary with account number "123456789012" already exists
    When the user enters account number "123456789012"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add Beneficiary button
    Then an error message "Beneficiary already exists" is displayed

  Scenario Outline: Add beneficiary with various valid data sets
    When the user enters account number "<account>"
    And the user enters IFSC code "<ifsc>"
    And the user clicks the Add Beneficiary button
    Then a success notification is displayed

    Examples:
      | account          | ifsc          |
      | 123456789012     | ABCD0123456   |
      | 987654321098     | WXYZ0987654   |
      | 1234567890123456 | LMNO1234567   |
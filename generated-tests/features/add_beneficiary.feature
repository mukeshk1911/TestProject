Feature: Add Beneficiary Management
  As a bank customer
  I want to manage my beneficiaries
  So that I can transfer funds securely

  Background:
    Given the user is logged in
    And the user is on the Add Beneficiary page

  Scenario: Verify adding a beneficiary with valid details
    When the user enters a valid account number "123456789012" and a valid IFSC "ABCD0123456"
    And the user clicks the "Add Beneficiary" button
    Then a success toast "Beneficiary added successfully" is displayed
    And the beneficiary appears in the beneficiary list

  Scenario: Verify error when IFSC format is invalid
    When the user enters a valid account number "123456789012" and an invalid IFSC "INVALIDIFSC"
    And the user clicks the "Add Beneficiary" button
    Then an error message "Invalid IFSC format" is shown

  Scenario: Verify error when account number contains non-numeric characters
    When the user enters an account number "abc123def" and a valid IFSC "QRST0001234"
    And the user clicks the "Add Beneficiary" button
    Then an error message "Account number must be numeric and 10‑16 digits" is shown

  Scenario Outline: Verify maximum allowed account number length
    When the user enters an account number "<accountNumber>" and a valid IFSC "QRST0001234"
    And the user clicks the "Add Beneficiary" button
    Then a success toast "Beneficiary added successfully" is displayed

    Examples:
      | accountNumber        |
      | 1234567890123456    |
      | 123456789012345     |
      | 12345678901234      |

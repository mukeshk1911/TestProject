Feature: Add Beneficiary
  As a logged‑in user
  I want to add a new beneficiary
  So that I can transfer funds to them

  Background:
    Given the user is authenticated and on the Beneficiary Management page

  Scenario: Successful beneficiary addition
    When the user navigates to the Add Beneficiary form
    And the user enters a valid account number "123456789012" and IFSC "MNOP0123456"
    And the user clicks the "Add Beneficiary" button
    Then a success message "Beneficiary added successfully" is displayed
    And the new beneficiary appears in the beneficiary list

  Scenario: Beneficiary addition fails with non‑numeric account number
    When the user enters an invalid account number "abc123" and a valid IFSC "QRST0001234"
    And the user clicks the "Add Beneficiary" button
    Then an error message "Account number must be numeric and 10‑16 digits" is displayed

  Scenario: Session expiration blocks beneficiary addition
    Given the user session has expired
    When the user attempts to add a beneficiary
    Then the system redirects to the login page or shows a "Session expired" message

  Scenario Outline: Add beneficiary with various account number lengths
    When the user enters account number <accountNumber> and IFSC "QRST0001234"
    And the user clicks the "Add Beneficiary" button
    Then <outcome> is displayed

    Examples:
      | accountNumber      | outcome                                 |
      | 1234567890          | success message                         |
      | 1234567890123456   | success message                         |
      | 12345               | error "Account number must be numeric and 10‑16 digits" |

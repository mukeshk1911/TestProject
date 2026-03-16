Feature: Instant Fund Transfer
  As a user of the banking app
  I want to manage beneficiaries and perform instant fund transfers
  So that I can send money quickly and securely

  Background:
    Given the user is logged in
    And the user has at least one beneficiary

  Scenario: Add beneficiary with valid details
    When the user navigates to the Beneficiary Management screen
    And the user clicks on 'Add Beneficiary'
    And the user enters a valid account number, IFSC code and name
    And the user clicks 'Save'
    Then a success toast is displayed
    And the new beneficiary appears in the list

  Scenario: Transfer money to an existing beneficiary
    When the user opens the Transfer screen
    And the user selects a beneficiary
    And the user enters a valid amount within limits
    And the user clicks 'Continue'
    And the user enters the correct OTP
    And the user clicks 'Confirm'
    Then a confirmation message is shown
    And the transaction appears in the history

  Scenario: OTP verification flow works for a transfer
    When the user initiates a transfer with a valid amount
    And the user clicks 'Continue' to request OTP
    And the user receives the OTP on the registered mobile
    And the user enters the correct OTP
    And the user clicks 'Confirm'
    Then the transfer is completed successfully

  Scenario Outline: Transfer amount exceeds maximum limit
    When the user attempts to transfer <amount>
    Then the system displays error message '<errorMessage>'

    Examples:
      | amount | errorMessage                                 |
      | 150000 | Transfer amount exceeds limit of ₹1,00,000 |
      | 200000 | Transfer amount exceeds limit of ₹1,00,000 |
Feature: Instant Fund Transfer
  As a user of the banking app
  I want to manage beneficiaries and perform instant fund transfers
  So that I can send money quickly and securely

  Background:
    Given the user is logged in

  Scenario: Verify adding a beneficiary with valid details
    When the user navigates to the Beneficiary Management screen
    And the user clicks on "Add Beneficiary"
    And the user enters a valid account number, IFSC code and name
    And the user clicks "Save"
    Then a success toast is displayed
    And the new beneficiary appears in the list

  Scenario: Verify successful money transfer to an existing beneficiary
    Given the user has at least one beneficiary
    When the user opens the Transfer screen
    And the user selects a beneficiary
    And the user enters a valid amount within limits
    And the user clicks "Continue"
    And the user enters the received OTP
    And the user clicks "Confirm"
    Then a confirmation message is shown
    And the transaction appears in the history

  Scenario: Verify OTP verification flow works for a transfer
    Given the user has selected a beneficiary
    When the user initiates a transfer with a valid amount
    And the user clicks "Continue"
    And the user receives an OTP on the registered mobile
    And the user enters the correct OTP
    And the user clicks "Confirm"
    Then the transfer is completed successfully

  Scenario Outline: Verify transfer fails when amount exceeds the maximum limit
    Given the user selects a beneficiary
    When the user enters an amount of <amount>
    And the user clicks "Continue"
    Then the error message "Transfer amount exceeds limit of ₹1,00,000" is displayed

    Examples:
      | amount |
      | 150000 |
      | 200000 |
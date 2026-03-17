Feature: Instant Fund Transfer
  As a banking customer
  I want to perform instant fund transfers and manage beneficiaries
  So that I can move money quickly and securely

  Background:
    Given the user is logged in

  Scenario: Verify adding a new beneficiary with valid details
    When the user clicks the 'Add Beneficiary' button
    And fills in valid account number, IFSC code, and beneficiary name
    And clicks the 'Save' button
    Then a confirmation toast is displayed
    And the new beneficiary appears in the beneficiary list

  Scenario: Verify successful instant fund transfer with correct OTP
    When the user navigates to the Transfer Money page
    And selects a beneficiary
    And enters a valid amount of 5000
    And clicks 'Proceed' to request OTP
    And enters the correct OTP "123456"
    And clicks 'Confirm Transfer'
    Then a success message is displayed
    And the transaction appears in the transaction history

  Scenario: Verify transaction history displays the recent transfer record
    When the user opens the Transaction History screen
    Then the most recent entry shows the correct amount, beneficiary, and status "Success"

  Scenario Outline: Verify transfer fails with invalid inputs
    When the user attempts a transfer with amount <amount>
    And requests OTP
    And enters OTP <otp>
    Then the system displays error message "<expectedMessage>"

    Examples:
      | amount | otp     | expectedMessage                     |
      | 150000 | N/A     | Transfer amount exceeds limit       |
      | 5000   | 000000  | Invalid OTP                         |
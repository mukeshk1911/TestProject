Feature: Transfer Money and Beneficiary Management
  As a banking user
  I want to manage beneficiaries and perform transfers
  So that I can move money securely

  Background:
    Given the user is logged in
    And the user is on the appropriate page

  Scenario: Verify adding a new beneficiary with valid account number and IFSC
    When the user navigates to the Add Beneficiary form
    And the user enters a valid name, numeric account number and a correct IFSC
    And the user clicks the Save button
    Then the beneficiary should be saved successfully and appear in the list

  Scenario: Verify successful money transfer within allowed amount range
    When the user selects an existing beneficiary
    And the user enters an amount of 5000
    And the user proceeds and provides a valid OTP
    And the user confirms the transfer
    Then the transfer should complete with a success message and the balance should be updated

  Scenario: Verify OTP verification blocks transfer when OTP is incorrect
    When the user selects a beneficiary and enters an amount of 5000
    And the user proceeds to request OTP
    And the user enters an incorrect OTP "000000"
    And the user attempts to confirm the transfer
    Then the transfer should be blocked and an "Invalid OTP" error message should be shown

  Scenario Outline: Verify transfer works with minimum and maximum allowed amounts
    When the user selects a beneficiary
    And the user enters an amount of <amount>
    And the user proceeds, enters a valid OTP and confirms
    Then the transfer should complete successfully with a success notification

    Examples:
      | amount |
      | 1      |
      | 100000 |

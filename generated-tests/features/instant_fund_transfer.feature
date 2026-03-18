Feature: Instant Fund Transfer
  As a banking user
  I want to add beneficiaries and transfer money instantly
  So that I can manage my finances efficiently

  Background:
    Given the user is logged into the mobile banking app
    And the user has at least one registered beneficiary

  Scenario: Add beneficiary with valid details
    When the user navigates to the Add Beneficiary screen
    And the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user taps the Save button
    Then the beneficiary should be added successfully
    And the beneficiary appears in the beneficiary list

  Scenario: Transfer money within allowed limits
    When the user selects a beneficiary "John Doe"
    And the user enters a transfer amount "5000"
    And the user submits the transfer request
    And the user enters the correct OTP "123456"
    Then the transfer should be processed
    And a confirmation message "Transfer successful" is displayed
    And the transaction appears in the history

  Scenario: Transfer fails after three incorrect OTP attempts
    When the user initiates a transfer of "3000" to "John Doe"
    And the user enters an incorrect OTP three times
    Then the transaction should be cancelled
    And an error message "OTP verification failed. Transaction cancelled." is shown

  Scenario Outline: Validate transfer amount limits
    When the user attempts to transfer "<amount>" rupees
    Then the system should display "<message>"

    Examples:
      | amount | message                                          |
      | 0      | "Transfer amount must be at least ₹1"           |
      | 1000000| "Transfer amount exceeds the maximum limit ₹1,00,000" |
      | 5000   | "Transfer amount is valid"